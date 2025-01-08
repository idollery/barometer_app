"""
Handles serial port communication for the barometer application.

Encapsulates logic for opening, closing, configuring, and communicating
over the serial port using the `pyserial` library.
"""

import serial
import time

class SerialHandler:
    """
    Handles serial communication logic.
    """

    def __init__(self):
        """
        Initializes the SerialHandler with a default port as None.
        """
        self.port = None

    def configure(self, port, baudrate, parity, stopbits, bytesize):
        """
        Configures the serial port with the specified parameters.

        Args:
            port (str): Serial port name (e.g., 'COM3' or '/dev/ttyUSB0').
            baudrate (int): Baud rate (e.g., 9600).
            parity (str): Parity (e.g., 'N' for None).
            stopbits (int): Number of stop bits (e.g., 1 or 2).
            bytesize (int): Byte size (e.g., 8).
        """
        self.port = serial.Serial(
            port=port,
            baudrate=baudrate,
            parity=parity,
            stopbits=stopbits,
            bytesize=bytesize,
            timeout=1  # Timeout for read/write operations
        )

    def open_connection(self):
        """
        Opens the serial connection if it is not already open.
        """
        if self.port and not self.port.is_open:
            self.port.open()

    def close_connection(self):
        """
        Closes the serial connection if it is currently open.
        """
        if self.port and self.port.is_open:
            self.port.close()

    def send(self, command):
        """
        Sends a command over the serial connection.

        Args:
            command (str): The command to send as a string.
        """
        if self.port and self.port.is_open:
            self.port.write(command.encode('utf-8'))

    def receive(self):
        """
        Reads a response from the serial connection.

        Returns:
            str: The received response as a string.
        """
        if self.port and self.port.is_open:
            return self.port.read_until().decode('utf-8')
       
    def receive_until_1(self, terminator, timeout=5):
        """
        Reads data from the serial port until a specific terminator is found or timeout occurs.

        Args:
            terminator (str): The character indicating the end of the response.
            timeout (int): Maximum time (in seconds) to wait for the response.

        Returns:
            str: The full response read from the serial port.

        Raises:
            TimeoutError: If the response terminator is not received within the timeout period.
        """
        if self.port and self.port.is_open:
            response = ""
            start_time = time.time()
            while True:
                # Check if timeout has elapsed
                if time.time() - start_time > timeout:
                    raise TimeoutError("Response timeout: Barometer did not respond.")
                
                # Read one byte at a time
                chunk = self.port.read(1).decode('utf-8')
                print(response)
                response += chunk
                
                # Check if the terminator is in the response
                if terminator in response:
                    break
            return response
        return ""
        
    def receive_until(self, terminator=">", timeout=5):
        """
        Reads multiline data from the serial port until a specific terminator is found or timeout occurs.

        Each line from the barometer is terminated with a carriage return (`\r`).

        Args:
            terminator (str): The character indicating the end of the response.
            timeout (int): Maximum time (in seconds) to wait for the response.

        Returns:
            list: A list of response lines read from the serial port.

        Raises:
            TimeoutError: If the terminator is not received within the timeout period.
        """
        if self.port and self.port.is_open:
            response_lines = []
            start_time = time.time()
            current_line = ""

            while True:
                # Check if timeout has elapsed
                if time.time() - start_time > timeout:
                    raise TimeoutError("Response timeout: Barometer did not respond.")

                # Read one byte at a time
                chunk = self.port.read(1).decode('utf-8')
                current_line += chunk

                # If a carriage return (`\r`) is detected, complete the current line
                if chunk == "\r":
                    response_lines.append(current_line.strip())  # Strip trailing `\r`
                    current_line = ""

                # If the terminator is in the current line, stop reading
                if terminator in current_line:
                    response_lines.append(current_line.strip())  # Add the final line
                    break

            return response_lines
        return []
