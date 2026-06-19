# ============================================================
# PYTHON ASSIGNMENTS - AREA AI BUILDERS BOOTCAMP
#BOOTCAMPI D: AIBD/001/086
# Name: Ponzing Abel Nimnan
# Date: 2026-06-18
# ============================================================


# ============================================================
# ASSIGNMENT 1: Personal Profile
# Objective: Understand variables and basic data storage
# ============================================================

name = "Abel"
age = 22
state_of_residence = "Plateau"
favorite_ai_tool = "Claude"

print("=" * 40)
print("       ASSIGNMENT 1: Personal Profile")
print("=" * 40)
print(f"Name              : {name}")
print(f"Age               : {age}")
print(f"State of Residence: {state_of_residence}")
print(f"Favorite AI Tool  : {favorite_ai_tool}")
print()


# ============================================================
# ASSIGNMENT 2: Data Types Practice
# Objective: Identify and work with different Python data types
# ============================================================

# String
my_string = "Artificial Intelligence"

# Integer
my_integer = 2026

# Float
my_float = 3.14159

# Boolean
my_boolean = True

# List (5 AI tools)
ai_tools_list = ["Claude", "ChatGPT", "Gemini", "Copilot", "Grok"]

# Tuple
my_tuple = ("Python", "Machine Learning", "Neural Networks")

# Dictionary
my_dictionary = {
    "name": "Abel Ponzing",
    "course": "Computer Science",
    "level": Beginer,
    "university": "Area AI",
    
}

print("=" * 40)
print("   ASSIGNMENT 2: Data Types Practice")
print("=" * 40)
print(f"String  : {my_string!r}  --> Type: {type(my_string)}")
print(f"Integer : {my_integer}           --> Type: {type(my_integer)}")
print(f"Float   : {my_float}       --> Type: {type(my_float)}")
print(f"Boolean : {my_boolean}          --> Type: {type(my_boolean)}")
print(f"List    : {ai_tools_list}")
print(f"         --> Type: {type(ai_tools_list)}")
print(f"Tuple   : {my_tuple}")
print(f"         --> Type: {type(my_tuple)}")
print(f"Dict    : {my_dictionary}")
print(f"         --> Type: {type(my_dictionary)}")
print()


# ============================================================
# ASSIGNMENT 3: String Operations
# Objective: Learn how to manipulate strings in Python
# ============================================================

original_string = "   Artificial Intelligence is the Future   "

# 1. Uppercase
uppercase_result = original_string.upper()

# 2. Lowercase
lowercase_result = original_string.lower()

# 3. Strip (removes leading/trailing whitespace)
stripped_result = original_string.strip()

# 4. Slicing (extract "Artificial Intelligence")
sliced_result = original_string.strip()[0:24]

# 5. Concatenation
concatenation_result = "Hello, " + original_string.strip() + "!"

print("=" * 40)
print("   ASSIGNMENT 3: String Operations")
print("=" * 40)
print(f"Original String : '{original_string}'")
print()
print(f"1. Uppercase    : '{uppercase_result}'")
print(f"2. Lowercase    : '{lowercase_result}'")
print(f"3. Strip        : '{stripped_result}'")
print(f"4. Slicing [0:24]: '{sliced_result}'")
print(f"5. Concatenation: '{concatenation_result}'")
print()
print("=" * 40)
print("       All Assignments Complete!")
print("=" * 40)
