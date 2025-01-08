"""
UI for the command input window.

Allows users to type and send commands to the connected serial port and send a predefined `?` command.
"""

import tkinter as tk
import tkinter.messagebox as messagebox
import threading

class CommandView(tk.Toplevel):
    """
    A window for sending commands to the serial port.
    """

    def __init__(self, title, serial_handler, process_response_callback):
        """
        Initializes the command window.

        Args:
            title (str): The title of the window (concatenated serial parameters).
            serial_handler: The SerialHandler instance for communication.
            process_response_callback: Callback function to process the captured response.
        """
        super().__init__()
        self.title(title)
        self.serial_handler = serial_handler
        self.process_response_callback = process_response_callback  # Callback to process responses

        # Textbox for Command Input
        self.command_entry = tk.Entry(self, width=50)
        self.command_entry.pack(pady=10)
        self.command_entry.bind("<Return>", self.send_command)

        # Button to Send `?` Command
        self.send_question_button = tk.Button(self, text="Send ? Command", command=self.send_question_command)
        self.send_question_button.pack(pady=10)

    def send_command(self, event=None):
        """
        Sends the command from the entry to the serial port.

        Args:
            event: The event triggering this action.
        """
        command = self.command_entry.get() + "\r\n"  # Append CRLF
        if self.serial_handler and self.serial_handler.port and self.serial_handler.port.is_open:
            self.serial_handler.send(command)
        self.command_entry.delete(0, tk.END)  # Clear the input field

    def send_question_command(self):
        """
        Sends the `?` command to the serial port and processes the response in a separate thread.
        """
        def process_command():
            try:
                # Send the `?` command and capture the response
                command = "?\r\n"
                if self.serial_handler and self.serial_handler.port and self.serial_handler.port.is_open:
                    self.serial_handler.send(command)
                    response = self.serial_handler.receive_until(">", timeout=5)  # 5-second timeout

                    # Process the captured response on the main thread
                    self.process_response_callback(response)
            except TimeoutError as e:
                # Display a timeout error message
                messagebox.showerror("Timeout", str(e))

        # Start the process in a separate thread
        threading.Thread(target=process_command, daemon=True).start()