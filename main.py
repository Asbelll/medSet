import sqlite3
import kivy
import kivymd
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.pickers import MDModalDatePicker
import time
import datetime

kivy.require('1.9.0')
con = sqlite3.connect('medset.db')
cur = con.cursor()

class Login(Screen):
    pass

#Register Screen
class Register(Screen):
    #Gets root access in an easier way
    app = MDApp.get_running_app()
    #Function triggered when pressing ok on the date picker
    #Closes date picker and puts value in the field
    def on_ok(self, instance_date_picker):
        instance_date_picker.dismiss()
        self.app.root.get_screen('register').ids.birthday.text = str(instance_date_picker.get_date()[0].strftime("%d/%m/%Y"))
    
    #Shows calendar, if not focused then closes
    def showCalendar(self, focus):
        if not focus:
            return
        
        date_dialog = MDModalDatePicker()
        date_dialog.bind(on_ok=self.on_ok)
        date_dialog.open()

    #Creates the account and commits to the database
    def createAccount(self):
        bday = self.app.root.get_screen('register').ids.birthday
        name = self.app.root.get_screen('register').ids.user
        if not bday.text or not name.text:
            if not bday.text:
                bday.error = "True"
            if not name.text:
                name.error = "True"
            return

        cur.execute("INSERT INTO user (name, birth) VALUES (?,?)", (name.text, int(time.mktime(datetime.datetime.strptime(bday.text, "%d/%m/%Y").timetuple()))))
        con.commit()
        #add feedback
        self.app.current = 'login'

#Builds and returns root widget
class medset(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Aliceblue"
        Builder.load_file('medset.kv')

        sm = ScreenManager()
        sm.add_widget(Login(name = 'login'))
        sm.add_widget(Register(name = 'register'))
        return sm
    
    
if __name__ == '__main__':    
    medset().run()