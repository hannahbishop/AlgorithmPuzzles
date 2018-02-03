class BinaryTree:
    def __init__(self, list_values):
        self.list_values = list_values
        self.last_seen = -99999 #initially set last_seen to the mininum

    # INITIAL ATTEMPT - 35 minutes
    # O(n) runtime
    # Needed to be streamlined
    # Looks at each recursive return value, and compares it to the current node's value
    '''
    def is_bst(self, index):
        if(index >= len(self.list_values)): 
            return None
        if(self.list_values[index] == None):
            return None
        else:
            left = self.is_bst(2*index + 1) #left subtree
            right = self.is_bst(2*index + 2) #right subtree
            if(left == None and right == None):
                return self.list_values[index]
            if(left == None): 
                if(right > self.list_values[index]):
                    return self.list_values[index]
            if(right == None): 
                if(left < self.list_values[index]):
                    return self.list_values[index]
            if(left < self.list_values[index] and right > self.list_values[index]): 
                return self.list_values[index]
            else: return -1
    '''

    # BETTER SOLUTION
    # O(n) runtime
    # More readable
    # Assumes no duplicate nodes
    def is_bst(self, index):
        if index >= len(self.list_values): 
            return True

        if self.list_values[index] == None: 
            return True

        if not self.is_bst(2 * index + 1): 
            return False

        if self.list_values[index] <= self.last_seen: 
            return False

        self.last_seen = self.list_values[index]

        if not self.is_bst(2 * index + 2): 
            return False
            
        else: 
            return True

def main():
    res = BinaryTree([2,1,3]).is_bst(0)
    print("bst") if res else print("not bst")
    return

main()