from WalkWoman.animation import *
import sys


def main(args=None):
    if args is None:
        args= sys.argv[1:]
    print("WalkWoman is running.")
    app = Animation()
    app.run()


if __name__ == '__main__':
    sys.exit(main())