
### Union and intersection

Set data structure was used to implement linked list intersection and union.
Linked lists were converted to set and appropriate set operation was called.
After that resulting linked list was build from resulting set.

### Time and Space complexity

Construction intermediate sets: O(n + m) n - number elements in the first 
list and m number elements in second list. There is a need to go over each element
in list and add them to set. Average complexity for adding elements to set is O(1)

Intersection as it is based on set: O(min(n, m)) 
Union as it is based on set: O(n+m)

