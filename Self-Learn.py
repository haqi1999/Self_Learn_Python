import random # This is called a module. In C++ its called a library This one is used for the random number function

# Comments use hashtag
# Python will execute from top to bottom (Control Flow)

# Using double quotes or single quoted print should show the same thing
print ("There is a world") 

# Python will use the most recent input in the variable of the same name.
# Example belows "Meat" as the latest and will be the final output. But it will still print the previous output in the previous line Remember to create a new print after new each variable used in the print
# The new print will NOT USE THE NEW VARIABLE if the new variable is updated AFTER THE new print.
meal = "An english muffin"
# Printing out breakfast
print ("Breakfast:")
print (meal)
# Now update meal to be lunch!
meal = "chicken"
meal = "lunch"
# Printing out lunch
print ("Lunch:")
print (meal)
# Now update "meal" to be dinner
meal = "Meat"
print ("Dinner:")
print (meal)

# SyntaxError = Something in the program is wrong 
# NameError = Python sees a word that it does not recognise (i.e Undefined variable)
# TypeError = When an operation is applied to an object of an innapropriate type

# ---------------------------------------------- Variables --------------------------------------------------------------
# When defining a variable, you dont have to assigned a data type variable with the variable name itself like in C++, Instead just create the name of the variable with the data stored
an_int = 2
a_float = 2.1 
a_double = 2.121212313
print (an_int)
print (an_int + a_float + a_double)


leaves_of_grass = """
Poets to come! orators, singers, musicians to come!
Not to-day is to justify me and answer what I am for,
But you, a new brood, native, athletic, continental, greater than
  before known,
Arouse! for you must justify me.
""" # Multiline Strings use 3 quotation marks

# Boolean Variables
# DONT USE QUOTATION MARKS for boolean variables
set_to_true = True
set_to_false = False
bool_one = 5 != 7 
bool_two = 1 + 1 != 2
bool_three = 3 * 3 == 9

print(bool_one)    # True

print(bool_two)    # False

print(bool_three)  # True


# Generating a random number from 1-9 and storing it in random_number variable
random_number = random.randint(1,9)

# --------------------------------- Mathematical Operations & String/Integer Concatenation --------------------------------
# NB : A variable cannot be multipled/divided by a number.
coffee_price = 1.50
number_of_coffees = 4
greeting_text = "Hey there! "
question_text = "How are you doing?"
birthday_string = "I am "
age = 10
birthday_string_2 = " years old today!"
number_of_miles_hiked = 12
hike_caption = "What an amazing time to walk through nature!"


print(coffee_price * number_of_coffees)
full_text = greeting_text + question_text # String concatenation
print(full_text) 
full_birthday_string = birthday_string + str(age) + birthday_string_2 # Concatenating an integer with strings is possible if we turn the integer into a string first
print(full_birthday_string) 
print(birthday_string, age, birthday_string_2) # This also prints "I am 10 years old today!"
print(birthday_string, "10", birthday_string_2) # This also prints "I am 10 years old today!"

print (25 * 68 + 13 / 28)
print(2 ** 10) # 2 to the 10th power, or 1024
print(29 % 5) # Prints 4 because 29 / 5 is 5 with a remainder of 4. If no remainder then will print out 0. Useful for performing an action every nth term

number_of_miles_hiked += 2 # Adds 2 from the old variable
print (number_of_miles_hiked)
hike_caption += " #nofilter" # Adds #nofilter from the old variable as a string concatenation
hike_caption += " #blessed"  # Adds #blessed" from the old variable as a string concatenation
print (hike_caption)

# --------------------------------------------------- User Input --------------------------------------------------------
# VariableName = input("question for interaction with the user")
likes_snakes = input("Do you like snakes? ") 

# ------------------------------------------------ Control Flow/Logic ---------------------------------------------------
# == Equals
# != Not Equals
# > Greater than
# >= Greater or equal to
# < Less than 
# <= Less than or equal to
# and Both needs to be true
# or Only one side needs to be true. 

# If Statements
# NB : the elif (else if) and the else should be at the same identation as the if.
# Dont forget the colon after the condition
# In an else statement, there shouldnt be a condition since it is the final.
# If not is basically saying if the reverse of the condition occurs. elif not exist too.
# return can be applied after each statement to produce the result.
user_name = "angela_catlady_87"
credits = 120
gpa = 1.8

