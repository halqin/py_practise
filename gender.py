import string

def translate(gender, dic_):
	'''
	>>> translations = {'he':'she', 'brother':'sister'}
	>>> translate('he', translations)
	'she'
	>>> translate('HE', translations)
	'SHE'
	>>> translate('He', translations)
	'She'
	>>> translate('brother', translations)
	'sister'
	>>> translate('my', translations)
	'my'
	'''
	lowStr = gender.lower()
	transStr = dic_.get(lowStr, gender)

	if gender.istitle():
		restult = transStr.capitalize()
	elif not gender.islower():
		restult = transStr.upper()
	else:
		restult = transStr

	return restult

def sexChange2(seq, dic_):
	'''
	>>> sexChange2("My Brother's girlfriend is taking HER sister to the movies.", {'brother': 'sister', 'girlfriend': 'boyfriend', 'sister': 'brother', 'her': 'his', 'vicereine': 'viceroy', 'leopard': 'leopardess'})
	"My Sister's boyfriend is taking HIS brother to the movies."
	'''
	stripStr = seq[:-1]
	seqList = stripStr.split()
	print(seqList)
	transList = [translate(word, dic_) for word in seqList]
	restult = ' '.join(transList)
	return restult+'.'

def sexChange(sentence, translations):
	'''
	>>> translations = {'he':'she', 'brother':'sister'}
	>>> sexChange('He is my brother.', translations)
	'She is my sister.'
	'''

# split sentence into words and apply translation on each word

	word, translation = '', ''

	for character in sentence:

		if character.isalpha():

			word += character

		else:

			translation += translate(word, translations) + character
			word = ''

	# return translated sentence

	return translation + translate(word, translations)



def undoSexChange(seq, dic_):
	'''
	>>> translations = {'he':'she', 'brother':'sister'}
	>>> undoSexChange('She is my sister.', translations)
	'He is my brother.'
	'''
	newDic = dict()
	newDic = { y:x for x,y in dic_.items()}

	return sexChange(seq, newDic)
	
if __name__ == '__main__':
	import doctest
	doctest.testmod()