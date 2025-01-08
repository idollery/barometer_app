from setuptools import setup, find_packages

# Read the contents of the README file
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="barometer_app",  # Name of the package
    version="0.1.0",  # Version of the package
    author="Your Name",  # Your name or organization
    author_email="your.email@example.com",  # Your email
    description="A Python application to communicate with a Vaisala PTB330 barometer over RS232.",  # Short description
    long_description=long_description,  # Long description from README.md
    long_description_content_type="text/markdown",  # Format of the long description
    url="https://github.com/yourusername/barometer_app",  # Project URL
    packages=find_packages(where="barometer_app"),  # Automatically find packages
    package_dir={"": "barometer_app"},  # Root directory for packages
    include_package_data=True,  # Include non-Python files specified in MANIFEST.in
    install_requires=[  # List of dependencies
        "pyserial>=3.5",  # Serial communication library
    ],
    classifiers=[  # Metadata about the project
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",  # Minimum Python version required
    entry_points={  # Define command-line scripts
        "console_scripts": [
            "barometer-app=barometer_app.main:main",  # Command to run the application
        ],
    },
)