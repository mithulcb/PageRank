#!/usr/bin/env python3
import sys
import json
path_to_w=sys.argv[1]
path_to_page_embedding=sys.argv[2]
adj_d={}
incoming={}

old_rank = {}
embedding = None

with open(path_to_w) as file:
	for line in file:
		rank_splitting = line.strip().split(",")
		old_rank[rank_splitting[0]]=float(rank_splitting[1])
	#print("old_rank\n",old_rank)

with open(path_to_page_embedding) as file:
	embedding=json.load(file)
	#print("embedding\n",embedding)


def similarity(p,q):
	p_vector=embedding[str(p)]
	q_vector=embedding[str(q)]
	dot_product=0
	q_vector_sq=0
	p_vector_sq=0
	for i,j in zip(p_vector,q_vector):
		dot_product+=i*j
		p_vector_sq+=i*i
		q_vector_sq+=j*j
	result=dot_product/(p_vector_sq + q_vector_sq - dot_product)
	return result
	

def contribution(p,q):
	contribute_result=old_rank[p]* similarity(p,q)/len(adj_d[p])
	return contribute_result



for hi in sys.stdin:     #reading adj list
	splitting = hi.strip("\n").split("\t")
	temp=list(map(int, splitting[1][1:-1].split(', ')))
	adj_d[splitting[0]]=temp    #make dictionary

#print("adj_d\n",adj_d)
for from_node, to_nodes in adj_d.items():
	for to_node in to_nodes:
		try:
			incoming[to_node].append(from_node)
		except:
			incoming[to_node]=[]
			incoming[to_node].append(from_node)

#print("incoming\n",incoming)			
adj_keys=adj_d.keys()
incoming_keys=incoming.keys()

for i in adj_keys:
	if int(i) not in incoming_keys:
		incoming[int(i)]=[]
#print("new_incoming\n",incoming)

for i in incoming:
	#print(i)
	if incoming[i]:
		for j in incoming[i]:
			#print(j)
			print(i,contribution(j,i))
	else:
		print(i,0)

