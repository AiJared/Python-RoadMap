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

Computing researchers and practitioners have developed a variety of organizational concepts and methodologies for designing quality object-oriented software that is concise, correct and reusable. There is the concept of **desgin pattern**, which describes s solution to a typical software design problem. A pattern provides a general template for a solution that can be applied in many different situations. It describes the main elements of a solution in an abstract way that can be specialized for a specific problem at hand. It consists of a **name** which identifies the patter, a **contenxt** which describes the scenarios for which this pattern can be applied, a **template** which describes how the pattern is applied and a **result** which describes and analyzes what the pattern produces.

The design patterns fall into two groups; patterns for solving *algorithm design problems* and patterns for solving *software engineering problems*

## Software Development

Traditional software development involves several phases. Three major steps are:

1. Design
2. Implementation
3. Testing and debugging

### 1. Design

In object-oriented programming, the design step is the most important phase in the process of developing software. It is at this phase that we decide how to divide the workings of our program into **classes**, how these classes will **interact**, what data each will **store** and what **actions** each will perform. There are some rules that can be applied when determining how to design classes:

- **Responsibilities**: Divide the work into different **actors**, each with a different responsiblity. Try to describe responsibilities using action verbs. These actions will form the classes for the program.

- **Independence**: Define the work for each class to be independent from other classes as possible. Subdivide responsibilities between classes so that each class has **autonomy** over some aspect of the program. Give data (as in stance variables) to the class that has jurisdiction over the actions that require access to this data.

- **Behaviors**: Define the behaviors for each class carefully and precisely, so that the consequences of each action performed by a class will be well understood by other classes that interact with it. These behaviors will define the methods that this class performs, and the set of behaviors for a class are the **interface** to the class, as these form the means for other pieces of code to interact with objects from the class.

Defining the classes, together with their instance variables and methods, are the key to the design on an object-oriented program.

One of the tools for developing an initial high-level design for a project is the use of **CRC cards**. Class-Responsibility-Collaborator (CRC) cards are simple index cards that subdivide the work required of a program. The main idea behind this is to have each card represent a component, which will ultimately become a class in the program. So we write the name of each component on the top of an index card. On the left side of the card, we begin writing the responsibilities for this component. On the right-hand side, we list the collaborators for this component, that is, the other components that this component will have to interact with to perform its duties.

The design process iterates through an **action/actor** cycle, where we first identify an action, that is, a **responsibility** and then we determine an actor, that is, a **component** that is best suited to perform that action. The design is complete when we have assigned all actions to actors. In using index cards for this process rather than larger pieces of paper, we are relying on the fact that each component should have a small set of responsibilities and collaborators. Enforcing this rule helps keep the individual classes manageable.

As the design takes form, a standard approach to explain and document the design in the use of **Unified Modeling Language (UML)** diagrams to express the organization of a program. UML diagrams are a standard visual notation to express object-oriented software designs. Several computer-aided tools are available to build UML diagrams. One type of UML is known as **class diagram**. An example is a consumer credit card class diagram that has three portions, with the first designated the *name of the class*, the second designated the recommended *instance variables* and the third designated the recommended *methods of the class*. 

## Class Definitions

A class is the primary means for **abstraction** in oop. I Python, every piece of data is representef ad an instance of some class. A class provides a set of behaviors in the form of **member functions** also know an **methods**, with implementations that are common to all instances of that class. A class also serves as a **blueprint** for each instance is represented in the form of **attributes** (also known as **fields**, **instance variables** or **data members**).

## Example: CreditCard Class

Based on the design described above, we are going to implement in a program (Python class) for credit card. The instances defined by the CreditCard class provide a simple model for traditional credit cards. They have identifying information about the **customer**, **bank**, **account number**, **credit limit**, and **current balance**. The class restricts charges that would cause a card's balance to go over its spending limit, but it does not charge **interest** or **late payments**.

The construct begins with the keyword **class**, followed by the **name** of the class, a **colon** and then an **indented block of code** of the class. The body includes definitions for all methods of the class. These methods are defined as **functions** yet with special parameters named **self**, that serves to identify the particular instance upon which a member is invoked.

### The self Identifier

In a Python class, the **self** identifier plays a very important role. In the context of the CreditCard class, there can presumably be many different **instances**, and each must maintain its own **balance**, its own **credit limit** and so on. Therefore, each instance stores its own instance variables to reflect its current state.

Syntactically, self identifies the instance upon which a method is invoked. For example, assume that a user of our class has a variable, **my_card**; that identifies an instance of the CreditCard class. When the user calls **my_card.get_balance()**, identifier **self**, within the definition of the get_balance method, refers to the card known as my_card by the caller. The expression **self._balance** refers to an instance variable, named **_balance**, stored as part of that particular credit card's state.

