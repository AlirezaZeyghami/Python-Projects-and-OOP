# 🔁 Object-Oriented Programming — Polymorphism in Python

**Polymorphism (چندریختی)** یکی از چهار اصل اصلی شی‌گرایی (OOP) است.  
به معنی “چند شکلی” است؛ یعنی **یک متد یا رفتار یکسان می‌تواند در کلاس‌های مختلف به شکل متفاوتی عمل کند.**

---

## 🧠 Concept

> در Polymorphism، یک اینترفیس واحد برای انواع مختلف اشیاء عمل می‌کند.

به زبان ساده‌تر:  
می‌توانیم متدی با نام یکسان در چند کلاس مختلف داشته باشیم،  
ولی هرکدام کار مخصوص خودشان را انجام دهند.

---

## 🔹 Types of Polymorphism

| نوع | توضیح |
|-----|--------|
| **Overriding** | بازنویسی متد در کلاس فرزند (رایج‌ترین نوع در پایتون) |
| **Overloading** | تعریف چند متد با نام یکسان اما پارامترهای متفاوت (در پایتون واقعی نیست؛ با *args و **kwargs شبیه‌سازی می‌شود) |

---

## 🧩 Example — Method Overriding

در این مثال، هر کلاس رفتار خاص خودش از متد `say_hello()` را دارد.

```python
from abc import ABC, abstractmethod

# -----------------------------
# 🎯 Base Class
# -----------------------------
class Language(ABC):
    @abstractmethod
    def say_hello(self):
        pass


# -----------------------------
# 🌍 Subclasses
# -----------------------------
class Iranian(Language):
    def say_hello(self):
        return "Salam 🇮🇷"


class English(Language):
    def say_hello(self):
        return "Hello 🇬🇧"


# -----------------------------
# 🧪 Polymorphic Behavior
# -----------------------------
ali = Iranian()
arthur = English()

def execute_hello(obj):
    print(obj.say_hello())

execute_hello(ali)
execute_hello(arthur)
```
## 🔸 Output:
```
Salam 🇮🇷
Hello 🇬🇧
```
همون تابع execute_hello() برای دو نوع متفاوت از آبجکت‌ها (Iranian, English)
رفتار متفاوتی داره — یعنی Polymorphism به شکل کامل ✨

## 🧩 Example — Operator Overloading

در پایتون حتی می‌تونی عملگرها (مثل +, *, ==) رو هم بازتعریف (Overload) کنی
تا برای کلاس‌هات معنا پیدا کنن.
```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, other):
        return self.salary + other.salary

emp1 = Employee("Alireza", 4000)
emp2 = Employee("Mina", 3500)

print(emp1 + emp2)  # Output: 7500
```
این نمونه از Operator Overloading یکی از زیرمجموعه‌های Polymorphism است.

## 🧩 Example — Simulating Overloading

در پایتون متد Overloading به‌صورت واقعی وجود ندارد
(مثل جاوا یا C++)، اما می‌توان با آرگومان‌های پویا شبیه‌سازی‌اش کرد:
```python
class Math:
    def add(self, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            return a + b + c
        elif a is not None and b is not None:
            return a + b
        else:
            return a

math = Math()
print(math.add(3, 4))        # 7
print(math.add(3, 4, 5))     # 12
```
## 💡 Why Use Polymorphism?
| مزیت                        | توضیح                                                     |
| --------------------------- | --------------------------------------------------------- |
| 🔄 انعطاف‌پذیری بالا        | بدون تغییر در ساختار کلی، رفتارهای متفاوت قابل تعریف‌اند. |
| 🧩 گسترش‌پذیری              | می‌توان کلاس‌های جدید با رفتار خاص خودشان اضافه کرد.      |
| 🧼 خوانایی بیشتر            | کدها ساده‌تر و نزدیک‌تر به تفکر انسانی می‌شوند.           |
| 🧠 استفاده از اینترفیس واحد | توابع عمومی می‌توانند با اشیای متفاوت کار کنند.           |

## ✅ Summary
| Concept                  | Description                                  |
| ------------------------ | -------------------------------------------- |
| **Overriding**           | بازنویسی متد در کلاس فرزند برای رفتار متفاوت |
| **Overloading**          | استفاده از آرگومان‌های مختلف برای متد یکسان  |
| **Operator Overloading** | تغییر رفتار عملگرها برای اشیای سفارشی        |

## 🧩 Real-world Example

فرض کن در سیستم پرداختت کلاس‌هایی برای روش‌های مختلف پرداخت داری:
```python
class Payment:
    def pay(self, amount):
        raise NotImplementedError

class CreditCard(Payment):
    def pay(self, amount):
        return f"Paid {amount}$ via Credit Card 💳"

class PayPal(Payment):
    def pay(self, amount):
        return f"Paid {amount}$ via PayPal 🪙"

def process_payment(payment_obj, amount):
    print(payment_obj.pay(amount))

process_payment(CreditCard(), 50)
process_payment(PayPal(), 75)
```
تابع process_payment() بدون اینکه بدونه با چه نوع پرداختی کار می‌کنه،
از Polymorphism استفاده می‌کنه تا درست‌ترین متد رو اجرا کنه.
