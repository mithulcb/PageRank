# PageRank
Implementation of pagerank algorithm using python in hadoop.
<br>
mapper.py and reducer.py are used to compute the initial page rank and adjacency list from an input data consisting of current page and page it is pointing to separated by a tab space. The path to file w is provided as a command line argument.
<br>
The initial page rank is stored locally a "w" and adjacency list is stored in HDFS.
<br>
sample_input.txt is given as
<br>
1	3<br>
2	1<br>
2	4<br>
4	5<br>
4	3<br>
4	1<br>
5 3<br>
<br>
w file will be
<br>
1,1<br>
3,1<br>
4,1<br>
5,1<br>
<br>
The computed sample_adjacency_list will be<br>
1	[3]<br>
2	[4, 1]<br>
4	[5, 1, 3]<br>
5	[3]<br>
<br>
mapper2.py and reducer2.py will compute the new page ranks according to page embeddongs provided and w file containing the ranks.
<br>
mapper2.py contains functions for computing contribution and similarity wrt current nodes and incoming nodes.
<br>
These vaues are then sent to reducer2.py as a key-value pair of current node and contribution from where new rank is calculated. 
<br>
Inputs to mapper2.py file will be sample_page_embeddings.json and w files as command line arguments. The adjacency list will be read directly from HDFS.
<br>
This can be manually be repeated till page ranks of previous iteration is same as current iteration.
