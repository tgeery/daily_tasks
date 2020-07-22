# daily_tasks
Track daily tasks that should be completed

# Overview
Store tasks as daily(in repeating.json) or once in a while(in unique.json). The data stores in json where the key represent the key of the task and its value is a UTC timestamp previously completed as shown in the following:
{<br/>
"feedly": 0, <br/>
"youtube": <br/>
{"gdc": 1595447766, <br/>
"backchannel": 0}, </br>
"thehill": 0</br>
}</br>

Two operations exist: todo - displays summary, mark - updates history<br/>
python3 mark.py gdc<br/>
python3 todo.py<br/>
Still need to do:<br/>
feedly<br/>
backchannel<br/>
thehill<br/>

Congrats completing:<br/>
gdc at 12:56:6
