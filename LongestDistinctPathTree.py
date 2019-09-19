'''
https://www.chegg.com/homework-help/questions-and-answers/task-process-binary-trees-containing-integers-nodes-example-tree-shown-figure-assume-follo-q36065576

'''

class Node:

	def __init__(self, val = None):
		self.val = val
		self.left = None
		self.right = None

class Solution:


	def length_longest_path(self, node, visited = None):

		if not visited:
		    visited = set()

		#base case
		if not node or node.val in visited:
			return len(visited)
		else:
			visited.add(node.val)

		max_right = max(len(visited), self.length_longest_path(node.right, visited.copy()))		
		max_left = max(len(visited), self.length_longest_path(node.left, visited.copy()))


		return max(max_right, max_left)



root = Node(10)
root.left = Node(20)
root.left.left = Node(40)
root.left.left.right = Node(50)
root.right = Node(30)
root.right.right = Node(20)
root.right.right.left = Node(5)
root.right.right.left.right = Node(15)

res = Solution().length_longest_path(root)
print(res)

