import re

def add_time(start, duration):

    return convert_duration_to_minutes(duration)


def convert_start_to_minutes(start):
    """ converts a start time like '11:06 AM' into minutes (since midnight) """
    (h, m, am_pm) = re.search(r"(.*):(.*) ([AP]M)", start).groups()

    minutes = int(h) * 60 + int(m)

    if am_pm == "PM":
        minutes += (12 * 60)
    
    return minutes

def convert_duration_to_minutes(duration):
    """ converts a duration like '2:02' into minutes """
    [h, m] = duration.split(':')
    return int(h) * 60 + int(m)