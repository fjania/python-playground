class node():
	def __init__(self, parent, value, count=0):
		self.parent = parent
		self.value = value
		self.count = count
		self.children = {}
	
	def add_child(self, letter):
		if not self.children.get(letter):
			self.children[letter] = node(self, letter)
		return self.children[letter]


class trie():
	def __init__(self):
		self.root = node(None, None)
	
	def add(self, word):
		n = self.root
		for l in word:
			n = n.add_child(l)
		n.count += 1


if __name__ == "__main__":
	t = trie()
	t.add("hello")
	t.add("nothing")
	t.add("note")
	t.add("nothing")
	t.add("he")
	t.add("nothing")
	
	def print_tree(n, t=0):
		print '.'*t , n.value
		if n.count:
			print '-'*t, n.count
		for c in n.children:
			print_tree(n.children[c], t+1)
			
	print_tree(t.root)
	
	def find_count(tree, word):
		n = tree.root
		for l in word:
			if n is None:
				print word, 0
				return
			n = n.children.get(l)
		print word, n.count
	
	import sys
	find_count(t, sys.argv[1])