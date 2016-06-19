import xbmcaddon, util

addon = xbmcaddon.Addon('plugin.audio.radioparadise')

#util.playMedia(addon.getAddonInfo('name'), addon.getAddonInfo('icon'), 
#               'rtmp://stream2.france24.yacast.net:80/france24_live/fr playpath=f24_livefr app=france24_live/fr')
util.playMedia(addon.getAddonInfo('name'), addon.getAddonInfo('icon'),
               'http://stream-uk1.radioparadise.com:80/mp3-128')
