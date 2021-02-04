__author__ = "Çağatay KARASU"
__course__ = "PG1926"

class School:
		def __init__(self, name, year, score, city, numberOfStudents):
				self.name = name
				self.year = year
				self.score = score
				self.city = city
				self.numberOfStudents = numberOfStudents
				print("School's name is \t\t\t\t:\t", name,
							"\nFoundation year of the school \t:\t", year,
							"\nSchool's score is \t\t\t\t:\t", score, "\nSchool is in", city,
							"\nSchool has", numberOfStudents, "students.")


class PrimarySchool(School):
		def __init__(self, name, year, score, city, numberOfStudents, femaleStudents):
				super().__init__(name, year, score, city, numberOfStudents)
				self.femaleStudents = femaleStudents
				print("School has", femaleStudents, "female students.")


class HighSchool(School):
		def __init__(self, name, year, score, city, numberOfStudents, mathClasses):
				super().__init__(name, year, score, city, numberOfStudents)
				self.mathClasses = mathClasses
				print("School has", mathClasses, "math classes.")


estu = School("Eskişehir Teknik Üniversitesi", 2016, 310, "Eskişehir", 12500)
print("# " + "=" * 78 + " #")
gaziIOO = PrimarySchool("Gazi İlköğretim Okulu", 1988, "nan", "Antalya", 550, 250)
print("# " + "=" * 78 + " #")
gaziLisesi = HighSchool("Gazi Lisesi", 1980, 278, "İstanbul", 700, 12)
