# Exercise
try:
    age = int(input("Enter your age: "))
except:
    age = 0

if age < 18:
    print("Ooops, you have no privileges... ")
else:
    try:
        mid_term = max(min(float(input("Enter your mid term score: ")), 100), 0)
        final = max(min(float(input("Enter your final score: ")), 100), 0)
        average = (mid_term + final) / 2
        if average < 30:
            print(f"your average score: {average}")
            print("failed")
        elif average >= 30 and average < 50:
            print(f"your average score: {average}")
            print("passed, Normal score")
        elif average >= 50 and average < 70:
            print(f"your average score: {average}")
            print("passed, Good")
        else:
            print(f"your average score: {average}")
            print("passed, Perfect")
    except:
        print("invalid input.")

# ITERATIONS STRUCTURE

i = 0
while i < 3:
    print(i)
    print(f"end of the {i+1}st loop")
    i = i+1

print("end of the script")


# counter
i = 0 # initial step
# i < 20 => final step (stop critera)
while i < 20:
    print("hello")
    i = i+1 # step
