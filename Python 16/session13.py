x = int(input("enter seconds: "))

# days = int(x/86400)
days = x//86400
rem_sec = x%86400

hours = rem_sec//3600
rem_sec = rem_sec%3600

minutes = rem_sec//60
seconds = rem_sec%60

print("Days: "+str(days)+" Hours: "+str(hours)+
      " Minutes: "+str(minutes)+" Seconds: "+str(seconds))

print(f'Days: {days} Hours: {hours} Minutes: {minutes} Seconds: {seconds}')


