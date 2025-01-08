"""
Controller for managing the serial port configuration.

Handles user interactions from the configuration view and interacts with the
SerialHandler to configure and connect to the serial port.
"""

from barometer_app.models.serial_handler import SerialHandler

class ConfigController:
    """
    Controller for managing configuration logic.
    """

    def __init__(self, view):
        """
        Initializes the ConfigController with a reference to the view and creates
        an instance of the SerialHandler.

        Args:
            view: The view component responsible for the configuration UI.
        """
        self.view = view
        self.serial_handler = SerialHandler()

    def connect(self):
        """
        Connects to the serial port using parameters set in the view.
        """
        try:
            # Get port and baud rate values from the UI inputs
            port = self.view.port_entry.get()
            baudrate = int(self.view.baud_rate_entry.get())
            
            # Configure the serial handler
            self.serial_handler.configure(port, baudrate, 'N', 1, 8)
            
            # Open the serial connection
            self.serial_handler.open_connection()
            
            print("Connection successfully opened!")  # Log success (could be replaced by a UI notification)
        except Exception as e:
            print(f"Failed to connect: {e}")  # Log the error (could be replaced by a UI error message)
