# GeneReconstruction
Repository for Introduction to bioinformatics project at FRI, UNI-LJ, winter semester 2016/2017

**Authors**: Jan Berčič, Jernej Henigman, Sara Kužnik, Filip Langr, Jasna Urbančič

##Instructions

TO BE TRANSFORMED INTO ABSTRACT!

Take a genome and divide it into k-mers. Use the k-mers to reconstruct the genome using various methods. Start with creating a graph where nodes represent k-mers and edges connect overlapping k-mers. Find a path through the graph that visits each node only once. Then construct another graph, where nodes represent (k-1)-mers and k-mers are placed on edges (de Bruijn graph). This time find a path through the graph where each edge is traversed exactly once. Lastly, create a paired de Bruijn graph from consecutive k-mers that are some distance d apart.

Test your methods on genomes of different length. Try different values for the parameters k and d. Report how the length of the genome affects each method, at which values of k and d you are able to reconstruct the original genome and the number of possible solutions you get.

##References
* Compeau & Pevzner: [Bioinformatics algorithms: an active learning approach](http://bioinformaticsalgorithms.com)
* Pevzner, P.A., Tang, H. and Waterman, M.S. (2001) An Eulerian path approach to DNA fragment assembly. Proc Natl Acad Sci U S A, 98, 9748-9753.
* Compeau, P.E., Pevzner, P.A. and Tesler, G. (2011) How to apply de Bruijn graphs to genome assembly. Nat Biotechnol, 29, 987-991.

###Data
* [Klebsiella pneumoniae strain OC217 AOT21_contig000040](https://www.ncbi.nlm.nih.gov/nuccore/971065155)
* [Citrobacter freundii strain AMA 948 contig_6](https://www.ncbi.nlm.nih.gov/nuccore/970964877)
* [Streptomyces silvensis strain ATCC 53525 53525_Assembly_Contig_82](https://www.ncbi.nlm.nih.gov/nuccore/970984238)
