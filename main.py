#!/usr/bin/env 


print "Started"
global found
answeryet = False
nextline = False
pos = []
small = 0
global answerb
answerb = 0
answers = open('/home/penagwin/.config/sublime-text-3/Packages/User/Question.txt', 'r')
questions = open('/home/penagwin/.config/sublime-text-3/Packages/User/Answers.txt', 'r')
for question in questions:
	found = False
	true = True
	while true == True:
		pos.append(answers.tell())
		currentquestion = question.replace("\n", "")
		answer = answers.readline()
		if answer == "END OF FILE":
			true = False
		if found == True:
			true = False
		if answer.find("Question") != -1:
			answerb = 1 
		if answer.find("Correct Answer:") != -1:
			answerb = 2
		if answerb == 1:
			print answerb
			if answer.find(currentquestion) != -1:
				print answer
				while answer.lower().find("answer:") == -1:
					 answer = answers.readline()
				answers.readline()
				print answers.readline()
				found =True

		if answerb == 2:
			if answer.find(currentquestion) != -1:
				print answer
				while answer.lower().find("answer") == -1 or answer.lower().find("answer:") != -1:
					small = small +1
					answers.seek(pos[len(pos)-small])
					answer = answers.readline()
					answers.seek(pos[len(pos)-small-1])
				print answers.readline() +"\n\n\n"
				answers.seek(pos[len(pos)-1])
				
				found = True
	answers.seek(0)
	answerb = 0
	pos = []

answers.close()
questions.close()