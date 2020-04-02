def board():
	print('_' + pieces['top-L'] + '_|_' + pieces['top-M'] +  '_|_' + pieces['top-R'] +  '_')
	print('_' + pieces['mid-L'] + '_|_' + pieces['mid-M'] +  '_|_' + pieces['mid-R'] +  '_')
	print(' ' + pieces['low-L'] + ' | ' + pieces['low-M'] +  ' | ' + pieces['low-R'] +  ' ')

pieces = {'top-L': '_', 'top-M': '_', 'top-R': '_',
		  'mid-L': '_', 'mid-M': '_', 'mid-R': '_',
		  'low-L': ' ', 'low-M': ' ', 'low-R': ' ', }

playing = True
while playing:
	board()
	play = input('Where would you like to put a piece? (top-L, mid-M, low-R etc): ')
	if play == 'top-L':
		xoro = input('Would you like to put an x or an o?: ')
		pieces['top-L'] = xoro
	elif play == 'top-M':
		xoro = input('Would you like to put an x or an o?: ')
		pieces['top-M'] = xoro
	elif play == 'top-R':
		xoro = input('Would you like to put an x or an o?: ')
		pieces['top-R'] = xoro
	elif play == 'top-R':
		xoro = input('Would you like to put an x or an o?: ')
		pieces['top-R'] = xoro
	elif play == 'mid-L':
		xoro = input('Would you like to put an x or an o?: ')
		pieces['mid-L'] = xoro
	elif play == 'mid-M':
		xoro = input('Would you like to put an x or an o?: ')
		pieces['mid-M'] = xoro
	elif play == 'mid-R':
		xoro = input('Would you like to put an x or an o?: ')
		pieces['mid-R'] = xoro
	elif play == 'low-L':
		xoro = input('Would you like to put an x or an o?: ')
		pieces['low-L'] = xoro
	elif play == 'low-M':
		xoro = input('Would you like to put an x or an o?: ')
		pieces['low-M'] = xoro
	elif play == 'low-R':
		xoro = input('Would you like to put an x or an o?: ')
		pieces['low-R'] = xoro
	else:
		print('This is not a valid option')
	if pieces['top-L'] == pieces['top-M'] == pieces['top-R']:
		print('The game has ended')
		break
	

