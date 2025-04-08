# Problem 1: Reverse a String
def reverse_string():
    string = input("Enter a string: ")
    return string[::-1]

print(reverse_string())

#  Problem 2: Count Vowels in a String
def vowels_count():
    count = 0
    string = input("Enter a string: ")
    for char in string.lower():
        if char in "aeiou":
            count +=1
    return count

print(vowels_count())

#  Problem 3: Sum of Digits
def sum_of_digits():
    sum = 0
    string = input("Enter a string containing numbers: ")
    if string.isdigit():
        for num in string:
            sum += int(num)
        return sum
    else:
        return "Invalid input. Please enter a string containing numbers."
    
print(sum_of_digits())