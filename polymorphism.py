try:
    class India():
        def capital(self):
            print('New delhi is the capital of india')

        def language(self):
            print('Hindi is the most widely spoken language of india')

        def type(self):
            print('India is a developing country')


    class USA():
        def capital(self):
            print('Washington D.C is the capital of USA')

        def language(self):
            print('English is the primary language of USA')

        def type(self):
            print('USA is a developed country')

    obj_ind=India()
    obj_usa=USA()
    for country in (obj_ind,obj_usa):
        country.capital()
        country.language()
        country.type()
except Exception as e:
    print(e)
