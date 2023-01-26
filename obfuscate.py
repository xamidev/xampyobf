import argparse
from clint.textui import colored

parser = argparse.ArgumentParser(
    prog = "obfuscator",
    description = "obfuscates code"
)

parser.add_argument('--target', dest="file", action="store_const", required=True)