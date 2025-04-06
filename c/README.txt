Use make to compile and make run to run the code.

To run the code you need to set 4 variables in the make file:
- N (size of connected sub-complex that you want to select randomly from the input simplicial complex)
- SAMPLES (number of samples for approximation)
- INPUT1
- INPUT2

You have to set the address of input files in the makefile for variables INPUT1 and INPUT2.  
INPUT1. dataset-nverts.txt
INPUT2. dataset-simplices.txt

These two files represent a vector of integers. There is one integer per line.
The first file contains the number of vertices within each simplex. The second
file is a contiguous list of the nodes comprising the simplices, where the
ordering of the simplices is the same as in the first file.

Consider an example dataset consisting of three simplices:
1. {1, 2, 3}
2. {2, 4}
3. {1, 3, 4, 5}
Then files would look as follows:

example-nverts.txt
3
2
4

example-simplices.xt
1
2
3
2
4
1
3
4
5
