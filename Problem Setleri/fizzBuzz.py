__author__ = "Çağatay KARASU"
__course__ = "PG1926"

myFizzBuzzList = []
startNumber = (int)(input("Please enter a start number : "))
stopNumber = (int)(input("Please enter a stop number : "))

if stopNumber <= startNumber or startNumber < 0 or stopNumber > 100:
		print("Your start or stop number is invalid!")

else:
		for i in range(startNumber, stopNumber):
				if i % 15 == 0:
						myFizzBuzzList.append("FizzBuzz")
				elif i % 5 == 0:
						myFizzBuzzList.append("Buzz")
				elif i % 3 == 0:
						myFizzBuzzList.append("Fizz")
				else:
						myFizzBuzzList.append(i)

print(myFizzBuzzList)
