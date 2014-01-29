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
	for answer in answers:
		pos.append(answers.tell())
		currentquestion = question.replace("\n", "")
		if answer.find("Question") != -1:
			answerb = 1 
		elif answer.find("Correct Answer:") != -1:
			answerb = 2
		
		if answer.find(currentquestion) != -1 and answerb == 1:
			print answer
		if answer.find(currentquestion) != -1 and answerb == 2:
			answers.seek(pos[len(pos)-2])
			while answer.find("Answer") != -1 and answer.find("Answer:") == -1:
				small = small +1
				answers.seek(pos[len(pos)-1])
			answers.seek(pos[len(pos)-small-2])
			print answer
			answers.seek(pos[len(pos)-1])
			small=0
			answerb = 0
	answers.seek(0)
	answerb = 0

answers.close()
questions.close()