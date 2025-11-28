# Dependency Inversion Principle (DIP)

The **Dependency Inversion Principle** states that:

> High-level modules should not depend on low-level modules.  
> Both should depend on abstractions.

This principle helps reduce tight coupling between components and increases flexibility, allowing systems to adapt to changes without breaking core logic.

---

## 🚫 A Violating Design (Bad Example)

In this version, the high-level class `Http` directly depends on the low-level service `XMLHttpService`:

```python
class XMLHttpService(XMLHttpRequestService):
    pass


class Http:
    def __init__(self, xml_http_service: XMLHttpService):
        self.xml_http_service = xml_http_service
    
    def get(self, url: str, options: dict):
        self.xml_http_service.request(url, 'GET')

    def post(self, url: str, options: dict):
        self.xml_http_service.request(url, 'POST')
```
## ❌ Problems:

```Http``` is tightly coupled to ```XMLHttpService```.

Replacing the underlying transport (e.g., switching from XMLHttp to Fetch, gRPC, Requests, etc.) requires modifying the high-level module.

High-level behavior becomes dependent on specific low-level implementations.

Violates DIP because the direction of dependency is reversed.

## ✅ DIP-Compliant Design (Correct Approach)

The goal is to invert the dependency so that both classes depend on an abstraction (interface-like contract), not each other.

## Step 1: Create an abstraction for all connection types:
```py
class Connection:
    def request(self, url: str, options: dict):
        raise NotImplementedError
```
This abstract class defines only the core behavior every connection must provide.

### Step 2: The high-level module depends on abstraction, not concrete classes:
```py
class Http:
    def __init__(self, http_connection: Connection):
        self.http_connection = http_connection
    
    def get(self, url: str, options: dict):
        self.http_connection.request(url, 'GET')

    def post(self, url: str, options: dict):
        self.http_connection.request(url, 'POST')
```
Now the high-level class no longer cares which connection is used.
Any connection that implements ```request()``` will work.

## Step 3: Create concrete low-level modules independently
For example:
```py
class XMLHttpService(Connection):
    def request(self, url: str, options: dict):
        # Implementation of XMLHttpRequest
        pass
```
Or maybe a new connection:
```py
class FetchService(Connection):
    def request(self, url: str, options: dict):
        # Implementation using Fetch API
        pass
```
Or even a Python backend:
```py
class RequestsService(Connection):
    def request(self, url: str, options: dict):
        # Implementation using python-requests
        pass
```
## 🎯 Why This Design Is Better
| Benefit          | Explanation                                                                              |
| ---------------- | ---------------------------------------------------------------------------------------- |
| **Low coupling** | High-level code does not depend on concrete low-level classes.                           |
| **Extendable**   | New connection types can be added without touching `Http`.                               |
| **Testable**     | Easy to mock the `Connection` interface for unit testing.                                |
| **Flexible**     | Switching between network layers or protocols requires zero changes in high-level logic. |

This is the essence of DIP:
Abstractions should not depend on details. Details should depend on abstractions.
