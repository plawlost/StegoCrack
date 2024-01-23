import itertools
import string
import subprocess
import sys

def brute_force_attack(image_path, charset, max_length, output_path):
    for length in range(1, max_length + 1):
        for password in itertools.product(charset, repeat=length):
            password = ''.join(password)
            try:
                subprocess.run(['steghide', 'extract', '-sf', image_path, '-p', password, '-xf', output_path],
                               check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                print(f"Success! Password: {password}")
                return True
            except subprocess.CalledProcessError:
                continue
    return False

def main():
    if len(sys.argv) != 5:
        print("Usage: python brute_force_attack.py <image_path> <charset> <max_length> <output_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    charset = sys.argv[2]
    max_length = int(sys.argv[3])
    output_path = sys.argv[4]

    if not brute_force_attack(image_path, charset, max_length, output_path):
        print("Failed to extract with brute force attack.")

if __name__ == "__main__":
    main()
