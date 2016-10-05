#this script gets info about the christiano ronaldo from wikipedia
from lxml import html
import requests
import sys
import calendar

print 'tell me the birth date in ddmmyyy format'

# full_date = raw_input()

# if len(full_date) != 8:
# 	print 'date is in wrong format'
# 	sys.exit()
# day = int(full_date[0] + full_date[1])
# month = int(full_date[2] + full_date[3])
# year = int(full_date[4] + full_date[5] + full_date[6] + full_date[7]) 

# event_month = 0

# if month<10:
# 	year = year -1
# 	event_month = month - 9 +12
# else:
# 	event_month = month - 9

# monthname = calendar.month_name[event_month]

#getting data from wiki page
# page = requests.get('https://en.wikipedia.org/wiki/' + str(year))
page = requests.get('https://en.wikipedia.org/wiki/%s'  % str(1965) )
#creating XPath tree out of it
tree = html.fromstring(page.content)

#parsing the tree 
# visit http://www.w3schools.com/xsl/xpath_nodes.asp for syntaxes 
# for specifying address of a tree node


#reaching january 4
# monthday = str(monthname + " " + str(day))
# print monthday
input_data = '//ul[following-sibling::h2[child::span[@id = "Births"]]]/li[child::a[@title = "January 4"]]//text()'  
event = tree.xpath(input_data)
print event

# str_of_event = ""

# # getting data out of event
# for tagn in range(2,len(event)):
# 	try:
# 		tag_data = str(event[tagn])
# 		if "\n" in tag_data:
# 			break
# 		if monthday in tag_data:
# 			break
# 		str_of_event = str_of_event + tag_data
		

# 	except UnicodeEncodeError: 
# 		continue

# if str_of_event is "":
# 	print "no record found"
# else:
# 	print str_of_event



