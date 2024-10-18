## What is OOP?

Object Oriented Programming is a programming paradigm centered around the concepts of **objects** and **classes**. It allows you to model real word entities as objects in your code and enables you to organize structure your code better.

#### Four Core Principles of OOP

1. Encapsulation
2. Inheritance
3. Polymophism
4. Abstraction

We'll dive into those principles later, now let's start with the building blocks of OOP - **classes** and **objects**.

### Classes and Objects

A **class** is a **blueprint** or **template** of creating objects. 
It defines the **attributes** (data) and **methods** (functions) that the objects created from the class will have.

An **object** is an **instance** of a class. You can think of it as an example of the class with real world data. 
Check out an example Python program demonstrating how classes and objects are created in the file **class_objects.py**.

Let's understand the code:

1. **Class Definition**: We define a class called **Car** using the **class** keyword. Inside the class we have.
    - **Attributes**: **brand**, **model** and **year**. These describe the state of the class.
    - **Methods**: Functions inside a class. This method **describe()** provides a way to describe the car.

2. **Constructor (__init__)**: The __init__ method is a special method that initializes the objects when it is created. It takes **self** as the first argument which refers to the object itself. We then pass values to the attributes (**brand**, **model** and **year**).

3. **Object Creation**: We create an object **my_car** of the class **Car** with a specific brand **Toyota**, **Corolla** and year **2020**.

4. **Accessing Attributes and Methods**: We can access objects' attributes (like **my_car.brand**) and call methods (like **my_car.describe()**) to perform actions on the object.

### Encapsulation

**Encapsulation** is the idea of building data (attributes) and functions (methods) 
that operate within a single unit - **the class**. 
It also controls access to the class by restricting outside inteference making it more 
modular and secure.

In Python you can control visibility of attributes by prefixing them with underscores.
 - **Public**: Accessible by everyone (default behavior)
 - **Private**: Cannot be accessed outside the class. Use **double underscore** (__) to make
 an attribute and/methods private.

 Check out the code in the file **encapsulation.py** for demonstration.

 Let's understand the code:

The class name is Person as defined using the keyword class. The constructor initializes two
attributes (**name** and **age**) but the two arguments differ in accessibility:
 - The name attribute is public, meaning that it can be directly accessed outside the class.
 - The age attribute is private, evidenced by double underscore (**__age**), meaning that
 it cannot be directly access from the outside.
 - There is a **describe()** methode that describes the object of the class **Person**.
 - There is a public method **get_age()** that can access the private attribute __age. 
 This means that the only way to access the attribute __age from the outside is through this method.

### Inheritance

**Inheritance** is a mechanism that allows to inherit the attributes and methods of another
class. This helps to reuse code and establish relationships between classes.

 - **Parent (super) class**: The class being inherited from.
 - **Child (sub) class**: The class inheriting from the parent class.

Check out a code demonstrating this in the file **inheritance.py**

Let's understand the code:

 - **Dog** inherits from the class **Animal** so it has access to the attribute **name** and the
 method **speak**.
 - The **speak()** method in the class Dog overrides the one in the class Animal 
 allowing the dog to **bark** instead of making a generic sound. 

### Polymorphism

Polymorphism allows objects of different classes to be treated as objects of a common superclass.
This means that even if different classes implement the same method, Python knows which class to
call based on the object type.

Check out the code in **polymorphism.py** to understand it better.

Let's understand what has been done in the code. Even though both classes of **Dog** and **Cat** have a similar method **speak()**, Python knows how to call each one of method for each class separately and accordingly due to **polymorphism**.