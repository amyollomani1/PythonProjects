#!/usr/bin/env python3
# above is a shabang line, which says program
# do chmod +x hello.py to change hello.py into executable]
# note: ls-l will ad x to permisions
#use black hello.py to format code


import argparse  # parses command line


def get_args():
    parser = argparse.ArgumentParser(description="Say hello")
    parser.add_argument(
        "-n", "--name", metavar="name", default="World", help="Name to greet"
    )
    return parser.parse_args()


def main():
    args = get_args()
    name = args.name
    print("Hello, " + name + "!")


if __name__ == "__main__":
    main()  # This tells compiler to run the main program
