#!/usr/bin/env python3

#Author ID: 103021226

#imports
import os

#variables/inputs/functions

def free_space():

    bashcommand = os.popen("df -h | grep '/$' | awk '{print $4}'").read()
    bashclean = bashcommand[0].decode('utf-8').strip()
    return bashcommand

#Script
print(free_space)
