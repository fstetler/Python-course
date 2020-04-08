# Web scraping

import webbrowser, sys
def spam1():
	webbrowser.open('https://inventwithpython.com/')


#! python3
# mapIt.py - Launches a map in
# command line or clipboard

# import webbrowser, sys, pyperclip
# if len(sys,argv) > 1:
# 	# Get address from command line.
# 	address = ''.join(sys.argv[1:])
# else:
# 	address = pyperclip.paste()

# webbrowser.open('https://www.google.com/maps/place/' + address)
# # TODO: Get address from clipboard

import requests
def spam2():

	res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
	print(type(res))
	print(res.status_code == requests.codes.ok)
	print(len(res.text))
	print(res.text[:250])

def spam3():

	res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
	try:
		res.raise_for_status()
	except Exception as exc:
		print('There was a problem: %s' % (exc))

def spam4():

	# Save a website as txt as a file
	res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
	res.raise_for_status()
	return res
	playFile = open('RomeoAndJuliet.txt','wb')
	for chunk in res.iter_content(100000):
		playFile.write(chunk)

def spam5():
	# r = requests.get('https://imgs.xkcd.com/comics/python.png')
	payload = {'username': 'corey', 'password': 'testing'} #{'page': 2, 'count': 25}
	# r = requests.get('https://httpbin.org/get', params = payload)
	r = requests.post('https://httpbin.org/post', data = payload)
	# with open('comic.png','wb') as f:
	# 	f.write(r.content)

	#print(r.text)
	r_dict = r.json()
	print(r_dict['form'])
	#print(r.status_code) # 200 = success, 300 = redirects, 400 = client effor, 500 = server error
	#print(r.ok) # Returns true if the page is OK
	#print(r.headers)



spam5()
















