text = 'hello iman,iman ask reza,reza ask mohammad,mohammad ask ali.'
count = {}
n = 0
char = ",.;/'"
for i in range(5):
    if char[i] in text:
        text = text.replace(char[i], ' ')
print('text : ', text)

for y in text.split():
    print('y :', y)
    for x in range(len(text.split())):
        print('x : ', x)
        if y == text.split()[x]:
            n += 1
        count[y] = n
    n = 0
print(count)
