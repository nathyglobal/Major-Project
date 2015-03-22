import random
reply = []
for i in range(9):
    tup = []
    teacher = ''
    for i in range(5):
        if i%2 == 0:
            teacher = 'Mr.'
        else:
            teacher = 'Ms.'
        char = random.randint(64,91)
        teacher += chr(char)
    subject = ''
    for i in range(5):
        char = random.randint(64,91)
        subject += chr(char)
    room = 'B' + str(random.randint(64,91))
    tup.append(teacher)
    tup.append(subject)
    tup.append(room)
    reply.append([tup[0], tup[1], tup[2]])
print reply