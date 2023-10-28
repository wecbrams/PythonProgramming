# Program that checks whether a yar is a leap year or not
year = int(input("Enter the year to be checked: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"The year '{year}' is a leap year!")
else:
    print(f"The year '{year}' isn't a leap year!")


# Program that checks whether an alphabet letter is consonant or a vowel

character = input("Enter a character")

# create a list of vowels
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

if character in vowels:
    print(f"The character '{character}' is a vowel!")
else:
    print(f"The character '{character}' is a consonant!")
