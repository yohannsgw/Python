print("Do you have covid?")

cough = input("Do you have a continuous cough? (yes/no)\n").lower() == "yes"
temp = input("Do you have a high temperature? (yes/no)\n").lower() == "yes"

if cough and temp:
    print("You may have covid")
elif cough or temp:
    print("You may not have covid")
else:
    print("You don't have covid")
 