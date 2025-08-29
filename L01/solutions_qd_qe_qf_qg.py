# Solutions for Qd, Qe, Qf, Qg - Simple and Clean

# =============================================================================
# Qd: Python Modules and Packages Howto
# =============================================================================

# Directory structure:
# mymodule/
#   __init__.py (makes it a package)
#   utils.py (module with functions)

# Import methods:
import sys
import os
sys.path.append(os.getcwd())  # Add current directory to path
from mymodule import utils    # Import module

# Alternative imports:
# import mymodule.utils as utils
# from mymodule.utils import say_hello

print("Module imported successfully")
print("Functions available:", [f for f in dir(utils) if not f.startswith('_')])

# =============================================================================
# Qe: Public and private functions, self keyword
# =============================================================================

class MyClass:
    # Class variable (shared by all instances)
    class_var = "shared"
    
    def __init__(self):
        self.public_var = "public"        # Public variable
        self._protected_var = "protected" # Protected (convention)
        self.__private_var = "private"    # Private (name mangling)
    
    def public_method(self):
        """Public method - can be called from outside"""
        return "This is public"
    
    def _protected_method(self):
        """Protected method - convention, should not be called outside"""
        return "This is protected"
    
    def __private_method(self):
        """Private method - name mangled, harder to access outside"""
        return "This is private"
    
    def test_access(self):
        """Test accessing all methods from inside class"""
        print("From inside class:")
        print(f"Public: {self.public_method()}")
        print(f"Protected: {self._protected_method()}")
        print(f"Private: {self.__private_method()}")

# Test the class
obj = MyClass()

# What is 'self'?
print("'self' refers to the instance of the class")
print(f"obj id: {id(obj)}")

# Test access from outside
print("\nFrom outside class:")
print(f"Public: {obj.public_method()}")
print(f"Protected: {obj._protected_method()}")

# Private method access (will fail)
try:
    print(f"Private: {obj.__private_method()}")
except AttributeError as e:
    print(f"Private method error: {e}")

# But can access with name mangling
print(f"Private via name mangling: {obj._MyClass__private_method()}")

# Test calling methods from inside
obj.test_access()

# What happens if you forget 'self'?
class BadClass:
    def method_without_self():  # Missing self parameter
        return "This will fail"

bad_obj = BadClass()

try:
    result = bad_obj.method_without_self()
    print(result)
except TypeError as e:
    print(f"Error when missing 'self': {e}")
    print("Python passes the instance as first argument, but method expects none")

# =============================================================================
# Qf: Constructor and Destructor
# =============================================================================

class MyClassWithConstructor:
    def __init__(self, name, value=0):
        """Constructor - called when object is created"""
        self.name = name
        self.value = value
        print(f"Object {self.name} created with value {self.value}")
    
    def __del__(self):
        """Destructor - called when object is garbage collected"""
        print(f"Object {self.name} is being destroyed")

# Test constructor
obj1 = MyClassWithConstructor("test1", 42)
obj2 = MyClassWithConstructor("test2")

print(f"obj1.name: {obj1.name}, obj1.value: {obj1.value}")

# Python has garbage collection
print("\nPython destructor notes:")
print("- Python has automatic garbage collection")
print("- __del__ is called when object is garbage collected")
print("- You rarely need to implement __del__")
print("- Python handles memory management automatically")

# Destructor will be called when objects go out of scope
del obj1
print("obj1 deleted manually")

# =============================================================================
# Qg: String representation (__str__ and __repr__)
# =============================================================================

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        """String representation for end users (readable)"""
        return f"{self.name}, {self.age} years old"
    
    def __repr__(self):
        """String representation for developers (unambiguous)"""
        return f"Person('{self.name}', {self.age})"

# Test string representations
person = Person("Alice", 25)

print("Using print() calls __str__:")
print(person)

print("\nUsing repr() calls __repr__:")
print(repr(person))

print("\nString conversion:")
print(f"str(person): {str(person)}")
print(f"repr(person): {repr(person)}")

# Without __str__, __repr__ is used as fallback
class SimpleClass:
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f"SimpleClass({self.value})"

simple = SimpleClass(42)
print(f"\nWithout __str__, print uses __repr__: {simple}")
