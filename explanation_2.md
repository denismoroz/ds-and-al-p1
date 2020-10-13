
### File recursion

At a first sight for this problem, it is possible to use a recursive function 
to iterate over all files and directories in a folder, but on a reason 
that number of files is unlimited and recursion can easily eat all frames 
at python stack limit. That is a primary reason to use a queue for storing 
results of the current directory listing.

### Time and Space complexity

On a space script stores in memory only directories in a current folder and
directories that are not processed yet in worth case it will be 
O(d) where d is a number of directories provided on input.

For a time complexity, it is O(d + f), where d is a number of all directories 
in a path provided on input and f is a number of all files because 
the script has to check each file/directory found in the current directory 
if a found file is a file o directory.