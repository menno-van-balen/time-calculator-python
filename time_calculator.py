def add_time(start, duration, day="Day"):
    # #### declaration of variables needed and error prevention #####
    # check the day input
    if type(day) != str:
        print("Error: day needs to be a string")
        return "Error: day needs to be a sting"

    day = day.lower().capitalize()

    days = ("Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday")

    if day not in days and day != "Day":
        print("Error: did you misspelled the day?")
        return "Error: did you misspelled the day?"

    # check input time and duration
    if type(start) != str or type(duration) != str:
        print("Error: start and duration have to be a string")
        return "Error: start and duration have to be a string"
    elif start.count(":") != 1 or duration.count(":") != 1:
        print("Error: start time and duration need to have a colon: hh:mm")
        return "Error: start and duration needs to have a colon: hh:mm"

    # we can create variables needed if input passed the checks
    start_time = start.split(" ")[0]
    period = start.split(" ")[1].upper()
    start_hours = start_time.split(":")[0]
    start_min = start_time.split(":")[1]
    duration_hours = duration.split(":")[0]
    duration_min = duration.split(":")[1]

    # check all other errors that can occur
    if (
        len(start_hours) < 1 or len(start_hours) > 2
    ):
        print('Error: hour notation from start time',
              'can only have 1 or 2 digits')
        return ('Error: hour notation from start time',
                'can only have one or two digits')
    elif (
        len(start_min) != 2 or
        len(duration_min) != 2
    ):
        print("Error: minutes need to have two digits")
        return "Error: minutes need to have two digits"
    elif not(period == "AM" or period == "PM"):
        print('Error: start time needs to have a period: hh:mm AM or PM')
        return 'Error: start time needs to have a period: hh:mm AM or PM'
    elif (
            start_hours.isdigit() is False or
            start_min.isdigit() is False or
            duration_hours.isdigit() is False or
            duration_min.isdigit() is False
    ):
        print('Error: only numbers are allowed in times')
        return 'Error: only numbers are allowed in times'

    start_hours = int(start_hours)
    if start_hours > 12:
        print("Error: please, use a 12 hour notation")
        return "Error: please, use a 12 hour notation"

    # #### Main functionality #####
    # convert strings to numbers for computation
    start_min = int(start_min)
    duration_hours = int(duration_hours)
    duration_min = int(duration_min)

    # convert start time to 24h notation
    if period == 'PM':
        start_hours += 12

    # convert all times to minutes to get total in minutes
    total_min = (60 * start_hours + start_min) + \
        (60 * duration_hours + duration_min)

    # compute the new time from total minutes
    new_hours = total_min // 60
    new_min = total_min - new_hours * 60
    new_days_count = new_hours // 24

    if day == "Day":
        new_day = str()
    else:
        new_day = ", " + day

    # handle period
    if new_hours - new_days_count * 24 < 12:
        period = "AM"
    else:
        period = "PM"

    # handle 12 hour notation and the day
    if new_days_count > 0:
        new_hours = new_hours - new_days_count * 24
        if new_hours == 0:
            new_hours = 12
        if day != "Day":
            i = days.index(day) + 1
            for i in range(i, new_days_count + i):
                new_day = days[i % len(days)]
            new_day = ", " + new_day

    if new_hours > 12:
        new_hours = new_hours - 12

    # create new time string
    new_hours = str(new_hours)
    # if len(new_hours) == 1:
    #     new_hours = "0" + new_hours

    new_min = str(new_min)
    if len(new_min) == 1:
        new_min = "0" + new_min

    if new_days_count == 0:
        new_days_count = str("")
    elif new_days_count == 1:
        new_days_count = " " + str("(next day)")
    else:
        new_days_count = " (" + str(new_days_count) + " days later)"

    new_time = new_hours + ":" + new_min + \
        " " + period + new_day + new_days_count

    # return the result
    print("new time:", new_time)
    return new_time


add_time("11:40 AM", "00:25")
