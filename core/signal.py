#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Capture SIGINT signal.
Thread safe with Ctrl+C
"""
import signal
interrupted = False

def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    global interrupted
    interrupted = True

signal.signal(signal.SIGINT, signal_handler)

print('Press Ctrl+C')
while True:
    if interrupted:
        sys.exit(0)