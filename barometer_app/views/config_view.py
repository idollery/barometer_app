"""
UI for configuring the serial port.
"""

import tkinter as tk
from tkinter import ttk
import serial.tools.list_ports

class ConfigView(tk.Frame):
    """
    A view for configuring serial port settings.
    """

    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller(self)

        # Serial Port Selection
        ttk.Label(self, text="Serial Port").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.port_combo = ttk.Combobox(self, values=self.get_available_ports(), state="readonly", width=20)
        self.port_combo.grid(row=0, column=1, padx=10, pady=5)
        self.port_combo.set("COM2")

        # Baud Rate Selection
        ttk.Label(self, text="Baud Rate").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.baud_rate_combo = ttk.Combobox(self, values=[9600, 19200, 38400], state="readonly")
        self.baud_rate_combo.grid(row=1, column=1, padx=10, pady=5)
        self.baud_rate_combo.set(9600)

        # Data Bits Combo Box
        ttk.Label(self, text="Data Bits").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.data_bits_combo = ttk.Combobox(self, values=[5, 6, 7, 8], state="readonly")
        self.data_bits_combo.grid(row=2, column=1, padx=10, pady=5)
        self.data_bits_combo.set(7)  # Default value is 7 data bits

        # Stop Bits Combo Box
        ttk.Label(self, text="Stop Bits").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.stop_bits_combo = ttk.Combobox(self, values=[1, 1.5, 2], state="readonly")
        self.stop_bits_combo.grid(row=3, column=1, padx=10, pady=5)
        self.stop_bits_combo.set(1)  # Default value is 1 stop bit

        # Parity Combo Box
        ttk.Label(self, text="Parity").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.parity_combo = ttk.Combobox(self, values=["None", "Even", "Odd", "Mark", "Space"], state="readonly")
        self.parity_combo.grid(row=4, column=1, padx=10, pady=5)
        self.parity_combo.set("Even")  # Default value is Even parity

        # Flow Control Combo Box
        ttk.Label(self, text="Flow Control").grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.flow_control_combo = ttk.Combobox(self, values=["None", "XON/XOFF", "RTS/CTS", "DTR/DSR"], state="readonly")
        self.flow_control_combo.grid(row=5, column=1, padx=10, pady=5)
        self.flow_control_combo.set("None")  # Default value is no flow control

        # Connect and Disconnect Buttons
        self.connect_button = ttk.Button(self, text="Connect", command=self.controller.connect)
        self.connect_button.grid(row=6, column=0, columnspan=2, pady=10)

        self.disconnect_button = ttk.Button(self, text="Disconnect", command=self.controller.disconnect)
        self.disconnect_button.grid(row=7, column=0, columnspan=2, pady=10)

    def get_available_ports(self):
        """
        Lists available serial ports.
        """
        ports = serial.tools.list_ports.comports()
        return [port.device for port in ports] or ["COM2"]
