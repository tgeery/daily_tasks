# daily_tasks
Track daily tasks that should be completed

# Overview
Store tasks as daily(in repeating.json) or once in a while(in unique.json). The data stores in json where the key represent the key of the task and its value is a UTC timestamp previously completed as shown in the following:<br/>
{<br/>
&nbsp;&nbsp;"feedly": 0, <br/>
&nbsp;&nbsp;"youtube": {<br/>
&nbsp;&nbsp;&nbsp;&nbsp;"gdc": 1595447766, <br/>
&nbsp;&nbsp;&nbsp;&nbsp;"backchannel": 0<br/>
&nbsp;&nbsp;}, <br/>
&nbsp;&nbsp;"thehill": 0<br/>
}<br/>

Two operations exist: todo - displays summary, mark - updates history<br/>
python3 mark.py gdc<br/>
python3 todo.py<br/>
&nbsp;&nbsp;Still need to do:<br/>
&nbsp;&nbsp;feedly<br/>
&nbsp;&nbsp;backchannel<br/>
&nbsp;&nbsp;thehill<br/>

&nbsp;&nbsp;Congrats completing:<br/>
&nbsp;&nbsp;gdc at 12:56:6
