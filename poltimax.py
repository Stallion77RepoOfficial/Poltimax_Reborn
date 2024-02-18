# main imports
import board
import evaluate
import search

# includes
import include.options as options
import include.pieces as pieces
import include.time as time
import include.uci as uci
from include.time import time

ENGINE_NAME = "Poltimax"
ENGINE_VERSION = "0.1"
ENGINE_AUTHOR = "Poltimax Team"
ENGINE_COPYRIGHT = "APACHE 2.0"
COMPILE_DATE = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

while True:
    input_line = input()

    if input_line == "uci":
        print("id name", ENGINE_NAME)
        print("id version", ENGINE_VERSION)
        print("id author", ENGINE_AUTHOR)
        print("id copyright", ENGINE_COPYRIGHT)
        print("id compiling date", COMPILE_DATE)
        print("uciok")
    elif input_line == "isready":
        print("readyok")