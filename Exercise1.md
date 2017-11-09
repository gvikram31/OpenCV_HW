1. How does a program read the cvMat object, in particular, what is the order of the pixel structure?

Answer:- The cvMat is a way to represent the pixels in an image in a matrix form. It reads the cvMat object from rows to column
then to the color channel dimensions.
Therefore, pixel values of a cvMat file can be accessed by using the cvMatName.at(x,y) where we can access a particular pixel at matrix entry point (x,y) where (0,0) would be the top-left entry of the matrix. Additionally, if the pixel has multiple color channels, then we could access a particular color channel by invoking cvMatName.at{x,y)[index] where index allows us to access particular values of the color channels (i.e. RGB). 
This method requires that we know the datatype of the entries. CVmat is replaced by mat in new versions.
