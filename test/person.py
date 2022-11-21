class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    #getter function
    @property
    def first_name(self):
        return self.__first_name


    #setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected a string")
        self.__first_name = value

    #deleter function
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete first_name")

    
def main():
    a = Person('Alana')
    
    a.first_name = 43

    del a.first_name



main()
