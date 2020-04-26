"""
Replace the contents of this module docstring with your own details
Name: YuYang Huang
Date started: 23 Apr 2020
GitHub URL: https://github.com/YuYangHuangJCU/1404.git
"""

# Import CSV file and append them to a list. Frame work of main function done.

import csv

song_list = []

with open('songs.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        print(line)
        song_list.append(line)

song_list.sort(
    key=lambda l: (l[1], l[0])
)


def main():

    print('Hi, welcome to this Songs-To-Learn Program! I\'m YuYang Huang.\n\nSongs to Learn 1.0 - by YuYang Huang\n\n{} songs loaded\n'.format(len(song_list)))
    running = True
    while running:
        # Display the menu
        running = Menu()