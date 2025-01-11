def linear_search_recursive(arr, key, index=0):
    # Base case: if index reaches the length of the array
    if index >= len(arr):
        return -1
    # If the current element matches the key
    if arr[index] == key:
        return index
    # Recursively search in the rest of the array
    return linear_search_recursive(arr, key, index + 1)

def linear_search_non_recursive(arr, key):
    for index in range(len(arr)):
        if arr[index] == key:
            return index
    return -1

# Example usage
if __name__ == "__main__":
    numbers = [10, 20, 30, 40, 50, 60]
    key_to_find = 30

    # Non-recursive linear search
    result_non_recursive = linear_search_non_recursive(numbers, key_to_find)
    if result_non_recursive != -1:
        print(f"Non-recursive: Key {key_to_find} found at index {result_non_recursive}.")
    else:
        print(f"Non-recursive: Key {key_to_find} not found.")

    # Recursive linear search
    result_recursive = linear_search_recursive(numbers, key_to_find)
    if result_recursive != -1:
        print(f"Recursive: Key {key_to_find} found at index {result_recursive}.")
    else:
        print(f"Recursive: Key {key_to_find} not found.")
