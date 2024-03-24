creator = "Boris"
PI = 3.14159

def add(a, b):
    """_summary_

    Args:
        a (int): give integer
        b (int): give integer

    Returns:
        int: return sum of a and b
    """
    return a + b

def subtract(a, b):
    return a - b

def area(radius):
    return PI * (radius ** 2)

_year = 2024

if __name__ == "__main__":
    print("This will only run when calculator.py is being executed as a script.")
    print(subtract(3, 5))
