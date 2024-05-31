import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

kivy.require('1.9.0')

Window.clearcolor = (0.5,0.5,0.5)
Window.size = (360,600)

class myClass(BoxLayout):

    def __init__(self):
        super(myClass, self).__init__()

    def change_label(self):
        self.ids.input_label.text = str(self.ids.input_text.text)

class medSet(App):
    def build(self):
        return myClass()
    
ms = medSet()
ms.run()