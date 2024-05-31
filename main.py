import sqlite3
import kivy
import kivymd
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.pickers import MDModalDatePicker

kivy.require('1.9.0')

class Login(Screen):
    pass

class Register(Screen):
    pass

class medset(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Aliceblue"
        Builder.load_file('medset.kv')

        sm = ScreenManager()
        sm.add_widget(Login(name = 'login'))
        sm.add_widget(Register(name = 'register'))
        return sm
    
    def on_ok(self, instance_date_picker):
        instance_date_picker.dismiss()
        self.root.get_screen('register').ids.birthday.text = str(instance_date_picker.get_date()[0])

    def showCalendar(self, focus):
        if not focus:
            return
        
        date_dialog = MDModalDatePicker()
        date_dialog.bind(on_ok=self.on_ok)
        date_dialog.open()
        print(self.root.current_screen)
    
medset().run()