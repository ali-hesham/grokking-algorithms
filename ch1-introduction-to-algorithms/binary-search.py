# binary search implementation
def binary_search(list, item):
    """
    params:
        list: list of numbers to to search in.
        item: search key.

    returns: returns key and index if found else None.
    """
    low = 0
    high = len(list) - 1
    list.sort()
    while  low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return guess, mid
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None
