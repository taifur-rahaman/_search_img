<h1 align="center"> Searching Image from Web using a GUI interface</h1>

An app that lets the user provide an input of an image name in a Screen and the app will produce the get the image link
from a wikipedia library. After that the image information will be downloaded to a file that will write the information
in a "Byte" file which the user will be able to see in the GUI interface by pressing the search button.

<h3> Objects </h3>

    Nouns:
        1. App - Object 1
        2. Screen - Object 2
        3. Image Link - Method of Screen
        4. Downloading Image - Method of Screen
        5. Setting the Image in Button - Method of Screen

Object Design

    App:
        build # Default kivy method for running the GUI interface
    
    RootWidget:
        # Default kivy object for running the GUI interface
        pass # It should be left alone if their ain't any specific work for it

    Screen:
        get_image_link
        download_image
        show_image
        