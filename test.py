import sys

action = sys.argv[1] 

def test_function (action):
    if action == 'stop':
        print("The Astra Dev Environment is stopped")
    if action == 'start':
        print("The Astra Dev Environment is started")
    if action == 'status':
        print("The Astra Dev Environment status is displayed")

print("The python script has been invoked")
test_function (action)