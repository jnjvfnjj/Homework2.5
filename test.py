user = input('ведите текст:')
with open('test.txt','w') as text:
    a = text.write(user)

with open('test.txt','r') as text:
    a = text.read()
    print(a)    