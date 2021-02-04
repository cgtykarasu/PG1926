__author__ = "Çağatay KARASU"
__course__ = "PG1926"

myList = []
listForZeros = []
values = True

print("Listinize eklemek istediğiniz sayıları giriniz\n"
			"Listeyi tamamlamak için giriş ekranına 'son' yazınız")

while values:
		numbers = input()
		if numbers == "son":
				break
		else:
				myList.append((int)(numbers))

print("Before sorting : \t", myList)

for zeros in myList:
		if zeros == 0:
				listForZeros.append(zeros)
				myList.remove(zeros)

myList = listForZeros + myList
print("After sorting : \t", myList)
