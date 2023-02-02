## Write a function with keyword arguments
## your function can be a mix of positional and keyword arguments
## it must use a default value for the keyword argument.
"""
    Input:
        length: int
        width: int, defaults to 10

    
    Returns:
        the area of the rectangle
    """
def rectangle(length,width=10):
    area=length*width
    return area
print(rectangle(4))