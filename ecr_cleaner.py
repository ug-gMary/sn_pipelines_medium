#!/usr/bin/python

import sys

action = sys.argv[1] 

print("The python script has been invoked with action:",action)

def test_function (action):
    if action == 'dev':
        print("The python script has been invoked in dev")
    if action == 'prod':
        print("The python script has been invoked in prod")

test_function (action)
