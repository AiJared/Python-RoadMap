marks = int(input("Enter the marks: "))

if marks < 40:
    print("Fail")
elif marks >=40 and marks <50:
    print("D")
elif marks >=50 and marks <60:
    print("C")
elif marks >=60 and marks <70:
    print("B")
elif marks >=70 and marks <=100:
    print("A")
else:
    print("Invalid input!")