Check the pseudocode for the credit card class in the file **credit_card_class.txt**.

Then check the actual in the file **credit_card_class.py**.

We draw attention to the difference between the method signature as declared within the class versus that used by a caller. For example, from a user's perspective we have seen that the **get_balance** method takes zero parameters, yet within the class definition, **self** is an explicit parameter. Likewise, the charge method is declared within the class having two parameters (self and price), even though this method is called with one parameter, for example, as my_card.charge(200). The interpretter automatically binds the instance upon which the method is invoked to the self paramter. 

### The Constructor

A user can create an instance of the CreditCard class using a syntx as: 

*cc = CreditCard('Jared Otieno', 'Co-operative bank', '5522 4433 6611 7788', 100)*

Internally this results in a call to the specifically named **__init__** method that serves as the **constructor** of the class. Its key job is to establish the state of a newly created credit card object with appropriet instance variables. In the case of of the CreditCard class, each object maintains five instance variables, which we name: **_customer, _bank, _account, _limit and _balance**. The initial values for the first four of those five are provided as explicit parameters that are sent by the user when instantiating the credit card, and assigned within the body of the constructor. For example, the command **self._customer = customer**, assigns the instance variable self._customer to the parameter customer; note that because customer is **unqualified** on the right-hand side, it refers to the parameter in the local namespace.

### Encapsulation

By convention, a single leading underscore in the name of a data member, such as **_balance** implies that it is intended as **nonpublic**. Users of a class should not dirrectly access such members.

As a general rule, we will treat all data members as nonpublic. This allows us to better enforce a consistent state for all instances. We can provide accessors, such as get_balance, to provide a user of our class **read-only** access to a trait. If we wish to allow the user to change the state, we can provide appropriate update methods. In the context of data structures, encapsulating the internal representation allows us greater flexibility to redesign the way a class works, perhaps to improve the efficiency of the structure.

### Additional Methods

The most interesting behaviors in our class are **charge** and **make_payment**. The charge function typically adds the given price to the credit card balance, to reflect a purchase of said price by the customer. However, before accepting the charge, our implementation verifies that the new purchase would not cause the balance to exceed the credit limit. The **make_payment** charge reflects the customer sending payment to the bank for the given amount, thereby reducing the balance on the card. We note that in the command, *self._balance -= amount*, the expression self._balance is qualified with the self identifier because it represents an instance variable of the card, while the unqualified amount represents the local parameter.

### Error Checking

The CreditCard implementation is not particularly robust. First, we note that we did not explicitly check the types of the parameters to charge and make_payment, nor any of the parameters to the constructor. If a user were to make a call such as **visa.charge('candy')**, our code would presumably crash when attempting to add that parameter to the current balance. If this class were to be widely used in a library, we moght use more rigorous techniques to raise **TypeError** when facing such misuse.

Apart from the type errors, the implementation may be susceptible to logical errors. For example, if a user were allowed to charge a negative price, such as **visa.charge(-300)**, that would serve to **lower** the customer's balance. This provides a loophole for lowering a balance without making a payment. Of course, this might be considered valid usage if modeling the credit received when a customer returns merchanise to a store.

### Testing the Class

These tests are enclosed within a condition, **if __name__ == '__main__'**, so that they can be embedded in the source code with class definition.
These tests provide **method coverage**, as each of the methods is called at least once, but it does not provide **statement converage**, as there is never a case in which a charge is rejected due to te credit limit. This is not a particularly advances form of testing as the output of the given tests must be manually audited in order to determine whether the class behaved as expected. Python has tools for formal testing so that resulting values can be automatically compared to the predicted outcomes, with output generated only when an error is detected.

### Operator Overloading and Python's Special Methods

Python's built-in classes provide natural semantics for many operators. For example, the syntax a + b invokes **addition** for numeric types, yet **concatenation** for sequence types. When defining a new class, we must consider whether a syntax like a + b should be defined when a or b is an instance of that class.

By default, the + operator is undefined for a new class. However, the author of a class may provide a definition using a technique known as **operator overloading**. This is done by implementing a specially named method. In particular, the + operator is overloaded by implementing a method named **__add__**, which takes the right-hand operand as a parameter and which returns the result of the expression. That is, the sytanx, a + b, is converted to a method call on object of the form, **a__add__(b)**. Similar specially named methods exist for other operators.

