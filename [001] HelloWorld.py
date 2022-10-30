# This prints some texts
print("Hello World")
print('What"s up') 
print("What's up")

#This is simple math
print(1+2)
print(4-2)
print(4*7) #multiplication
print(5/2) #division
print(2**3) #expodentiol
print(5//2) #discard leftovers
print(5%2) #leftovers of divison

#how to use Variables
##Variable Naming
#Variables shouldn't start with a number
#spaces are not allowed
#cannot be keywords
#Case sensitive
red_bucket = "Raymond" #Value is a "String"(str)
red_bucket = 10  #Value is a "Integer"(int)
print(red_bucket)
#second line overrides first value
#22nd line takes out "Raymond" value assignmnet
print(type(red_bucket) )
#prints out <class 'int'> integer = number

blue_bucket="Richmond"
print(blue_bucket)
print(type(blue_bucket))
#prints out <class'str'> strings = text

del red_bucket
#deletes variable "red_bucket"
print(red_bucket)
#because variable "red_bucket"was deleted
#variable "red_bucket" is not defiend under this line

