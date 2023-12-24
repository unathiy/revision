
def convert_datetime(datetime_input):
    date, time = datetime_input.split() #split input 
    year, month, day = date.split('-')
    hour, minute = time.split(':')

    year = "'" + year[-2:] #converts year to its last two digits and add single quote

    #converts month to month name
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
    month = months[int(month) - 1]

    #to convert hours to 12-hour format and add suffix
    hour = int(hour)
    if hour == 0:
        time_suffix = 'am'
        hour = 12
    elif hour < 12:
        time_suffix = 'am'
    elif hour == 12:
        time_suffix = 'pm'
    else:
        time_suffix = 'pm'
        hour -= 12

    
    day = int(day)
    #day suffix
    if 4 <= day <=20 or 24 <= day <= 30:
        day_suffix = 'th'

    else:
        suffixes = ['st', 'nd', 'rd']
        day_suffix = suffixes[(day - 1) % 10]

    #combines the parts to form long form datetime
    long_form = f"{hour}:{minute} {time_suffix} on the {day}{day_suffix} of {month}{year}"

    return long_form # returns long form

datetime_input = input("Enter the date and time (yyyy-mm-dd hh:mm): ") #prompts user input 
long_form_datetime = convert_datetime(datetime_input)

print(long_form_datetime)
