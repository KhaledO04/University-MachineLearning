# Simple utils module for SWMAL L01
import numpy as np

def say_hello(name="Student"):
    """Simple greeting function"""
    return f"Hello {name}!"

def add_numbers(a, b):
    """Add two numbers"""
    return a + b

def create_matrix(rows=2, cols=2):
    """Create a simple matrix"""
    return np.ones((rows, cols))

def test_my_functions():
    """Test all my functions"""
    print("Testing my simple module:")
    print(f"Greeting: {say_hello('ML Student')}")
    print(f"Adding 5 + 3 = {add_numbers(5, 3)}")
    print(f"Matrix:\n{create_matrix(3, 2)}")

print("My simple module loaded!")
