from collections import namedtuple

class fp_tree_node(object):
    def __init__(self,tree,item,count=1):
        """
        -This is a constructor class used to define the node in an FP Tree.
        -Parameters passed:
            -item : Name of the item present in a transaction.
            -count : Number of occurences of that item.
        -Definitions: 
            -parent : Link to parent of the current node .
            -children : Link to children of the current node.
            -next_pointer : Link to the same item present in another branch.
        """
        self._tree=tree
        self._item=item # data point is item
        self._count=count
        self._parent=None
        self._children={}
        self._next_pointer=None        
    
    def find_node(self,item):
        """
        Function to find the node in which the item is present. 
        -Returns corresponding node of the item passed. 
        -Parameters Passed: 
            -item: An item is passed to find it in the child branch.
        """
        try:
            return self._children[item]
        except:
            return None
        
    def get_tree(self):
        """
        Function to get the FP Tree
        """
        return self._tree
    
    def get_item(self):
        """
        Function to get the item from FP Tree node
        """
        return self._item
    
    def get_count(self):
        """
        Function to get the item from FP Tree node
        """
        return self._count
    
    def get_children(self):
        """
        Function to get the item from FP Tree node
        """
        return self._children
    
    def increment_count(self):
        """
        Function to increase the count of the item node in the FP Tree
        """
        self._count += 1
    
    def get_next_item(self):
        """
        Function to increase the count of the item node in the FP Tree
        """
        return self._next_pointer
        
    def print_node(self):
        """
        Function to print FP tree nodes and its values 
        """
        print(self._item, self._count)
        for child in self._children.keys():
            self._children[child].print_node()
            
    def print_leaves(self):
        """
        Function to print FP tree leaves and its values 
        """
        if len(self._children.keys()) == 0:
            print(self._item, self._count)
        
        for child in self._children.keys():
            self._children[child].print_leaves()
            
    def add_node(self,node):
        """
        Function to add a node to a parent
        -Parameters passed:
            -item : An item is passed as a node
        """
        if node.get_item() not in self._children:
            self._children[node.get_item()] = node
            node.parent = self
        
class FPTree(object):
    Track = namedtuple("Track", "start end") # Why this

    def __init__(self):
        """
        1. Creating a root node for the FP tree with NULL value.
        2. Creating an empty header table
        """
        self._root = fp_tree_node(self, None, None)
        self._header = {}
    
    def print_tree(self):
        root_node = self._root
        root_node.print_leaves()
        
    def fetch_nodes(self, item):
        """
        
        """
        # Accessing first node from the header table 
        node = self._header[item][0]
        
        while node is not None:
            yield node
            node = node.get_next_item
                
    def add_items(self, transaction):
        """
        Funtion to add items present in a transaction to the FP tree
        Parameters passed: 
            -transaction : ordered transaction
        Functionality:
            1. Take each item from the transaction.
            2. Check whether the item exists in the FP tree
                a. If exists -> Increment count of the node by 1.
                b. Does not exist -> Create a new node of the item and add the item with the count of 1 to the FP tree.
                 
        """
        current_node = self._root
        for item in transaction:
            next_node = current_node.find_node(item)
            if next_node:
                next_node.increment_count()
            else:
                next_node = fp_tree_node(self,item)
                current_node.add_node(next_node)
            current_node = next_node
            
    def fetch_items(self):
        """
        Function to return items in the header table and its corresponding nodes
        Using yield instead of return to use fetch_items function as a generator so as to store local variables(not executing the function with a return)
        """
        for item in self._header.keys():
            yield item, self.fetch_nodes(item)
