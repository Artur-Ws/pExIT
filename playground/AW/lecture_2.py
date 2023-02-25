from copy import deepcopy
import time
# LIST

mylist = [1, 2, 3, 4]
print(mylist)
mylist[1] = 'banana'
print(mylist)

#slicing
print(mylist[0:3])
print(mylist[:])
mylist = [1, 2, 3, 4, 5, 6]
print(mylist[1::2])

mylist_rev = mylist[::-1]
print(mylist_rev)

# adding elements
mylist1 = [1, 2, 3]
mylist1.insert(2, 'banana')

mylist1.append('apple')
print(mylist1)

print('-'*100)

mylist1 = [1, 2, 3]
mylist2 = mylist1
print(f'list1 ID: {id(mylist1)}, list2 ID: {id(mylist2)}')
mylist2.append('banana')
print(mylist2)
print(mylist1)

print('-'*25, ' WAY TO COPY LIST NR 1 ', '-'*25)
mylist1 = [1, 2, 3]
mylist2 = mylist1.copy()
print(f'list1 ID: {id(mylist1)}, list2 ID: {id(mylist2)}')
mylist2.append("banana")
print(mylist2)
print(mylist1)

print('-'*25, ' WAY TO COPY LIST NR 2 ', '-'*25)
mylist1 = [1, 2, 3]
mylist2 = mylist1[:]
print(f'list1 ID: {id(mylist1)}, list2 ID: {id(mylist2)}')
mylist2.append("banana")
print(mylist2)
print(mylist1)

# deepcopy

print('-'*25, ' WAY TO COPY LIST NR 3 ', '-'*25)
mylist1 = [[1, 2, 3], [1, 2, 3]]
mylist2 = deepcopy(mylist1)
print(f'list1 ID: {id(mylist1)}, list2 ID: {id(mylist2)}')
mylist2[0][1] = 'banana'
print(mylist2)
print(mylist1)

numbers = [1, 2, 3, 4]
if 5 in numbers:
    print('3 in list')
else:
    print('3 not in list')

print('-'*25, ' REMOVING FROM LIST ', '-'*25)

mylist1 = [1, 2, 3, 1, 2, 3, 2, 2]
print(mylist1.count(2))
for i in range(mylist1.count(2)):
    mylist1.remove(2)
print(mylist1)

mylist1.pop()
print(mylist1)
print(len(mylist1))

print('-'*25, ' STRINGS ', '-'*25)

mystr = 'Hello world'
print(len(mystr))
print(mystr[0:4])
print(mystr[::-1])
print('Hell' in mystr)
mylist = list(mystr)
print(mylist)
mylist = mystr.split()
print(mylist)
print(list(''.join(mylist)))

print('-'*25, ' FOR LOOP ', '-'*25)

for i in range(5):
    print(f'{i+1} hello world')

mylistfor = [1, 2, 3, 4, 5, 6]
for number in mylistfor:
    if number % 2 == 0:
        print(number)

animals = ['dog', 'cat', 'horse']
colors = ['black', 'brown', 'white']

for animal in animals:
    for color in colors:
        print(color, animal)

print('-'*25, ' WHY NOT TO USE FOR LOOPS ', '-'*25)

mylist = []
before = time.time()
for i in range(10_000_000):
    mylist.append(i)
after = time.time()
print(after - before)
print('-'*5, ' summ list with for loop ', '-'*5)
result = 0
before = time.time()
for i in mylist:
    result += i
print(result)
after = time.time()
print(after - before)
print('-'*5, ' summ list with sum function ', '-'*5)
before = time.time()
print(sum(mylist))
after = time.time()
print(after - before)

n=[]
for i in range(21):
    n.append(i)
mylistfor = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers = [i for i in animals if 'o' in i]
print(numbers)
print([i for i in mylistfor if mylistfor])
