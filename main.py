#!/usr/bin/env 


print "Started"


answers = open('/home/penagwin/.config/sublime-text-3/Packages/User/Question.txt', 'r')
questions = open('/home/penagwin/.config/sublime-text-3/Packages/User/Question', 'r')
for question in questions:
	for answer in answers:
		currentquestion = "".join(question.split())
		if answer.find(currentquestion) != -1:
			print answer
answers.close()
questions.close()