import os
import urllib.request

pf = 'Package Control.sublime-package'
ipp = '/Users/chenshunliang/Library/Application Support/Sublime Text 3/Installed Packages'
urllib.request.install_opener(urllib.request.build_opener(urllib.request.ProxyHandler()))
open(os.path.join(ipp, pf), 'wb').write(
    urllib.request.urlopen('http://sublime.wbond.net/' + pf.replace(' ', '%20')).read())
