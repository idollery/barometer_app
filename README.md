# Barometer Application

This Python application connects to a **Vaisala PTB330 barometer** over a serial port (RS232) and allows users to send commands and receive responses. The application features a user-friendly interface with separate windows for sending commands, displaying responses, and configuring the serial connection.

---

## Features

- **Serial Port Configuration**: Select an available serial port and configure parameters (baud rate, parity, stop bits).
- **Command and Response Display**: Send text commands to the barometer and view responses in separate windows.
- **Connection Management**: Open and close the serial connection with a single button.
- **Modular Design**: Separates business logic, user interface, and control logic for maintainability and scalability.

---

## Prerequisites

Before running the application, ensure you have the following installed:

- **Python 3.8 or higher**
- **Required Python Packages**:
  - `pyserial` (for serial communication)
  - `tkinter` (for the graphical user interface)

You can install the required packages using the following command:

pip install pyserial

## Directory Structure

barometer_app/
├── barometer_app/                  # Main application package
│   ├── model/                      # Business logic and data handling
│   ├── view/                       # User interface components
│   ├── presenter/                  # Mediator between Model and View
│   └── utils/                      # Utility functions and helpers
├── tests/                          # Unit and integration tests
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
└── setup.py                        # Installation script (optional)

## Installation

- 1. Clone the repository:

    git clone https://github.com/yourusername/barometer_app.git
    cd barometer_app

- 2. Install the required dependencies:
    
    pip install -r requirements.txt

- 3. Run the application:
 
    python -m barometer_app.main

## Usage

- 1. Launch the Application:

        Run the program using the command above. The main window will open.

- 2. Configure Serial Port:

        Open the Serial Configuration Window.

        Select an available serial port from the dropdown menu.

        Set the serial parameters (baud rate, parity, stop bits).

        Click Open Connection to establish a connection to the barometer.

- 3. Send Commands:

        Enter a command in the Command Window and press Send.

        The sent command and the barometer's response will be displayed in their respective windows.

- 4. Close Connection:

        When done, click Close Connection in the Serial Configuration Window to disconnect from the barometer.

## Testing

	python -m pytest tests/
	
## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

    Fork the repository.

    Create a new branch for your feature or bugfix.

    Commit your changes and push to the branch.

    Submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- ** Vaisala for manufacturing the PTB330 barometer.**
- ** pyserial for providing an easy-to-use serial communication library.**
- ** Tkinter for enabling the creation of a graphical user interface.**