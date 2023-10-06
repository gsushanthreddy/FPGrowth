import logging

from fp_tree_node import *
from fp_growth import *
from collections import defaultdict

# Setting up a logger
logger = logging.getLogger()  # Initiating a logger
logging.basicConfig(filename="logs.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger.setLevel(logging.DEBUG)



def order_transaction(transaction,itemset):
    """
    Main functionality of this function is to order a transaction in decreasing order of the count of attributes. 
    Sorted transaction is returned as the output. 
    Parameters:
        -transaction: transaction present in the transactional data 
        -itemset: 
    """
    transaction = sorted(transaction,key=lambda x:itemset[x],reverse=True)
    return transaction

def conditional_pattern_base(fp_tree, itemlist_retrieved):
    """
    Algo for conditional pattern base
    
    """
    

def mine_frequent_itemsets(transactions,threshold):
    
    # Initializing a default dictionary which assigns a value 0 if that key is not present in the dict
    itemset = defaultdict(lambda:0)

    # Calculating count of attributes from transactional data and storing them in itemset
    for transaction in transactions:
        for attribute in transaction:
            if attribute is not None:
                itemset[attribute] += 1
    
    logger.info("---------------Count of Items stored in a Dictionary---------------")
    # Sorting the itemsets in decreasing order of their count
    try:
        itemset=dict(sorted(itemset.items(), key=lambda item:item[1],reverse=True))
    except Exception as e:
        logger.error(e)
    
    logger.info("---------------Itemset sorted in decreasing order of their count---------------")    
    
    # Now we have to rearrange the items present in each transaction in the same way the itemsets are arranged
    
    try:
        for index, transaction in enumerate(transactions):
            transactions[index] = order_transaction(transaction,itemset)
    except Exception as e:
        logger.error(e)
        
    logger.info("---------------Items in each transaction are sorted---------------")
    
    # It is time to build the FP Tree using the items present in the ordered transaction in transactional data
    
    fp_tree = FPTree()
    try:
        for transaction in transactions:
            if len(transaction) is not 0:
                fp_tree.add_items(transaction)
     
    except Exception as e:
        return(e)
    
    logger.info("---------------FP Tree created---------------")
    
    # Now we have to mine the frequent patterns from the FP tree that was created using the items from the transaction data
    
    for frequent_itemsets in conditional_pattern_base(fp_tree,[]):
        return frequent_itemsets
    
    
    
        
    