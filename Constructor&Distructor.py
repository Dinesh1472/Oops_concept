
try:
    class AccountHolder:
        def __init__(self,Accname,fname,lname,address):

          self.Accname=Accname
          self.fname=fname
          self.lname=lname
          self.address=address


        def display(self):
            print(self.Accname+'\n',self.fname+'\n',self.lname+'\n',self.address+'\n')

        def __del__(self):
            print('class obj has been destroyed')

    obj=AccountHolder('saving','sub','ash','marathalli')
    obj.display()
    obj.__del__()
    obj.display()
except Exception as e:
    print(e)
