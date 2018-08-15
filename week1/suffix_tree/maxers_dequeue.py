# python3
import sys
import time

from collections import deque

class Node:
	def __init__ (self, front, end, nid):
		self.front = front
		self.end = end
		self.nid = nid
		self.children = deque()


def build_suffix_tree(content):
	n = len(content)
	j, x = 0, 0  # j = new string starting point, x = node id
	branch, match = deque(), deque()
	while j < n:
		match = branch.copy()
		add_new = True
		while len(match) > 0:  # check for branch(i = j); check for subbranch(i = rest string starting point)
			while len(match) > 0:
				node = match.pop()
				if match_or_not(i, content, node):
					child = node
					add_new = False
					break
			if not add_new:
				i, f, e = matching(i, content, child)  # f = child front
				if f >= e:
					match = child.children.copy()  # not update i since new string not end, next while check for subbranch
				else:
					if child.front < f:  # only when mother node has space
						child.end = f
						relic = Node(f, e, x)
						x = x + 1
						relic.children = child.children.copy()
						child.children.clear()
						child.children.append(relic)
					new_child = Node(i, n, x)
					x = x + 1
					child.children.append(new_child)
					match.clear()
		if add_new:
			new = Node(j, n, x)
			x = x + 1
			branch.append(new)
		j = j + 1  # new string set and while for next string
		i = j
	return branch


def match_or_not(i, content, target):
	return content[i] == content[target.front]


def matching(i, content, target):
	f = target.front
	e = target.end
	while f < e and content[i] == content[f]:  # need to mark off target end from not match
		i, f = i + 1, f + 1
	return i, f, e


def harvest(tree, content):
	fruits = list()
	while len(tree) > 0:
		fruit = tree.pop()
		fruits.append(content[fruit.front: fruit.end])
		children = fruit.children
		while len(children) > 0:
			child = children.pop()
			tree.append(child)
	return fruits


if __name__ == '__main__':
	text = sys.stdin.readline().strip()
	tree = build_suffix_tree(text)
	result = harvest(tree, text)
	print("\n".join(result))
