from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput

class HomeScreen(Screen):
    pass

class SettingScreen(Screen):
    pass

class NewDoeScreen(Screen):
    pass

GUI = Builder.load_file("main.kv")

class MainApp(App):
    def build(self):
        return GUI

    '''Change the screens'''
    def change_screen(self, screen_name):
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen_name

    '''How many factors we have for the DOE'''
    def select_factor_counts(self, text):
        return text

    def add_factor_names(self, text):
        for i in range(int(text)):
            textinput = TextInput()
            self.root.ids.new_doe_faktor_name.add_widget(textinput)
            
MainApp().run()