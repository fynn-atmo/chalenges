# Calculate the Missing Value with Ohm's Law

Create a function that calculates the missing value of 3 inputs using Ohm's law. The inputs are v, r or i (aka: voltage, resistance and current).

Ohm's law:

V = R * I

Return the missing value rounded to two decimal places.

## Examples

ohmsLaw(12, 220, None) ➞ 0.05

ohmsLaw(230, None, 2) ➞ 115

ohmsLaw(None, 220, 0.02) ➞ 4.4

ohmsLaw(None, None, 10) ➞ "Invalid"

ohmsLaw(500, 50, 10) ➞ "Invalid"

## Notes

    Missing values will be None
    If there is more than one missing value, or no missing value, return "Invalid"
    Only numbers will be given.