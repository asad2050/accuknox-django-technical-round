class Rectangle:
    def __init__(self, length: int, width: int):
        """Initialize the rectangle with length and width. Then length and width are passed as argument when the constructor is called."""
        self.length = length
        self.width = width

    def __iter__(self):
        """Allow iteration over the rectangle's dimensions. 
        This method is a special (or magic) method in Python that allows an object to be iterated over, like a list or dictionary.
        Since yield is used, the method becomes a generator, meaning it can return values one at a time during iteration. This is memory efficient, as the values are generated only when needed.
        """
        yield {'length': self.length}
        yield {'width': self.width}

# Example usage
if __name__ == "__main__":
    '''Creating an instance of class Rectangle and storing its reference in rect. Passing 10,5 as positional arguments length, width.'''
    rect = Rectangle(10, 5)
    ''' For loop is used to iterate through the object and print every property in that object.'''
    for dimension in rect:
        print(dimension)
