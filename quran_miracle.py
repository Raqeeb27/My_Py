""" import matplotlib.pyplot as plt

# Correct list of Surah numbers and their corresponding number of verses
surah_numbers = list(range(1, 115))
verses_count = [
    7, 286, 200, 176, 120, 165, 206, 75, 129, 109, 123, 111, 43, 52, 99, 128, 111, 110, 98, 135,
    112, 78, 118, 64, 77, 227, 93, 88, 69, 60, 34, 30, 73, 54, 45, 83, 182, 88, 75, 85, 54, 53,
    89, 59, 37, 35, 38, 29, 18, 45, 60, 49, 62, 55, 78, 96, 29, 22, 24, 13, 14, 11, 11, 18, 12,
    12, 30, 52, 52, 44, 28, 28, 20, 56, 40, 31, 50, 40, 46, 42, 29, 19, 36, 25, 22, 17, 19, 26,
    30, 20, 15, 21, 11, 8, 8, 19, 5, 8, 8, 11, 11, 8, 3, 9, 5, 4, 7, 3, 6, 3, 5, 4, 5, 6
]

# Create the plot
plt.figure(figsize=(15, 8))
plt.plot(surah_numbers, list(reversed(verses_count)), marker='o', linestyle='-', color='b')
plt.title('Number of Verses in Each Surah of the Quran')
plt.xlabel('Surah Number')
plt.ylabel('Number of Verses')
plt.grid(True)

# Show the plot
plt.show() """
""" import matplotlib.pyplot as plt

# Correct list of Surah numbers and their corresponding number of verses
surah_numbers = list(range(1, 115))
verses_count = [
    7, 286, 200, 176, 120, 165, 206, 75, 129, 109, 123, 111, 43, 52, 99, 128, 111, 110, 98, 135,
    112, 78, 118, 64, 77, 227, 93, 88, 69, 60, 34, 30, 73, 54, 45, 83, 182, 88, 75, 85, 54, 53,
    89, 59, 37, 35, 38, 29, 18, 45, 60, 49, 62, 55, 78, 96, 29, 22, 24, 13, 14, 11, 11, 18, 12,
    12, 30, 52, 52, 44, 28, 28, 20, 56, 40, 31, 50, 40, 46, 42, 29, 19, 36, 25, 22, 17, 19, 26,
    30, 20, 15, 21, 11, 8, 8, 19, 5, 8, 8, 11, 11, 8, 3, 9, 5, 4, 7, 3, 6, 3, 5, 4, 5, 6
]

# Create the plot
plt.figure(figsize=(15, 8))
plt.plot(surah_numbers, list(reversed(verses_count)), marker='o', linestyle='-', color='b')
plt.fill_between(surah_numbers, list(reversed(verses_count)), color='lightblue', alpha=0.5)
plt.title('Number of Verses in Each Surah of the Quran')
plt.xlabel('Surah Number')
plt.ylabel('Number of Verses')
plt.grid(True)

# Show the plot
plt.show() """

""" import matplotlib.pyplot as plt

# Correct list of Surah numbers and their corresponding number of verses
surah_numbers = list(range(1, 115))
verses_count = [
    7, 286, 200, 176, 120, 165, 206, 75, 129, 109, 123, 111, 43, 52, 99, 128, 111, 110, 98, 135,
    112, 78, 118, 64, 77, 227, 93, 88, 69, 60, 34, 30, 73, 54, 45, 83, 182, 88, 75, 85, 54, 53,
    89, 59, 37, 35, 38, 29, 18, 45, 60, 49, 62, 55, 78, 96, 29, 22, 24, 13, 14, 11, 11, 18, 12,
    12, 30, 52, 52, 44, 28, 28, 20, 56, 40, 31, 50, 40, 46, 42, 29, 19, 36, 25, 22, 17, 19, 26,
    30, 20, 15, 21, 11, 8, 8, 19, 5, 8, 8, 11, 11, 8, 3, 9, 5, 4, 7, 3, 6, 3, 5, 4, 5, 6
]

# Create the plot
plt.figure(figsize=(15, 8))
plt.plot(surah_numbers, list(reversed(verses_count)), linestyle='-', color='#4B0082')
plt.fill_between(surah_numbers, list(reversed(verses_count)), color='#4B0082', alpha=0.5)
plt.title('Number of Verses in Each Surah of the Quran')
plt.xlabel('Surah Number')
plt.ylabel('Number of Verses')
plt.grid(True)

# Show the plot
plt.show() """
import matplotlib.pyplot as plt

# Correct list of Surah numbers and their corresponding number of verses
surah_numbers = list(range(1, 115))
verses_count = [
    7, 286, 200, 176, 120, 165, 206, 75, 129, 109, 123, 111, 43, 52, 99, 128, 111, 110, 98, 135,
    112, 78, 118, 64, 77, 227, 93, 88, 69, 60, 34, 30, 73, 54, 45, 83, 182, 88, 75, 85, 54, 53,
    89, 59, 37, 35, 38, 29, 18, 45, 60, 49, 62, 55, 78, 96, 29, 22, 24, 13, 14, 11, 11, 18, 12,
    12, 30, 52, 52, 44, 28, 28, 20, 56, 40, 31, 50, 40, 46, 42, 29, 19, 36, 25, 22, 17, 19, 26,
    30, 20, 15, 21, 11, 8, 8, 19, 5, 8, 8, 11, 11, 8, 3, 9, 5, 4, 7, 3, 6, 3, 5, 4, 5, 6
]

# Create the plot
plt.figure(figsize=(15, 8))
plt.plot(surah_numbers, list(reversed(verses_count)), linestyle='-', color='#4B0082')
plt.fill_between(surah_numbers, list(reversed(verses_count)), color='#4B0082', alpha=0.5)
plt.title('Number of Verses in Each Surah of the Quran')
plt.xlabel('Surah Number')
plt.ylabel('Number of Verses')
plt.grid(True)

# Show the plot
plt.show()

