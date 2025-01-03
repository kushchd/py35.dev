#
import sys

def main():
    if len(sys.argv) != 2 or sys.argv[1] in ("-h", "--help"):
        print("usage: square.py number [-h]")
        print("\n  positional arguments:")
        print("    number         display a square of a given number")
        print("\n  options:")
        print("    -h | --help  show this help message and exit")
    else:
        try:
            number = float(sys.argv[1])
            print(f"The square of {number} is {number**2}")
        except ValueError:
            print("Please provide a valid number.")

if __name__ == "__main__":
    main()
