# hello_python.py
import sys

def main(argv):
    if len(argv) > 1:
        print(f"Hello, {argv[1]}")
    else:
        print("Hello, World")
        

if __name__ == "__main__":
    main(sys.argv)
