import sys

if (len(sys.argv) != 2):
	sys.exit("Requires course ID")

CID = sys.argv[1]
term = 'SP12'
thisClass = 'SP12_'+CID+'.txt'
myfile = open(thisClass, "r").readlines()
survey = "INSERT INTO survey VALUES('', '"+CID+"', '"+term+"', '?', '?', '?', '?', '?',' ?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?');"
for line in myfile:
	questions = line.split("/");
	insertSQL = survey[0:]
	length = len(questions[0])
	if (length < 16):
		sys.exit("***Error: too few ratings supplied")
	if (length > 16):
		sys.exit("***Error: too many ratings supplied")
	for rating in questions[0]:
		##print rating+", "
		insertSQL = insertSQL.replace("?", rating, 1)
	for response in questions[1:]:
		response = response.replace("\'", "\\\'")
		insertSQL = insertSQL.replace("?",response, 1)
	##result.append(insertSQL)
	print insertSQL+'\n'
##print result 
