#!/usr/bin/env 


print "Started"

answeryet = False
nextline = False
pos = []
small = 0
answerb = False
answers = open('/home/penagwin/.config/sublime-text-3/Packages/User/Question.txt', 'r')
questions = open('/home/penagwin/.config/sublime-text-3/Packages/User/Answers.txt', 'r')
for question in questions:
	for answer in answers:
		pos.append(answers.tell())
		currentquestion = question.replace("\n", "")
		if answer.find("Correct Answer:") != -1:
			answerb = True
		if answer.find("Question") != -1:
			answerb = False 
		if answer.find(currentquestion) != -1:
			answeryet = True
		if answer.find(currentquestion) != -1 and answer == True:
			while pos.index(len(pos)-small) != "Answer":
				small = small + 1
				answers.seek(pos.index(len(pos)-small))

			answers.seek(pos.index(len(pos)-small-1))
			print answers
			answers.seek(pos.index(len(pos)))
			small=0

		if nextline == True and answer != "\n":
			print question
			print answer + "\n \n"
			nextline = False
			answeryet = False
		
		

		


	answers.seek(0)
	nextline = False
	answeryet = False

answers.close()
questions.close()