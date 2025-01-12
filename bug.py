def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_list = []
average = calculate_average(my_list) #this line will not raise exception
print(f"The average is: {average}")