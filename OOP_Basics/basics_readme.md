## What is OOP

Object Oriented Programming is a programming paradigm centered around the concepts of **objects** and **classes**. It allows you to model real word entities as objects in your code and enables you to organize structure your code better.

#### Four Core Principles of OOP

1. Encapsulation
2. Inheritance
3. Polymophism
4. Abstraction

We'll dive into those principles later, now let's start with the building blocks of OOP - **classes** and **objects**.

### Classes and Objects

A **class** is a **blueprint** or **template** of creating objects. It defines the **attributes** (data) and **methods** (functions) that the objects created from the class will have.

An **object** is an **instance** of a class. You can think of it as an example of the class with real world data. Check out an example Python program demonstrating how classes and objects are created in the file **class_objects.py**.

Let's understand the code:

1. **Class Definition**: We define a class called **Car** using the **class** keyword. Inside the class we have.
    - **Attributes**: **brand**, **model** and **year**. These describe the state of the class.
    - **Methods**: Functions inside a class. This method **describe()** provides a way to describe the car.

2. **Constructor (__init__)**: The __init__ method is a special method that initializes the objects when it is created. It takes **self** as the first argument which refers to the object itself. We then pass values to the attributes (**brand**, **model** and **year**).