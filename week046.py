seq = input()

missing = None
digit = 1
while missing == None and digit <= len(seq)//2:
	next_ = int(seq[:digit])
	seq_rem = seq[digit:]

	while seq_rem:
		next_ +=1
		if seq_rem.startswith(str(next_)):
			seq_rem = seq_rem[len(str(next_)):]
		elif missing == None:
			missing = str(next_)
		else:
			missing = None
			seq_rem=''
	digit +=1

print('no missing number' if missing == None else missing)
