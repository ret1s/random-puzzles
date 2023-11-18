# 18/11/2023
### BINARY SEARCH TREE
- To implement Breadth First Search in a Binary Tree, we use queue data structure. First, we check if the root of the BT is null or not. If it's a null pointer, we return the function. Otherwise, we print out the value of root then push the left and right child of it into the queue. Next, we use a while loop to implement BFS. In detail, we check the front value of the queue. If it's not null pointer, we print out its value and push the left and right child of it and then pop it out of the queue. Repeat this procedure until the queue is empty.  
- To count node that has two childs in a BT, we will use recursion approach. First, we craft a recursion function that has input parameters is the root of the BT and a count variable. We implement recursion algorithm by including all the possible cases that can be happened. 
  + First case, when the current node is node has two childs, we increase count and call the recursion function with input is the left and right childs.
  + Second case, when node has only one child, we call recursion function for this child.
  + Last case, when node has no child, we do nothing.
- To count node that has single child in a BT