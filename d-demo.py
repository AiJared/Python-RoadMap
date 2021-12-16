def salary(name, basic_salary, sales):
    commision = 0
    if sales > 1000000:
        commision = sales * 0.2
    salary = basic_salary + commision
    print(f"{name}'s salary:{salary}")
salary('Tony', 100000, 1500000)
salary('Jared', 1500000, 5000000)