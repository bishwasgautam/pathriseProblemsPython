# Input: [2, 0, 4, 0, 0]

# Output: [2, 4, 0, 0, 0]


def right_shift_all_zeroes(arr):
	zero_ptrr =0
	non_zero_ptrr=1
	while(zero_ptrr < len(arr) -1):
		if(arr[zero_ptrr] == 0):
			while(non_zero_ptrr < len(arr) -1 and arr[non_zero_ptrr] == 0):
				non_zero_ptrr+=1

			#swap			
			arr[zero_ptrr], arr[non_zero_ptrr] = arr[non_zero_ptrr], arr[zero_ptrr]
			
		zero_ptrr+=1

	return arr


res = right_shift_all_zeroes([2, 0, 4, 0, 0])

res1 = right_shift_all_zeroes([2, 0, 0,0,9,0,4, 0, 0])

print(res)

print(res1)






