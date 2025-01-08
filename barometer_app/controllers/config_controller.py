"""
Controller for managing the serial port configuration and command interactions.
"""

from barometer_app.models.serial_handler import SerialHandler
from barometer_app.views.command_view import CommandView
from barometer_app.views.response_view import ResponseView

class ConfigController:
    """
    Controller for managing configuration logic.
    """

    def __init__(self, view):
        """
        Initializes the ConfigController.

        Args:
            view: The ConfigView instance controlling the UI.
        """
        self.view = view
        self.serial_handler = SerialHandler()
        self.command_window = None
        self.response_window = None
        self.captured_responses = []  # List to store captured responses

    def connect(self):
        """
        Connects to the serial port using parameters from the view and opens command and response windows.
        """
        try:
            # Retrieve serial settings and connect (same as before)
            port = self.view.port_combo.get()  # Selected serial port
            baudrate = int(self.view.baud_rate_combo.get())  # Baud rate
            data_bits = int(self.view.data_bits_combo.get())  # Data bits
            stop_bits = float(self.view.stop_bits_combo.get())  # Stop bits
            parity = self.view.parity_combo.get()  # Parity type
            flow_control = self.view.flow_control_combo.get()  # Flow control

            # Map parity values to pyserial-compatible codes
            parity_map = {
                "None": "N",
                "Even": "E",
                "Odd": "O",
                "Mark": "M",
                "Space": "S"
            }

            # Configure the SerialHandler with the selected parameters
            self.serial_handler.configure(
                port=port,
                baudrate=baudrate,
                parity=parity_map[parity],
                stopbits=stop_bits,
                bytesize=data_bits
            )

            # Open the serial connection
            self.serial_handler.open_connection()
            print(f"Connected to {port} at {baudrate} baud.")

            # Open Command and Response Windows
            title = f"{port} {baudrate} {data_bits} {stop_bits} {parity} {flow_control}"
            self.command_window = CommandView(title, self.serial_handler, self.process_response)  # Pass the callback
            self.response_window = ResponseView(title, self.serial_handler)
        except Exception as e:
            print(f"Failed to connect: {e}")

    def disconnect(self):
        """
        Disconnects the serial port and closes the command and response windows.
        """
        try:
            # Close the serial connection
            self.serial_handler.close_connection()
            print("Disconnected.")

            # Close the command and response windows if open
            if self.command_window:
                self.command_window.destroy()
            if self.response_window:
                self.response_window.destroy()
        except Exception as e:
            print(f"Failed to disconnect: {e}")
            
    def process_response(self, response):
        """
        Processes and stores the captured response from the `?` command and updates the response window.

        Args:
            response (str): The full response captured from the `?` command.
        """
        print("Captured Response:", response)  # Log the response
        self.captured_responses.append(response)  # Store the response

        # Update the Response Window if it is open
        if self.response_window:
            self.response_window.append_response(response)
