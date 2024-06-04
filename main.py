from config import *

app = MDApp.get_running_app()

class Login(Screen):
    pass

#Register Screen
class Register(Screen):
    #Gets root access in an easier way

    #Function triggered when pressing ok on the date picker
    #Closes date picker and puts value in the field
    def on_ok(self, instance_date_picker):
        instance_date_picker.dismiss()
        app.root.get_screen('register').ids.birthday.text = str(instance_date_picker.get_date()[0].strftime("%d/%m/%Y"))
    
    #Shows calendar, if not focused then closes
    def showCalendar(self, focus):
        if not focus:
            return
        
        date_dialog = MDModalDatePicker()
        date_dialog.bind(on_ok=self.on_ok)
        date_dialog.open()

    #Creates the account and commits to the database
    def createAccount(self):
        bday = app.root.get_screen('register').ids.birthday
        name = app.root.get_screen('register').ids.user
        if not bday.text or not name.text:
            if not bday.text:
                bday.error = "True"
            if not name.text:
                name.error = "True"
            return

        cur.execute("INSERT INTO user (name, birth) VALUES (?,?)", (name.text, int(time.mktime(datetime.datetime.strptime(bday.text, "%d/%m/%Y").timetuple()))))
        con.commit()
        self.showSnackBar("Conta criada com sucesso")
        app.root.current = 'login'

    def showSnackBar(self, message):
        MDSnackbar(
            MDSnackbarSupportingText(
                text=message,
            ),
            MDSnackbarButtonContainer(
                MDSnackbarCloseButton(
                    icon="close",
                ),
                pos_hint={"center_y": 0.5}
            ),
            y=24,
            orientation="horizontal",
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
        ).open()

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