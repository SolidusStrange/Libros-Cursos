#The first of them tries to find the greater value in the list. Look at the code in the editor.
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)

#The code may be rewritten to make use of the newly introduced form of the for loop:

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list:
    if i > largest:
        largest = i

print(largest)

#Now let's find the location of a given element inside a list:

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False
 
for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break
 
if found:
    print("Element found at index", i)
else:
    print("absent")
    
# Let's assume that you've chosen the following numbers in the lottery: 3, 7, 11, 42, 34, 49.
# The numbers that have been drawn are: 5, 11, 9, 42, 3, 49.
# The question is: how many numbers have you hit?

drawn = [5, 11, 9, 42, 3, 49] #list stores all the drawn numbers;
bets = [3, 7, 11, 42, 34, 49] #the bets list stores your bets;
hits = 0 #the hits variable counts your hits.
 
for number in bets:
    if number in drawn:
        hits += 1
 
print(hits)

# imagine a list ‒ not very long, not very complicated, just a simple list containing 
# some integer numbers. Some of these numbers may be repeated, and this is the clue. 
# We don't want any repetitions. We want them to be removed.

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []

for number in my_list:
    if number not in new_list:
        new_list.append(number)

my_list = new_list[:]

print("The list with unique elements only:")
print(my_list)

