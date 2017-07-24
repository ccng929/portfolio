

from random import *





#Create the list of words you want to choose from.

appetizer_list = ["quinoa", "pizza", "ice cream", "sausage"]
main_course_list = ["banana","dumpling"]
dessert_list = ["cookie","bread"]

#Generates a random integer.

x = randint(0, len(dessert_list)-1)
y = randint(0, len(main_course_list)-1)
m = randint(0, len(appetizer_list)-1)

print (dessert_list[x])
print (main_course_list[y])
print (appetizer_list[m])
