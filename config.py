import sqlite3
import kivy
import kivymd
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.pickers import MDModalDatePicker
import time
import datetime
from kivymd.uix.snackbar import *
from kivymd.uix.menu import MDDropdownMenu

kivy.require('1.9.0')
con = sqlite3.connect('medset.db')
cur = con.cursor()