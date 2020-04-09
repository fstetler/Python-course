from bs4 import BeautifulSoup
import requests
import webbrowser
import csv

#webbrowser.open(r'https://www.smhi.se/q/Roslags-N%C3%A4sby/T%C3%A4by/')
# Requests information from the website
source = requests.get('https://coreyms.com').text
#webbrowser.open(r'https://www.faceit.com/en/players/Sowipee')
# prints the information from the website
soup = BeautifulSoup(source, 'lxml')
 
csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline','summary','video_link'])
for article in soup.find_all('article'):

	headline = article.header.h2.a.text
	print(headline)

	#print(article.prettify())
	summary = article.find('div', class_='entry-content').p.text
	print(summary)
	
	try:
		vid_src = article.find('iframe', class_='youtube-player')['src']
		vid_id = vid_src.split('/')
		yt_link = f'https://youtube.com/watch?v={vid_id[4][:11]}'
		print(yt_link)
	except:
		print('No video was found for this article')
	#print(vid_src)

	
	print()

	csv_writer.writerow([headline, summary, yt_link])

csv_file.close()
