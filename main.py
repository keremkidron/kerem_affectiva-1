import json
import matplotlib.pyplot as plt

subject_id = 1024

x = json.load((open('data/%d.0.json' % subject_id)))
# x[step_id] = (time, affectiva)

# example:
step_id = '0'
time_step = 0
time_stamp = x[step_id][time_step][0]
aff = x[step_id][time_step][1]
expression = aff['expressions']
emotions = aff['emotions']
print(time_stamp)
print(emotions[7])

x_axis = [x[step_id][i][0] for i in range(len(x))]
y_axis = [x[step_id][i][1]['emotions'][7] for i in range(len(x))]

print(x_axis)
print(y_axis)
plt.plot(x_axis,y_axis)
plt.show() 