When a binary operator is applied to two instances of different types, as in 3 * 'love me', Python gives deference to the class of the **left** operand. In this example, it would effectively check if the int class provides sufficient definition for how to multiply an instance by a string, via the **__mul__** method. However, if that class does not implement such a behavior, Python checks the class definition for the right-hand operand, in the form of a special method named **__rmul__**, that is, **right multiply**. This provides a way for a new **user-defined** class to support mixed operations that involve an instance of an existing class (given that an existing class would presumably not have defined a behavior involving this new class). The distinction between __mul__ and __rmul__ also allows a class to different semantics in cases, such as **matric multiplication**, in which an operation is **noncummulative**, that is, A * x may differ from x * A.

#### Non-Operator Overloads

In addition to traditional operator overloading, Python relies on specially named methods to control the behavior of various other functionality, when applied to user-defined classes. For example, the syntax, **str(foo)**, is formally a call to the constructor for the string class. Of course, if the parameter is an instance of a user-defined class, the original authors of the string class could not have known how that instance should be portrayed. So the string constructor calls a specially named method, **foo.__str__()**, that must return an appropriate string representation. 

Similar special methods are used to determine how to construct an **int**, **float** or **bool** based on a parameter from a user-defined class. The conversion to a Boolean value is particularly importance because the syntax, **if foo:,** can be used even when foo is not formally a Boolean value. For a user-defined class, that condition is evaluated by the special method **foo.__bool__()**.

Several other top-level functions rely on calling specially named methods. For example, the standard way to determine the size of a container type is by calling the top-level len function. Note well that the calling syntax, **len(foo)** is not the traditional method-calling syntax with the dot operator. However, in the case of a user-defined class, the top-level len function relies on a call to a specially named __len__ method of that class. That is, the call len(foo) is evaluated through a method call, foo.__len__(). When developing data structures, we will routinely define the __len__ method to return a measure of the size of the structure.

#### Implied Methods

If a particular special method is not implemented in a user-defined class, the standard syntax that relies upon that method will raise an **exception**. For example, evaluating the expression, a + b, for instances of a user-defined class without __add__ or __radd__ will raise an error.

There are some operators that have default definitions provided by Python, in the absence of special methods and there are some operators whose definitions are derived from others. For example, the __bool__ method, which supports the syntax **if foo:,** has default semantics so that every object other than None is evaluated as True. However, for container types, the __len__ method is typically defined to return the size of the container. If such a method exists, then the evaluation of bool(foo) is interpreted by default to be True for instances with nonzero length, and False for instances with zero length, allowing a syntax such as **if waitlist:** to be used to test whether there are one more entries in the waitlist.

If a container class provides implementations for both __len__ and __getitem__, a default iteration is provided automatically. Furthermore, once an iterator is defined, default functionality of __contains__ is provided.

The expression *a is b* evaluates whether the identifiers a and b are **aliases** for the same object. The expression a == b is testing a notion of whether the two identifiers reference **equivalent** values. The notion of **equivalence** depends upon the context of the class, and semantics is defined with the __eq__ method. However, if no implmentation is given for __eq__, the syntax a == b is legal with semantics of a is b, that is, an instance is equivalent to itself and no others. 

You should be aware that some natural implications are not automatically provided by Python. For example, the __eq__ method supports syntax a == b, but providing that method does not affect the evaluation of syntax a != b. The __ne__ method should be provided, typically returning **not(a == b)** as a result. Similarly providing a __lt__ method supports syntax a < b and indirectly b > a, but providing both __lt__ and __eq__ does not imply semantics for a == b.

**Example: Multidimensional Vector Class**

To demonstrate the use of *operator overloading* via *special methods*, let's look at an implementation of a **Vector class** representing the coordinates of a vector in a **multideimentional space**. For example, we might wish to represent a vector with coordinates (5, -2, 3). Although it might be tempting to directly use Python list to represent those coordinates, a list does not provide an appropriate **abstraction** for a geometric vector. In particular, if using lists, the expression [5, -2, 3] + [1, 4, 2] results in the list [5, -2, 3, 1, 4, 2]. When working with vectors, if u=(5, -2, 3) and v = (1, 4, 2), one would expect the expression u + v to return a 3D vector with coordinates (6, 2, 5).

We therefore define a vector class that provides a better abstraction for the notion of a geometric vector. Internally, our vector relies upon an instance of a list, **_coords**, as its **storage mechanism**. By keeping the internal list **encapsulated**, we can enforce the desired public interface for instances of our class. A demonstration of supported behaviors invludes the following:

v = Vector(5) # construct 5D <0,0,0,0,0>

v[1] = 23 # <0,23,0,0,0>(based on use of __setitem__)

v[-1] = 45 # <0,23,0,0,45>(also via __setitem__)

print(v[4]) # output 45 (via __getitem__)