if user_name == "Dave":
  print("Get off my computer Dave!")
elif user_name == "angela_catlady_87":
  print("I know it is you, Dave! Go away!")
else:
  print("I know it is you, Dave! Go away!")

if not credits >= 120: 
  print("You do not have enough credits to graduate.")

if not gpa >= 2.0:
  print("Your GPA is not high enough to graduate.")

if not (credits >= 120) and not (gpa >= 2.0):
  print("You do not meet either requirement to graduate!")

# ------------------------------------------------ Lists ---------------------------------------------------
# List is sequential 
# .append() allows addition to the list a the end of the list. Only takes 1 input arguement
# .remove() allows removal of the literally input arguement. Use quotation for strings. 
# .remove() will remove only 1 of the dupilcated elements in the list. Prioritises 1st instance
# .count() count the number of occurences of an element in a list
# .insert() insert an element into a spefic index of list (index,element inserted)
# .pop() remove an element from a specific index or from the end of list (index)
# range(start,end,increment of) create a sequence of integers. range(10) creates 0-9.
# len(list) get length of a list. Specifically number of elements on that list NOT INDEX
# .sort() sort the original list and returns none. Thus if applied into a variable, will return None. Just print the original list name to get the sorted list.
# sorted(list) same as sort but CREATES A NEW LIST of the list that is sorted. Can be put into a new variable.
# list(range) creates a list from the range created
# zip() function allows combining data sets without the needing to rely on multi-dimensional lists. Makesure to use the list() function afterwards to change it from memory address to the actual elements contained that have been combined.
# NB the list created using zip() and list is actually a TUPLE
# Only the same data type can be "+" together.
# Indexing start with 0 and uses []. Must use int not float. By using int() function to forcefully remove decimals.
# Negative indexing start with -1, reads from the last.


heights = [61, 70, 67, 64, 65]
mixed_list_common = ["Mia", 27, False, 0.5]
empty_list = []
emtpylist2 = list()

append_example = [ 'This', 'is', 'an', 'example']
append_example.append('list')

print(append_example)

example_list = [1, 2, 3, 4]

#Using Append adds  the number 5 
example_list.append(5)
print(example_list)

#Using Remove, below removes the number 2 NOT INDEX 2. Use quotation marks to remove string
example_list.remove(2) 
print(example_list)

# Adding more than 1 data to the list to a pre-existing lists
items_sold = ["cake", "cookie", "bread"]
items_sold_new = items_sold + ["biscuit", "tart"]
print(items_sold_new)
print (items_sold_new[1])

# Negative indexing. Prints out tart
print (items_sold_new[-1]) 

# Modifying lists
items_sold_new [0] = "fruits"
print(items_sold_new)

# 2D Lists
heights = [["Noelle", 61], ["Ava", 70], ["Sam", 67], ["Mia", 64]]
noelles_height = heights[0][1] 
get_ava = heights [1][0] 
mia_height = heights [-1][-1]
print(noelles_height)
print(get_ava)
print(mia_height)

heights_final = heights + [["Noelle", 61], ["Haqi",70]]
print(heights_final)

tic_tac_toe = [
            ["X","O","X"], 
            ["O","X","O"], 
            ["O","O","X"]
]
for row in tic_tac_toe:
    for column in row:
        print(column + " ", end='') # end= stops the code from going to the next line
    print()

# Example of using range printing from 0-9
my_range = range(10) 
print(my_range)
# 2-8 range printed below, Notice how the start number is the same as the input arguement unlike the end number
my_list = range(2, 9) 
# The list function is required here to create the list from the range 0-9
print(list(my_list)) 
print(list(my_range)) 
# Each number is greater than 2 than the previous number example [2,4,6,8]
my_range2 = range(2, 9, 2)
print(list(my_range2))

# Good example of range
examples = ['red', 'green', 'blue', 'orange']
# This will print 4 which is the number of elements in examples.
print(len(examples))
# This will return a list ([0, 1, 2, 3]) which provides indexes to the examples.
for color in range(len(examples)):
   print(examples[color])
