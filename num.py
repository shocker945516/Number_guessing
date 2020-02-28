import random
ans = random.randint(1, 100)
while True:
	num = input('Guess a number between 1 to 100: ')
	num = int(num)
	if num == ans:
		print('Correct!')
		break
	else:
		if ans < num:
			print('Incorrect. The number is smaller then your guess.')
		else:
			print('Incorrect. The number is bigger then your guess.')