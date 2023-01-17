class Progression:
    """ Iterator producing a generic Progression.
    
    Default iterator implementation for whole numbers 0,1,2,3...

    """

    def __init__(self, start=0):
        """ initialized current to the first value"""
        self._current = start

    def _advance(self):
        """ update current"""
        self._current += self

    def __next__(self):
        """ return the next value"""
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def print_progression(self, n):
        print(' '.join(str(next(self)) for j in range(n)))





if __name__ == '__main__':
    print("defualt progression")
    Progression().print_progression(10)
