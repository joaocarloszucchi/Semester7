#reconhecer datas no formato "aammdd"

def isYearValid(year):
    if type(year) == int:
        return year >= 0
    return False

def isMonthValid(month):
    if type(month) == int:
        return month > 0 and month < 13
    return False

def isDayValid(day, month):
    if type(day) == int:
        return checkValidDay(day, month)
    return False

def checkValidDay(day, month):
    months = {1: 31, 2: 28, 3:31, 4: 30, 5: 31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    limit = months[month]
    if day > limit:
        return False
    return True

def parser(date):
    if len(date) != 6:
        return False
    
    year = int(date[:2])
    month = int(date[2:4])
    day = int(date[4:6])

    if isYearValid(year):
        if isMonthValid(month):
            if isDayValid(day, month):
                return True

    return False
text = ['120531', '001030', '300230']

for date in text:
    if parser(date): 
        print(f"Passou em: {date}")
    else:
        print(f"Falhou em: {date}")