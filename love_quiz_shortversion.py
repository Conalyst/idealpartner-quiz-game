#!/user/bin/env python3

def play_exit():
	print("#### OUTLOOK ON LOVE ####")
	print("This quiz tells you your outlook on love based on your choices for each option.\nWould you like to play?\n\n'PLAY' (enter 1)   'EXIT' (enter 2)")
	while True:
		usr_input = input()
		if usr_input == 1:
			return False
		if usr_input == 2:
			exit()


def user_input():
	while True:
		print("Please enter the number of your choice")
		usr_input = input()
		if usr_input == 1 or usr_input == 2 or usr_input == 3 or usr_input == 4:
			return usr_input
		else:
			print("Please enter either 1, 2, 3 or 4")


def chosen_option():
	u = user_input() - 1
	answers.append(u)		


def show_question(question, options, n):
	a = question[n]
	b = options[n]
	print(a)
	print(b)
	chosen_option()


def convert_answer(a_list, o_list):
	indx = 0
	while indx < len(a_list):
		current_a = a_list[indx]
		current_o = o_list[indx]
		trans = current_o[current_a]
		converted.append(trans)
		indx += 1


def end_story(s_list, a_list):
	indx = 0
	while indx < len(a_list):
		if indx == 2:
			print(s_list[indx].format(a_list[indx]))
		else:
			print("\n" + s_list[indx] + a_list[indx])
		indx += 1


############ QUIZ GAME ###################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
#The quiz
question_list = ["\nThe end of the world is coming.\nIf you can save only one kind of animal, which would you choose?", "\nSuddenly, you transform into an animal.\nWhat are you?", "\nYou gained the power to make one species disappear forever, which one will it be?", "\nAn animal is speaking with you, which animal is speaking?", "\nYou are on an isolated island and you have a companion, which animal is with you?", "\nYou have the ability to tame all creatures.\nWhich creature would you prefer as a pet?", "\n~Bibbidi~bobbidi~doo~ You have turned into an animal for 5 minutes.\nWhat animal have you turned into?"]
options_list = ["1) Rabbit\n2) Sheep\n3) Deer\n4) Horse", "1) Snake\n2) Cat\n3) Dog\n4) Horse", "1) Snake\n2) Crocodile\n3) Lion\n4) Shark", "1) Bird\n2) Rabbit\n3) Sheep\n4) Horse", "1) Bird\n2) Dog\n3) Pig\n4) Cow", "1) White Leopard\n2) White Tiger\n3) Polar Bear\n4) Dinosaur", "1) Dove\n2) Cat\n3) Lion\n4) Horse"]
story_list = ["The type of person you are most likely to be attracted to is percieved as being ", "On the other hand, the self-impression you want to give to your partner is that you are ", "If your partner is very {}, it could lead you to break up with him/her.", "The kind of relationship that you wish to build with your partner is ", "When it comes to the question if you are capable of cheating, ", "Your view on marriage is ", "In the present moment, your view on love is "]

#### The answers
q1 = ["cold as ice on the outside, but warm on the inside.", "obedient and warm.", "elegant and and well-mannered.", "unbridled and free-spirited."]
q2 = ["an intuitive and flexible person.", "a creative person.", "a loyal and faithful person.", "an optimistic person."]
q3 = ["emotional and moody, and you don't know how to please him/her", "ruthless", "arrogant and authoritative", "insecure"]
q4 = ["a long-lasting relationship.", "the kind that makes you feel warm and always in love.", "the kind where you both know what the other person is thinking without saying a word.", "the kind where you are able to talk about everything and anything with no secrets between the two of you."]
q5 = ["you don't really like to make commitments and could maybe cheat.", "you likely would not.", "you have a hard time resisting desire and lust and is likely to cheat.", "you do not reject advances from other people, but also try to not to cheat."]
q6 = ["that you have always wanted to get married but don't actually know what it is all about.", "that it is something precious. Once married, you treasure you partner and the marriage very much.", "that you are actually a little bit afraid of marrieage, and you think it will take away your freedom.", "quite pessimistic. You don't think happy marriages exist anymore nowadays."]
q7 = ["that it is a commitment of both parties.", "as something you can get and trash anytime. Some may say you are a bit self-entered.", "that you are thirsty for it and can do anything for love, however, you won't fall for it easily.", "that you don't really want to be tied by a steady relationship, you just want to flirt around."]
options = [q1, q2, q3, q4, q5, q6, q7]
answers = []
converted = []


#### The game	
play_exit()

lazy = 0
while lazy != 7:
	show_question(question_list, options_list, lazy)
	lazy += 1

print("\n#### Here are the results! ####\n")
convert_answer(answers, options)
end_story(story_list, converted)