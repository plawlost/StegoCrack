import argparse
import sys
from dictionary_attack import extract_with_password
from brute_force_attack import brute_force_attack

def print_header():
    header = """
<!-- ##################################################################### -->
<!-- #                                                                   # -->
<!-- #      ____  _                    ____                _             # -->
<!-- #     / ___|| |_ ___  __ _  ___  / ___|_ __ __ _  ___| | __         # -->
<!-- #     \___ \| __/ _ \/ _` |/ _ \| |   | '__/ _` |/ __| |/ /         # -->
<!-- #      ___) | ||  __/ (_| | (_) | |___| | | (_| | (__|   <          # -->
<!-- #     |____/ \__\___|\__, |\___/ \____|_|  \__,_|\___|_|\_\   V1.0  # -->
<!-- #                    |___/                                          # -->
<!-- #                                                                   # -->
<!-- ##################################################################### -->

<!-- .------------------------------------------------------------------------------. -->
<!-- |                                                                              | -->
<!-- |     ______   __    ____  ____  _        ___        ___     ___  ____ _____   | -->
<!-- |    | __ ) \ / /   / __ \|  _ \| |      / \ \      / / |   / _ \/ ___|_   _|  | -->
<!-- |    |  _ \\ V /   / / _` | |_) | |     / _ \ \ /\ / /| |  | | | \___ \ | |    | -->
<!-- |    | |_) || |   | | (_| |  __/| |___ / ___ \ V  V / | |__| |_| |___) || |    | -->
<!-- |    |____/ |_|    \ \__,_|_|   |_____/_/   \_\_/\_/  |_____\___/|____/ |_|    | -->
<!-- |                   \____/                                                     | -->
<!-- |                                                                              | -->
<!-- '------------------------------------------------------------------------------' -->
    """
    print(header)

def main():
    print_header()

    parser = argparse.ArgumentParser(description="StegoCrack: A Tool for Steganography Password Cracking")
    subparsers = parser.add_subparsers(dest="command")

    # Dictionary attack parser
    dict_parser = subparsers.add_parser('dictionary', help='Perform a dictionary attack')
    dict_parser.add_argument('image_path', help='Path to the image file with hidden data')
    dict_parser.add_argument('wordlist_path', help='Path to the wordlist file')
    dict_parser.add_argument('output_path', help='Path to output the extracted data')

    # Brute force attack parser
    brute_parser = subparsers.add_parser('brute-force', help='Perform a brute force attack')
    brute_parser.add_argument('image_path', help='Path to the image file with hidden data')
    brute_parser.add_argument('charset', help='Character set to use for brute force attack')
    brute_parser.add_argument('max_length', type=int, help='Maximum length of the password')
    brute_parser.add_argument('output_path', help='Path to output the extracted data')

    args = parser.parse_args()

    if args.command == 'dictionary':
        if not extract_with_password(args.image_path, args.wordlist_path, args.output_path):
            print("Failed to extract with provided wordlist.")
    elif args.command == 'brute-force':
        if not brute_force_attack(args.image_path, args.charset, args.max_length, args.output_path):
            print("Failed to extract with brute force attack.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
