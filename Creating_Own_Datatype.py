class Fraction:
    """
    A class to represent a simplified mathematical fraction and perform basic arithmetic operations
    using operator overloading with error handling.
    """

    def __init__(self, numerator, denominator):
        """Initialize the Fraction and simplify it."""
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")

        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        """Return a user-friendly string representation."""
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        """Overload the + operator to add two fractions."""
        new_num = self.numerator * other.denominator + self.denominator * other.numerator
        new_deno = self.denominator * other.denominator
        return Fraction(new_num, new_deno)

    def __sub__(self, other):
        """Overload the - operator to subtract two fractions."""
        new_num = self.numerator * other.denominator - self.denominator * other.numerator
        new_deno = self.denominator * other.denominator
        return Fraction(new_num, new_deno)

    def __mul__(self, other):
        """Overload the * operator to multiply two fractions."""
        new_num = self.numerator * other.numerator
        new_deno = self.denominator * other.denominator
        return Fraction(new_num, new_deno)

    def __truediv__(self, other):
        """Overload the / operator to divide two fractions."""
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by a fraction with numerator 0.")
        new_num = self.numerator * other.denominator
        new_deno = self.denominator * other.numerator
        return Fraction(new_num, new_deno)

# ---------- Example Usage ----------
if __name__ == "__main__":
    fr1 = Fraction(2, 3)
    fr2 = Fraction(4, 5)
#gggg
    print("Fraction 1:", fr1)
    print("Fraction 2:", fr2)
    print("Addition:", fr1 + fr2)
    print("Subtraction:", fr1 - fr2)
    print("Multiplication:", fr1 * fr2)
    print("Division:", fr1 / fr2)
