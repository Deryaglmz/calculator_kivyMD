from kivy.app import App
from kivy.metrics import dp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.colorpicker import ColorPicker

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDRectangleFlatButton
import threading

import scripts.calculateFunctions as calculateFunctions

Builder.load_file('main.kv')
Window.size = (450, 530)

class MainScreen(MDScreen):

    def clear(self):
        threading.Thread(calculateFunctions.clearFunc(self)).daemon=True
    
    def button_release(self,button):
        threading.Thread(calculateFunctions.button_releaseFunc(self,button)).daemon=True

    def math_sign(self, sign):
        threading.Thread(calculateFunctions.math_signFunc(self,sign)).daemon=True

    def equals(self):
        threading.Thread(calculateFunctions.equalsFunc(self)).daemon=True

class Myapp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"

        sm = MDScreenManager(size_hint=(1, 1))
        sm.add_widget(MainScreen(name="mainScreen"))
        return sm

if __name__ == "__main__":
    Myapp().run() 