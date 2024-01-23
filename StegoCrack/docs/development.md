# StegoCrack Development Guide

## Project Structure

### Version: 1.0.0

The StegoCrack project is organized as follows:

**StegoCrack/
│
├── src/
│ ├── stegocrack.py # Main application script.
│ ├── dictionary_attack.py # Dictionary attack module.
│ └── brute_force_attack.py # Brute force attack module.
│
├── wordlists/
│ └── example_wordlist.txt # Example wordlist file of most common 10,000 passwords.
│
├── docs/
│ ├── usage.md # Usage instructions (here).
│ └── development.md # Development notes and documentation.
│
├── requirements.txt # Required Python libraries.
└── README.md # Project description and general information.**


- **src/**: This directory contains the main Python scripts for StegoCrack. `stegocrack.py` is the main application script, while `dictionary_attack.py` and `brute_force_attack.py` are modules for the respective attack methods.

- **wordlists/**: Users can place their wordlist files in this directory, or use the provided `example_wordlist.txt` as a reference.

- **docs/**: Documentation files are stored here. `usage.md` provides usage instructions, while `development.md` contains development notes and guidelines.

- **requirements.txt**: Lists the required Python libraries for the project.

## Development Guidelines

- Follow Python's PEP 8 style guide for code formatting and style.

- Use meaningful variable and function names to enhance code readability.

- Document your code using docstrings for functions and modules.

- Write unit tests to ensure the correctness of your code. Testing is important, even if test files are not included in the project.

- When making significant changes or adding new features, update the documentation accordingly.

- Collaborate with other contributors and follow Git best practices for version control.

- Feel free to propose new features or improvements to the project.

## Contribution

If you'd like to contribute to StegoCrack, please fork the repository, make your changes, and submit a pull request. Your contributions are highly appreciated!

### Github link: https://github.com/plawlost/stegocrack