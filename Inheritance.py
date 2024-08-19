try:
    class baseclass:
        def basefun(self):
            print('I am in base class')#base class


    class derived(baseclass):
        pass

    obj1=baseclass()
    obj2=derived()
    obj2.basefun()

except Exception as e:
    print(e)
