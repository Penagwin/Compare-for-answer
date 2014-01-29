#!/usr/bin/env 


print "Started"

answeryet = False
nextline = False
answers = open('/home/penagwin/.config/sublime-text-3/Packages/User/Question.txt', 'r')
questions = open('/home/penagwin/.config/sublime-text-3/Packages/User/Answers.txt', 'r')
for question in questions:
	for answer in answers:
		currentquestion = question.replace("\n", "")
		if answer.find(currentquestion) != -1:
			answeryet = True
		if nextline == True and answer != "\n":
			print question
			print answer + "\n \n"
			nextline = False
			answeryet = False
		if answer.find("Correct Answer:") != -1:
			nextline = True
		


	answers.seek(0)
	nextline = False
	answeryet = False

answers.close()
questions.close()