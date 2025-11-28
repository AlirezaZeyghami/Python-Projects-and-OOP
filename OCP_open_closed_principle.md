# Open–Closed Principle (OCP)

**Open–Closed Principle** states that software entities such as classes, modules, and functions should be:

- **Open for extension** → new behavior can be added  
- **Closed for modification** → existing code should not need to change  

When code violates OCP, every new feature forces changes in the old logic, making the system fragile and harder to maintain.

---

## 🚫 A Bad Example (violating OCP)

```python
class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

animals = [
    Animal('lion'),
    Animal('mouse')
]

def animal_sound(animals: list):
    for animal in animals:
        if animal.name == 'lion':
            print('roar')
        elif animal.name == 'mouse':
            print('squeak')
```
Adding a new animal such as ```Snake``` forces you to modify the existing function:
```py
animals = [
    Animal('lion'),
    Animal('mouse'),
    Animal('snake')
]

def animal_sound(animals: list):
    for animal in animals:
        if animal.name == 'lion':
            print('roar')
        elif animal.name == 'mouse':
            print('squeak')
        elif animal.name == 'snake':
            print('hiss')
```
Every new type → new ```elif``` → constant modification → breaks OCP.

# ✅ A Better Design (respecting OCP)

Let each animal define its own behavior using polymorphism:
```py
class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

    def make_sound(self):
        pass


class Lion(Animal):
    def make_sound(self):
        return 'roar'


class Mouse(Animal):
    def make_sound(self):
        return 'squeak'


class Snake(Animal):
    def make_sound(self):
        return 'hiss'


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())
```
### Now:

* Adding a new animal → create a new class

* No need to touch existing code

* Core logic stays unchanged

The system becomes naturally extendable and stable.

## 🛒 Another Example: Discounts
## ❌ Wrong (violates OCP)
```py
class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        if self.customer == 'fav':
            return self.price * 0.2
        if self.customer == 'vip':
            return self.price * 0.4
```
Each new customer type requires modifying ```give_discount```.
As the system grows, this becomes unmanageable.

# ✅ Correct (OCP-friendly design)

Use inheritance and polymorphism:
```py
class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def get_discount(self):
        return self.price * 0.2
```

```py
class VIPDiscount(Discount):
    def get_discount(self):
        return super().get_discount() * 2
```

Now you can extend without modification:
```py
class SuperVIPDiscount(VIPDiscount):
    def get_discount(self):
        return super().get_discount() * 2
```
No original logic changes — new behavior is added only through extension.

# ✨ Why OCP Matters
| Benefit                  | Explanation                                                 |
| ------------------------ | ----------------------------------------------------------- |
| **Flexibility**          | New behaviors are added without touching the existing code. |
| **Stability**            | Reduces risk of breaking working components.                |
| **Scalability**          | Perfect for growing systems with many variants.             |
| **Cleaner architecture** | Encourages polymorphism and modular design.                 |

