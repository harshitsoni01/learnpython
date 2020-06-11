print("AREA OF CIRCLE!!")

r = input("Radius: ")
r = float(r)
def area(r):
	pi = 3.142
	return pi*( r * r )
print("The area of the circle of radius {1} is {0}".format(area(r), r))


print("___________________________________")
print("PRIME NUMBERS!!")

p = input("Prime numbers upto: ")
p = int(p)
for i in range (1, p+1):
	if i > 1:
		for n in range(2, p):
			if (i%n)==0:
				break
	else :
		print(i)
		
print("____________________________________")
print("PATTERNS!!")

n = input("Number of rows:")
n = int(n)
for i in range(0, n):
	for j in range(0, i+1):
		print("* ", end = "")
	print(" ")	
x = 1
for i in range(0, n):
	for j in range(0, i+1):
		print(x , end = "")
		x+=1
	print(" ")
		 
