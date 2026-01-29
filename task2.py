import re 

def generator_numbers(text):
    """Finds all numbers in text and gives them back one at a time"""
    pattern = r'\b\d+\.?\d*\b'
    numbers = re.findall(pattern, text)
    
    # Return each number as a float (decimal number)
    for num in numbers:
        yield float(num)

def sum_profit(text, func):
    """Adds up all numbers found by the given function"""
    total = 0  # Start with zero
    
    for number in func(text):
        total += number
    
    return total


# Example usage
text1 = "Salary: 1000.01, bonus: 27.45, extra: 324.00"
result1 = sum_profit(text1, generator_numbers)
print(f"Text: {text1}")
print(f"Total income: {result1}")
print("-" * 40)