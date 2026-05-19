# Write the code for your lab 1 here.  Read the specs carefully.  
# Function name must be exactly as provided.  
# Names of variables and parameters can be whatever you wish it to be
#
# To test, run the following command :
#     python test_lab1.py
#
# Author: Shariful Islam	
# Student Number: 106975246
#

def wins_rock_scissors_paper(player, opponent):
	if player.lower() =="rock" and opponent.lower() == "scissors":
		return True
	elif player.lower() =="scissors" and opponent.lower() == "paper":
		return True
	elif player.lower() =="paper" and opponent.lower() == "rock":
		return True	
	return False

def factorial(n):

	result = 1
	if n == 0:
		result = 1
	
	for i in range (1, n+1):
		result = result*i

	return result


def fibonacci(n):

    if n == 0:
        return 0

    if n == 1:
        return 1

    a = 0
    b = 1

    for i in range(2, n + 1):

        temp = a + b
        a = b
        b = temp

    return b

def sum_to_goal(numbers, goal):
	
	for i in range(len(numbers)):
		for j in range(i+1, len(numbers)):
			if numbers[i] + numbers[j] == goal:
				return numbers[i]*numbers[j]
	return 0

    

class UpCounter:

    def __init__(self, step=1):

        self.step = step
        self.value = 0

    def count(self):

        return self.value

    def update(self):

        self.value = self.value + self.step


class DownCounter(UpCounter):
	
	def update(self):
		self.value = self.value - self.step


