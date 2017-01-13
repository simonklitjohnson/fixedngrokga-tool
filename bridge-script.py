#!/usr/local/bin/python3

import subprocess
import sys

subprocess.call("fixedngrokga &", shell=True)
subprocess.call("ngrok " + " ".join(sys.argv[1:]), shell=True)