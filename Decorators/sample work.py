def car(wheel):
    def speed(x,y):
        print("full speed ")
        wheel(x,y)
        print("verified")
    return speed

@car
def calculate(x,y):
    print("answer : ",x*y)


calculate(5,8)
