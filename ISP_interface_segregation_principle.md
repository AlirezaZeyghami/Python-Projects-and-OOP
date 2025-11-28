# Interface Segregation Principle (ISP)

The **Interface Segregation Principle** states that:

> Clients should not be forced to depend on methods they do not use.

In other words:  
A class should never be required to implement unnecessary or irrelevant methods.

Large, general-purpose interfaces lead to messy class hierarchies and unnecessary complexity.  
Small, focused interfaces keep code clean, maintainable, and scalable.

---

## 🚫 A Violating Design (Bad Example)

Here, the interface `IShape` forces all classes to implement methods they do **not** need:

```python
class IShape:
    def draw_square(self):
        raise NotImplementedError
    
    def draw_rectangle(self):
        raise NotImplementedError
    
    def draw_circle(self):
        raise NotImplementedError
```
Now every subclass looks like this:
```py
class Circle(IShape):
    def draw_square(self):
        pass

    def draw_rectangle(self):
        pass
    
    def draw_circle(self):
        pass
```
And similarly for the ```Square``` and ```Rectangle``` classes.

❌ Problems:

* Each class must implement irrelevant methods.

* Many methods become empty (```pass```), which is a design smell.

* Violates ISP because clients depend on methods they don’t need.

* More boilerplate, more bugs, and difficult to maintain.

## 🚫 Still Wrong: Expanding the Interface

Even adding more methods only makes things worse:
```py
class IShape:
    def draw_square(self): ...
    def draw_rectangle(self): ...
    def draw_circle(self): ...
    def draw_triangle(self): ...
```
This inflates the interface, forcing every shape to deal with every method—regardless of relevance.

This is the opposite of ISP.

## ✅ Correct ISP-Compliant Design

Create a minimal, focused interface that expresses only one capability:
```py
class IShape:
    def draw(self):
        raise NotImplementedError
```
Now each shape defines its own drawing logic—clean, simple, reusable:
```py
class Circle(IShape):
    def draw(self):
        pass


class Square(IShape):
    def draw(self):
        pass


class Rectangle(IShape):
    def draw(self):
        pass
```

✔ No irrelevant methods
✔ No redundant logic
✔ No empty method definitions
✔ Easy to add new shapes
✔ Perfectly aligned with Interface Segregation Principle

## ✨ Why ISP Matters
| Benefit                 | Explanation                                           |
| ----------------------- | ----------------------------------------------------- |
| **Less coupling**       | Classes depend only on what they actually use.        |
| **More readable**       | Each interface is small, coherent, and meaningful.    |
| **Easier to maintain**  | Changing one interface won’t break unrelated classes. |
| **Cleaner hierarchies** | Subclasses only implement what’s truly relevant.      |

ISP encourages building small, specific interfaces instead of large, general-purpose ones.
