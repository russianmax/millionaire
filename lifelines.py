import random
import time
name = 'Matthew'
j = 0

answerlist = ["A","B","C","D", "Correct"]

#open randon random line in file
i = 1
while i <= 16:
	f = (random.choice(list(open('test.txt'))))
	lines = f.split('[')
	question = lines[0]
	answers = lines[1].strip("\n").split(',')

	print 'Question:', i 

	print question
	time.sleep(3)
	print 'A: ' + answers[0]
	time.sleep(1)
	print 'B: ' + answers[1]
	time.sleep(1)
	print 'C: ' + answers[2]
	time.sleep(1)
	print 'D: ' + answers[3]
	time.sleep(1)

	#assigning values to answers
	a = random.choice(answers)
	b = random.choice(answers)
	c = random.choice(answers)
	d = random.choice(answers)
	# print a , b , c , d 

	answerdict = {
	'A' : answers[0],
	'B' : answers[1],
	'C' : answers[2],
	'D' : answers[3],

	}
	#print answers[4]
	select = raw_input("Select an answer " + name + ":\n")
	select = select.upper()
	
#phone a friend idea

	#Phone a friend
	if select == "2":
		print "Phone a friend"
		time.sleep(1)
	
		while j == 0:
			friend = raw_input("Please enter the name of the person yout want to ring " + name + ":\n")
			print "...dialling " + friend + "... "
			time.sleep(2)
			print "Hi " + friend + " it's Chris Tarrent here, " + name + " needs your help!"
			print "Can you help " + name + " by answering this question"
			time.sleep(1)
			print question
			print 'A: ' + answers[0]
			print 'B: ' + answers[1]
			print 'C: ' + answers[2]
			print 'D: ' + answers[3]
			print friend + ":" + answers[7]
			lifeline2 = raw_input("Chris Tarrent: Please select an answer " + name + "\n")
		j = j + 1 
		#phone a friend

	select = lifeline2.upper()

	if select in answerdict:
		if answerdict[select] == answers[4]:
			print 'Correct\n' 
		else:
			print 'Hard luck ' + name  + ', Game over'
			break
		if i == 16:
			print "Congratulations You are a millionaire"

		#50/50
	if select == "1":
		print "50/50"
		time.sleep(1)

		while k == 1:
			print "OK" + name + ",we are going to randomly remove two incorrect answers," 
			time.sleep(2)
			print "which will leave you with one incorrect answer along with the correct one\n"
			time.sleep(2)
			print "OK here is what you're left with:\n"
			time.sleep(0.5)
			print answers[5] + answers[6]
			lifeline1 = raw_input("Please select an answer " + name + ":\n")
			#select = lifeline1.upper()
		k = k + 1
			#50/50

	select = lifeline1.upper()
	if select in answerdict:
		if answerdict[select] == answers[4]:
			print 'Correct\n' 
		else:
			print 'Hard luck ' + name  + ', Game over'							
			break
		if i == 16:
			print "Congratulations You are a millionaire"
			time.sleep(5)
			break


	if select in answerdict:
		if answerdict[select] == answers[4]:
			print 'Correct\n' 
		else:
			print 'Hard luck ' + name  + ', Game over'
			break
		if i == 16:
			print "Congratulations You are a millionaire"
i = i + 1
	








