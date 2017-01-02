# GeneReconstruction
Repository for Introduction to bioinformatics project at FRI, UNI-LJ, winter semester 2016/2017

**Authors**: Jan Berčič, Jernej Henigman, Sara Kužnik, Filip Langr, Jasna Urbančič

##Introduction

*TO BE TRANSFORMED INTO ABSTRACT OR PROPER INTRODUCTION!*

Take a genome and divide it into k-mers. Use the k-mers to reconstruct the genome using various methods. Start with creating a graph where nodes represent k-mers and edges connect overlapping k-mers. Find a path through the graph that visits each node only once. Then construct another graph, where nodes represent (k-1)-mers and k-mers are placed on edges (de Bruijn graph). This time find a path through the graph where each edge is traversed exactly once. Lastly, create a paired de Bruijn graph from consecutive k-mers that are some distance d apart.

Test your methods on genomes of different length. Try different values for the parameters k and d. Report how the length of the genome affects each method, at which values of k and d you are able to reconstruct the original genome and the number of possible solutions you get.

##Methods
*please write sth about the part that you did*

###Overlapping kmers

###De Brujin graph

###Paired de Brujin graph

*TO DO: motivation, theoretical background...*

First step in building a paired de Brujin graph is spliting the genome into read-pairs. Read-pair consists of two reads (*k*-mers) that are separated by a fixed distance *d*. We denote them as *(k, d)-mers*. In the next step we compute prefix and suffix for each of the read-pairs. Given a *(k, d)*-mer *(a1, a2, ..., aK | b1, b2, ..., bK)* its prefix is *(a1, ..., a(K-1) | b1, ..., b(K-1))* and its suffix is *(a2, ..., aK | b2, ..., bK)*. It should be noted that for two consecutive *(k, d)*-mers, the suffix of the first read-pair is equal to the prefix of the second. We use prefix and suffix to create nodes of the de Brujin graph and *(k, d)*-mers as edges.

Once we have successfully constructed the paired de Brujin graph we can use the same algorithm to find an Euler path as before. Once we have found the path we assemble a *prefixString* (a sequence obtained by joining the first items of nodes) and a *suffixString* (a sequence obtained by joining the second items of nodes). The *suffixString* is delayed for *k + d* nucleotides compared to the *prefixString*. It can happen that an Eulerian path in the graph does not spell the solution, so we have to check if the overlapping substrings of *prefixString* and *suffixString* match. If they match, we concatenate *prefixString* with the last *k + d* characters of *suffixString*.

##Experiments
*sth. about the experiments and possibly results --- according to general instructions:*
>*The results would often include a tabular representation of quantitative results of experiments and any visualization.*

##Results
*possibly conclusion or sth. if overlapping with Experiments chapter*


##References
* Compeau & Pevzner: [Bioinformatics algorithms: an active learning approach](http://bioinformaticsalgorithms.com)
* Pevzner, P.A., Tang, H. and Waterman, M.S. (2001) An Eulerian path approach to DNA fragment assembly. Proc Natl Acad Sci U S A, 98, 9748-9753.
* Compeau, P.E., Pevzner, P.A. and Tesler, G. (2011) How to apply de Bruijn graphs to genome assembly. Nat Biotechnol, 29, 987-991.

###Data
* [Klebsiella pneumoniae strain OC217 AOT21_contig000040](https://www.ncbi.nlm.nih.gov/nuccore/971065155)
* [Citrobacter freundii strain AMA 948 contig_6](https://www.ncbi.nlm.nih.gov/nuccore/970964877)
* [Streptomyces silvensis strain ATCC 53525 53525_Assembly_Contig_82](https://www.ncbi.nlm.nih.gov/nuccore/970984238)
