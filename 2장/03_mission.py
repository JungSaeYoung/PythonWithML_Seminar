filename = "03_mission.py"

f = open(filename)
lines = []
for line in f:
    lines.append(line.strip())
print(lines)

"""
['filename = "03_mission.py" # this code',
'',
'f = open(filename)',
'lines = []',
'for line in f:',
'lines.append(line.strip())',
'',
'print(lines)']
"""