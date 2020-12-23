# Hello world Kivy app from https://kivy.org/doc/stable/guide/basic.html,
# however, with the following lines removed to prevent conflict with the
# version of Kivy used by buildozer.
#
# import kivy
# kivy.require('1.0.6')


from kivy.uix.label import Label
from kivy.app import App


class MyApp(App):

    def build(self):
        return Label(text='Hello world')


if __name__ == '__main__':
    MyApp().run()
