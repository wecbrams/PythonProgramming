# Data Type
# integer
# float
# string
# boolean


number = 100  # int
second = 56.78  # float
text = "Hello there"  # str
isPythonIteresting = True  # bool

# storing multiple values in a variable
cars = ["toyota", "nissan", "VW", 50]  # List
fruits = ("banana", "oranges", "apples")  # Tuple
countries = {"Kenya", "Tanzania", "Tunisia", "Algeria"}  # Set
details = {
    "firstname": "Bramuel",
    "age": 23,
    "course": "Web development",
    "nationality": "Kenyan"
}  # Dictionary

print(details["firstname"])
print(details["age"])
print(second)
print(text)
print(countries)

# Determine  a data type
print(type(text))
print(type(countries))
print(type(details))

# Typecasting Converting one data type to another
print(float(number))
print(int(second))
