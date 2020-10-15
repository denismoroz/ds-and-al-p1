
### Block chain.

It is build based on linked list. Each new data that is added to it contains a hash
of the previous block plus timestamp. This allows to check block chain blocks for modification.

### Time and Space complexity

Add new data block is O(1) - because used linked list and data is added to tail.
Validation - O(n) where is n is number of blocks.
It requires O(N*BLOCK_SIZE) space to store blockchain information.