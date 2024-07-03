# Object-Oriented Programming

## What is Object-Oriented Programming?

**Objects** are the real deal in object-oriented programming. An object is an **instance** of a **class**. A class presents to the outside world a concise and consistent view of the objects that are its instances in a simple and direct manner possible while not showing the inner workings of the objects or in this case its instances.

The definition of the class specifies **instance variables** which are also called **data members** that the object has and **methods**, which are also called **member functions**, that the object can execute.

### Object-Oriented Design Goals

Software implementations should achieve **robustness**, **adaptability** and **reusability**.

1. **Robustness**

This is the ability of software to handle unexpected inputs that are not explicitly defined for its application. For example, if a program is expecting a positive integer(perhaps representing the price of an item) and instead it is given a negative integer, then the program should be able to revocer gracefully from this error.

2. **Adaptability**

Software needs to be able to evolve over time in response to changing conditions in its environment. That is why adaptability, also known as **evolvability** is a very important goal of object-oriented design. Related to this concept is **portability**, which is the ability of software to run with minimal change on different hardware and operating system platforms. Python has a great advantage of being portable that is why it is very efficient in writing software.

3. **Reusability**

Software should be reusable, that is, the same code should be usable as a component of different systems in various applications. Developing quality software can be an expesive enterprise and its cost can be offset somewhat if the software is designed in a way that makes it easily reusable in future applications.

### Object-Oriented Design Principles

Below are the object-oriented design principles which intend ti facilitate the goals outlines above.

- Modularity
- Abstraction
- Encapsulation

1. **Modularity**

Modularity refers to an organizing principle in which different components of a software system are divided into separate functional units.

Using modularity in software system can also provide a powerful organizing framework that brings **clarity** to an implementation. In Python a **module** is a collection of closely related functions and classes that are defined together in a *single file* of source code. Python's standard libraries include, for example, the **math** module, which provides definitions for key mathematical constants and functions, and the **os** module, which provides support for interacting with the operating system.

The use of modularity helps support the object-oriented design goals. **Robustness** is greatly increased because it is easier to test and debug separate components before they are integrated into a larger software system. In addition to that, bugs created in an already complete system might be traced to a particular component, which can be solved on its own. Modularity also ensures a structure that supports software reusability.

2. **Abstraction**

The idea behind abstractio is to break a complicated system down to its most fundamental parts. Consequently, describing the parts of a system involves naming them and explaining thier functionality. The application of abstraction paradigm to the design on data structures gives the rise of **abstract data types** (ADTs). 

An ADT is a mathematical model of data structure that specifies the type of data stored, the operations supported on them and the types of parameters of the operations. An ADT specifies **what** each operation does but not **how** it does it. Here, we will typically refer to the collective set of behaviors supported by an ADT as its **public interface**