import csv, sys, math

class Survey:
	def __init__(self, row):
		self.id, self.class_id, self.term = row[:3]
		self.ratings = []
		self.ratings = row[3:18]
		if (len(row) > 19 and row[19]): self.how_heard = row[19]
		else: self.how_heard = ''
		if (len(row) > 20 and row[20]): self.liked_most = row[20]
		else: self.liked_most = ''
		if (len(row) > 21 and row[21]): self.liked_least = row[21]
		else: self.liked_least = ''
		if (len(row) > 22 and row[22]): self.comments = row[22]
		else: self.comments = ''
		
	def get_facility_rating(self):
		return self.ratings[5]
		
	def get_CID(self):
		return self.class_id

	def get_rating(self, q):
		return self.ratings[q]

	def get(self):
		return (self.id, self.class_id, self.term, self.ratings, self.how_heard, self.liked_most, self.liked_least, self.comments)

	def printout(self):
		print self.how_heard
		
		
class Class:
	def __init__(self, row):
		self.id, self.name, self.day, self.time, self.facility_id, self.term, self.instructor_id = row
		
	def get_id(self):
		return self.id
		
	def get_facility_id(self):
		return int(self.facility_id)
		
	def get_instructor_id(self):
		return self.instructor_id

	def printout(self):
		print self.name

		
class Instructor:
	def __init__(self, row):
		self.id, self.name = row
		
	def get_id(self):
		return self.id
		
	def get_name(self):
		return self.name

	def printout(self):
		print self.name

		
class Facility:
	def __init__(self, row):
		self.id, self.name = row
		self.net_grade = 0.0
		self.num_surveys = 0.0
		self.grade = 0.0

	def add_rating(self, rating):
		self.net_grade += float(rating)
		self.num_surveys += float(1)
		
	def get_grade(self):
		#return '' + float(self.net_grade)/float(self.num_surveys)
		if self.num_surveys > 0:
			self.grade = float(self.net_grade) / float(self.num_surveys)
			return "%2f" % self.grade
		else: return '[N/A]'
	
	def get_num_surveys(self):
		return "%d" %self.num_surveys
		
	def get_id(self):
		return self.id
		
	def get_name(self):
		return self.name

	def printout(self):
		print self.name

##################


facilities = {}
facilities_list = []

classes = {}
classes_list = []
instructors = []
surveys = []

filename = 'survey_view.csv'
f = open(filename, 'rb')
reader = csv.reader(f)
reader.next() # read header line from csv
surveys = list(map(Survey, reader))

filename = 'class.csv'
f = open(filename, 'rb')
reader = csv.reader(f)
reader.next() # read header line from csv
classes_list = list(map(Class, reader))

filename = 'facility.csv'
f = open(filename, 'rb')
reader = csv.reader(f)
reader.next() # read header line from csv
facilities_list = list(map(Facility, reader))

filename = 'instructor.csv'
f = open(filename, 'rb')
reader = csv.reader(f)
reader.next() # read header line from csv
instructors = list(map(Instructor, reader))

for f in facilities_list:
	facilities[f.get_id()] = f; # initialize all class grades to 0
	print "facilitities of " +f.get_id()+ " is " +f.get_name()

for survey in surveys:
	#s.printout()
	class_id = survey.get_CID()
	#survey.printout()
	for c in classes_list:
		if (c.get_id() == class_id):	# push the grade
			facilities[c.get_facility_id()].add_rating(survey.get_facility_rating())
	
for f in facilities:
	print 'Grade for '+f.get_name()+ ' is ' +f.get_grade()+ ' based on ' +f.get_num_surveys() + ' surveys'