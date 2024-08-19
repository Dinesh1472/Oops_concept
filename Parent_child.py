try:
    class parent: #define parent class
        parentAttr = 100 #class variable
        def __init__(self):
            print('calling parent constructors')

        def parentMethod(self):
            print('calling parent method')

        def setAttr(self,attr):
            parent.parentAttr =attr
            print('inside parent')

        def getAttr(self):
            print('parent attribute :',parent.parentAttr)

    class child(parent): #define child class
        #print parent.parentAttr
        def __init__(self,x=20,y=30):
            self.x =x
            self.y =y
            print('calling child constructor')

        def childMethod(self):
            print('calling child method')
        def setAttr(self):
            print('calling child attributes')
            print('set attribute :',self.x)

        def display(self):
            print(self.x,self.y)

        def setAttr(self,attr):
            self.x =attr
            self.y =attr
            print('inside child method')

    c =child()  #insttance of child
 #   c.parentAttr()
    c.display()
    c.childMethod()   #child calls its method
    c.parentMethod()  #calls parent's method
    c.setAttr(400)     #again call parent's method
    c.getAttr()      #again call parent's method
    c.display()
        
except Exception as e:
    print(e)
