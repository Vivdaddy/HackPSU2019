# Dungeons and Dragons Alignment Control	
# Version 1.0 "Monty Python in my Pants"
# Version 2.0 "My Anandconda Don't"

# Ten questions 

# Two Forks

# Good Vs Evil
# Chaotic Vs Neutral

# Need goodness counter 
# Need chaos counter
goodness_counter=0
chaos_counter=0


goodness_questions=["Have you betrayed anyone's trust?\n","Do you care about yourself more than others?\n",
"Would you sacrifice yourself for the survival several others?\n","Would you kill a cockroach you find in the bathroom?\n"]
goodness_answers=['n','n','y','n']

chaos_questions=["If a law was unjust, would you follow it?\n","Would you change a system instead of following it?\n",
"Do people know what's good for them?\n", "If your subordinate made a mistake, would you take responsibility for his actions when you explain to a superior?\n"]
chaos_answers=['n','y','y','n']

def invalid_message():
	print("Please use yes (or) no")

def ask_question(question_list,question_index):
	answer=str(input(question_list[question_index]))
	if answer!="yes" or answer!="no":
		return answer
	#print(answer)
	while answer !="yes" or answer != "no":
		invalid_message()
		ask_question(question_list,question_index)
		
	return answer

def update_counter(counter, index, answer, answer_list):
	if answer == answer_list[index]:
		counter+=1
	return 

def calc_goodness(counter):
	if counter<2:
		return "Evil"
	elif counter==2:
		return "Neutral"
	else:
		return "Good"

def calc_chaotic(counter):
	if counter<2:
		return "Lawful"
	elif counter==2:
		return "Neutral"
	else:
		return "Chaotic"

def initialize():
	goodness_counter=0
	chaos_counter=0
	print('''
			 Welcome to the Dungeons and Dragons Alignment Determiner!

			 This was created during Hack PSU 2019 by Sydney Montgomery and Vivek Anand
	 		 Version 1.0 "Monty Python in my Pants"
	 		 Version 2.0 (Upcoming) "My Anandconda Don't"
	 		 
	 		 Please answer the following questions with a y/n and we will determine your alignment
	  ''')
	return

def run_questionnaire():
	initialize()
	for good_question_index in range(0,len(goodness_questions)):
		answer=ask_question(goodness_questions,good_question_index)
		update_counter(goodness_counter, good_question_index, answer, goodness_answers)
		goodness_description=calc_goodness(goodness_counter)

	for chaos_question_index in range(0,len(chaos_questions)):
		answer=ask_question(chaos_questions,chaos_question_index)
		update_counter(chaos_counter, chaos_question_index, answer, chaos_answers)
		chaos_description=calc_chaotic(chaos_counter)
	print(''' You have been found to be %s %s person. Thank you for taking part! Have a lovely day!

		''' %(chaos_description,goodness_description))
	return

run_questionnaire()






