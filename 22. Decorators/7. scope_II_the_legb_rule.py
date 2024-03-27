# LEGB rule
# Local
# Enclosing function
# Global
# Built-in


# def outer():
#     x = 10
    
#     def inner():
#         x = 5
#         return x
    
#     return inner()

# def outer():
#     x = 10
    
#     def inner():
#         return x
    
#     return inner()

# x = 15 # Global scope

# def outer():
#     # Enclosing function scope
#     def inner():
#         # Local scope
#         return x
    
#     return inner()


def outer():
    # Enclosing function scope
    def inner():
        # Local scope
        return len
    
    return inner()


print(outer())