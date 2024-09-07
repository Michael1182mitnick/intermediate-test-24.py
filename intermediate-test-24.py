# Write a function to generate all permutations of a given list of numbers.

def generate_permutations(nums):
    """
    Function to generate all permutations of a given list of numbers.

    :param nums: List of numbers.
    :return: List of all possible permutations.
    """
    def backtrack(start, end):
        # If we've reached the end of the list, add the permutation to the result
        if start == end:
            result.append(nums[:])
        for i in range(start, end):
            # Swap the current element with the start element
            nums[start], nums[i] = nums[i], nums[start]
            # Recurse on the rest of the list
            backtrack(start + 1, end)
            # Backtrack (swap back to the original configuration)
            nums[start], nums[i] = nums[i], nums[start]

    # List to store all permutations
    result = []
    # Call the helper function with initial values
    backtrack(0, len(nums))
    return result


# Example usage
numbers = [1, 2, 3]
permutations = generate_permutations(numbers)
print("All permutations of the list are:")
print(permutations)
