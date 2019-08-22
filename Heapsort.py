import numpy as np;
import math;
import sys
#sys.setrecursionlimit(100000)
def parent(i):
	return(math.floor(i/2))
def Left(i):
	return(2*i);
def Right(i):
	return(2*i+1);

def  max_heapify(A,i,size):
	l=Left(i);
	r=Right(i);
	if l<=size and A[l-1]>A[i-1]:
		largest=l;
	else :
		largest=i;
	if r<=size and A[r-1]>A[largest-1]:
		largest=r;
	if largest!=i:
		a=A[i-1];
		A[i-1]=A[largest-1];
		A[largest-1]=a;
		max_heapify(A,largest,size);
	#print (A,i,largest)

def Build_heap(A):
	size=math.floor(len(A)/2);
	for i in range(size,0,-1):
		#print (i)
		max_heapify(A,i,len(A));
	return A;
def Heapsort(A):
	A=Build_heap(A);
	heap_size=len(A);
	print(A)
	for i in range(len(A),1,-1):
		a=A[i-1];
		A[i-1]=A[0];
		A[0]=a;
		print (A)
		heap_size=heap_size-1
		max_heapify(A,1,heap_size)
	return A;
	pass
#test=[16,14,10,8,7,9,3,2,4,1]:
test=[4,1,3,2,16,9,10,14,8,7,20,33,23,0,-3,23,23,23,4,1,4,5,67,8,23,3,-1]
print(len(test))
print(Heapsort(test))
print(dir(Heapsort))