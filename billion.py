def reverseComplement2(seq):
	'''
	>>> reverseComplement2('GATATC')
	'GATATC'
	>>> reverseComplement2('GCATGC')
	'GCATGC'
	>>> reverseComplement2('AGCTTC')
	'GAAGCT'
	'''

	seq_list = list(seq)
	seq_list.reverse()
	
	new_seq = []
	for i in seq_list:
		if i == 'A':
			new_seq.append('T')
		elif i == 'T':		
			new_seq.append('A')
		elif i == 'G':
			new_seq.append('C')
		elif i == 'C':
			new_seq.append('G')

	reverse_list = "".join(new_seq)
	
	return reverse_list


def reverseComplement(seq):
	'''
	>>> reverseComplement('GATATC')
	'GATATC'
	>>> reverseComplement('GCATGC')
	'GCATGC'
	>>> reverseComplement('AGCTTC')
	'GAAGCT'
	'''
	dna_dic = { i:j for i,j in zip('ACTG', 'TGAC')}

	return ''.join(dna_dic[i] for i in seq[::-1])


def reversePalindrome(seq):
	'''
	>>> reversePalindrome('GATATC')
	True
	>>> reversePalindrome('GCATGC')
	True
	>>> reversePalindrome('AGCTTC')
	False
	'''

	return seq == reverseComplement(seq)


def restrictionSites(seq, minLength=4, maxLength = 12):
	'''
	>>> restrictionSites('TCAATGCATGCGGGTCTATATGCAT')
	[(4, 'ATGCAT'), (5, 'TGCA'), (6, 'GCATGC'), (7, 'CATG'), (17, 'TATA'), (18, 'ATAT'), (20, 'ATGCAT'), (21, 'TGCA')]
	>>> restrictionSites('AAGTCATAGCTATCGATCAGATCAC', minLength=5)
	[(6, 'ATAGCTAT'), (7, 'TAGCTA'), (12, 'ATCGAT')]
	>>> restrictionSites('ATATTCAGTCATCGATCAGCTAGCA', maxLength=5)
	[(1, 'ATAT'), (12, 'TCGA'), (14, 'GATC'), (18, 'AGCT'), (20, 'CTAG')]
	'''
	cnt = 0
	result_list = []
	#pali_tuple= ()
	for _ in seq[:-minLength+1]:
		seq_nest = seq[cnt:]
		#for _ in seq_nest[:-minLength]:
		for j in range(minLength,maxLength+1):
			if reversePalindrome(seq_nest[:j]) and len(seq_nest) >= j:
				pali_tuple = (cnt+1, seq_nest[:j])
				result_list.append(pali_tuple)
		cnt += 1
	#print(result_list)

	return result_list


if __name__ == "__main__":
	import doctest
	doctest.testmod()

# print (restrictionSites('AGCACTGATA', minLength=2, maxLength=5))