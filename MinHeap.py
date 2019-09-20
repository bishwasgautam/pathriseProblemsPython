'''

Construct a minimum heap

'''


class MinHeap:

	def __init__(self, arr):
		self.heap = self.build_heap(arr)

	def build_heap(self, arr):
		#find the lowest parent (midpoint of arr)
		lowest_parent = (len(arr) - 2)//2		
		#loop back to the front of arr		
		for i in range(lowest_parent, -1, -1):
			self.shift_down(i, arr)

		return arr


	def insert(self, num):
		self.add(num)
		self.shift_up(len(self.heap)-1)

	def add(self, num):
		self.heap.append(num)

	def remove(self):
		self.swap(0,-1, self.heap)
		val = self.heap.pop()
		self.shift_down(0, self.heap)
		return val

	def peek(self):
		return self.heap[0]


	def shift_up(self, startIndex):
		#base case : until the start of range
		if startIndex <= 0:
			return
		
		parentIndex = (startIndex -1)//2
		
		if self.heap[parentIndex] > self.heap[startIndex]:
			self.swap(parentIndex, startIndex, self.heap)			
			self.shift_up(parentIndex)


	def shift_down(self, index, arr):
		#base case : until the end of range
		leftChild = 2*index + 1
		rightChild = 2*index + 2


		if leftChild >= len(arr):
			return
		elif rightChild >= len(arr) or arr[rightChild] > arr[leftChild]:
			smallest_child = leftChild
		else:
			smallest_child = rightChild

		if arr[index] > arr[smallest_child]:
			self.swap(index, smallest_child, arr)
			self.shift_down(smallest_child, arr)

	def swap(self, firstIndex, secondIndex, arr):
		arr[firstIndex], arr[secondIndex] = arr[secondIndex], arr[firstIndex]



mh = MinHeap([5,2,7,8,12,15,10,3])
heap = mh.heap
print(heap) #[2, 3, 7, 5, 12, 15, 10, 8]
print(mh.peek()) # 2
print(mh.remove()) # 2
print(heap) #[3, 5, 7, 8, 12, 15, 10]

