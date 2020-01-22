<<<<<<< HEAD
'''
There are (at least) a couple of libraries openly available for this now:
* pystray
* infi.systray
I just started using infi.systray in a project, and it's worked well for me. Here's how little code you need to do something very basic (taken from their docs):
from infi.systray import SysTrayIcon
def say_hello(systray):
    print("Hello, World!")
menu_options = (("Say Hello", None, say_hello),)
systray = SysTrayIcon("icon.ico", "Example tray icon", menu_options)
systray.start()


'''
from infi.systray import SysTrayIcon
import uploadMyMoneydb as up
def say_hello(systray):
    print("Hello, World!")
menuList = ()
 
menu_options = (("Say Hello", None, say_hello),
		("檔案上傳",None,up.main)
	)
systray = SysTrayIcon("icon/scriptx.ico", "Example tray icon", menu_options)
=======
'''
There are (at least) a couple of libraries openly available for this now:
* pystray
* infi.systray
I just started using infi.systray in a project, and it's worked well for me. Here's how little code you need to do something very basic (taken from their docs):
from infi.systray import SysTrayIcon
def say_hello(systray):
    print("Hello, World!")
menu_options = (("Say Hello", None, say_hello),)
systray = SysTrayIcon("icon.ico", "Example tray icon", menu_options)
systray.start()


'''
from infi.systray import SysTrayIcon
import uploadMyMoneydb as up
def say_hello(systray):
    print("Hello, World!")
menuList = ()
 
menu_options = (("Say Hello", None, say_hello),
		("檔案上傳",None,up.main)
	)
systray = SysTrayIcon("icon/scriptx.ico", "Example tray icon", menu_options)
>>>>>>> 838e42868da025d6a072c605a558b80b50910bfd
systray.start()