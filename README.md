# GeneReconstruction
Repository for Introduction to bioinformatics project at FRI, UNI-LJ, winter semester 2016/2017

**Authors**: Jan Berčič, Jernej Henigman, Sara Kužnik, Filip Langr, Jasna Urbančič

##Introduction

In Gene reconstruction research project we examine three different methods for genome assembly. We divide genome into k-mers and then we use various methods to reconstruct genome into original sequence. First method is called overlapping kmers. We start by creating a graph where nodes represent *k*-mers and edges connect overlapping *k*-mers. Second method we implement is de Brujin graph in which we are searching for Eulerian path. Third method
also uses de Brujin graph but instead of single reads (*k*-mers) we use read-pairs where pairs are some distance *d* apart.

Our input data consists of 3 different bacteria genomes. Each bacteria genome has different number of nucleotides. Bacterias Klebsiella pneumoniae, Streptomyces silvensis and Citrobacter freundii have 40955, 104514, 180261 nucleotides respectively.

In our research project we implement de Brujin graph methods and test them on genomes of different lengths. In the experiment we try different values for parameters *k* and *d* and report how the length of the genome affects each method. We find smallest possible values for parameters *k* and *d* so that genomes are are still reconstructed correctly.

##Methods

###Overlapping kmers

Genome reconstruction with overlapping *k*-mers starts with building an overlap graph --- *k*-mers represent nodes and edges connect two nodes for which it holde that suffix of the first is prefix of the second. Once that we have build the overlap graph we are looking for a path that visits each node exactly once. Such path is called Hamiltonian path. However, we skiped the implementation of overlapping kmers method because time required to solve the problem using any currently known algorithm increases very quickly as the size of the problem grows. Determining whether such paths and cycles exist in graphs is the Hamiltonian path problem, which is NP-complete.

###De Brujin graph

In overlapping *k*-mers method we have a graph where nodes represent k-mers and edges connect overlapping *k*-mers. When using this graph to construct original genome, we have to Hamiltonian path which is NP-complete problem. So we use better method, we construct a graph where we assign k-mers to edges and nodes represent *(k-1)*-mers. When having graph like that, we have to find Eulerian path.

Graph where nodes represent *(k-1)*-mers and edges represent k-mers is called de Brujin graph. When building de Bruin graph we must first split the genome into *k*-mers. For each *k*-mer we than construct two nodes with *(k-1)*-mer connected with directed edge representing given *k*-mer. For example, for *k*-mer ACCTG we then get two *(k-1)*-mer nodes ACCT --> CCTG and to the directed edge *k*-mer ACCTG is assigned. Then we just glue identically labeled nodes together. When gluing identically labeled nodes together, we must keep all edges, so sometimes we get more than one edge between two nodes.


###Paired de Brujin graph

In order to increase the read length we looked at paired de Brujin graphs. Pair-reads indirectly increase the read length and contain more information than *k*-mers.

First step in building a paired de Brujin graph is spliting the genome into read-pairs. Read-pair consists of two reads (*k*-mers) that are separated by a fixed distance *d*. We denote them as *(k, d)-mers*. In the next step we compute prefix and suffix for each of the read-pairs. Given a *(k, d)*-mer *(a1, a2, ..., aK | b1, b2, ..., bK)* its prefix is *(a1, ..., a(K-1) | b1, ..., b(K-1))* and its suffix is *(a2, ..., aK | b2, ..., bK)*. It should be noted that for two consecutive *(k, d)*-mers, the suffix of the first read-pair is equal to the prefix of the second. We use prefix and suffix to create nodes of the de Brujin graph and *(k, d)*-mers as edges.

Once we have successfully constructed the paired de Brujin graph we can use the same algorithm to find an Euler path as before. Once we have found the path we assemble a *prefixString* (a sequence obtained by joining the first items of nodes) and a *suffixString* (a sequence obtained by joining the second items of nodes). The *suffixString* is delayed for *k + d* nucleotides compared to the *prefixString*. It can happen that an Eulerian path in the graph does not spell the solution, so we have to check if the overlapping substrings of *prefixString* and *suffixString* match. If they match, we concatenate *prefixString* with the last *k + d* characters of *suffixString*.

##Experiments

We examine our de Brujin and paired de Brujin methods on 3 different genomes. Methods are implemented in euler_path.py. We start with parameter values *k = 2* and *d = 0*. When algorithms produce correct output results for given parameters value we stop. If the output result are not correct we increment parameter values by 1. At the end of execution we are left with smallest possible values of parameters *k* and *d*.

##Results

We had to find smallest possible parameters *k* and *d* so that genome sequence is still reconstructed correctly.


###Single de Brujin graph
|Genome length| k  | Possible solutions |
|----------------| ------------- | ------------- |
|~40k| 18  | ?  |
|~100k| 27  | ?  |
|~180k| 60  | ?  |

Next we present a table of smallest found distances between two reads *d* for given small-enough lengths of the reads *k* in a paired de Brujin graph. Also a smallest k for *d = 0* is presented.

###Paired de Brujin graph
|Genome length| k | smallest d for given k| Possible solutions |
|----------------| ------------- | -------------| ------------- |
|~40k| 11  | 0  |? |
|~40k| 9  | 7  |? |
|~40k| 8  | 2238  |? |
|~100k| 14  | 0  |?|
|~100k| 11  | 33  |?|
|~100k| 10  | 145  |?|
|~100k| 9  | 50000*  |?|
|~180k| 30| 0  |? |
|~180k| 20| 20  |? |
|~180k| 10| 60  |? |

*k* - length of the reads

*d* - distance between two reads

\* - Not every *d* in (0 ; 50000) interval was tested.

We implemented another version of path finding algoritm that outputs all possible solutions (euler_path_all_paths.py), however it is computationally very complex. We had it running overnight on genome of length 40k, but it was automatically killed at some point. Therefore we are unable to provide this answers.

##References
* Compeau & Pevzner: [Bioinformatics algorithms: an active learning approach](http://bioinformaticsalgorithms.com)
* Pevzner, P.A., Tang, H. and Waterman, M.S. (2001) An Eulerian path approach to DNA fragment assembly. Proc Natl Acad Sci U S A, 98, 9748-9753.
* Compeau, P.E., Pevzner, P.A. and Tesler, G. (2011) How to apply de Bruijn graphs to genome assembly. Nat Biotechnol, 29, 987-991.

###Data
* [Klebsiella pneumoniae strain OC217 AOT21_contig000040](https://www.ncbi.nlm.nih.gov/nuccore/971065155)
* [Citrobacter freundii strain AMA 948 contig_6](https://www.ncbi.nlm.nih.gov/nuccore/970964877)
* [Streptomyces silvensis strain ATCC 53525 53525_Assembly_Contig_82](https://www.ncbi.nlm.nih.gov/nuccore/970984238)
