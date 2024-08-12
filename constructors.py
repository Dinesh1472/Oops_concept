try:
    class skillspeed:
        def __init__(self):#using __init__
           print('this is the constructors blocks')

        def setFullName(self,employeename):
            self.employeename=employeename

        def printFullname(self):
            print(self.employeename)

    x=skillspeed()
    x.setFullName('robert')
    x.printFullname()
except Exception as e:
    print(e)
