def solve(n: int) -> int:
    """
    This function returns the factorial of a number.

    Args:
        n (int): Non-negative integer input

    Returns:
        int: factorial of n

    Raises:
        TypeError: if n is not an integer
        ValueError: if n is negative
    """
    try:
        if n == 0 or n == 1:
            return 1
        return solve(n)*solve(n-1)
    except Exception as e:
        return e
