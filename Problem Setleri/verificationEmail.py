__author__ = "Çağatay KARASU"
__course__ = "PG1926"

import re

pattern = str("^[a-zA-Z0-9]+[-_]?[a-zA-Z0-9]+[@][a-zA-Z0-9]+[.]+[a-zA-Z]+[a-zA-Z]")

length = int(input("mail adresinin @ işaretinden sonraki eleman sayısını giriniz : "))
mail = input("Mail adresinizi giriniz : ")


def test_last(testMail):
		if not re.match(pattern, testMail):
				print("Mail adresiniz yanlıştır.")

		elif not pattern:
				print("Forgot to enter a pattern!")

		else:
				print("Mail adresiniz doğrudur.")


def test_email(testMail, testLength):
		x = mail.replace("@", " ")
		y = x.replace(".", " ")
		z = y.split()
		loop = True

		while loop:
				if testLength == 1:
						if len(z) == 2:
								test_last(mail)
								break
						else:
								print("Mail adresiniz yanlıştır.")
								break

				elif testLength == 2:
						if len(z) == 3:
								test_last(mail)
								break
						else:
								print("Mail adresiniz yanlıştır.")
								break

				elif testLength == 3:
						if len(z) == 4:
								test_last(mail)
								break
						else:
								print("Mail adresiniz yanlıştır.")
								break

				else:
						print("Geçersiz uzunluk!")
						correct = False
						break

test_email(mail, length)
