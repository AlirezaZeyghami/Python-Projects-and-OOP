# 🧠 Object-Oriented Programming — Abstraction in Python

**Abstraction (انتزاع)** یکی از چهار پایه‌ی اصلی شی‌گرایی است.  
هدف آن این است که **پیچیدگی داخلی** یک کلاس یا سیستم را پنهان کنیم  
و فقط **عملکردهای ضروری** را برای استفاده ارائه دهیم 💡  

---

## 🔹 What Is Abstraction?

در پایتون، Abstraction یعنی تعریف ساختار کلی (interface) بدون مشخص‌کردن جزئیات اجرایی.  
این کار معمولاً با **کلاس‌های Abstract** و **متدهای Abstract** انجام می‌شود.

---

## 🧩 Python Tools for Abstraction

برای پیاده‌سازی Abstraction از ماژول داخلی `abc` استفاده می‌کنیم:

```python
from abc import ABC, abstractmethod, abstractproperty
```
| مفهوم               | توضیح                                         |
| ------------------- | --------------------------------------------- |
| `ABC`               | کلاس پایه برای ساخت کلاس‌های Abstract         |
| `@abstractmethod`   | متدی که باید در کلاس‌های فرزند پیاده‌سازی شود |
| `@abstractproperty` | همان `@property` است، ولی برای متدهای انتزاعی |

## 🧱 Example: Abstract Base Class
from abc import ABC, abstractmethod, abstractproperty

```python
# -----------------------------
# 🎯 Abstract Class
# -----------------------------
class Person(ABC):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    # Abstract Method (must be implemented in child class)
    @property
    @abstractmethod
    def full_name(self):
        pass


# -----------------------------
# 🧩 Concrete Subclasses
# -----------------------------
class Employee(Person):
    salary = 4000

    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)


class Employer(Person):
    salary = 16000

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)


# -----------------------------
# 🧪 Usage
# -----------------------------
emp_01 = Employee("Alireza", "Zeyghami")
print(emp_01.full_name())   # Employee implements method

emp_02 = Employer("Fatemeh", "Zeyghami")
print(emp_02.full_name)     # Employer implements property
```
# 🧠 Key Concepts
## 🧩 1. Abstract Class

کلاسی است که نمی‌توان از آن مستقیم نمونه‌سازی (instantiate) کرد.
هدفش این است که پایه‌ای برای کلاس‌های دیگر باشد.
```python
p = Person("Ali", "Zeyghami")  # ❌ TypeError: Can't instantiate abstract class
```
## 🧩 2. Abstract Method

متدی است که فقط تعریف می‌شود ولی بدنه ندارد.
کلاس‌های فرزند باید آن را پیاده‌سازی کنند.
```python
@abstractmethod
def full_name(self):
    pass
```
اگر یکی از متدهای انتزاعی در کلاس فرزند پیاده‌سازی نشود،
پایتون اجازه ساخت شی از آن کلاس را نمی‌دهد.

## 🧩 3. Abstract Property

در واقع همان ترکیب @property و @abstractmethod است،
برای زمانی که می‌خواهیم یک property اجباری در کلاس‌های فرزند داشته باشیم.
```python
@abstractproperty
def full_name(self):
    pass
```
(در نسخه‌های جدید پایتون فقط از @property + @abstractmethod استفاده می‌شود.)

### 💡 Why Use Abstraction?
| مزیت             | توضیح                                                     |
| ---------------- | --------------------------------------------------------- |
| 🎯 ساختار منظم   | تمام کلاس‌های فرزند مجبور به پیاده‌سازی متدهای خاص هستند. |
| 🔒 امنیت و کنترل | جلوگیری از دسترسی مستقیم به پیاده‌سازی‌های داخلی.         |
| 🧩 توسعه‌پذیری   | افزودن یا تغییر کلاس‌ها بدون آسیب به بقیه سیستم.          |
| 📚 خوانایی بهتر  | به‌وضوح مشخص است که هر کلاس چه مسئولیتی دارد.             |

### ✅ Summary
| Concept             | Keyword / Decorator             | Description                       |
| ------------------- | ------------------------------- | --------------------------------- |
| Abstract Base Class | `ABC`                           | پایه‌ای برای ساخت ساختارهای مشترک |
| Abstract Method     | `@abstractmethod`               | الزام فرزندان به پیاده‌سازی       |
| Abstract Property   | `@property` + `@abstractmethod` | الزام property مشخص در subclasses |

## 🧩 Real-world Example

فرض کن در پروژه‌ای کلاس پایه‌ای برای وسایل نقلیه داری:
```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Airplane(Vehicle):
    def move(self):
        print("Flying ✈️")

v1 = Car()
v2 = Airplane()

v1.move()
v2.move()
```
* 🔹 هر کلاس فرزند روش مخصوص حرکت خودش را دارد
بدون اینکه ساختار کلی Vehicle به هم بخورد.
