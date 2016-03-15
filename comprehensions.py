import csv
from functools import reduce


sent = "List Comprehensions are the Greatest!"
vowels_removed = ''.join([letter for letter in sent if letter not in "aeiou"])
print(vowels_removed)

with open("buoy.csv") as file:
    reader = csv.DictReader(file)
    water_temps = [row["Water Temp"] for row in reader]
    print(water_temps)
    floats = [float(x) for x in water_temps]
    print(floats)
    fahrenheit = [int(((float(9)/5) * x + 32)) for x in floats]
    print(fahrenheit)

with open("buoy.csv") as file:
    reader = csv.reader(file)
    headers = next(reader)
    wave_height = {row[5]: row[1] for row in reader}
    print(wave_height)

new_dict = {'Gale': {'Homework 1': 88, 'Homework 2': 76},
            'Jordan': {'Homework 1': 92, 'Homework 2': 87},
            'Peyton': {'Homework 1': 84, 'Homework 2': 77},
            'River': {'Homework 1': 85, 'Homework 2': 91}}

homework_avg = [i['Homework 1'] for i in new_dict.values()]
print(reduce(lambda x, y: x + y, homework_avg) / len(homework_avg))
