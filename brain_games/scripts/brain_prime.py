import prompt
import random
def easy_number():
	counter_number = 0
	print('Welcome to the Brain Games!')
	name = prompt.string('May I have your name? ')
	print('Hello,', name + '!')    
	print('Answer "yes" if given number is prime. Otherwise answer "no".')
	counter_answer = 0
	for i in range(3):
		number = random.randint(2, 100)
		print('Question:', number)
		answer = prompt.string('Your answer: ')
		flag = True
		for j in range(2, (number // 2 + 1)):	
			if number % j == 0: 
				flag = False
		if answer == 'yes' and flag == True or answer == 'no' and flag == False:
			counter_number += 1
			print('Correct!')
		elif answer != 'yes' and flag == True:
			print("'no' is wrong answer ;(. Correct answer was 'yes'.")
			print("Let's try again,", name + '!')
			return False
		elif answer != 'no' and flag == False:	
			print("'yes' is wrong answer ;(. Correct answer was 'no'.")
			print("Let's try again,", name + '!')
			return False
		if counter_number == 3:
			print('Congratulations,', name + '!')
			return True
        		
        		
def main():
    easy_number()
if __name__ == "__main__":  
    main()
