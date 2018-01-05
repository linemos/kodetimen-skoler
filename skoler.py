#!/usr/bin/python

import os
import sys
import codecs
reload(sys)
sys.setdefaultencoding('utf-8')

class Skole:
	# id, school, address, contacts, levels, year, students
	def __init__(self, args):
		self.school = args[1]
		self.contacts =args[3]
		self.year = args[5]

	def get_school_name(self):
		return self.school.decode('utf-8').replace("\"", "")

	def get_email(self):
		c = self.contacts.split()
		emails = ""
		for i in c:
			if "@" in i:
				emails += "{},".format(i.replace(":", ""))
		return emails

	def get_emails_as_list(self):
		c = self.contacts.split()
		emails = []
		for i in c:
			if "@" in i:
				emails.append(i.replace(":", ""))
		return emails

	def get_year(self):
		return self.year

class Reader:
	def __init__(self):
		self.schools = []
		self.readFile()
		#self.find_not_paamledte_eposter()
		self.find_paamleldte()


	def find_paamleldte(self):
		this_year = {}

		for school in self.schools:
			if school.get_year() == "2017":
				this_year[school.get_school_name()] = school 

		for school in this_year:
			s = next((sc for sc in self.schools if sc.get_school_name() == school), None)
			print school, ",", s.get_email()	

	def find_not_paamledte_skoler(self):
		last_year = {}
		this_year = {}

		for school in self.schools:
			if school.get_year() == "2016":
				last_year[school.get_school_name()] = school
			if school.get_year() == "2017":
				this_year[school.get_school_name()] = school 

		not_paameldte = set(last_year.keys()) - set(this_year.keys()) # finds schools not in 2017 set

		for school in not_paameldte:
			s = next((sc for sc in self.schools if sc.get_school_name() == school), None)
			print school, ",", s.get_email()

	def find_not_paamledte_eposter(self):
		last_year = {}
		this_year = {}

		for school in self.schools:
			if school.get_year() == "2016":
				last_year[school.get_school_name()] = school
			if school.get_year() == "2017":
				this_year[school.get_school_name()] = school 

		paameldte = set(last_year.keys()) & set(this_year.keys()) # finds schools in both sets

		for school in paameldte:
			s2016 = next((sc for sc in self.schools if sc.get_school_name() == school and sc.get_year() == "2016"), None)
			s2017 = next((sc for sc in self.schools if sc.get_school_name() == school and sc.get_year() == "2017"), None)

			emails = ""
			for email in s2016.get_emails_as_list():
				if email not in s2017.get_emails_as_list():
					emails += "{},".format(str(email))
			print str(school) + "," + emails

	def create_schools(self, lines):
		for line in lines[1:]:
			self.schools.append(Skole(line.split(",")))

	def readFile(self):
		with codecs.open("new2016.csv", "r", encoding='utf-8') as skole_file:
			lines = skole_file.readlines()

		lines = [str(x.strip()).decode('utf-8') for x in lines]
		self.create_schools(lines)        

if __name__ == '__main__':
	Reader()
