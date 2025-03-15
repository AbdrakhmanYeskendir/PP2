

### **1. Match a string with 'a' followed by zero or more 'b'**

import re

pattern = r'ab*'  # 'a' followed by zero or more 'b'

test_strings = ["a", "ab", "abb", "ac", "b", "aabb"]
for s in test_strings:
    if re.fullmatch(pattern, s):
        print(f"Matched: {s}")

#### **Output**

# Matched: a
# Matched: ab
# Matched: abb


### **2. Match a string with 'a' followed by two to three 'b'**

pattern = r'ab{2,3}'  # 'a' followed by 2 or 3 'b'

test_strings = ["ab", "abb", "abbb", "abbbb"]
for s in test_strings:
    if re.fullmatch(pattern, s):
        print(f"Matched: {s}")

#### **Output**

# Matched: abb
# Matched: abbb


### **3. Find sequences of lowercase letters joined with an underscore**

pattern = r'\b[a-z]+_[a-z]+\b'

text = "hello_world test_example regex_exercise Hello_World"
matches = re.findall(pattern, text)
print(matches)

#### **Output**

['hello_world', 'test_example', 'regex_exercise']


### **4. Find sequences of one uppercase letter followed by lowercase letters**

pattern = r'[A-Z][a-z]+'

text = "Hello World Regex Exercise test example"
matches = re.findall(pattern, text)
print(matches)

#### **Output**

# ['Hello', 'World', 'Regex', 'Exercise']


### **5. Match a string with 'a' followed by anything, ending in 'b'**

pattern = r'a.*b$'

test_strings = ["ab", "axb", "a123b", "abc", "b"]
for s in test_strings:
    if re.fullmatch(pattern, s):
        print(f"Matched: {s}")

#### **Output**

# Matched: ab
# Matched: axb
# Matched: a123b


### **6. Replace spaces, commas, or dots with a colon**

pattern = r'[ ,.]'

text = "Hello, world. This is a test"
result = re.sub(pattern, ":", text)
print(result)

#### **Output**

# Hello:world:This:is:a:test


### **7. Convert snake_case to camelCase**

def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.capitalize() for x in components[1:])

print(snake_to_camel("hello_world_example"))  # Output: helloWorldExample


### **8. Split a string at uppercase letters**

pattern = r'(?=[A-Z])'

text = "HelloWorldRegexExercise"
result = re.split(pattern, text)
print(result)

#### **Output**

['', 'Hello', 'World', 'Regex', 'Exercise']


### **9. Insert spaces between words starting with capital letters**

pattern = r'([A-Z])'

text = "HelloWorldRegexExercise"
result = re.sub(pattern, r' \1', text).strip()
print(result)

#### **Output**

# Hello World Regex Exercise

### **10. Convert camelCase to snake_case**

def camel_to_snake(camel_str):
    return re.sub(r'([A-Z])', r'_\1', camel_str).lower().lstrip('_')

print(camel_to_snake("helloWorldExample"))  # Output: hello_world_example
