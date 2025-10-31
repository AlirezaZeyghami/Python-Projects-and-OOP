# 🧬 Object-Oriented Programming — Inheritance in Python

Inheritance allows a class (called **child** or **subclass**) to inherit attributes and methods from another class (called **parent** or **superclass**).  
It’s one of the most powerful features of OOP because it promotes **code reuse**, **hierarchical relationships**, and **extensibility**.

---

## 🔹 Types of Inheritance

| Type | Description |
|-------|-------------|
| **Single Inheritance** | A subclass inherits from a single parent class. |
| **Multi-Level Inheritance** | A class inherits from another derived class (like a chain). |
| **Multiple Inheritance** | A class inherits from more than one parent class. |
| **Hierarchical Inheritance** | Multiple subclasses inherit from the same parent class. |

---

## 🧱 Example 1: Single Inheritance

```python
# 👤 Person class
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


# 👨‍💼 Employee inherits from Person
class Employee(Person):
    salary = 4000

    def __init__(self, first_name, last_name, position):
        # Using super() to call parent constructor
        super().__init__(first_name, last_name)
        self.position = position

    def job(self):
        return f"I am {self.first_name} {self.last_name}, {self.position}"
```
# Explanation:
```text
Employee inherits all properties and methods from Person.

The super() function calls the parent’s __init__() so attributes are initialized properly.

Employee adds its own properties (position, salary) and methods (job()).
```
# 🧩 Example 2: Multi-Level Inheritance
```text
We can extend inheritance like a chain — for example, a CTO can inherit from Employee, which itself inherits from Person.
```
```python
# 👑 CTO inherits from Employee (multi-level)
class CTO(Employee):
    salary = 8000

    def __init__(self, first_name, last_name, position):
        super().__init__(first_name, last_name, position)

    def job(self):
        return f"I am {self.first_name} {self.last_name}, CTO of the company."
```
# ⚙️ Example 3: Multiple Inheritance
```text
Python supports multiple inheritance, where a class can inherit from multiple parents.
This is powerful but should be used carefully to avoid ambiguity (handled via MRO — Method Resolution Order).
```
```python
# 👔 Manager class
class Manager:
    def authority(self):
        return "Can hire and fire anyone."


# 👑 CTO inherits from Employee and Manager
class CTO(Employee, Manager):
    salary = 8000

    def __init__(self, first_name, last_name, position):
        super().__init__(first_name, last_name, position)

    def job(self):
        return f"I am {self.first_name} {self.last_name}, CTO of the company."
```
# ✅ Here:
```text
CTO gets both job() from Employee and authority() from Manager.

Python determines which parent’s method to use using MRO (Method Resolution Order).

You can check it like this:
```
```python
print(CTO.__mro__)
```
## Output:
```kotlin
(<class '__main__.CTO'>, <class '__main__.Employee'>, <class '__main__.Person'>, <class '__main__.Manager'>, <class 'object'>)
```
# 🌱 Example 4: Hierarchical Inheritance
```text
Several subclasses can share the same parent.
```
```python
# 🧑‍💻 Intern also inherits from Employee
class Intern(Employee):
    salary = 2000

    def job(self):
        return f"I am {self.first_name} {self.last_name}, a learner of new skills."
```
## 🧠 Example Usage
```python
emp_1 = Employee('Alireza', 'Zeyghami', 'Product Manager')
print(emp_1.job())
print(emp_1.salary)

emp_2 = CTO('Alireza', 'Zeyghami', 'Product Manager')
print(emp_2.job())
print(emp_2.salary)
print(emp_2.authority())

emp_3 = Intern('Alireza', 'Zeyghami', 'Software Engineer')
print(emp_3.job())
print(emp_3.salary)
```
## 🖨️ Output:
```css
I am Alireza Zeyghami, Product Manager
4000
I am Alireza Zeyghami, CTO of the company.
8000
Can hire and fire anyone.
I am Alireza Zeyghami, a learner of new skills.
2000
```
# 🧩 Summary
| Type             | Example                              | Key Idea                       |
| ---------------- | ------------------------------------ | ------------------------------ |
| **Single**       | `Employee(Person)`                   | One parent                     |
| **Multi-Level**  | `CTO(Employee)`                      | Parent → Child → Grandchild    |
| **Multiple**     | `CTO(Employee, Manager)`             | Multiple parents               |
| **Hierarchical** | `Intern(Employee)` & `CTO(Employee)` | One parent → multiple children |

# 💡 Notes
```text
Always use super() to initialize parent attributes.

Use __mro__ to inspect the method resolution order.

Prefer composition over deep inheritance trees when possible.

Avoid naming conflicts in multiple inheritance.
```
