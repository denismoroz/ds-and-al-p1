
### LRU Cache

To implement LRU cache with O(1) requirement on operation I used 2 data structures.
for fast inserting/search I used dictionary object. To keep order of elements 
double linked list was used. That allowed to have O(1) on time for inserting, 
removing, deleting of elements.


### Time and Space complexity

Space complexity 0(n) all elements are stored once.
Time complexity: add, get, remove - O(1) due using dict and linked list.
 