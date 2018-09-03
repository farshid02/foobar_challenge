import math
def answer(area):
    '''Write a function answer(area) that takes as its input 
    a single unit of measure representing the total area of solar panels 
    you have (between 1 and 1000000 inclusive) and returns a list of 
    the areas of the largest squares you could make out of those panels, 
    starting with the largest squares first. So, following the example above, 
    answer(12) would return [9, 1, 1, 1]. '''
    res = []
    while area > 0:
        root_value = int(math.sqrt(area))
        area_squared = root_value**2
        res.append(area_squared)
        area = area - area_squared
    return res