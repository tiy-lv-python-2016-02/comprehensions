import csv


def remove_vowels(sentence):
    vowels = "aeiou"
    return "".join([x for x in sentence if x not in vowels])


def temps_data(reader):
    """ Return a list of water temps """
    temps = [row["Water Temp"] for row in reader]
    return temps


def temps_float(temps):
    return [float(x) for x in temps]


def celsius_to_fahrenheit(temps):
    return [int((x * 1.8) + 32) for x in temps]


def date_waveheight_dict(info):
    return {row["Date"]: row["Wave Height"] for row in info}


def first_homework(homework):
    grades = [x["Homework 1"]
              for x in [homework[key] for key in homework]
              ]
    return sum(grades) / len(grades)


if __name__ == '__main__':

    with open("buoy.csv") as file:
        reader = csv.DictReader(file)
        info = [x for x in reader]

    temps_list = temps_data(info)
    float_temps = temps_float(temps_list)
    fahrenheit_temps = celsius_to_fahrenheit(float_temps)
    wave_dict = date_waveheight_dict(info)

    old_sentence = "List Comprehensions are the Greatest!"
    new_sentence = remove_vowels(old_sentence)

    homework = {'Gale': {'Homework 1': 88, 'Homework 2': 76},
                'Jordan': {'Homework 1': 92, 'Homework 2': 87},
                'Peyton': {'Homework 1': 84, 'Homework 2': 77},
                'River': {'Homework 1': 85, 'Homework 2': 91}
                }
    homework_avg = first_homework(homework)


