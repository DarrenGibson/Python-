


#   Python Tutorial for Beginners 2017 Part 1 | Python Programming Tutorial | Python Basics


#   this is how you comment
age = 10
#   created an integer variable named age
name = 'Darren'
#   created a string variable named name
print(age)
#   10
print(name)
#   Darren
print(type(age))
#   <class> 'int'>
print(type(name))
#   <class 'str'>
print(age, name)
#   10 Darren
chess_board  = [1,2,3,]

print(chess_board)
#   [1, 2, 3]
print(type(chess_board))
#   <class 'list'>
print(min(chess_board))
#   1
print(max(chess_board))
#   3
print(len(chess_board))
#   3
last_name = '''Gibson'''

print(last_name)
#   Gibson

var1 = "Tyler "
var2 = "James "
var3 = "Gibson "

full_name = (var1 + var2 + var3)

print(full_name)
#   Tyler James Gibson
s1 = 'this is string in single quotes\n'
s2 = 'this is string in double quotes\n'
s3 = 'this is string in triple quotes\n'

s4 = '''this is a multiline string
in triple single quotes 
that occupies several lines of code'''

print(s1, s2, s3, s4)
#   this is string in single quotes
#    this is string in double quotes
#    this is string in triple quotes
#    this is a multiline string
#    in triple single quotes
#    that occupies several lines of code
print(s1 + s2 + s3 + s4)
#   this is string in single quotes
#    this is string in double quotes
#    this is string in triple quotes
#    this is a multiline string
#   in triple single quotes
#   that occupies several lines of code
print(s1[0])
#   t
print(s1[0:6])
#   this i
print(s1[0:10:2])
#    ti ss
print(s1[-2])
#   s
print(len(s1))
#   32
x = '1'
y = '2'

print(type(x))
#   <class 'str'>
sum = int(x) + int(y)

print(type(x))
#   <class 'str'>
print(sum)
#   3
print(type(x))
#   <class 'str'>
char_list = ['a', 'b', 'c']

print(char_list)
#   ['a', 'b', 'c']
string_list = ['first','middle','last']

print(string_list)
#   ['first', 'middle', 'last']
print(string_list[2])
#   last
print(string_list[1:2])
#   this only displays ['middle'] why?  it works
#   integers from programs from earlier
places = ("Mercury ",4,"Earth")
#
#   When I added a tab indent after all the #'s they it was
#   much easier to just click anywhere after # and have it start
#   there.  But when you save the program, all the tabs indents
#   are removed
print(places)
#   ('Mercury ', 'Venus', 'Earth')
#   a turple is different than the list(array)
#   you can declare ints and chars and strings all in the same
#   list.  However when you cannot change the values of the values
#   later on.  But in a list with all the same data types you can
#   you change the vaules
#   places = ["Mercury", 4 , "Earth"] will not compute must have ()
#
#   if you wanted to access the values in you your list by indexing
#   you will use [] brackets as your request for either lists or
#   tuples
first_list = [7,8,9]
print(first_list[0])
#   7
first_tuple = (4, 'g', "someone")
print(first_tuple[0])
#   4
first_list[0] = 2
print(first_list)
#   [2, 8, 9]
# first_tuple[0] = 6   DOES NOT COMPILE
print(first_tuple)
#                       blank
#   this did not compile or produce results, but did not
#   display an error message either.
#
#   thus proving, tuples cannot change values
#
#   tuples are immutable, lists are mutable ?!
#
#   Dictionary's similar to hashmap in Java
#
#   you have a key and a value,[k v] the key can be either simple
#   or complex. the value can be either simpel or complex
#   the key part is immutable.  lists cannot be used as a key
#   because they are mutable.  values can use either.
first_dict = {"Michigan":"Lansing","California":"Sacramento" }
#   you canot access indexs in dictionaries
print(first_dict["Michigan"])
#   Lansing
#   Instead this is how you see a value, by typing the key
#
print(first_dict)
#   {'Michigan': 'Lansing', 'California': 'Sacramento'}

salary = {"senior":100,"Mid":50,"junior":25}
print(type(salary))
#   <class 'dict'>
print(salary["senior"])
#   100
print(salary.keys())
print(salary.values())
#
#   loops
#
i = 1
while (i < 11):
    print(i)
    i = i+1
#   this displays akk the numbers through 10 each with a new line
#
for x in range(0,11):
    print(x)

#   prints the numbers 1 trough 10, each on thier own line
#
new_dictionary = {"darren": 36, "tyler": 5}
name = input("please enter your name: ")

print(name)

if (name in new_dictionary.keys()):
    print("age is: %d" % new_dictionary[name])
else:
    print("Key %s does not exist" % name)















