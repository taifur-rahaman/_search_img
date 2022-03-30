from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


class Hero_Screen(Screen):
    """
    Hero_Screen is an object that inherited the methods from the *Screen* class of *kivy.uix.screenmanager* package. This class determine the action of the Hero Screen (First Screen) of the GUI interface.
    """

    def get_image_link(self):
        """
        get_image_link gets user query from the TextInput of Kivy file and find the image from the wikipedia package
        """
        pass

    def download_image(self):
        """
        download_image gets the image information in a byte form using the *request* package and convert the byte information into an image file
        """
        pass

    def show_image(self):
        """
        show_image transfer the image in the kivy GUI interface and shows the image
        """
        pass


class RootWidget(ScreenManager):
    """
    RootWidget is a Required Object that is needed for running the GUI interface screen and the methods of this object is being inherited from the *ScreenManager* class of the *kivy.uix.screenmanager* package
    """
    pass


class MainApp(App):
    """
    MainApp is the Required Kivy Object for running the App
    """

    def build(self):
        """
        build is a method that has been inherited from the *App* class from the *kivy.app package
        """
        return RootWidget()
