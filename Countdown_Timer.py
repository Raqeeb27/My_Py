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
try:
    input_time = int(input("\nEnter the time in seconds: "))
    if input_time <= 0:
        print("\nEnter Positive integer!\n")
        exit(1)
    input("\nPress Enter to start the timer")
    countdown(input_time)
except (ValueError, OSError) as e:
    print(f"\n\nError: {e}")
    exit(1)
except (KeyboardInterrupt, EOFError):
    print("\n\nKeyboard Interrupt!!!\nExiting...\n")
    exit(1)

print('\n\n!!! Times Up !!!\n')
