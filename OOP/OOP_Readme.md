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

Python has a tradition of handling abstraction implicitly using a mechanism known as **duck typing** As an interpreted and dynamically typed language, there is no **compile time** checking of data types in Python, and no formal requirement for declarations of abstract base classes. Instead programmers assume that an object supports a set of known behaviors, with the interpreter raising a **runtime error** if those assumptions fail. The description of this as duck typing comes from an adage attributed to poet James Whitcomb Riley, stating that "When I see a bird that walks like a duck and swims like a duck and quacks like a duck, I cal that bird a duck."

Python supports abstract data types using a mechanism known as **abstract base class** (ABC). An abstract base class cannot be instantiated, that is, you cannot directly create an instance of that class, but it defines one or more common methods that all implementations of the abstraction must have. An ABC is realized by one or more **concrete classes** that inherit from the abstract base class while providing implementations for those methods declared by the ABC. Python's ABC module provides formal support for ABCs, although we omit such such declarations for simplicity. 

3. **Encapsulation**

Different components of a software system should not show the internal information of their respective functionality. Encapsulation gives the programmer an advantage of a freedom to implement details of a component, without concern that other programmers will be writing code that intricately depends on those internal decisions. The only constraint on the programmer of a component is to maintain the public interface for the component, as other programmers will be writing code that depends on that interface. Encapsulation achieves robustness and adaptability, for it allows the implementation details of parts of a program to change without adversely affecting other parts, thereby making it easier to fix bugs or add new features with relatively local changes to a component.

By convention, names of members of a class (both data members and member functions) that start with a single underscore character(_secret) are assumed to be nonpublic and should not be relied upon. Those conventions are reinforced by the intentional omission of those members from automatically generated documentation.