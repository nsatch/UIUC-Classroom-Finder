import requests

# Change url to be the url of classes you want to look through. For me, I want a U.S Minority gen ed class.
url = 'https://courses.illinois.edu/search?year=2021&term=fall&genedCode1=1US&genedType=all' 


desired_classroom = "Campus Instructional Facility"   # Change this to the desired classroom. I wanted the CIF.

# Test case that shows CS 357 and TAM 541 do return as classes that are in CIF
#url = 'https://courses.illinois.edu/search?year=2021&term=fall&keyword=numerical+methods&keywordType=qs&genedCode1=-1&genedType=all'

res = requests.get(url)  			      # Obtain the HTML data of the page we search through
html_page = res.content

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find_all('tr')                            # I want to navigate through every class and each class is a new table row (tr) on the page.
					              # so this still takes a lot of excess page, but narrows it down slightly

class_counter = 0  			              # Set an empty counter variable to make sure we count all classes 
list_class = []				              # Create an empty list to append desired class urls to

for x in text:				              # Iterate thru all of the scraped text to find class urls
	if class_counter % 2 == 0:   		      # In the text iteration, each class has 2 elements
		class_counter += 1 		      # in the list. The second component (odd) has the 
		continue			      # link so we ignore the first (even component
	y = str(x)
	print("\n\n\n\n" + y)                         # Originally this was for debugging, but I leave it in cuz its cool to see it scrape info in real time
	split_list = y.split("href=\"")               # I noticed that each url started with "href=\" through Inspect Element, so I split it there to isolate the url
	
	if len(split_list) >= 3:                      # Actual url starts at index 2 of split list so we grab that section. If statement there to prevent indexing errors
		des_section = str(split_list[2])
	else: 
		class_counter += 1
		continue
	list2 = des_section.split("\"")               # Cut out the text after the url 
	link = list2[0]                               # Store the url into the link variable
	start_link = 'https://courses.illinois.edu'   # The grabbed url is only the ending part of the full link, so we concatanate with the start of the url to get full link
	full_link = start_link + link
	print(full_link)                              # Again originally for debugging but left in cuz it looked cool


	res2 = requests.get(full_link)                # Grab the HTML data of the class web page which will contain the classroom info
	html_page = res2.content
	soup = BeautifulSoup(html_page, 'html.parser')
	text = soup.find_all(text=True)
	z = str(text)
	s = z.split(desired_classroom)                # Scan the text ripped from the web page for the desired class room, if it is found, it creates a list with size greater than 1
	if len(s) > 1:                                # If the size of the list is greated than 1, a split occured meaning the classroom string was found 
		print("Class found! -> " + full_link)
		list_class.append(full_link)
	class_counter += 1

print(class_counter)# + "(There may be duplicates)") 
print(list_class)                                     # Print the list of classes in the desired classroom

#y = str(text[10])
#print(y)
#print(type(y))

#print(len(split_list))
#print(split_list)
#print(split_list[2])

#print("link = " + link)

#text = soup.find_all("div", {"class": "app-meeting"})
#text = soup.find_all("div", class_="app-meeting")
#text = soup.find_all(class_="app-meeting")
#text = soup.find_all(class_="adjh")
#print(text)
#print(z)

#print(full_link)
#print(s)
#print(len(s))

	


	

