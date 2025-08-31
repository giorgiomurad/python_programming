class MyList:
    # Constructor
    def __init__(self, clist):
        self.clist = clist

    # 1. Function to return the length of the list
    def __len__(self):
        return len(self.clist)

    # 2. Function to return element at the given index
    def __getitem__(self, idx):
        return self.clist[idx]

    # 3. Function to set the item at the given index
    def __setitem__(self, idx, value):
        self.clist[idx] = value

    # 4. Function that deletes the value at given indev
    def __delitem__(self, idx):
        del self.clist[idx]

    # 5. Function that returns list for iteration (commonly used for loops)
    def __iter__(self):
        return iter(self.clist)

    # 6. Function that returns true if the list contains the given value, and false if otherwise
    def __contains__(self, item):
        return item in self.clist