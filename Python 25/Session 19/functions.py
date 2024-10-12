def calDays(days, courses, hours, schedule, i):
    for j in range(len(days[i])):
        if days[i][j] == 'shanbe':
            ind = checkHour(hours[i][j])
            print(courses[i])
            schedule[0][ind] = courses[i]
        elif days[i][j] == 'yekshanbe':
            ind = checkHour(hours[i][j])
            print(courses[i])
            schedule[1][ind] = courses[i]
        elif days[i][j] == 'doshanbe':
            ind = checkHour(hours[i][j])
            print(courses[i])
            schedule[2][ind] = courses[i]
        elif days[i][j] == 'seshanbe':
            ind = checkHour(hours[i][j])
            print(courses[i])
            schedule[3][ind] = courses[i]
        elif days[i][j] == 'charshanbe':
            ind = checkHour(hours[i][j])
            print(courses[i])
            schedule[4][ind] = courses[i]
        elif days[i][j] == 'panjshanbe':
            ind = checkHour(hours[i][j])
            print(courses[i])
            schedule[5][ind] = courses[i]
        return schedule
            
def checkHour(h) :
    if h == '8':
        return 0
    elif h == '10':
        return 1
    elif h == '12':
        return 2
    elif h == '14':
        return 3
    elif h == '16':
        return 4
    elif h == '18':
        return 5
    
    