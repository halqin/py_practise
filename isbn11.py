def isISBN13(code):
	"""

	Checks whether or not the given ISBN-13 code is valid.

	>>> isISBN13('9789743159664')
	True

	>>> isISBN13('9787954527409')
	False

	>>> isISBN13('8799743159665')
	False

	"""
	# check whether the given code is a string
	if not isinstance(code, str):
		return False
	# check whether the given code contains 10 characters
	if len(code) != 13:
		return False
	# check prefix of the given code
	if code[:3] not in {'978', '979'}:
		return False
	# check whether first nine characters of the given code are digits
	if not code[:12].isdigit():
		return False
	# check the check digit
	return checkdigit(code) == code[-1]

def checkdigit(code):
	"""
	Helper function that computes the ISBN-13 check digit.
	"""
	# compute the check digit
	check = sum((2 * (i % 2) + 1) * int(code[i]) for i in range(12))
	# convert the check digit into a single digit
	return str((10 - check) % 10)

def remove_tags(s):
	s = s.strip()
	while s.find('<') >= 0:
		start = s.find('<' )
		stop = s.find('>')
		#if stop == -1:
		#	stop = len(s)
		s = s[:start] + s[stop + 1:]

def displayBookInfo(code):

	'''
	>>> displayBookInfo('9780136110675')
	Title: The Practice of Computing using Python
	Authors: William F Punch, Richard Enbody
	Publisher: Addison Wesley
	>>> displayBookInfo('9780136110678')
	Wrong ISBN-13 code
	'''
	if not isISBN13(code):
		print('Wrong ISBN-13 code')
		return
	import urllib.request
	url = 'http://isbndb.com/api/books.xml'
	parameters = '?access_key=ZFD8L2Z5&index1=isbn&value1=' + code.strip()
	info = urllib.request.urlopen(url + parameters)
	#print(info)
	for line in info:
		line = line.decode('utf-8')
		if line.startswith('<Title>'):
			print('Title: {}'.format(remove_tags(line)))
		elif line.startswith('<AuthorsText>'):
			print('Authors: {}'.format(remove_tags(line).rstrip('', '')))
		elif line.startswith('<PublisherText '):
			print('Publisher: {}'.format(remove_tags(line).rstrip('', '')))
	# close web page
	info.close()


if __name__ == '__main__':
	import doctest
	doctest.testmod()
#print(remove_tages('<PublisherText publisher_id="addison_wesley_a01">Addison Wesley</PublisherText>'))