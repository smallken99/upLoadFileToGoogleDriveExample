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
import doanloadMyMoneydb as dl
def say_hello(systray):
    print("Hello, World!")
menu_options = ( ("檔案上傳",None,up.main),
		("檔案下載", None, dl.main))
systray = SysTrayIcon("icon/scriptx.ico", "Example tray icon", menu_options)
systray.start()