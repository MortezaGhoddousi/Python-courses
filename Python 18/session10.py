import numpy as np

# print(numpy.pi)

def cal_circle(r):
    primeter = 2*r*np.pi
    area = np.pi*(r**2)
    return primeter, area

r = float(input("Enter the radius: "))
primeter, area = cal_circle(r)

if area > 50:
    print(f"Radius {r} with an area of {area} is OK")


def can_avg_min_max(mylist):
    sum = 0
    Max = -1
    Min = 21
    for score in mylist:
        sum = sum+score
        if score > Max:
            Max = score
        if score < Min:
            Min = score
    average = sum/len(mylist)
    return average, Max, Min

mylist = [20, 19, 19.5]

average, Max, Min = can_avg_min_max(mylist)

print(f"Average is {average}, Maximum number is {Max} and Minimum number is {Min}")