def isTriangle(a,b,c):
    if a < b+c and b < a+c and c < a+b:
        if a == b and b == c:
            print("Equilateral triangle")
        elif a != b and b !=c and a != c:
            print("Scalene Triangle")
        else:
            print("Isosceles Triangle")
    else:
        print("Invalid triangle")
    
if __name__ == "__main__":
    while True:
        a = int(input('Enter side a: '))
        if a < 1 or a > 10:
            print("Invalid side a")
            continue
        b = int(input('Enter side b: '))
        if b < 1 or b > 10:
            print("Invalid side b")
            continue
        c = int(input('Enter side c: '))
        if c < 1 or c > 10:
            print("Invalid side c")
            continue
        isTriangle(a,b,c)


