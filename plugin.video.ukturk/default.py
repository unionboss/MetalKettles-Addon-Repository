import xbmc,xbmcaddon,xbmcgui,xbmcplugin,urllib,urllib2,os,re,sys,urlresolver
from resources.libs.common_addon import Addon

addon_id        = 'plugin.video.ukturk'
selfAddon       = xbmcaddon.Addon(id=addon_id)
addon           = Addon(addon_id, sys.argv)
fanart          = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
icon            = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
baseurl         = 'http://www.metalkettle.co/UKTurk/Index.txt'
adultopt        = selfAddon.getSetting('adult')
adultpass       = selfAddon.getSetting('password')
iconimage       = addon.queries.get('iconimage', '')

def Index():
        link=open_url(baseurl)	
	match=re.compile('name="(.+?)".+?url="(.+?)".+?img="(.+?)"',re.DOTALL).findall(link)
	for name,url,iconimage in match:
                if not 'XXX' in name:
                        iconimage = iconimage.replace(' ','%20') 
                        url = url.replace(' ','%20')
                        addDir(name,url,1,iconimage,fanart)
                if 'XXX' in name:
                        if adultopt == 'true':
                                if adultpass == '':
                                    dialog = xbmcgui.Dialog()
                                    ret = dialog.yesno('Adult Content', 'You have opted to show adult content','','Please set a password to prevent accidental access','Cancel','Lets Go')
                                    if ret == 1:
                                        keyb = xbmc.Keyboard('', 'Set Password')
                                        keyb.doModal()
                                        if (keyb.isConfirmed()):
                                            passw = keyb.getText()
                                            selfAddon.setSetting('password',passw)      
                                        iconimage = iconimage.replace(' ','%20') 
                                        url = url.replace(' ','%20')
                                        addDir(name,url,1,iconimage,fanart)
                        if adultopt == 'true':
                                if adultpass <> '':
                                        iconimage = iconimage.replace(' ','%20') 
                                        url = url.replace(' ','%20')
                                        addDir(name,url,1,iconimage,fanart)
        addLink('UK Turk Twitter Feed','url',2,'http://www.metalkettle.co/UKTurk/thumbs/twitter.jpg',fanart)
        xbmc.executebuiltin('Container.SetViewMode(500)')
      
def GetChans(url):
        if 'Index' in url:
                CatIndex(url)
        if 'XXX' in url:
                if adultpass <> '':
                        dialog = xbmcgui.Dialog()
                        ret = dialog.yesno('Adult Content', 'Please enter the password you set','to continue','','Cancel','Show me the money')
                        if ret == 1:
                           try:     
                              keyb = xbmc.Keyboard('', 'Set Password')
                              keyb.doModal()
                              if (keyb.isConfirmed()):
                                    passw = keyb.getText()
                              if passw == adultpass:
                                channels = GetList(url)
                                for channel in channels:
                                       addLink(channel["name"],channel["url"],3,iconimage,fanart)
                           except:pass
        else:
                channels = GetList(url)
                for channel in channels:
                        addLink(channel["name"],channel["url"],3,iconimage,fanart)
        xbmc.executebuiltin('Container.SetViewMode(50)')
        
def CatIndex(url):
        link=open_url(url)	
	match=re.compile('name="(.+?)".+?url="(.+?)".+?img="(.+?)"',re.DOTALL).findall(link)
	for name,url,iconimage in match:
                iconimage = iconimage.replace(' ','%20') 
                url = url.replace(' ','%20')
                addDir(name,url,1,iconimage,fanart)
        xbmc.executebuiltin('Container.SetViewMode(50)')








def GetList(url):
	link=open_url(url)	
	matches=re.compile('^#.+?:-?[0-9]*(.*?),(.*?)\n(.*?)$',re.I+re.M+re.U+re.S).findall(link)
	li = []
	for params, name, url in matches:
		item_data = {"params": params, "name": name, "url": url}
		li.append(item_data)
	list = []
	for channel in li:
		item_data = {"name": channel["name"], "url": channel["url"]}
		matches=re.compile(' (.+?)="(.+?)"',re.I+re.M+re.U+re.S).findall(channel["params"])
		for field, value in matches:
			item_data[field.strip().lower().replace('-', '_')] = value.strip()
		list.append(item_data)
	return list
             
def PLAYLINK(url):
            
            if urlresolver.HostedMediaFile(url).valid_url():
                streamurl = urlresolver.HostedMediaFile(url).resolve()
            else: streamurl=url 
            ok=True
            liz=xbmcgui.ListItem(name, iconImage=iconimage,thumbnailImage=iconimage); liz.setInfo( type="Video", infoLabels={ "Title": name } )
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=streamurl,listitem=liz)
            try:
                xbmc.Player ().play(streamurl, liz, False)
                return ok
            except:
                pass
            
def TWITTER():
        text = ''
        twit = 'https://script.google.com/macros/s/AKfycbyBcUa5TlEQudk6Y_0o0ZubnmhGL_-b7Up8kQt11xgVwz3ErTo/exec?588677963413065728'
        link = open_url(twit)
        link = link.replace('/n','')
        link = link.decode('utf-8').encode('utf-8').replace('&#39;','\'').replace('&#10;',' - ').replace('&#x2026;','')
        match=re.compile("<title>(.+?)</title>.+?<pubDate>(.+?)</pubDate>",re.DOTALL).findall(link)[1:]
        for status, dte in match:
            try:
                            status = status.decode('ascii', 'ignore')
            except:
                            status = status.decode('utf-8','ignore')
            dte = dte[:-15]
            status = status.replace('&amp;','')
            dte = '[COLOR blue][B]'+dte+'[/B][/COLOR]'
            text = text+dte+'\n'+status+'\n'+'\n'
        showText('[COLOR blue][B]@uk_turk[/B][/COLOR]', text)

def showText(heading, text):
    id = 10147
    xbmc.executebuiltin('ActivateWindow(%d)' % id)
    xbmc.sleep(100)
    win = xbmcgui.Window(id)
    retry = 50
    while (retry > 0):
        try:
            xbmc.sleep(10)
            retry -= 1
            win.getControl(1).setLabel(heading)
            win.getControl(5).setText(text)
            return
        except:
            pass
                                     
def open_url(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        link = link.replace('\r','').replace('\t','').replace('&nbsp;','').replace('\'','')
        response.close()
        return link

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
               
def addDir(name,url,mode,iconimage,fanart,description=''):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def addLink(name,url,mode,iconimage,fanart,description=''):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok

params=get_params(); url=None; name=None; mode=None; site=None; iconimage=None
try: site=urllib.unquote_plus(params["site"])
except: pass
try: url=urllib.unquote_plus(params["url"])
except: pass
try: name=urllib.unquote_plus(params["name"])
except: pass
try: mode=int(params["mode"])
except: pass
try: iconimage=urllib.unquote_plus(params["iconimage"])
except: pass
 
print "Site: "+str(site); print "Mode: "+str(mode); print "URL: "+str(url); print "Name: "+str(name)
 
if mode==None or url==None or len(url)<1: Index()
elif mode==1:GetChans(url)
elif mode==2:TWITTER()
elif mode==3:PLAYLINK(url)



xbmcplugin.endOfDirectory(int(sys.argv[1]))
