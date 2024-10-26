from time import sleep

def countdown(timer):
	print()
	while timer:
		hours, remainder = divmod(timer, 3600)
		minutes, seconds = divmod(remainder, 60)
		display_time = f'{hours:02d}:{minutes:02d}:{seconds:02d}'
		print(f'--{display_time}--', end="\r")
		sleep(1)
		timer -= 1
	print(f'--00:00:00--', end="\r")

print("\n" + " Countdown ".center(19, "-"))
input_time = int(input("Enter the time in seconds: "))

try:
	countdown(input_time)
except KeyboardInterrupt:
    print("\n\nKeyboard Interrupt!!!\nExiting...\n")
    exit(1)

print('\n\n!!! Times Up !!!\n')
