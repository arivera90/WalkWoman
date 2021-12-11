import sys

def main(args=None):
    if args is None:
        args= sys.argv[1:]
    print("Main is alive")


if __name__ == '__main__':
    sys.exit(main())