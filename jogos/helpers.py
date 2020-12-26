import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def normalize(word):
    return word.strip().upper()


def find_all(word, letter):
    indexes = []
    current_index = 0
    can_search = letter in word

    while (can_search):
        found_index = word.find(letter, current_index)
        indexes.append(found_index)

        current_index = found_index + 1
        can_search = letter in word[current_index:]

    return indexes


def map_positions(word):
    positions_dict = {}

    for i in range(len(word)):
        letter = word[i]
        if (letter not in positions_dict):
            positions_dict[letter] = []
        positions_dict[letter].append(i)

    return positions_dict