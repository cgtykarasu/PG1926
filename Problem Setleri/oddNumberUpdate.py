__author__ = "Çağatay KARASU"
__course__ = "PG1926"

myList = []
values = True

print("Listinize eklemek istediğiniz sayıları giriniz\n"
			"Listeyi tamamlamak için giriş ekranına 'son' yazınız")

while values:
		numbers = input()
		if numbers == "son":
				break
		else:
				myList.append((int)(numbers))

print("Your list : ", myList)
myList.sort(reverse=True)

for i in myList:
		if i % 2 == 1:
				print("Biggest odd number in your list is : ", i)
				break
