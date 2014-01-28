#!/usr/bin/env 


print "Started"


answers = open('/home/penagwin/.config/sublime-text-3/Packages/User/Question.txt', 'r')
questions = open('/home/penagwin/.config/sublime-text-3/Packages/User/Question', 'r')
for question in questions:
	if not question == "\n":
		for answer in answers:
			if answer.find("Core Democratic Values") != -1:
				print answer
