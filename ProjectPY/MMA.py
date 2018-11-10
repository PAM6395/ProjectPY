#Media Meta Analysis

import os #needed for file operations
import kivy #UI design

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from urllib.request import Request,urlopen #for web based operations
from bs4 import BeautifulSoup #web scraping lib

class MainUI(GridLayout):
	pass

class mmaApp(App):
	def build(self):
		return MainUI()

UIframe = mmaApp()
UIframe.run()
				
#Folder Scan process
print ("\n-----------------------------------")
print ("            -MetaViewer-")
print ("-----------------------------------")


path = input("Please enter path of folder: ")

fList = os.listdir(path)
fCount = 0
fObj = open('FolderList.txt','w+')
for folder in fList:
	if(folder.find(".") == -1):
		fObj = open('FolderList.txt','a+')
		fObj.write(folder+"\n")
		fObj.close()
		fCount += 1
		
if(fCount > 0):
	print (fCount,"folders found!")
else:
	print ("No folders found!")

#Result generation process
	
dataGen = input("\nGenerate Scores for Media?")
if dataGen == "n" or dataGen == "N": 
	exit()
else: 
	print ("Generating Scores for...")

fObj = open('FolderList.txt','r')
rCount = 0

for line in fObj:
	searchitem = line.replace("\n","") #search item is folder name
	search = searchitem.replace(" ","+")+"+metacritic+rating+score"
	#print (search)	

	url="https://www.google.co.in/search?hl=en&source=hp&ei=AjbHW8anC5Kz9QOZ2bboCw&q="+ search +"&oq=" + search +"&gs_l=psy-ab.3..33i160k1l2.1327.11447.0.11639.24.24.0.0.0.0.186.2962.0j20.20.0....0...1c.1.64.psy-ab..4.20.2961...0j0i131k1j0i22i30k1j33i22i29i30k1.0.59UWC1qZ_Vg"
	#print (url)

	req = Request(url,headers={'User-Agent':'Mozilla/5.0'})
	page = urlopen(req).read()
	parsedPage = BeautifulSoup(page,'html.parser')

	div = parsedPage.find('div',attrs = {'class':'g'})
	if (div.text.count('Metacritic') > 0 and div.text.count('Rating:') > 0 and div.text.count('votes') > 0):#check for metacritic
		h3 = div.find('h3')
		searchCheck = h3.find('b')
		searchCheck = searchCheck.text.lower()
		if (searchCheck.count(searchitem.lower()) > 0):
			print (searchitem) #print media name
			score = div.find('div', attrs = {'class':'f slp'})
			score = score.text.replace(" ","").replace(" ","") #replace normal and special spaces
			score = score.split("%-") #contains rating & votes
			rating = score[0].replace("Rating:","")
			rfObj = open('MetaReviews.txt','a+')
			rfObj.write(searchitem+"\t\tMetascore: "+rating+"%\n")
			rCount += 1
			rfObj.close()
			#print (score[0].replace("Rating:",""))
			#print (score[1].replace("votes",""))
	else:
		print (searchitem,"- No Metascore Found!") #print media with no metascore

fObj.close()
print (rCount,"Review(s) generated!!!")





