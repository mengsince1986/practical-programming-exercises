"""
3. Variables full and empty refer to Boolean values. Write an expression that produces True if and only if at most one of the variables is True.
"""

full = True
empty = False

(full != empty) or (not full and not empty)
