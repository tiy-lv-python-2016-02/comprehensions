import datetime
import csv
from collections import defaultdict


def day_dict(info):
    """
    Loops through info and converts Date to a datetime weekday number.
    :param info: A list of dicts containing a "Date" field.
    :return: Updated dicts and a set of days of the week found in info.
    """
    days = []

    new = []

    for d in info:
        date = d["Date"]
        year, month, day = [int(x) for x in date.split("-")]
        new_date = datetime.date(year, month, day).weekday()
        days.append(new_date)

        new_row = d.copy()
        new_row["Date"] = new_date
        new.append(new_row)

    return new, set(days)


def combine_day(data, day):
    """
    Combines all information from dicts which match the day given.
    :param data: List of dictionaries
    :param day: Numerical day of the week.
    :return: A dictionary combined on day.
    """
    combined = defaultdict(list)
    keys = [x for x in data[0].keys() if x not in ["", "Date"]]
    for row in [x for x in data if x["Date"] == day]:
        for key in keys:
            combined[key].append(row[key])
    return dict(combined)


def dict_averages(working_dict, days):
    """
    Take dict with values combined by day and replace the list with
    an average.
    :param working_dict: A dict of dicts combined by day.
    :param days: Days that working_dict was combined on.
    :return: A dict of values averaged.
    """
    avgerages_dict = defaultdict(dict)
    for day in days:
        for key in working_dict[day].keys():
            new_val = [float(x) for x in working_dict[day][key]]
            avgerages_dict[day][key] = sum(new_val) / len(new_val)
    return dict(avgerages_dict)


def best_surf(info):
    """
    Rates the best days for surfing in the data set by multiplying the
    water temp by wave height.
    :param info: List of dictionaries with daily information.
    :return: Prints out the top five results by score.
    """
    ratings = {}
    for row in info:
        score = float(row["Water Temp"]) * float(row["Wave Height"])
        ratings[row["Date"]] = score
    ranked = sorted(ratings.items(), key=lambda x: x[1], reverse=True)
    for day, score in ranked[:5]:
        print(day, score)
    return "Done"


if __name__ == '__main__':
    with open("buoy.csv") as file:
        reader = csv.DictReader(file)
        info = [x for x in reader]

    data, days = day_dict(info)

    by_day_dict = {}
    for day in days:
        combined = combine_day(data, day)
        by_day_dict[day] = combined

    daily_avg_dict = dict_averages(by_day_dict, days)
    print(best_surf(info))
