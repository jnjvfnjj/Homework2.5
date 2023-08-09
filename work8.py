# a = [1,33,24,56,32,4,7,56,4,5,23,90]
# max_number = lambda numbers: max(numbers)
# print(max_number(a))


# #       2
# num = lambda numbers: numbers %2==0
# print(num(34))


#       3
# strock = ['hello','world','potato','tomato','good','morning','sun','he']
# len_strock = 3
# filter = filter(lambda a: len(a) > len_strock, strock)
# list = list(filter)
# print(list)

#       4
with open('example.txt','r') as text:
    content = text.read()
    print(content)


#       5
with open('output.txt','w') as text:
    comtent = text.write('Hello to everyone')