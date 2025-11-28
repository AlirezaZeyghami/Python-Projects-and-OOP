# Liskov Substitution Principle (LSP)

**Liskov Substitution Principle** states that objects of a subclass should be usable in place of objects of their superclass **without altering the correctness or expected behavior** of the program.

In simple terms:  
> A child class must be fully substitutable for its parent class.

If substituting a subclass breaks the logic, then the design violates LSP.

---

## 🚫 A Bad Example (violating LSP)

```python
def animal_leg_count(animals: list):
    for animal in animals:
        if isinstance(animal, Lion):
            print(lion_leg_count(animal))
        elif isinstance(animal, Mouse):
            print(mouse_leg_count(animal))
        elif isinstance(animal, Pigeon):
            print(pigeon_leg_count(animal))
```

Issues:

* The function needs to know every subclass (Lion, Mouse, Pigeon).

* Adding a new animal requires modifying this function.

* Strong coupling between logic and subclass types.

* Breaks LSP and OCP simultaneously.

This design will not scale as the number of animal types grows.

## ✅ Correct LSP-Compliant Design

Let each subclass define how many legs it has.
The parent defines the interface; children implement their own behavior.
```py
def animal_leg_count(animals: list):
    for animal in animals:
        print(animal.leg_count())
```

Now:

* The function does not care about the concrete type.

* Any subclass with a valid ```leg_count()``` method works seamlessly.

* No conditional logic.

* Fully respects the Liskov Substitution Principle.

## ✨ Why This Works

As long as each subclass preserves the expectations defined by the parent class, substitution becomes safe.

### Key rules for LSP:
| Rule                          | Meaning                                                                   |
| ----------------------------- | ------------------------------------------------------------------------- |
| **Behavioral consistency**    | The child should not change the meaning of the parent’s behavior.         |
| **No stronger preconditions** | Child methods must not require more than the parent’s contract.           |
| **No weaker postconditions**  | Child methods must meet at least what the parent promises.                |
| **Interface fidelity**        | Child classes must implement the parent interface in a compatible manner. |

If any subclass violates these rules, replacing the parent with the child could break the program — violating LSP.

# 🐾 Example Structure (Informal)
```py
class Animal:
    def leg_count(self):
        raise NotImplementedError


class Lion(Animal):
    def leg_count(self):
        return 4


class Mouse(Animal):
    def leg_count(self):
        return 4


class Pigeon(Animal):
    def leg_count(self):
        return 2
```

With this structure:
```py
animal_leg_count([Lion(), Mouse(), Pigeon()])
```
works flawlessly — without modification — regardless of how many child classes you add.

## Benefits of Following LSP
| Benefit            | Explanation                                                  |
| ------------------ | ------------------------------------------------------------ |
| **Extensibility**  | New subclasses can be added without touching existing logic. |
| **Predictability** | Behavior stays consistent when replacing parent with child.  |
| **Reduced bugs**   | Eliminates conditional logic based on type checking.         |
| **Cleaner APIs**   | Encourages designing clear interfaces and contracts.         |

