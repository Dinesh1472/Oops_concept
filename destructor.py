
try:
    class skillspeed:
        def __init__(self):
            print('this is a constructor block')

        def __del__(self):
            print('our class object is destroyed')

    x=skillspeed()
    x.__del__()

except Exception as e:
    print(e)
