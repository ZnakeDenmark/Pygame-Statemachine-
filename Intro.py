import time

text = "Its was rainning and you were running"
delay = 0.1 # adjust delay as needed

for char in text:
    print(char, end="", flush=True)
    time.sleep(delay)

print()    
text = "You were now close til the hotel"

for char in text:
    print(char, end="", flush=True)
    time.sleep(delay)

print()
text = "And you open the door to go inside"

for char in text:
    print(char, end="", flush=True)
    time.sleep(delay)

print()
