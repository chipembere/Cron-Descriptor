import re, sys, datetime

def to_datetime(time):
    '''
    Get current time input and convert to datetime object
    Parameters
        ----------
        N/A

    Returns
        ------
        time: 
            As a datime object.
    '''
    # time = sys.argv[0]
    current_time = datetime.datetime.strptime(time,'%H:%M').time()
    return current_time

# print(type(to_datetime('1:46')))

def parse_cron_syntax(cron_syntax):
    """
        Parameters
        ----------
        path : str 
            With the format: "* 1 /bin/run_me_daily".

        Returns
        ------
        A tuple: 
            An array of the time/s the programme is scheduled to run per day.
            And the command
        """
    # Separate cron syntax by space
    split_string = cron_syntax.split()
    command = split_string[2]
    # [0] = minutes and [1] = hours
    m = range(0,60) if split_string[0] == "*" else split_string[0]
    h = range(0,60) if split_string[1] == "*" else split_string[1]
    permutated_lists = [(x,y) for x in h for y in m]  
    result = [str(x[0]) + ":" + str(x[1]) for x in permutated_lists]
    return result, command

# print(parse_cron_syntax("* 1 /bin/run_me_daily"))

def get_next_time(current_time,scheduled_times, command):
    """
        Parameters
        ----------
            current_time : str
                The currrent time in the format HH:MM.
            scheduled_times : list
                even if the list object has one element.
        Returns
        ------
        The next scheduled run time.
            As a datetime object.
        """
    current_time_dt = to_datetime(current_time)

    if len(scheduled_times) > 1:

        if current_time in scheduled_times:
            #  If the current time is equal to a scheduled time.
            print(f"{current_time} today - {command}")

        elif min(scheduled_times) > current_time:
            # If all the scheduled_times have passed.
            print(f"{min(scheduled_times)} tomorrow - {command}")

        elif min(scheduled_times) < current_time:
            # If all the scheduled_times have not yet passed.
            print(f"{min(scheduled_times)} today - {command}")
        
        else:
            # Find and return the nearest scheduled time > than current time
            next_time = min(scheduled_times, key=lambda x:(x-current_time))

            # # Absolute distance
            # greater_numbers = all(x > current_time for x in scheduled_times)
            # next_time = min(greater_numbers, key=lambda x:abs(x-current_time))
            print(f"{next_time} today - {command}")

    else:
        if current_time_dt > scheduled_times[0]:
            #  if command runs once a day and the time has already passed.
            print(f"{scheduled_times[0]} tomorrow - {command}")

    next_ = []    
    return next_

