#!/usr/bin/env python
# coding=utf-8

import codecs
import sys
#only for query
#the node class
class edge():
	def __init__(self):
	 	self.words = 0
	 	self.prefix = 0
	 	self.sons = {}		#use dictionary, hash map faster

	def addWord(self,word):
		if word == '':
			self.words = self.words+1
		else:
			self.prefix = self.prefix+1
			k = word[0]
			son = self.sons.get(k)
			if son == None:
				self.sons[k] = edge()
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

## add more data
def gener_more(file_name):
	with codecs.open(file_name,"r","utf-8") as f:
		for line in f:
			word = line.strip('\n')
			yield word

if __name__ == '__main__':
	print "########################################################"
	print "Hello Prof:"
	print "Initializing: buiding tree..."
	tree = edge()
	for lines in gener('data.txt'):
		for word in lines:
			tree.addWord(word)

	for word in gener_more('more_data.txt'):
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


		if res == -1 or len(res)==0:
			print "******************************************"
			print "Not Found!"
			print "******************************************\n\n"

		else:
			print "******************************************"
			#show 15 items at most
			show_len = len(res) if len(res)<=15 else 15

			for item in res[:show_len]:
				print item," Prefix: ",tree.countPrefix(item)," Word: ", tree.countWord(item)
			print "******************************************\n\n"





