from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
import random

class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super(ScreenManagement, self).__init__(**kwargs)


class RegisterWindow(Screen):
    def __init__(self, **kwargs):
        super(RegisterWindow, self).__init__(**kwargs)
        self.choise()
        self.show_word = ''
        for char in self.word:
            if char in self.letters:
                self.show_word += char
            else:
                self.show_word += "*"
        self.layout = GridLayout(rows=2, cols=2)

        self.lbl = Label(text=self.show_word)
        self.try_ = Label(text="try")
        self.leter_ti = TextInput(text='Введите букву здесь', multiline=False)
        self.add = Button(text="try letter")

        self.layout.add_widget(self.lbl)
        self.layout.add_widget(self.try_)
        self.layout.add_widget(self.leter_ti)
        self.layout.add_widget(self.add)
        self.add.bind(on_press=self.chek)

        self.add_widget(self.layout)
    def choise(self):
        self.letters = []
        with open("words_en.txt") as file:
            data = file.read()
        words = data.split()
        self.word = random.choice(words)
        print(self.word)

    def chek(self, instance):
        self.letters.append(self.leter_ti.text)
        print(self.letters)
        self.show_word = ""
        for char in self.word:
            if char in self.letters:
                self.show_word += char
            else:
                self.show_word += "*"
            self.lbl.text = self.show_word
        self.leter_ti.text = ""
        if self.show_word.count('*') == 0:
            print("win")
            self.lbl.text = "win"
            self.screen_transition()

    def screen_transition(self, *args):
        self.manager.current = 'login'



class LoginWindow(Screen):
        def __init__(self, **kwargs):
            super(LoginWindow, self).__init__(**kwargs)
            self.layout = GridLayout(rows = 2)
            self.text = Label(text = "You win")
            self.btn2 = Button(text='Restart')
            self.layout.add_widget(self.text)
            self.layout.add_widget(self.btn2)
            self.btn2.bind(on_press = self.screen_transition)
            self.add_widget(self.layout)

        def screen_transition(self, *args):
            self.manager.current = 'register'


class Application(App):
    def build(self):
        sm = ScreenManagement(transition=FadeTransition())
        sm.add_widget(RegisterWindow(name='register'))
        sm.add_widget(LoginWindow(name='login'))

        return sm


if __name__ == "__main__":
    Application().run()