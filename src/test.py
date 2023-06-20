from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.storage.jsonstore import JsonStore
from kivy.lang import Builder
from kivy.core.window import Window
#Windown config
Window.size = (310, 580)

class LoginPage(MDScreen):
    def __init__(self, **kw) -> None:
        super(LoginPage, self).__init__(**kw)
        self.name="login-page"
    def toSignup(self) -> None:
        self.manager.transition.direction = "left"
        self.manager.current = "signup-page"

class HomePage(MDScreen):
    def __init__(self, **kw) -> None:
        super(HomePage, self).__init__(**kw)
        self.name = "home-page"
    def logOut(self) -> None:
        self.manager.transition.direction = 'right'
        self.manager.current = 'login_screen'

class DevideControlPage(MDScreen):
    def __init__(self, **kw):
        super(DevideControlPage, self).__init__(**kw)
        self.name = "devicecontrol-page"

class SignUpPage(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.name = "signup-page"
    def toLogin(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login-page"
class MobileApp(MDApp):
    title = "Smart Home Camera"
    def __init__(self, **kwargs):
        """
            [constant] sm: ScreenManager
            [constant] self.SCREENS: dict
            key: screen instance
            value: path to kivy file
        """
        super().__init__(**kwargs)
        self.sm = ScreenManager()
        self.SCREENS = {
            LoginPage: "./kv_folder/LoginPage.kv",
            SignUpPage: "./kv_folder/SignUpPage.kv",
            HomePage: "./kv_folder/HomePage.kv",
            DevideControlPage: "./kv_folder/DeviceControlPage.kv",
        }
    def build(self):
        self.addMultipleWidgets()
        self.sm.current = "login-page"
        return self.sm
    def addMultipleWidgets(self):
        for screen, path in self.SCREENS.items():
            try:
                Builder.load_file(path)
            except Exception as err:
                exit(err)
            screen.kv_file = path
            self.sm.add_widget(screen())
if __name__ == '__main__':
    MobileApp().run()