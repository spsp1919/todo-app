feet_inches=input("enter the feet and inches")



def parse(feetinches):
    parts = feetinches.split(" ")
    feet=float(parts[0])
    inches=float(parts[1])
    return feet,inches

def convert(feet,inches):
    meters= feet * 0.3048 + inches * 0.0254
    return meters

f,i=parse(feet_inches)
print(f,i)

result= convert(f,i)

if result < 1:
    print("kid is too small")
else:
    print("kid is allowed")