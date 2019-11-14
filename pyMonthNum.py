def month_num(arg):
    if arg =="JAN":
        return "01"
    if arg =="FEB":
        return "02"
    if arg =="MAR":
        return "03"
    if arg =="APR":
        return "04"
    if arg =="MAY":
        return "05"
    if arg =="JUN":
        return "06"
    if arg =="JUL":
        return "07"
    if arg =="AUG":
        return "08"
    if arg =="SEP":
        return "09"
    if arg =="OCT":
        return "10"
    if arg =="NOV":
        return "11"
    if arg =="DEC":
        return "12"

def monthFormat(dates):
    delim = ' '
    split_date = dates.split(" ")
    month = month_num(split_date[2])
    format = month + "/" + split_date[1] +"/" + split_date[3]
    print (format)
