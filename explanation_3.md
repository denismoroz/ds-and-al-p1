
### Huffman Encoding

On the first step to build frequency map of characters dictionary was used. 
That helped to do that with O(n) complexity. It requires only one time to go 
through all elements to build a frequency map.

One of the main parts while building Huffman tree is to select nodes with the 
minimal frequency, for this part min heap was used. It allows to retrieve the 
minimal element with O(1) and extracting minimal element with O(logN) complexity.

While building encoding map Breadth First Search to iterate over all Huffman tree
nodes and collect encoding codes. 

### Complexity
Building a frequency map: O(N)
Building a hoffman Tree: O(NlogN), for each element we have to traverse a tree and find appropriate place.
Encoding a message: using a encoding map: O(N) where N is number of characters in input sequence.
Decoding message: O(N) where is N is number of bits in encoded sequence.
 