for color in range(4):
    print(examples[color])

# Slicing list
# NB: It will extract from starting number to the number before the end and uses indexing extraction
# Just take not of the colon position (How we extract things in MATLAB Too)
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]
middle = suitcase[2:4] 
print(middle)
print(suitcase[:3]) # Take Firts :n elements (Normal Indexing)
print(suitcase[-3:]) # Take Last -n: elements (Like Inverse Indexing)
print(suitcase[:-1]) # All element but not the last element

# Sorting
names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]
names.sort() # Alphabetical
print(names) 
names.sort(reverse=True) # Reverse
print(names)
sorted_names = sorted(names) # Inserted in a variable
print(sorted_names)

inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]
inventory_len = len(inventory)
first = inventory[0]
last = inventory[-1]
inventory_2_6 = inventory[2:6]
first_3 = inventory[:3]
twin_beds = inventory.count("twin bed")
removed_item = inventory.pop(4)
inventory.insert(10,"19th Century Bed Frame")
inventory.sort()
print(inventory)
print(removed_item)

# Example of list comprehension using for loop 
# new_list = [<expression> for <element> in <collection>]
# NB Square brackets.
grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades = [grade + 10 for grade in grades]
grade_above_80 =  [grade for grade in grades if grade > 80]
print (scaled_grades)
print (grade_above_80)

# Example of list comprehension using for and if statements
# Notice the differcen
numbers = [2, -1, 79, 33, -45]
no_if   = [num * 2 for num in numbers]
if_only = [num * 2 for num in numbers if num < 0]
if_else = [num * 2 if num < 0 else num * 3 for num in numbers]


# ------------------------------------------------ Tuples ---------------------------------------------------
# Similar to Lists, but you cant change anything to it or you cant modify it.
# Instead of square brackets, you use normal bracket parantheses ()
# you can extract the tuples contents by using named variables respectively
# NB you can create one element tuple by using the trailing coma beside the element . I.e) name = (4,)

# Example of a tuple
my_info = ("Haqi",24,"Indonesia")
# Extracting data from tuple A.k.a Unpacking
name,age,country = my_info
print (name)
print (age)
print (country)

# Using zip() function. Can be 2 or more lists
namess = ["Jenny", "Alexus", "Sam", "Grace"]
heightss = [61, 70, 67, 64]
combine_namess_heightss = zip(namess,heightss)
print(combine_namess_heightss) # this will show the location a.k.a the memory address of the TUPLES FORMAT combined
print(list(combine_namess_heightss)) # This will show the actual lists but in TUPLES FORMAT combined. Shown in termminal by the parantheses and not the square brackets

# ------------------------------------------------ Loops ---------------------------------------------------
# Indefinite iteration = number of times the loops is executed depends on how many conditions are met
# Definite iteration = number of times the loops is executed is defined advanced

# For loops
# The temporary variable is the elements inside the list.
# The temporary variable represent the actual values in the list itself
# The name of the temporary varible will not affect the content of the variable itself but it is better for you to name it in a way that it makes relation to the actual data
"""
for <temporary variable> in <list of length>:
     <action>
"""
sport_games = ["football", "hockey", "baseball", "cricket"]
for i in sport_games:
  print(i)

# In this case, temp is used to track the number of loops is executed. +1 Because range starts at 0-5.
for temp in range(6):
  print("Loop is on iteration number " + str(temp + 1))

# One line operation of for loop
for i in sport_games: print(sport_games)

# Example of using break, stops loop at break at that iteration after printing it
items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]
print("Checking the sale list!")

for item in items_on_sale:
  print(item)
  if item == "knit dress":
    break
print("End of search!")

# Example of using continue , skips the current iteration
big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]
for i in big_number_list:
  if i <= 0:
    continue
  print(i)

# While loops
# Identation is important. If the identation is the same as While, it will recognise it outside the loop
"""
while <conditional statement>:
  <action>
"""
count = 0
while count <= 3:
  # Loop Body
  print(count)
  count += 1

# Example of a one line operation of while loop
while count <= 3: print(count); count += 1

# Nested loops
# Loop through each sublist
project_teams = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]
for team in project_teams:
  # Loop elements in each sublist
  for student in team:
    print(student)