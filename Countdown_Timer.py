from time import sleep

def countdown(timer):
	
	while timer:
		minutes, seconds = divmod(timer, 60)
		display_time = f'{minutes:02d}:{seconds:02d}'
		print(f'--{display_time}--', end="\r")
		sleep(1)
		timer -= 1

input_time = int(input("Enter the time in seconds: "))

countdown(input_time)

print('\n!!! Times Up !!!\n')
