ass_to_json.py
"""


def class_to_json(obj):
    """ retuns the dictionary description with simple data structure """

    structure = {}
    if hasattr(obj, "__dict__"):
        tudent.py
'''


class Student:
    ''' Student class '''

    def __init__(self, first_name, last_name, age):
        ''' Constructor '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' Method that returns directory description with filter '''

        if isinstance(attrs, list):
            if all(isinstance(attr, str) for attr in attrs):
                res = {}
                for i in attrs:
                    if i in self.__dict__:
                        rsscal_triangle.py
'''


def pascal_triangle(n):
    '''
    returns a list of lists of integers representing
    the Pascal’s triangle of n
    '''

    triangle = [[1], [1, 1]]
    if n <= 0:
        return []

    if n == 1:
        return [[1]]

    for term in range(3, n + 1):
        temp = []
        last_term = triangle[-1]
        for i in range(len(last_term)- 1):
            sum_ = last_term[i] + last_term[i + 1]
            temp.append(sum_)
        temp.insert(0, 1)
        temp.append(1)
        triangle.append(temp)
    return trianglees[i] = self.__dict__[i]
                return res
        return self.__dict__tructure = obj.__dict__.copy()
    return structure
