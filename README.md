# StegoCrack
**> Version:** 1.0.0

StegoCrack is a robusttool designed for cracking steganography passwords via dictionary and brute force attacks. Its usability and efficiency make it an essential utility for cybersecurity professionals and enthusiasts interested in the field of steganography.

**Disclaimer: StegoCrack is developed for educational purposes only. The author (@plawlost) is not responsible for any misuse or for any damages resulting from the use of this tool. All users must adhere to local laws and ethical guidelines when using StegoCrack.**

## Installation

Ensure you have **python 3.10** and [steghide](https://github.com/StefanoDeVuono/steghide) installed on your system. 
Clone the repository using the following command:

```git clone https://github.com/plawlost/stegocrack.git```

Navigate into the StegoCrack directory:

```cd stegocrack/StegoCrack```

Install required dependencies with:

```pip install -r requirements.txt```

## Usage

For detailed usage instructions, refer to the [usage guide](StegoCrack/docs/usage.md).

---------------------------------------------

### Quick Start

- Perform a dictionary attack:
```python StegoCrack/src/stegocrack.py dictionary <image_path> <wordlist_path> <output_path>```

- Perform a brute force attack:
```python StegoCrack/src/stegocrack.py brute-force <image_path> <charset> <max_length> <output_path>```


## Development

Refer to [development.md](StegoCrack/docs/development.md) for an overview of the project structure and guidelines on how to contribute to the codebase.

## Contributing

Contributions to StegoCrack are welcome! Please fork the [repository](https://github.com/plawlost/stegocrack), make your changes, and submit a pull request for review.

## License

StegoCrack is released under the MIT License. See the [LICENSE](LICENSE) file for further details.
