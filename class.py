#built is attribute
try:
   class ex_self:
      """
       sample class methods which
       used for defining a self in
       side class method
       """


      def myFunction(self):
          print("welcome to Elegant")

   print(ex_self.__dict__)

   print(ex_self.__doc__)#Document present inside the class
   obj=ex_self()
   obj.myFunction()#internally translates into ex_self.myFunctions(obj)
except Exception as e:
   print(e)
