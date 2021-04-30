#!/usr/bin/env python3


def play_exit():
	while True:
		print("'Play' (enter 1)'    'Exit' (enter 2)")
		usr_input = input()
		if usr_input == 1:
			return False
		if usr_input == 2:
			exit()
		else:
			print("Please enter either 1 or 2")


def user_input():
	loop = True
	while loop == True:
		n = input()
		if n == 1 or n == 2 or n == 3 or n == 4:
			choice = n
			loop = False
			return choice
		else:
			print ("Please enter either 1, 2, 3, or 4")


def Q1():
	print("\nThe end of the world is coming.\nIf you can save only one kind of animal, which would you choose?\n")
	print("Please enter the number of your choice")
	print("1) Rabbit\n2) Sheep\n3) Deer\n4) Horse")
	n = user_input()
	if n == 1:
		print("You chose Rabbit.\n")
		answer_list.append("cold as ice on the outside, but warm on the inside.")
	if n == 2:
		print("You chose Sheep.\n")
		answer_list.append("obedient and warm.")
	if n == 3:
		print("You chose Deer.\n")
		answer_list.append("elegant and and well-mannered.")
	if n == 4:
		print("You chose Horse.\n")
		answer_list.append("unbridled and free-spirited.")


def Q2():
	print("\nSuddenly, you transform into an animal.\nWhat are you?\n")
	print("Please enter the number of your choice")
	print("1) Snake\n2) Cat\n3) Dog\n4) Horse")
	n = user_input()
	if n == 1:
		print("You chose Snake.\n")
		answer_list.append("an intuitive and flexible person.")
	if n == 2:
		print("You chose Cat.\n")
		answer_list.append("a creative person.")
	if n == 3:
		print("You chose Dog.\n")
		answer_list.append("a loyal and faithful person.")
	if n == 4:
		print("You chose Horse.\n")
		answer_list.append("an optimistic person.")
	

def Q3():
	print("\nYou gained the power to make one species disappear forever, which one will it be?\n")
	print("Please enter the number of your choice")
	print("1) Snake\n2) Crocodile\n3) Lion\n4) Shark")
	n = user_input()
	if n == 1:
		print("You chose Snake.\n")
		answer_list.append("emotional and moody, and you don't know how to please him/her")
	if n == 2:
		print("You chose Crocodile.\n")
		answer_list.append("ruthless")
	if n == 3:
		print("You chose Lion.\n")
		answer_list.append("arrogant and authoritative")
	if n == 4:
		print("You chose Shark.\n")
		answer_list.append("insecure")


def Q4():
	print("\nAn animal is speaking with you, which animal is speaking?\n")
	print("Please enter the number of your choice")
	print("1) Bird\n2) Rabbit\n3) Sheep\n4) Horse")
	n = user_input()
	if n == 1:
		print("You chose Bird.\n")
		answer_list.append("a long-lasting relationship.")
	if n == 2:
		print("You chose Rabbit.\n")
		answer_list.append("the kind that makes you feel warm and always in love.")
	if n == 3:
		print("You chose Sheep.\n")
		answer_list.append("the kind where you both know what the other person is thinking without saying a word.")
	if n == 4:
		print("You chose Horse.\n")
		answer_list.append("the kind where you are able to talk about everything and anything with no secrets between the two of you.")


def Q5():
	print("\nYou are on an isolated island and you have a companion, which animal is with you?\n")
	print("Please enter the number of your choice")
	print("1) Bird\n2) Dog\n3) Pig\n4) Cow")
	n = user_input()
	if n == 1:
		print("You chose Bird.\n")
		answer_list.append("you don't really like to make commitments and could maybe cheat.")
	if n == 2:
		print("You chose Dog.\n")
		answer_list.append("you likely would not.")
	if n == 3:
		print("You chose Pig.\n")
		answer_list.append("you have a hard time resisting desire and lust and is likely to cheat.")
	if n == 4:
		print("You chose Cow.\n")
		answer_list.append("you do not reject advances from other people, but also try to not to cheat.")


def Q6():
	print("\nYou have the ability to tame all creatures.\nWhich creature would you prefer as a pet?\n")
	print("Please enter the number of your choice")
	print("1) White Leopard\n2) White Tiger\n3) Polar Bear\n4) Dinosaur")
	n = user_input()
	if n == 1:
		print("You chose White Leopard.\n")
		answer_list.append("that you have always wanted to get married but don't actually know what it is all about.")
	if n == 2:
		print("You chose White Tiger.\n")
		answer_list.append("that it is something precious. Once married, you treasure you partner and the marriage very much.")
	if n == 3:
		print("You chose Polar Bear.\n")
		answer_list.append("that you are actually a little bit afraid of marrieage, and you think it will take away your freedom.")
	if n == 4:
		print("You chose Dinosaur.\n")
		answer_list.append("quite pessimistic. You don't think happy marriages exist anymore nowadays.")


def Q7():
	print("\n~Bibbidi~bobbidi~doo~ You have turned into an animal for 5 minutes.\nWhat animal have you turned into?\n")
	print("Please enter the number of your choice")	
	print("1) Dove\n2) Cat\n3) Lion\n4) Horse")
	n = user_input()
	if n == 1:
		print("You chose Dove.\n")
		answer_list.append("that it is a commitment of both parties.")
	if n == 2:
		print("You chose Cat.\n")
		answer_list.append("as something you can get and trash anytime. Some may say you are a bit self-entered.")
	if n == 3:
		print("You chose Lion.\n")
		answer_list.append("that you are thirsty for it and can do anything for love, however, you won't fall for it easily.")
	if n == 4:
		print("You chose Horse.\n")
		answer_list.append("that you don't really want to be tied by a steady relationship, you just want to flirt around.")

def results(n):
	if n == 2:
		a = story[2]
		b = answer_list[2]
		print(a.format(b) + "\n")
	else:
		a = story
		b = answer_list
		print(a[n] + b[n] + "\n")



############ GAME TEST ##################################################################################
while True:
	story = ["The type of person you are most likely to be attracted to is percieved as being ", "On the other hand, the self-impression you want to give to your partner is that you are ", "If your partner is very {}, it could lead you to break up with him/her.", "The kind of relationship that you wish to build with your partner is ", "When it comes to the question if you are capable of cheating, ", "Your view on marriage is ", "In the present moment, your view on love is "]
	answer_list = []
	
	print("\n#### ROMANCE QUIZ ####\n\nWelcome!\nThis quiz provides you your outlook on love.\nYour choices represent your views on love and relationships.\n\nDo you want to play this quiz?\n")
	play_exit()
	Q1()
	Q2()
	Q3()
	Q4()
	Q5()
	Q6()
	Q7()
	
	print("\n#### Here are the results! ####\n")
	results(0)
	results(1)
	results(2)
	results(3)
	results(4)
	results(5)
	results(6)
	break