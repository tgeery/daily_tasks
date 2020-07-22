# daily_tasks
Track daily tasks that should be completed

# Overview
Store tasks as daily(in repeating.json) or once in a while(in unique.json). The data stores in json where the key represent the key of the task and its value is a UTC timestamp previously completed as shown in the following:
{"feedly": 0, "youtube": {"gdc": 1595447766, "backchannel": 0}, "thehill": 0}

Two operations exist: todo - displays summary, mark - updates history
python3 mark.py gdc
python3 todo.py
Still need to do:
feedly
backchannel
thehill

Congrats completing:
gdc at 12:56:6
