#!/usr/bin/env python
# coding=utf-8
#####root!  error
import codecs
import sys
#only for query
#the node class
class edge():
	temp_ID = 0
	# root = None
	sub_dict = {}
	def __init__(self):
		self.id = self.__class__.temp_ID
		self.father = None
		self.letter = None
		# self.id_list = [self.id]
	 	self.words = 0
	 	self.prefix = 0
	 	# sub_dict = {}
	 	self.sons = {}		#use dictionary, hash map faster

	def addWord(self,word):
		if word == '':
			self.words = self.words+1
		else:
			self.prefix = self.prefix+1
			k = word[0]
			son = self.sons.get(k)
			if son == None:
				self.__class__.temp_ID = self.__class__.temp_ID + 1
				self.sons[k] = edge()
				self.sons[k].father = self
				self.sons[k].letter = k
			sub_items = self.__class__.sub_dict.get(k)
			if sub_items == None:
				self.__class__.sub_dict[k] = [self.sons[k]]
			else:
				for sub_item in sub_items:
					if self.sons[k].id == sub_item.id:
						break
					else:
						sub_items.append(self.sons[k])
			word = word[1:]
			self.sons[k].addWord(word)

	def countWord(self,word):
		if word == '':
			return self.words
		else:
			k = word[0]
			son = self.sons.get(k)
			if son == None:
				return -1
			else:
				word = word[1:]
				return son.countWord(word)

	def countPrefix(self,word):
		if word == '':
			return self.prefix
		else:
			k = word[0]
			son = self.sons.get(k)
			if son == None:
				return -1
			else:
				word = word[1:]
				return son.countPrefix(word)

#store all the items below the node
def get_subword(node,word,result):
	if len(node.sons.keys()) == 0:
		if word not in result:
			result.append(word)
	else:
		for (first_letter,sub_node) in node.sons.items():
			new_word = word+first_letter
			if sub_node.words >0:
				result.append(new_word)
			get_subword(sub_node, new_word, result)

def get_father_string(node,result):
	if node.id == 0:
		pass
	else:
		result.append(node.letter)
		get_father_string(node.father, result)


def queryWord(word,result,node,initial_word):
	if word == '':
		result.append(initial_word)
		#store all the items below
		get_subword(node, initial_word, result)
		return result
	else:
		k = word[0]
		son = node.sons.get(k)
		if son == None:
			return -1
		else:
			word = word[1:]
			queryWord(word, result, son,initial_word)
			return result

def queryMidWord(word,node,result):
	k = word[0]
	node_list = node.__class__.sub_dict.get(k)
	# final_result = []
	if len(node_list) == 0:
		pass
		# return -1
	else:
		for midNode in node_list:
			temp_result = []
			res = queryWord(word, temp_result, midNode.father, word)
			if res == -1:
				pass
			elif len(res)==0:
				pass
			else:
				letters_above = []
				get_father_string(midNode, letters_above)
				string_above = ''.join(reversed(letters_above))
				for item in res:
					temp = string_above+item
					if temp not in result:
						result.append(temp)



##data processing
def gener(file_name):
	with codecs.open(file_name,"r","utf-8") as f:
		for line in f:
			temp_line = []
			# line = unicode(line,'utf-8')
			line = line.strip('\n')
			items = line.split(u',')
			for item in items[:-1]:
				temp_line.append(item)
			for item in items[-1].split(u'；'):
				temp_line.append(item)
			yield temp_line


if __name__ == '__main__':
	print "########################################################"
	print "Hello Prof:"
	print "Initializing: buiding tree..."
	tree = edge()
	# tree.__class__.root = tree
	for lines in gener('data.txt'):
		for word in lines:
			tree.addWord(word)

	print "Initializing finished!"
	print "########################################################"
	print "Please enter a word:"
	while True:
		word = raw_input().decode(sys.stdin.encoding)
		if word == '':
			print "Please enter some words!"
			print "******************************************\n\n"
			continue
		result = []
		initial_word = word
		res = queryWord(word, result, tree, initial_word)
		queryMidWord(word, tree, res)



		if res == -1 or len(res)==0:
			print "******************************************"
			print "Not Found!"
			print "******************************************\n\n"

		else:
			print "******************************************"
			#show 15 items at most
			show_len = len(res) if len(res)<=30 else 30

			for item in res[:show_len]:
				print item," Prefix: ",tree.countPrefix(item)," Word: ", tree.countWord(item)
			print "******************************************\n\n"





