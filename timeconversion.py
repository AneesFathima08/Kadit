def timeConversion(s):
    time_parts = s[:-2].split(":")
    hours = int(time_parts[0])
    minutes = int(time_parts[1])
    seconds = int(time_parts[2])
    if "PM" in s and hours != 12:
        hours += 12
    elif "AM" in s and hours == 12:
        hours = 0
    time_24_hour = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
    return time_24_hour
time_string = input()
result = timeConversion(time_string)
print(result)