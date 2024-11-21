# 5. Search value in a dictionary and return the key
def search_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None  # Return None if value not found

# Example usage
a = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4"
}
print(search_value(a, "value3"))  # Output: key3