import re

def add_time(start, duration, day_of_week=None):
    start_minutes = convert_time_to_minutes(start)
    duration_minutes = convert_duration_to_minutes(duration)
    new_time_in_minutes = start_minutes + duration_minutes
    days, hours, minutes = calculate_days_hours_minutes(new_time_in_minutes)

    new_time = format_12hr_time(hours, minutes)

    if day_of_week:
        new_time += ", " + add_day_of_week(day_of_week, days)

    new_time += format_days_later(days)

    return new_time


def convert_time_to_minutes(start):
    """ converts a time like '11:06 AM' into minutes (since midnight) """
    (h, m, am_pm) = re.search(r"(.*):(.*) ([AP]M)", start).groups()

    minutes = int(h) * 60 + int(m)

    if am_pm == "PM":
        minutes += (12 * 60)

    return minutes


def convert_duration_to_minutes(duration):
    """ converts a duration like '2:02' into minutes """
    [h, m] = duration.split(':')
    return int(h) * 60 + int(m)


def calculate_days_hours_minutes(minutes):
    """ Calculates the total days, hours, and minutes from minutes """
    days, minutes = divmod(minutes, (60 * 24))

    hours, minutes = divmod(minutes, 60)

    return (days, hours, minutes)


def format_12hr_time(hours, minutes):
    """ Takes hours and minutes and returns a string with the corresponding 12-hour time (ex: "11:05 PM") """

    minutes = str(minutes).rjust(2, '0')

    if hours == 0:
        return f"12:{minutes} AM"
    elif hours < 12:
        return f"{hours}:{minutes} AM"
    elif hours == 12:
        return f"12:{minutes} PM"
    else:
        return f"{hours - 12}:{minutes} PM"


def format_days_later(days):
    if days == 0:
        return ""
    elif days == 1:
        return " (next day)"
    else:
        return f" ({days} days later)"


def add_day_of_week(day_of_week, num_days):
    """ Returns the day of the week `num_days` after the provided `day_of_week` """

    days_of_the_week = [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday"
    ]

    current_num = days_of_the_week.index(day_of_week.lower())
    next_num = (current_num + num_days) % 7

    return days_of_the_week[next_num].title()