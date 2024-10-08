from datetime import datetime

# Define the days and their schedules
WhatDay = [[0, 'Monday'], [1, 'Tuesday'], [2, 'Wednesday'], [3, 'Thursday'], [4, 'Friday'], [5, 'Saturday'], [6, 'Sunday']]
schedule = {
    "Monday": {
        "Form Time": "08:30",
        "Period 1": "09:00",
        "Period 2": "09:55",
        "Break Time": "10:50",
        "Period 3": "11:10",
        "Period 4": "12:05",
        "Lunch": "13:00",
        "Mincha": "13:55",
        "Period 5": "14:10",
        "Period 6": "15:05",
        "No Lessons": "16:00"
    },
    "Tuesday": {
        "Form Time": "08:30",
        "Period 1": "09:00",
        "Period 2": "09:55",
        "Break Time": "10:50",
        "Period 3": "11:10",
        "Period 4": "12:05",
        "Lunch": "12:55",
        "Mincha": "13:45",
        "Period 5": "14:00",
        "Period 6": "14:50",
        "No Lessons": "15:40"
    },
    "Wednesday": {
        "Form Time": "08:30",
        "Period 1": "09:00",
        "Period 2": "09:55",
        "Break Time": "10:50",
        "Period 3": "11:10",
        "Period 4": "12:05",
        "Lunch": "13:00",
        "Mincha": "13:55",
        "Period 5": "14:10",
        "Period 6": "15:05",
        "No Lessons": "16:00"
    },
    "Thursday": {
        "Form Time": "08:30",
        "Period 1": "09:00",
        "Period 2": "09:55",
        "Break Time": "10:50",
        "Period 3": "11:10",
        "Period 4": "12:05",
        "Lunch": "13:00",
        "Mincha": "13:55",
        "Period 5": "14:10",
        "Period 6": "15:05",
        "Lessons End": "16:00"
    },
    "Friday": {
        "Period 1": "08:30",
        "Period 2": "09:20",
        "Period 3": "10:10",
        "Break": "11:00",
        "Period 4": "11:50",
        "Period 5": "12:40",
        "Lessons End": "13:30"
    },
    "Saturday": {},
    "Sunday": {}
}

# Helper function to convert time strings to datetime objects for comparison
def time_to_datetime(time_str):
    return datetime.strptime(time_str, "%H:%M")

# Find the current, end, and next period based on the current time
def find_period(fschedule, current_day, fcurrent_time):
    if current_day in fschedule:
        current_period = None
        next_period = None
        start_time_current = None
        start_time_next = None

        periods = fschedule[current_day]  # Dictionary of periods and their times

        # Convert fcurrent_time to datetime for comparison
        current_time_dt = time_to_datetime(fcurrent_time)

        # Iterate through periods to find the current and next one
        for i, (period, start_time) in enumerate(periods.items()):
            period_start_time = time_to_datetime(start_time)
            if current_time_dt >= period_start_time:
                current_period = period
                start_time_current = start_time
                if i + 1 < len(periods):
                    next_period = list(periods.keys())[i + 1]
                    start_time_next = list(periods.values())[i + 1]
                else:
                    next_period = "No more periods"
                    start_time_next = "End of day"

        # Determine the output
        if current_period:
            current_info = f"Currently: {current_period}"
        else:
            current_info = "No current period."

        if next_period != "No more periods":
            next_info = f"Next: {next_period} ({start_time_next})"
        else:
            next_info = "School day over."

        return current_info, next_info
    else:
        return "No schedule available for today.", ""

def get_schedule_info():
    # Get current time and day
    current_time = datetime.now()

    # Stores hour, minute, and time of the day and the day
    DOW = current_time.weekday()
    HOD = str(current_time.time().hour).zfill(2)  # Add leading zero to hours
    MOD = str(current_time.time().minute).zfill(2)  # Add leading zero to minutes
    TOD = HOD + ":" + MOD

    # Checks what day of the week it is
    for row in WhatDay:
        if DOW in row:
            DOW = row[1]

    # Get current and next period
    current_info, next_info = find_period(schedule, DOW, TOD)
    return current_info, next_info,TOD

