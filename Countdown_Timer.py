import sys
import pyfiglet
from time import sleep


def countdown(timer):
    print()
    last_lines = 0
    while timer >= 0:
        hours, remainder = divmod(timer, 3600)
        minutes, seconds = divmod(remainder, 60)
        display_time = f'{hours:02d}:{minutes:02d}:{seconds:02d}'

        # Render figlet text
        big_text = pyfiglet.figlet_format(display_time, font="big")
        lines = big_text.splitlines()

        # Move cursor up to overwrite previous lines
        if last_lines:
            sys.stdout.write("\033[F" * last_lines)

        # Print and flush
        for line in lines:
            sys.stdout.write("\033[K" + line + "\n")
        sys.stdout.flush()

        last_lines = len(lines)
        timer -= 1
        if timer < 0:
            return
        sleep(1)


print("\n" + " Countdown ".center(19, "-"))
input_time = int(input("\nEnter the time in seconds: "))
if input_time <= 0:
    print("\nEnter Positive integer!\n")
    exit(1)
input("\n --> Press Enter to start the timer: ")
try:
    countdown(input_time)
except (ValueError, OSError) as e:
    print(f"\n\nError: {e}")
    exit(1)
except (KeyboardInterrupt, EOFError):
    print("\n\nKeyboard Interrupt!!!\nExiting...\n")
    exit(1)

print('!!! Times Up !!!\n')
