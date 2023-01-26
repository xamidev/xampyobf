import argparse
import py_compile
from clint.textui import colored

# Argument parsing

parser = argparse.ArgumentParser(description='Obfuscates Python code')
parser.add_argument('-t', '--target')
args = parser.parse_args()
file = args.target

py_compile.compile(file, cfile=f"{file[:-3]}-obf.py")