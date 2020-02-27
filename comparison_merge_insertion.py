import random
from time import time 
import matplotlib.pyplot as plt
from insertion_sorting import insertionSort
from merge_sorting import mergeSort

randomnum=random.sample(range(100000),100000)

insertion_sort=[]
merge_sort=[]
xdomain=[]
j=0


for i in range(1000,10000,1000):
	start_time_merge=time()
	mergeSort(randomnum[0:i])
	end_time_merge=time()
	print(end_time_merge-start_time_merge)
	merge_sort.insert(j,end_time_merge-start_time_merge)
	xdomain.insert(j,i)
	j+=1
	

print("********************")


for i in range(1000,10000,1000):
	start_time_insertion=time()
	insertionSort(randomnum[0:i])
	end_time_insertion=time()
	print(end_time_insertion-start_time_insertion)
	insertion_sort.insert(j,end_time_insertion-start_time_insertion)
	j+=1



plt.plot(xdomain,insertion_sort,'r',label="Insertion Sort")
plt.plot(xdomain,merge_sort,'g',label="Merge Sort")
plt.title("Comparison Between Merge and Insertion Sorting Algorithm")
plt.xlabel('Input Size')
plt.ylabel('Sorting Time')
plt.legend(loc='upper left')
plt.show()




