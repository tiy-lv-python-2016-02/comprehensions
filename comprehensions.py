import csv
from functools import reduce

if __name__ == '__main__':

    sent = "List Comprehensions are the Greatest!"
    vowels_removed = ''.join([letter for letter in sent if letter not in "aeiou"])
    print(vowels_removed)

    with open("buoy.csv") as file:
        reader = csv.DictReader(file)
        rows = [row for row in reader]

    water_temps = [row["Water Temp"] for row in rows]
    print(water_temps)

    floats = [float(x) for x in water_temps]
    print(floats)

    fahrenheit = [int(((float(9)/5) * x + 32)) for x in floats]
    print(fahrenheit)

    wave_height = {row['Wave Height']: row['Date'] for row in rows}
    print(wave_height)

    new_dict = {'Gale': {'Homework 1': 88, 'Homework 2': 76},
                'Jordan': {'Homework 1': 92, 'Homework 2': 87},
                'Peyton': {'Homework 1': 84, 'Homework 2': 77},
                'River': {'Homework 1': 85, 'Homework 2': 91}}

    homework_avg = [i['Homework 1'] for i in new_dict.values()]
    print(reduce(lambda x, y: x + y, homework_avg) / len(homework_avg))
