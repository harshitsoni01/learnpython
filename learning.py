print("py\t""thon")
print(3*"un"+"ium")
print("This is cool.")
word = "python data"
number = 1
print (word[0])#this is used to get one character from string
print("The ninth character is '%s'" %word[9])
print(word[-1])
print(word[-2])
print(word[-3])
print(word[-4])
print(word[1:4])#yth this is used to get one or more character from a string #this can also be used for [1,2,3] kind of strings
print(word[:4])#pyth
print(len(word[:4]))#this is used to find the length of the specified string
print("The lenght of the string is '%s'"%len(word))#this can be used to find the length of the string
print("The lenght of PRINT is '%s'"%len("print"))
print(word.index("t"))#2#this is used to find the positon of the character
print(word.index("p"))#0
print(word.count("p"))#counts the nos of specified letters
print("a occurs %d times" % word.count("a"))#occurence of the specified char
print(word[2:5:2])#to  #this will skip 2nd character   #this used for skiping a given no of terms#[start:stop:step]
print(word[2:5:3])#t  #this will 2nd and 3rd character
print("The reverse of the string is '%s'"%word[::-1])#this is used to reverse the string
print("The characters with odd index are '%s'" %word[1::2]) #0-based indexing
print(word.lower())#this is to convert it into lowercase
print(word.upper())#this is to convert it into uppercase
print(word.startswith("pyth"))#this will print TRUE#this is used to find if a string starts with a specified string
print(word.startswith("data"))#FALSE
print(word.endswith("data"))#TRUE
words=word.split(" ")#this is used to split a string at the specified character 'here " "' and to make it a list
print(words)	
if word=="python data" and number==1:#we can use boolean operators 'and' & 'or'
	print("The word is %s and the number is %d"%(word,number))#which allows to make us to make complex boolean expressions
if number == 1 or number == 2:
	print("The number is either 1 or 2 ")
word1 = "python"
if word1 in words:#this is used to check whether the specified object is in the iterable object container
	print("Your word is either pyhton or data")
print((not False)==(True))#True#NOT is a boolean operator which inverts the expression
if not number:#this can also be use to check if the numbers is 0/1 i.e. true/false
 	print("Number is 1")#this won't print as the number is "not" zero
if number:
	print("The number is 1")#this will print as the number is 1

a,b=3,4
print(a**b/a)#this is used for operations
print(a==3)#True #this is used for checking if the value matches by printing if it's true/false


print("\t\t FIBONACCI SERIES\n")
a,b=0,1
while a<1000:#instead of curly brakets like in c we use "Tab space" indentation(meaning tab space for keeping things in loop/function)
	print(a,end=',')#end=',' is used to put a comma after everything before it
	a,b=b,a+b#this type of equality is used for, demonstrating that the expressions on the right-hand side are all evaluated first before any of the assignments take place. The right-hand side expressions are evaluated from the left to the right.


name = "Harshit "#string
name += "Soni"#adding things in a string
age = 18
college  = "Tsec"
print("\nMy name is %s"% name)
print("\nMy name is %s.And i'm %d.I'm currently studying in %s"%(name, age, college))
mystr=[1,2,3]#string representationn
mystr += [4,5,6]#adding things in a string
print("\n My string is %s"% mystr)
data = ("Harshit", "soni",18, "Tsec")#data representation
string = "\nMy name is %s %s.And I'm %d.I'm currently studying in %s" #string representation
print(string % data)
#Since ** has higher precedence than -, -3**2 will be interpreted as -(3**2) and thus result in -9. To avoid this and get 9, you can use (-3)**2.
print("""\
\n message:this can be used for writing multiple line of string 
		  do you wanna cont?
		  1.yes 2.no
""")#this can be used for mutliple lines of strings

#looping 

x = [i for i in range(10)]#this is use for making a list using 'for' loop and variable assignment
print(x)

for  x in range(3,8):
	print(x)

for x in range(3,8,2):
	print(x)

#WHILE loop
count=0
while count<5:
	print("NUmbers using while loop %d"%count)
	count +=1

#break
count= 0 
while 1:
	print("NUmbers using break while looping %d"%count)
	count+=1
	if count>=5:
		break

#contiune
for x in range(10):
	if x % 2==0:
		continue #skips the choosen number/thing
	print("Odd numbers using contiune and for loop %d"%x)#prints odd numbers 
print("Number of odd numbers are %d" %count)
	
for x in range(10):
	if not x % 2==0:
		continue #skips the choosen number/thing
	print("Even numbers using contiune and for loop %d"%x)#prints even numbers 
	
	
# Prints out 0,1,2,3,4 and then it prints "count value reached 5"
# "else" can be used with loops
count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")
	
for i in range(10):
	print(i)
else:
	print("this 10")		
	
#Functions 

def my_function():#defining a function 
	print("This is a function.")
	
my_function()#calling a function

username = "har"
greeting = "shit"
def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

my_function_with_args(username, greeting)

def adding_two_strings(username, greeting):
	return username + greeting
print(adding_two_strings(username, greeting))

a = 2
b = 3
def sum_two_numbers(a, b):
    return a + b
print(sum_two_numbers(a, b))	

#classes and object
class Myclass:
	variable = "shit"
	
	def function(self):
		print("This mesage is inside the class.")

objectx = Myclass()#Now the variable "objectx" holds an object of the class "MyClass" that contains the variable and the function defined within the class called "MyClass".
print(objectx.variable)
objectx.function()#calling a function from a class

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yackity"

# Then print out both values
print(myobjectx.variable)
print(myobjecty.variable)

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# your code goes here
car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00

# test code
print(car1.description())
print(car2.description())

#modules
#modules are python files  with extension .py
#Modules are imported from other modules using the "import" command. 

#packages
#Each package in Python is a directory which MUST contain a special file called __init__.py. 
#If we create a directory called foo, which marks the package name, we can then create a module inside that package called bar. 
#import foo.bar
#OR
#from foo import bar