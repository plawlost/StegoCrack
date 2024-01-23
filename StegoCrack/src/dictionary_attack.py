import subprocess
import sys

def extract_with_password(image_path, wordlist_path, output_path):
    """
    Attempts to extract hidden data from an image file using passwords from a wordlist.

    :param image_path: Path to the image file with hidden data.
    :param wordlist_path: Path to the wordlist file.
    :param output_path: Path to output the extracted data.
    :return: Returns True if extraction is successful, else False.
    """
    try:
        with open(wordlist_path, 'r') as wordlist:
            for password in wordlist:
                password = password.strip()
                try:
                    subprocess.run(['steghide', 'extract', '-sf', image_path, '-p', password, '-xf', output_path],
                                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    print(f"Success! Password: {password}")
                    return True
                except subprocess.CalledProcessError:
                    continue
        return False
    except FileNotFoundError:
        print("Wordlist file not found.")
        return False

def main():
    if len(sys.argv) != 4:
        print("Usage: python dictionary_attack.py <image_path> <wordlist_path> <output_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    wordlist_path = sys.argv[2]
    output_path = sys.argv[3]

    if not extract_with_password(image_path, wordlist_path, output_path):
        print("Failed to extract with provided wordlist.")

if __name__ == "__main__":
    main()
