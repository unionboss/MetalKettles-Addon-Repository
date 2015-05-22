import base64,urllib,urllib2,re,cookielib,string,os,xbmc, xbmcgui, xbmcaddon, xbmcplugin, random, datetime,urlparse,mknet

addon_id        = 'plugin.video.SportsDonkey'
selfAddon       = xbmcaddon.Addon(id=addon_id)
datapath        = xbmc.translatePath(selfAddon.getAddonInfo('profile'))
fanart          = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
icon            = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
user            = selfAddon.getSetting('hqusername')
passw           = selfAddon.getSetting('hqpassword')
cookie_file     = os.path.join(os.path.join(datapath,''), 'SD.lwp')
net             = mknet.Net()

if user == '' or passw == '':
    if os.path.exists(cookie_file):
        try: os.remove(cookie_file)
        except: pass
    dialog = xbmcgui.Dialog()
    ret = dialog.yesno('Sports Donkey', 'Please enter your Sports Donkey account details','or register if you dont have an account','at http://sportsdonkey.club','Cancel','Login')
    if ret == 1:
        keyb = xbmc.Keyboard('', 'Enter Username')
        keyb.doModal()
        if (keyb.isConfirmed()):
            search = keyb.getText()
            username=search
            keyb = xbmc.Keyboard('', 'Enter Password:')
            keyb.doModal()
            if (keyb.isConfirmed()):
                search = keyb.getText()
                password=search
                selfAddon.setSetting('hqusername',username)
                selfAddon.setSetting('hqpassword',password)
user = selfAddon.getSetting('hqusername')
passw = selfAddon.getSetting('hqpassword')

#############################################################################################################################

def setCookie(srDomain):
    html = net.http_GET(srDomain).content
    r = re.findall(r'<input type="hidden" name="(.+?)" value="(.+?)" />', html, re.I)
    post_data = {}
    post_data['amember_login'] = user
    post_data['amember_pass'] = passw
    for name, value in r:
        value = value.replace('https','http')
        post_data[name] = value
    net.http_GET('http://sportsdonkey.club/site/member')
    net.http_POST('http://sportsdonkey.club/site/member',post_data)
    net.save_cookies(cookie_file)
    net.set_cookies(cookie_file)

    
def Index():
    setCookie('http://sportsdonkey.club/site/member')
    response = net.http_GET('http://sportsdonkey.club/site/live/')
    if not 'http://sportsdonkey.club/site/logout' in response.content:
        dialog = xbmcgui.Dialog()
        dialog.ok('Sports Donkey', 'Login Error','An error ocurred logging in. Please check your details','Ensure your account is active at http://sportsdonkey.club')
        quit()
    addDir('Calendar','url',6,icon,fanart)
    addDir('Live Streams','url',1,icon,fanart)
    addDir('Video on Demand','url',4,icon,fanart)
    
def live():
    net.set_cookies(cookie_file)
    response = net.http_GET('http://sportsdonkey.club/site/live/')
    link = response.content
    link = cleanHex(link)
    link=link.replace('onclick=SwitchMenu','\nonclick=SwitchMenu')
    cats=re.compile("\('.+?'\)>(.+?)</div>").findall(link)
    for name in cats:
        addDir(name,name,2,icon,fanart)

def getchannels(name,url):
    net.set_cookies(cookie_file)
    response = net.http_GET('http://sportsdonkey.club/site/live/')
    link = response.content
    link = cleanHex(link)
    link=link.replace('onclick=SwitchMenu','\nonclick=SwitchMenu').replace('</a><br ','')
    match=re.compile("onclick=SwitchMenu(.+?)\n").findall(link)
    for catdata in match:
        cats=re.compile("\('.+?'\)>(.+?)</div>").findall(catdata)
        for catname in cats:
            if catname == name:
                channels=re.compile("<a href=(.+?)>(.+?)/>-").findall(catdata)
                for url, name in channels:
                    url = 'http://sportsdonkey.club/site/live/'+url
                    addLink(name,url,3,icon,fanart)
                    
