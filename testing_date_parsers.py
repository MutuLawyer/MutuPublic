from datetime import datetime, timedelta
from timefhuman import timefhuman 
import  dateparser
import datefinder


testing_strings = ["now", "today", "1.12.2019", "1.12.2019 12.30", "1/12/2019 12:30", "the first of January two thousand nineteenth year", "week ago", "2 weeks ago", "two weeks ago", "in two weeks", "in two years", "friday", "this friday", "this noon", "wensday noon"]
timefhumanops =[]
dateparserops = []
datefinderpos = []

for i in testing_strings:
	a = timefhuman(i)
	timefhumanops.append(str(a)+" - " +i)
	b = dateparser.parse(i)
	dateparserops.append(str(b)+" - " +i)
	c = datefinder.find_dates(i)
	for match in c:
		datefinderpos.append(str(match)+" - " +i) 

print(timefhumanops)
print(dateparserops)
print(datefinderpos)