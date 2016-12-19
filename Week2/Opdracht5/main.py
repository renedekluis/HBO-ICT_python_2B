def swap(a,i,j):
	a[i],a[j] = a[j],a[i]

import random

count = 0

def qsort(a,low=0,high=-1):
	global count
	if high == -1:
		high = len(a) -1
	if low < high:
		minimum_of_part_list_a = a[low:high+1].index(min(a[low:high+1]))
		if minimum_of_part_list_a >= low:
			swap(a,low, minimum_of_part_list_a)

		m = low
		for j in range(low+1,high+1):
			count+=1
			if a[j] < a[low]:
				m += 1
				swap(a,m,j)
                            # low < i <= m : a[i] < a[low]
                            # i > m        : a[i] >= a[low]
		swap(a,low,m)
                            # low <= i < m : a[i] < a[m]
                            # i > m              : a[i] >= a[m]
		if m > 0:
			qsort(a,low,m-1)
		qsort(a,m+1,high)

		
		
def isSorted(a):
	i = 0;
	while i < len(a)-1 and a[i] <= a[i+1]:
		i += 1

	return i == len(a)-1

if __name__ == '__main__':
	ia = [9,5,2,6,2,7,1,2]
	print(ia)
	qsort(ia)
	print(ia)

	a = []
	for x in range(10000):
		a.append(random.randint(0,10000))
	qsort(a)
	print("Comparing times between two values: ",count)


	b = list(a)

	print(isSorted(ia))

	b.sort()
	print(a == b)



	

