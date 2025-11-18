#!/usr/bin/python3
import sys
argv = sys.argv
if len(argv) == 1:
    print("0 arguments.")
else:
    print("{} argument:".format(len(argv) - 1))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
