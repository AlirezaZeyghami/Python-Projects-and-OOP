# 🧠 Object-Oriented Programming — Decorators, Class Method, Static Method & Property

In this section, we will learn how to write **special methods in classes** that interact with data in different ways, without having to complicate the class structure.

---

## 🔹 What Are Decorators in Classes?

A **decorator** is simply a way to **modify or enhance** the behavior of a function or method — without changing its code directly.  
In classes, we have three commonly used types of decorators:

1. `@classmethod`
2. `@staticmethod`
3. `@property`

---

## 🧩 Example: `Employee` Class

```python
class Employee:
    salary = 4000
    total_employee = 0

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        Employee.total_employee += 1

    # -----------------------------
    # 📍 PROPERTY DECORATOR
    # -----------------------------
    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
    
    @fullname.setter
    def fullname(self, name):
        self.first_name, self.last_name = name.split(" ")

    @fullname.deleter
    def fullname(self):
        self.first_name = None
        self.last_name = None

    # -----------------------------
    # 📍 CLASS METHOD DECORATOR
    # -----------------------------
    @classmethod
    def raise_salary(cls, new_salary):
        if type(new_salary) == int:
            cls.salary = new_salary
        else:
            raise ValueError("Salary must be an integer!")

    @classmethod
    def create_from_string(cls, string):
        first_name, last_name = string.split("-")
        return cls(first_name, last_name)

    # -----------------------------
    # 📍 STATIC METHOD DECORATOR
    # -----------------------------
    @staticmethod
    def is_workday(day):
        if day.weekday() in (5, 6):  # 5 = Saturday, 6 = Sunday
            return False
        return True


# -----------------------------
# 🧪 Usage
# -----------------------------
emp_01 = Employee('Alireza', 'Zeyghami')
emp_02 = Employee('Samira', 'Azimi')

print(emp_02.fullname)               # Property getter
emp_02.fullname = "Mariam Malmir"    # Property setter
print(emp_02.fullname)
del emp_02.fullname                  # Property deleter
print(emp_02.fullname)

print("Before:")
print(emp_01.fullname, "-", emp_01.salary)
print(emp_02.fullname, "-", emp_02.salary)

Employee.raise_salary(8000)          # Class method

print("After:")
print(emp_01.fullname, "-", emp_01.salary)
print(emp_02.fullname, "-", emp_02.salary)

emp_03 = Employee.create_from_string("Alireza-Zeyghami")

import datetime
date = datetime.date(2025, 11, 1)
print(emp_03.is_workday(date))
print(emp_03.fullname)
```
# 🔍 Breakdown of Decorators
## 🧩 1. @property

Allows you to access methods like attributes.
Perfect for read-only or computed attributes.
```python
class Example:
    @property
    def info(self):
        return "This is a property."

obj = Example()
print(obj.info)  # No parentheses needed!
```
## ✅ You can also define:

@property → getter

@<property_name>.setter → setter

@<property_name>.deleter → deleter

## 🧠 Used when you want attribute-like access but still need logic behind it.

## 🧩 2. @classmethod

Works on the class itself, not the instance.
The first parameter is always cls, which refers to the class.
```python
class Employee:
    salary = 4000

    @classmethod
    def raise_salary(cls, amount):
        cls.salary = amount
```

### ✅ Use it when:

You want to modify class-level data (not instance-level).

You want to define alternative constructors like create_from_string().

### 🧩 3. @staticmethod

A static method belongs to the class logically,
but does not depend on the class or instance data.

class MathTool:
    @staticmethod
    def add(a, b):
        return a + b

### ✅ Use it when:

The method doesn’t use self or cls.

You just want a utility or helper function inside a class.

## 💡 Common Use Cases

| Use Case                               | Decorator       | Example          |
| -------------------------------------- | --------------- | ---------------- |
| Modify class attributes                | `@classmethod`  | `raise_salary()` |
| Perform logic not tied to any instance | `@staticmethod` | `is_workday()`   |
| Manage attributes like computed fields | `@property`     | `fullname`       |

## 🧠 Key Takeaways

✅ @property → Access methods like attributes
✅ @classmethod → Works with the class itself (cls)
✅ @staticmethod → Independent utility function
✅ Decorators make code cleaner, safer, and more Pythonic 🐍
