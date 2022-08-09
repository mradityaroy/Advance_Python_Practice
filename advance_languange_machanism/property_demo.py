class Person:
    def __init__(self, name):
        self._name = name
    def getName(self):
        print("I am inside getName")
        return (self._name)
    managedx = property()
def main():
    p = Person("Aditya")
    print("Person.__dict__:------",Person.__dict__)
    print("p.__dict__:------",p.__dict__)
    print("p.getName():-----",p.getName())
    print("p.managedX:-----",p.managedX)
main()
