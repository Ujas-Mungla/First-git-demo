from datetime import datetime

def decorated(fxn):
    def modify_deco():
        start = datetime.now()
        print(f"brefore time taken {start}")
        fxn()
        end = datetime.now()
        print(f"after time taken {end}")
        
        print(f"the total time taken by function is {end - start}")

    return modify_deco

@decorated
def print_fxn():
    print("hello this is a print function")
    for i in range(1000000000):
        pass

print_fxn()