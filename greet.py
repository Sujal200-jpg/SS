import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = int(time.strftime('%H'))
print(timestamp)

# https://docs.python.org/3/library/time.html#time.strftime

if(timestamp>=00 and timestamp<12):
    print("Good Morning!")
elif(timestamp>+12 and timestamp<17):
    print("Good Morning!")
else:
    print("Good Evening!")