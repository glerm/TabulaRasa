def expandefen(x):
	for s in x:
		if (s=='1'):
			x=x.replace('1','ø')
		elif (s=='2'):
			x=x.replace('2','øø')
		elif (s=='3'):
			x=x.replace('3','øøø')
		elif (s=='4'):
			x=x.replace('4','øøøø')
		elif (s=='5'):
			x=x.replace('5','øøøøø')
		elif (s=='6'):
			x=x.replace('6','øøøøøø')
		elif (s=='7'):
			x=x.replace('7','øøøøøøø')
		elif (s=='8'):
			x=x.replace('8','øøøøøøøø')
	return x