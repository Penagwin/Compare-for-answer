#!/usr/bin/env 


print "Started"
global found
answeryet = False
nextline = False
pos = []
small = 0
global answerb
answerb = 0
final = open('/home/penagwin/final.txt', 'w')
answers = open('/home/penagwin/.config/sublime-text-3/Packages/User/Question.txt', 'r')
questions = open('/home/penagwin/.config/sublime-text-3/Packages/User/Answers.txt', 'r')
for question in questions:
	found = False
	true = True
	while true == True:
		pos.append(answers.tell())
		currentquestion = question.lower().replace("\n", "")
		answer = answers.readline()
		if answer == "END OF FILE":
			true = False
		if answer.find("Question") != -1:
			answerb = 1 
		if answer.find("Answer") != -1:
			answerb = 2
		if answerb == 1:
			if answer.lower().find(currentquestion) != -1:
				final.write(answer)
				while answer.lower().find("correct answer:") == -1:
					 answer = answers.readline()
				answers.readline()
				final.write(answers.readline()+"\n\n\n")
				true = False

		if answerb == 2:
			if answer.lower().find(currentquestion) != -1:
				final.write(answer)
				while answer.lower().find("answer") == -1 or answer.lower().find("answer:") != -1:
					small = small +1
					answers.seek(pos[len(pos)-small])
					answer = answers.readline()
					answers.seek(pos[len(pos)-small-1])
				final.write(answers.readline() +"\n\n\n")
				answers.seek(pos[len(pos)-1])	
				true = False
	answers.seek(0)
	answerb = 0
	pos = []

answers.close()
final.close()
questions.close()