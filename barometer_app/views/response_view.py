"""
UI for the response display window.

Displays responses received from the connected serial port and allows scrolling
and resizing.
"""

import tkinter as tk
from tkinter import ttk
from threading import Thread

class ResponseView(tk.Toplevel):
    """
    A window for displaying responses from the serial port.
    """

    def __init__(self, title, serial_handler):
        """
        Initializes the response window.

        Args:
            title (str): The title of the window (concatenated serial parameters).
            serial_handler: The SerialHandler instance for communication.
        """
        super().__init__()
        self.title(title)
        self.serial_handler = serial_handler
        self.running = True

        # Configure resizing for the Toplevel window
        self.rowconfigure(0, weight=1)  # Allow frame to resize vertically
        self.columnconfigure(0, weight=1)  # Allow frame to resize horizontally

        # Frame for the text widget and scrollbar
        frame = ttk.Frame(self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.rowconfigure(0, weight=1)  # Allow text widget to resize vertically
        frame.columnconfigure(0, weight=1)  # Allow text widget to resize horizontally

        # Text widget for displaying responses
        self.response_display = tk.Text(frame, wrap="word", width=60, height=20, state="disabled")
        self.response_display.grid(row=0, column=0, sticky="nsew")  # Expand to fill space

        # Scrollbar for the text widget
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.response_display.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.response_display.configure(yscrollcommand=scrollbar.set)

        # Start a background thread to read responses
        self.reader_thread = Thread(target=self.read_responses, daemon=True)
        self.reader_thread.start()

    def read_responses(self):
        """
        Continuously reads responses from the serial port and updates the display.
        """
        while self.running:
            if self.serial_handler and self.serial_handler.port and self.serial_handler.port.is_open:
                response = self.serial_handler.receive()
                if response:
                    self.update_response_display(response)

    def update_response_display(self, response):
        """
        Updates the response display with new data.

        Args:
            response (str): The received response to display.
        """
        self.response_display.config(state="normal")  # Enable text widget for editing
        self.response_display.insert(tk.END, response + "\n")  # Insert new response
        self.response_display.config(state="disabled")  # Disable text widget to prevent user editing
        self.response_display.see(tk.END)  # Automatically scroll to the bottom

    def destroy(self):
        """
        Cleans up the response window and stops the reader thread.
        """
        self.running = False
        super().destroy()
        
    def append_response(self, response):
        """
        Appends a new response to the display.

        Args:
            response (str): The response string to append.
        """
        self.response_display.config(state="normal")  # Enable editing
        self.response_display.insert(tk.END, response + "\n")  # Append response
        self.response_display.config(state="disabled")  # Disable editing
        self.response_display.see(tk.END)  # Scroll to the latest response