def playstream(url,name):
    net.set_cookies(cookie_file)
    response = net.http_GET(url)
    link = response.content
    link = cleanHex(link)
    strurl=re.compile("file: '(.+?)',").findall(link)[0] +' live=true timeout=20'
    strurl
    ok=True
    liz=xbmcgui.ListItem(name, iconImage=icon,thumbnailImage=icon); liz.setInfo( type="Video", infoLabels={ "Title": name } )
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
    try:
        xbmc.Player ().play(strurl, liz, False)
        return ok
    except:
        pass       
   
def vod():
    net.set_cookies(cookie_file)
    response = net.http_GET('http://sportsdonkey.club/site/live/vod/')
    link = response.content
    link = cleanHex(link)
    link=link.replace('onclick=SwitchMenu','\nonclick=SwitchMenu')
    cats=re.compile("\('.+?'\)>(.+?)</div>").findall(link)
    for name in cats:
        addDir(name,name,5,icon,fanart)

def vodfolders(url,name):
    net.set_cookies(cookie_file)
    if url==name:
        response = net.http_GET('http://sportsdonkey.club/site/live/vod/')
    else:
        response = net.http_GET(url)
    link = response.content
    link = cleanHex(link)
    link=link.replace('onclick=SwitchMenu','\nonclick=SwitchMenu').replace('</a><br ','')
    match=re.compile("onclick=SwitchMenu(.+?)\n").findall(link)
    for catdata in match:
        cats=re.compile("\('.+?'\)>(.+?)</div>").findall(catdata)
        for catname in cats:
            if catname == name:
                channels=re.compile("<a href=(.+?)>(.+?)/>-").findall(catdata)
                for url, name in channels:
                    url = 'http://sportsdonkey.club/site/live/'+url
                    addDir(name,url,5,icon,fanart)

def schedule():
    net.set_cookies(cookie_file)
    response = net.http_GET('http://sportsdonkey.club/calendar')
    link = response.content
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('  ','')
    match=re.compile("<li>(.+?)</li>").findall(link)
    i = 0
    for dte in match:
        if 'href' not in dte:
            i = i+1
            addLink(dte,'url','mode',icon,fanart)
        link=link.replace("fixture-row'><a href='#'>","fixture-row'><a href='####'>")
        match=re.compile("##(.+?)##").findall(link)
        for data in match:
            match=re.compile("fixture-row-left'>(.+?)<div>(.+?)</div>").findall(data)
            print match
            for name,tme in match:
                addLink(name+'  '+tme,'url','mode',icon,fanart)
            
    
def addDir(name,url,mode,iconimage,fanart,description=''):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def addLink(name,url,mode,iconimage,fanart,description=''):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
    
def cleanHex(text):
    def fixup(m):
        text = m.group(0)
        if text[:3] == "&#x": return unichr(int(text[3:-1], 16)).encode('utf-8')
        else: return unichr(int(text[2:-1])).encode('utf-8')
    return re.sub("(?i)&#\w+;", fixup, text.decode('ISO-8859-1').encode('utf-8'))

def notification(title, message, ms, nart):
    xbmc.executebuiltin("XBMC.notification(" + title + "," + message + "," + ms + "," + nart + ")")

def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param
              
params=get_params(); url=None; name=None; mode=None; iconimage=None
try:url=urllib.unquote_plus(params["url"])
except:pass
try:name=urllib.unquote_plus(params["name"])
except:pass
try:mode=int(params["mode"])
except:pass
try:iconimage=urllib.unquote_plus(params["iconimage"])
except:pass

print "Mode: "+str(mode); print "Name: "+str(name); print "Thumb: "+str(iconimage)
if mode==None or url==None or len(url)<1:live()
elif mode==1:live()
elif mode==2:getchannels(name,url)
elif mode==3:playstream(url,name)
elif mode==4:vod()
elif mode==5:vodfolders(url,name)
elif mode==6:schedule()







        
xbmcplugin.endOfDirectory(int(sys.argv[1]))
