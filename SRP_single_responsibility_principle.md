# Single Responsibility Principle (SRP)

**Single Responsibility Principle** — each class should have **only one responsibility** or one reason to change.  
If a class handles more than one responsibility, it creates tight coupling.  
When one behavior changes, you may have to change unrelated parts elsewhere — leading to fragile, hard-to-maintain code.

---

## 🚫 A Bad Example (violating SRP)

```python
class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name

    def save(self, animal: 'Animal'):
        # saves the object to a database
        pass
```
## Here, Animal has two responsibilities:

1. Representing an animal (its name, properties)

2. Persisting data (database storage)

```Animal``` If you later change how the database works or change class properties, all code that uses or inherits Animal will be affected.
This ripple effect makes code brittle and hard to extend.

# ✅ A Better Design (respecting SRP)

Split responsibilities into separate classes:
```py
class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name

class AnimalDB:
    def get_animal(self) -> Animal:
        # retrieve Animal from database
        pass

    def save(self, animal: Animal) -> None:
        # save the Animal to database
        pass
```
### Now:

```Animal``` handles only the animal data and behavior (its properties).

```AnimalDB``` handles only persistence (database operations).

This separation ensures that changes in DB logic or animal properties remain isolated — no unexpected side effects elsewhere.

## 🔁 Why SRP Matters
| Benefit             | Explanation                                                                     |
| ------------------- | ------------------------------------------------------------------------------- |
| **Maintainability** | When code has one responsibility, it’s easier to read, understand, and modify.  |
| **Loose Coupling**  | Different concerns (data model vs storage) stay separated, reducing dependency. |
| **Extensibility**   | You can change or replace one part (e.g. database) without touching others.     |
| **Testability**     | Smaller classes with a single responsibility are easier to test.                |
| **Reusability**     | Components with clear roles can be reused across projects.                      |

## 🛠️ Tips for Applying SRP

* Identify distinct responsibilities — data model, storage, logging, business logic, etc.

* Define separate classes for each concern.

* Keep class methods focused on a single task.

* Avoid mixing IO (database, network, file) with data domain logic in the same class.

* Favor composition over inheritance when combining behaviors.
