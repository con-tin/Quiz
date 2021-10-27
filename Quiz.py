from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

import random

# letters = []
# global word
# turn = 0
# global show_woard


class Game(App):
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
            turn = 50
        # turn += 1
        

    def build(self):
        self.choise()
        self.show_word = ''
        for char in self.word:
            if char in self.letters:
                self.show_word += char
            else:
                self.show_word += "*"
        layout = GridLayout(rows=2, cols=2)

        self.lbl = Label(text=self.show_word)
        self.try_ = Label(text="try")
        self.leter_ti = TextInput(text='Введите букву здесь', multiline=False)
        self.add = Button(text="try letter")

        layout.add_widget(self.lbl)
        layout.add_widget(self.try_)
        layout.add_widget(self.leter_ti)
        layout.add_widget(self.add)
        self.add.bind(on_press=self.chek)
        return layout
        

       

    def choise(self):
        self.letters = []
##        global word
        with open("words_en.txt") as file:
            data = file.read()
        words = data.split()
        self.word = random.choice(words)
        print(self.word)


if __name__ == '__main__':
    Game().run()

# show_woard_str = " ".join(show_word)
# print(show_woard_str)
# show_woard_str = " ".join(show_word)
# print(show_woard_str)
