def mix(text1, text2, destination = None):
	'''
	>>> mix('tom_waits.txt', 'adele.txt')
	Operator, number, please
	-->Hello from the other side<--
	It's been so many years
	-->I must have called a thousand times<--
	Will she remember my old voiced
	-->To tell you I'm sorry for everything that I've done<--
	While I fight the tears?
	-->But when I call you never seem to be home<--
	'''
	reader1 = open(text1, 'r')
	reader2 = open(text2, 'r')

	outfile = open(destination, 'w') if destination is not None else None

	for line1,line2 in zip(reader1, reader2):
		#print(line2)
		print(line1, end='', file=outfile )
		print('-->{}<--'.format(line2.rstrip('\n')), file=outfile)
		#print('-->{}<--'.format(line2))
	reader1.close()
	reader2.close()

	if outfile is not None:
		outfile.close()

if __name__ == '__main__':
	import doctest
	doctest.testmod()
			





