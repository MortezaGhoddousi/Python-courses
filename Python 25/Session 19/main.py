import functions
import json

data = []
# while True:
#     data.append(input('enter your schedule: '))
#     if data[-1] == 'q':
#         data.pop(len(data)-1)
#         break


file_path = './text.txt'
with open(file_path, 'r') as file:
    data = file.readlines()

data = [line.strip() for line in data]

days = []
courses = []
hours = []
for i in data:
    splittedData = i.split(' ')
    courses.append(splittedData[0])
    if len(splittedData) > 4:
        days.append([splittedData[1], splittedData[4]])
        hours.append([splittedData[2], splittedData[5]])
    else:
        days.append([splittedData[1]])
        hours.append([splittedData[2]])
        
    
    
# schedule = np.zeros([6, 6], dtype=str)
schedule = [[0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0]]

for i in range(len(days)):
    schedule = functions.calDays(days, courses, hours, schedule, i)
    
print(schedule)

json_string = json.dumps(schedule)

print(json_string)

newFile = open('json.json', 'w')
newFile.write(json_string)
        
