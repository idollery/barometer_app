"""
Start point for the Barometer Communications Application.
"""

from barometer_app.controllers.main_controller import MainController

if __name__ == "__main__":
    # Initialize and run the main controller
    app = MainController()
    app.run()