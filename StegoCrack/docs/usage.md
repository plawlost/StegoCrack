# StegoCrack Usage Guide

StegoCrack is a tool for steganography password cracking created by @plawlost. ,It provides two modes of attack: 
**- dictionary attack**,
**- brute force attack.**
This guide will help you understand how to use StegoCrack effectively.

## Installation

Before using StegoCrack, make sure you have the following prerequisites installed:

**- Python 3.x**
**- Steghide (for steganography)**

You can install Python from the official website (https://www.python.org/downloads/) and Steghide using your package manager (e.g., `apt-get` on Debian-based systems).

## Usage


### Dictionary Attack

To perform a dictionary attack, use the following command:

**python stegocrack.py dictionary <image_path> <wordlist_path> <output_path>**

- `<image_path>`: Path to the image file with hidden data.
- `<wordlist_path>`: Path to the wordlist file.
- `<output_path>`: Path to output the extracted data.

Example:

**python stegocrack.py dictionary secret_image.jpg wordlist.txt extracted_data.txt**


### Brute Force Attack

To perform a brute force attack, use the following command:

**python stegocrack.py brute-force <image_path> <charset> <max_length> <output_path>**

- `<image_path>`: Path to the image file with hidden data.
- `<charset>`: Character set to use for brute force attack.
- `<max_length>`: Maximum length of the password.
- `<output_path>`: Path to output the extracted data.

Example:

**python stegocrack.py brute-force secret_image.jpg 0123456789 4 extracted_data.txt**
