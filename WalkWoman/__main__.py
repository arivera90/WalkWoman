import sys
from WalkWoman.animation import *

def main(args=None):
    if args is None:
        args= sys.argv[1:]
    print("Main is alive on fire")
    app = Animation()
    app.run()


if __name__ == '__main__':
    sys.exit(main())