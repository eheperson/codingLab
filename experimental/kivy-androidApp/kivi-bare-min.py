import kivy
kivy.require('2.0.0') # replace with your current kivy version !
#
from kivy.app import App
from kivy.uix.label import Label
#
##
# Creating a kivy application is as simple as:
#     1- sub-classing the App class
#     2- implementing its build() method so it returns a Widget instance (the root of your widget tree)
#     3- instantiating this class, and calling its run() method.
#
class MyApp(App): # sub-classing the App class
    #
    def build(self):
        # implementing its build() method so it returns a Widget instance (the root of your widget tree)
        return Label(text='Hello world')
    #
#
if __name__ == '__main__':
    MyApp().run() # instantiating this class, and calling its run() method.
    #