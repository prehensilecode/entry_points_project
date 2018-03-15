#!/usr/bin/env python3
import sys

def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    print("This is the main routine.")

def do_something():
    """The do_something routine."""
    print("do_something.")

if __name__ == "__main__":
    main()

