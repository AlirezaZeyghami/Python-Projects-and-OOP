# 🧱 Object-Oriented Programming (OOP) in Python

Object-Oriented Programming (OOP) is a paradigm where software is organized around **objects** — entities that combine data and behavior.  
Python, being a fully object-oriented language, allows you to design and implement OOP concepts easily and naturally.

---

## 🔹 Base Concepts of OOP

| Concept | Description |
|----------|--------------|
| **Object** | A real-world entity with attributes (data) and methods (behavior). |
| **Class** | A blueprint or template used to create objects. |
| **Attributes** | Variables inside a class (properties of an object). |
| **Methods** | Functions inside a class (behaviors of an object). |

---

## 🔸 Main Principles of OOP

| Principle | Meaning |
|------------|----------|
| **Abstraction** | Hiding complex details and showing only the necessary parts. |
| **Inheritance** | Creating new classes from existing ones to reuse code. |
| **Encapsulation** | Keeping data safe from outside interference. |
| **Polymorphism** | Allowing methods or operations to behave differently based on the object type. |

---

## 🧩 Class and Object in Python

Everything in Python is an **object**.  
Each object is an instance of a **class**, which defines how that object behaves.

```python
class Employee:
    salary = "4000 $"  # class variable

    def __init__(self, name, age):
        self.name = name        # instance (object) variable
        self.age = age

    def hello(self):            # instance method
        return "Hello"

    @staticmethod
    def hi():                   # class (static) method
        return "Hi"

    def work(self, project_name):
        return f"Working on {project_name}"

    def introduce(self):
        return f"Hi, I'm {self.name}"

    # Dunder (Magic) Methods
    def __str__(self):
        return "This is an Employee object"

    def __repr__(self):
        return self.__class__.__name__

    def __add__(self, other):
        return self.age + other.age
```
# ⚙️ Creating and Using Objects
```python
emp1 = Employee("Alireza", 34)
emp2 = Employee("Mina", 32)

print(emp1)                # Calls __str__()
print(repr(emp1))          # Calls __repr__()
print(emp1 + emp2)         # Calls __add__()

print(emp1.hello())        # Instance method
print(Employee.hi())       # Static method
print(emp1.work("Django Blog"))
print(emp1.introduce())
```
## 🧠 Explanation:
```text
__init__: Initializes object attributes (called automatically when you create an instance).

__str__: Defines how the object is represented as a string.

__repr__: Returns a developer-friendly representation.

__add__: Overloads the + operator to work with objects.
```
# ⚡ Magic (Dunder) Methods

**Python allows you to customize built-in operations using magic methods, also called dunder methods (double underscore methods).**

| Magic Method | Description                       | Example                                 |
| ------------ | --------------------------------- | --------------------------------------- |
| `__init__`   | Called when an object is created. | `emp1 = Employee("Alireza", 34)`        |
| `__str__`    | Defines what `print(obj)` shows.  | `print(emp1)`                           |
| `__repr__`   | Developer view of an object.      | `repr(emp1)`                            |
| `__add__`    | Customizes the `+` operator.      | `emp1 + emp2`                           |
| `__len__`    | Defines `len(obj)` behavior.      | `len("Hello")` → `str.__len__("Hello")` |
| `__mul__`    | Customizes the `*` operator.      | `"Hi" * 3` → `str.__mul__("Hi", 3)`     |

## 🧠 Additional Notes
```text
Instance Variable: Belongs to a specific object.

Class Variable: Shared among all instances.

Instance Method: Works with object data (self).

Static/Class Method: Doesn’t depend on an object — often used for utility functions.
```
## 💡 Example — Custom Dunder Usage
```python
print(1 * 4)                # 4
print("1" * 4)              # "1111"
print(int.__mul__(1, 4))    # 4
print(str.__mul__("1", 4))  # "1111"

print(len("Hello"))         # 5
print(str.__len__("Hello")) # 5
```
## 🧭 Summary
| Concept       | Example                        | Description          |
| ------------- | ------------------------------ | -------------------- |
| Class         | `class Employee:`              | Blueprint            |
| Object        | `emp1 = Employee("Ali", 30)`   | Instance             |
| Method        | `emp1.work()`                  | Behavior             |
| Dunder Method | `__add__`, `__str__`           | Operator Overloading |
| Inheritance   | `class Manager(Employee): ...` | Reuse logic          |

## 📘 Pro Tip:
**Try adding more magic methods to your class — like __len__, __eq__, or __lt__ — to understand how Python handles custom objects behind the scenes!**
