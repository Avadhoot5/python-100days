# for Loop with else
# IMPORTANT: else block will only be executed when for/while loop is succesfully executed for all values.
# else executes when loop ends, not when loop breaks.

for i in range(5):
    print(i)
else:
    print("the loop has ended")

for i in range(5):
    print(i)
    if i == 3:
        break
else:
    print("The loop is broken")

i = 0
while i<5:
    print(i)
    i = i+1
    if i>3:
        break
else:
    print("while loop is done")

