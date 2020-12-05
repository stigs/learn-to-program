

def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(75)
    2
    >>> num_buses(0)
    0
    >>> num_buses(50)
    1
    """

    if n % 50 != 0:
        return n // 50 + 1
    else:
        return n // 50
        

    
    


def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    >>> stock_price_summary([])
    (0, 0)
    >>> stock_price_summary([-0.05, -0.01, -0.01, 0])
    (0, -0.07)
    
    """
    pos_chg = 0
    neg_chg = 0

    for change in price_changes:
        if change >= 0:
            pos_chg = pos_chg + change
        else:
            neg_chg = neg_chg + change

    return (pos_chg, neg_chg)


def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]

    >>> nums = []
    >>> swap_k(nums,0)
    >>> nums
    []

    >>> nums = [5]
    >>> swap_k(nums,0)
    >>> nums
    [5]

    >>> nums = [1, 2]
    >>> swap_k(nums, 1)
    >>> nums
    [2, 1]

    >>> nums = ["one", "two", "three"]
    >>> swap_k(nums, 1)
    >>> nums
    ["three", "two", "one"]

    >>> nums = [5, 4, 3, 2]
    >>> swap_k(nums, 2)
    >>> nums
    [3, 2, 5, 4]

 
    """

## Approach #1 (failing to change the list at the end per unittest):

##    if len(L) >=2 and k <= len(L) // 2:
##        temp_end = []
##        temp_beg = []
##
##        for i in range(0, k):
##            
##            ## Copy the first item to a temporary list (add at the end) and
##            ## remove it from the original list
##            temp_end.append(L[0])
##            L.pop(0)
##
##
##            ## Copy the last item to a temporary list (add at the beginning) and
##            ## remove it from the original list
##            temp_beg.insert(0, L[-1])
##            L.pop(-1)
##
##        
##        L = temp_beg + L + temp_end
        
## APPROACH #2: Use slicing to create copies of the beginning and end,
## then overwrite the original list
    
    if len(L) >= 2 and k <= len(L) // 2:
        
        ## copy the first k items of the list, and the last k items
        beg = L[0:k]
        end = L[-k:]

        # iterate through the items in beginning and end and overwrite them to L.
        for i in range(k):
            L[i] = end[i]
            L[-(i+1)] = beg[-(i+1)]

        
            
        

    

if __name__ == '__main__':
    import doctest
    doctest.testmod()
