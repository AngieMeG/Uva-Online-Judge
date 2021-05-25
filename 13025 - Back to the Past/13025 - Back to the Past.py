from datetime import datetime
date = datetime(2013, 5, 29)
days = {0 : "Monday", 1 : "Tuesday", 2 : "Wednesday", 3 : "Thursday", 4 : "Friday", 5 : "Saturday", 6 : "Sunday"}
print(date.strftime("%B %d, %Y") + " " + days[date.weekday()])