u = v + v # <0,46,0,0,90> (via __add__)

print(u) # output <0, 46, 0, 0, 90> via (__add__)

total = 0 

for entry in v: # implicit iteration via __len__ and __getitem__

    total += entry

We implement many of the behaviors by trivially invoking a similar behavior on the underlying list of coordinates. However, our implementation of __add__ is customized. Assuming the two operands are vectors with the same length, this method creates a new vector and sets the coordinates of the new vector to be equal to the respective sum of the operands' elements.

It is important to note that the class definition automatically supports the syntax u = v + [5, 3, 10, -2, 1], resulting in a new vecotr that is **element-by-element** "sum" of the first vector and the list instance. This is a result of Python's **Polymorphism**. Literally, polymorphism means many forms. Although it is tempting to think of the other parameter of our __add__ method as another vector instance, we never declared it as such. Within the body, the only behaviors we rely on for parameter other is that it supports len(other) and access to other[j]. Therefore, the code executes when the right_hand operand is a list of numbers (with matching length).

### Iteration

Iteration is an important concept in the design of data structures. an **iterator** for a collection provides one key behavior: It upports a special method named **__next__** that returns the next element of the collection if any or raises a **StopIteration** exception to indicate that there are no further elements.

Fortunately, it is rare to have to directly implement an iterator class. The preferred approach is the use of the **generator** syntax which automatically produces an iterator of yielded values.

Python also helps by providing an automatic iterator implementation for any class that defines both __len__ and __getitem__. To provide an instructive example of a low-level iterator, the code in the file **sequence_iterator.py** demonstrates such an iterator class that works on any collection that supports both __len__ and __getitem__. This class can be instantiated as **SequenceIterator(data)**. It operates by keeping an internal reference to the data sequence, as well as a current index into the sequence. Each time __next__ is called, the index is incremented, until reaching the end of the sequence.

#### Example: The Range Class

Prior to Python 3 being released, range was implemented as a function and it returned a list instance with elements in the specified range. For example **range(2,10,2)** returned the list [2,4,6,8]. However, a typical use of the function was to support a **for-loop syntax**, such as **for k in range(100000000)**. Unfortunately, this caused the instantiation and initialization of a list with the range of numbers. That was an unnecessary expensive step, in terms of both **time** and **memory** usage.

The mechanism used to support range in Python is entirely different (though it existed in Python 2 under the name **xrange**). It uses a strategy known as **lazy evaluation**. Rather than creating a new list instance, range is a class that can effectively represent the desired range of elements without ever storing them explicitly in memory. To better explore the built-in range class it is recommended to create an instance as *r = range(8,140,5)*. The result is a relatively **lightweight** object, an instance if the range class, that has only a few behaviors. The syntax *len(r)* will report the number of elements in the range (27 in this example). A range also supports the __getitem__ method, so that syntax r[15] reports the sixteenth element (as r[0] is the first element). Because the class supports both __len__ and __getitem__, it inherits automatic support for iteration which is why it is possible to execute a *for loop* over a range.

The code in the file **range.py** provides a class named **Range** (so as to clearly differentiate it from **built-in** range). The biggest challenge in the implementation is properly computing the number of elements that belong in the range, given the parameters sent by the caller when constructing a range. By computing that value in the constructor and storing it as **self._length**, it becomes trivial to return it from the __len__ method. To properly implement a call to __getitem__(k), we simply take the starting value of the range plus k times the step size (i.e., for k=0, we return the start value). There are a few subtleties worth examining in the code:

- We compute the number of elements in the range as *max(0, (stop - start + step - 1) // step). It is worth testing this formula for both positive and negative step sizes.

- The __getitem__ method properly supports negative indices by converting an *index - k* to *len(self) - k* before computing result.

### Inheritance

A natural way to organize various structural components of a software package is in a **hierarchical** fashion, with similar abstract definitions grouped together in a *level-by-level* manner that goes from specific to more general as one traverses up the hierarchy.
An example is that of a building. Using mathematical notations, the set of houses is a **subset** of the set of buildings, but a **superset** of the set of ranches. The correspondence between levels is often referred to as a **relationship** as a house is a building and a ranch is a house.

A hierarchical design is useful in software development, as common functionilty can be grouped at the most general level, thereby promoting reuse of code, while differentiated behaviors can be viewed as extensions of the general case, In object-oriented programming, the mechanism for a modular and hierarchical organization is a technique known as **inheritance**. This allows a new class to be defined based upon an existing class as the starting point. In object-oriented terminology, the existing class is typically described as the **base class**, **parent class**, or **super class**, while the newly defined class is known as the **subclass** or **child class**.