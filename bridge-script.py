#!/usr/local/bin/python3

import subprocess
import sys

subprocess.call("fixedngrok &", shell=True)
subprocess.call("ngrok " + " ".join(sys.argv[1:]), shell=True)