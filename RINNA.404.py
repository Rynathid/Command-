import os, sys
try:
    __import__("RYnna").login()
except Exception as e:
    exit(str(e))
