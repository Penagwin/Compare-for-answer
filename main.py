#!/usr/bin/env 


print "Started"

answeryet = False
nextline = False
pos = []
small = 0
answerb = 0
answers = open('/home/penagwin/.config/sublime-text-3/Packages/User/Question.txt', 'r')
questions = open('/home/penagwin/.config/sublime-text-3/Packages/User/Answers.txt', 'r')
for question in questions:
	while True:
		pos.append(answers.tell())
		currentquestion = question.replace("\n", "")
		answer = answers.readline()
		if answer == "END OF FILE":
			break
		if answer.find("Question") != -1:
			answerb = 1 
		elif answer.find("Correct Answer:") != -1:
			answerb = 2
		
		if answer.find(currentquestion) != -1 and answerb == 1:
			print answer
		elif answer.find(currentquestion) != -1 and answerb == 2:
			while answer.lower().find("answer") == -1 or answer.lower().find("answer:") != -1:
				small = small +1
				print " "+str(len(pos)-small)+ "        " + str(len(pos)) + '                '+ answers.readline()
				answers.seek(pos[len(pos)-small])
				answer = answers.readline()
				answers.seek(pos[len(pos)-small-1])
			print answers.readline()
			answers.seek(pos[len(pos)-1])
			small=0
			answerb = 0
		else:
			print "\n"
	answers.seek(0)
	answerb = 0

answers.close()
questions.close()