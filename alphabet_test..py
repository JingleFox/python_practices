import random
A = int(input("Enter the input for A: "))
B = int(input("Enter the input for B: "))
C = int(input("Enter the input for C: "))
countA = 0
countB = 0
countC = 0
total = 0
alpha = ""
temp = ""
x = ""
count = 0
line = ""
status = False

# adding the input into a string and splitting the strings into char in string array
def split(alpha):
    return [char for char in alpha]

while countA < A:
    alpha = alpha + "a"
    countA = countA+1

while countB < B:
    alpha = alpha + "b"
    countB = countB+1

while countC < C:
    alpha = alpha + "c"
    countC = countC+1

alphabet = split(alpha)
print(alphabet)

# removing char from one array and placing them in another string array [****not done yet!!!]
def arrayCharRemoval(index):
    index = 2
    # alpha.join(alphabet)
    if len(alpha) > index:
        alphabet = alpha[0:index: ] + alpha[index + 1: :]
        temp = alphabet[index]
        print("string slice: " + alpha)
        print("new temp string: " + temp)

# summing the total char in the string
total = A + B + C
print(total)

#if finding that latest 3 count[i-1] and count[i-2] and count[i-3] for "aaa" or "bbb" or "ccc" exists, place
#status as true, else status remains false
while count < total:
    x = random.choice(alphabet)
    line = line + x
    arrayCharRemoval(x)
    print("This is the output: " + line)
    print(status)
    if status == False:
        count = count + 1
        print(count)
        if count >= 2:
            if line[count-1] == "a" and line[count-2] == "a" and line[count-3] == "a":
                    status = True
            elif line[count-1] == "b" and line[count-2] =="b" and line[count-3] == "b":
                    status = True
            elif line[count-1] == "c" and line[count-2] == "c" and line[count-3] == "c":
                    status = True
    else:
        count = 0
        line = ""
        line = random.choice(alphabet)
        count = count + 1
        status = False
        print(line)

    if count == total:
        print("It is possible. This is one of the output: " + line)
        break




