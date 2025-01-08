"""
Main controller that orchestrates the application.
"""

from tkinter import Tk
from barometer_app.views.config_view import ConfigView
from barometer_app.controllers.config_controller import ConfigController

class MainController:
    def __init__(self):
        """
        Initializes the main controller and sets up the application window.
        """
        self.root = Tk()
        self.root.title("Barometer Control App")

        # Initialize views and controllers
        config_view = ConfigView(self.root, ConfigController)
        config_view.pack(padx=10, pady=10)

    def run(self):
        """
        Runs the Tkinter main event loop.
        """
        self.root.mainloop()
