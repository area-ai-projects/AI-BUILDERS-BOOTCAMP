# String Operations

text = "   Artificial Intelligence   "

# Original string
print("Original String:", text)

# Strip spaces
stripped_text = text.strip()
print("After Strip:", stripped_text)

# Uppercase
print("Uppercase:", stripped_text.upper())

# Lowercase
print("Lowercase:", stripped_text.lower())

# Slicing
print("Sliced String:", stripped_text[0:10])

# Concatenation
new_text = stripped_text + " is transforming the world."
print("Concatenated String:", new_text)