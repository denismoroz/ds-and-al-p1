
### Active Directory user search

To make effective solution recursive algorithm was used to iterate over all users in groups.

### Time and Space complexity

Time depends on a active directory size in worth case there is a need to 
iterate over all groups and users, so time complexity is O(U*G) U is number of users and 
G is number of groups.

Space complexity of this algorithm is proportional to maximum depth of active directory tree. 
If each function call takes O(m) space and if the maximum depth of active direcotry tree is 'n' 
then space complexity would be O(nm). Each call required to save a single stack frame.

