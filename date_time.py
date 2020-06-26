import datetime

GMT_TIME = {"Los Angeles": -8, "New York": -5, "Caracas": -4.5, "Buenos Aires": -3, "London": 0, "Rome": 1,
            "Moscow": 3, "Tehran": 3.5, "New Delhi": 5.5, "Beijing": 8, "Canberra": 10}

months = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8,
          "September": 9,
          "October": 10, "November": 11, "December": 12}

COMMA, SPACE, COLON = ",", " ", ":"


def current_timestamp(s: str):
    month, date, year, time = s.replace(COMMA, SPACE).split()
    hours, minutes = time.split(COLON)
    time_stamp = datetime.datetime(int(year), months[month], int(date), int(hours), int(minutes))
    return time_stamp


def time_diff(city_a, timestamp, city_b):
    difference = abs(GMT_TIME[city_a] - GMT_TIME[city_b])
    timestamp_now = current_timestamp(timestamp)
    return timestamp_now + datetime.timedelta(hours=difference)


print(time_diff("Los Angeles", "April 1, 2011 23:23", "Canberra"))
print(time_diff("London", "July 31, 1983 23:01", "Rome"))
print(time_diff("New York", "December 31, 1970 13:40", "Beijing"))








