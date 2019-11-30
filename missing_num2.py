# 15, Oct., 2019
def bit_loop(str_):
	loop_cnt = 1
	for i in range(int(len(str_)/loop_cnt)):
		flag_= count_(str_, loop_cnt)
		loop_cnt += 1
		if flag_ == 1:
			break
	#print('no missing number')


def  missing (str_, start_bit):
	cnt_  = 0
	missing_list = []
	for i in range(int(len(str_)/start_bit)-1):
		if int(str_[i*start_bit:start_bit*(i+1)]) == int(str_[(i+1)*start_bit: (i+2)*start_bit])-1:
			continue
		else:
			cnt_ +=1 
			missing_list.append(int(str_[i*start_bit:start_bit*(i+1)])+1)
	return cnt_, missing_list

def count_(str_, loop_cnt):
	cnt_,missing_list =missing(str_,loop_cnt)
	if cnt_ == 1:
		print ( missing_list[0])
		return cnt_
	#else:
	#	print ('no missing number')


a = input('input the num. series')
bit_loop(a)