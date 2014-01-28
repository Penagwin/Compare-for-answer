#!/usr/bin/env 


print "Started"


answers = open('/home/penagwin/.config/sublime-text-3/Packages/User/Question.txt', 'r')
questions = open('/home/penagwin/.config/sublime-text-3/Packages/User/Question', 'r')
for question in questions:
	if not question == "\n":
		for answer in answers:
				print answer.find(question)
				print answer
				print question
