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