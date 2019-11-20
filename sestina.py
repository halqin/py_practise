def endword(str_):
	'''
	>>> endword("Lo ferm voler qu'el cor m'intra")
	'intra'
	>>> endword("no'm pot ges becs escoissendre ni ongla")
	'ongla'
	>>> endword("de lauzengier qui pert per mal dir s'arma;")
	'arma'	
	'''
	import re
	s = str_.split(' ')
	endword = re.sub(r'[^\w\s]','',s[-1])
	print(s)
	return endword


if __name__ == '__main__':
	import doctest
	doctest.testmod()