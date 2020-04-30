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

# Menu function responsible for displaying the menu


def Menu():
    choice_valid = False
    # Loop unitil valid choice is entered.
    while choice_valid == False:

        choice = input(  # Get input and change to lower case
            '\nMenu:\nL - List songs\nA - Add new song\nC - Complete a song\nQ - Quit\n>>> ').lower()
        choice_valid = Menu_Handler(choice)
    if choice == 'l':  # Selection
        song_list.sort(
            key=lambda l: (l[1], l[0])
        )
        List_Songs()
        return True
    elif choice == 'a':
        Add_new_songs()
        return True
    elif choice == 'c':
        Complete_Songs()
        return True
    else:
        with open('songs.csv', 'w', newline='\n') as f:  # Write to csv and quit
            writer = csv.writer(f)
            for i in song_list:
                writer.writerow(i)
        print('{} songs saved to songs.csv\nHave a nice day :)'.format(
            len(song_list)))
        return False


# Menu error handling.
def Menu_Handler(choice):

    if(choice != 'l' and choice != 'a' and choice != 'c' and choice != 'q'):
        print('Invalid Menu Choice!')
        return False
    else:
        return True
# List all songs.


def List_Songs():
    learned = 0
    unlearned = 0
    for i in range(len(song_list)):

        if(song_list[i][-1] == 'u'):
            unlearned += 1
            print('  {}. * {} - {}  ({})'.format(i,
                                                 song_list[i][0], song_list[i][1], song_list[i][2]))
        else:
            learned += 1
            print('  {}.   {} - {}  ({})'.format(i,
                                                 song_list[i][0], song_list[i][1], song_list[i][2]))
    print('{} songs learned, {} songs still to learn'.format(learned, unlearned))

# Add new songs function


def Add_new_songs():
    # Loop to validate until correct
    invalid = True
    while invalid:
        title = input('Title: ')
        invalid = Add_new_songs_handler(title)

    invalid = True
    while invalid:
        artist = input('Artist: ')
        invalid = Add_new_songs_handler(artist)

    invalid = True
    while invalid:
        year = input('Year: ')
        try:
            year = int(year)
        except:  # Exception
            print('Invalid input; enter a valid number')
            continue

        if year == '':
            print('Year cannot be blank')

        elif year < 0:
            print('Number must be >= 0')
        else:
            invalid = False
    print('{} by {} ({}) added to song list'.format(title, artist, year))
    song = [title, artist, year, 'u']
    song_list.append(song)

# Function for handling add new song input


def Add_new_songs_handler(name):
    if(name == ''):
        print('Input cannot be blank')
        return True
    else:
        return False

# Function for complete a song


def Complete_Songs():
    Learned = 0
    # See whether a song is learned or unlearned
    for i in song_list:
        if i[-1] == 'l':
            Learned += 1
        else:
            Learned -= 1
    if(Learned == len(song_list)):
        print('No more songs to learn!')
        return
    else:

        invalid = True
        while invalid:
            number = input(
                'Enter the number of a song to mark as learned\n>>>')
            invalid = Complete_Songs_Handler(number)
        if(song_list[int(number)][3] == 'l'):
            print('You have already learned {}'.format(
                song_list[int(number)][0]))
        elif(song_list[int(number)][3] == 'u'):
            print('{} by {} learned '.format(
                song_list[int(number)][0], song_list[int(number)][1]))
            song_list[int(number)][3] = 'l'

# Function for handling correct output for complete a song


def Complete_Songs_Handler(number):
    try:
        number = int(number)
    except:
        print('Invalid input; enter a valid number')
        return True
    if number < 0:
        print('Number msut be >= 0')
        return True
    elif number >= len(song_list):
        print('Invalid song number')
        return True
    else:
        return False


main()  # Activate main function