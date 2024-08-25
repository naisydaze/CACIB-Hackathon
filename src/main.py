from utils.letter_generation_utils import find_and_fill_next_item

# Path to your workbook
workbook_path = '/Users/shanaisyuen/Downloads/Letter of Reference For Year 2024.xlsx'

# Data retrieval (example)
db_value = "Database Value"  # Replace with actual DB retrieval code
user_input = "User Input"  # Replace with actual user input code

# Values to insert into columns B to F (you can add more values as needed)
values_to_insert = [db_value, user_input, "Value 3", "Value 4", "Value 5"]


# Call the function and get the next item number
next_item_no = find_and_fill_next_item(workbook_path, values_to_insert)

if next_item_no:
    print(f"The next item number is: {next_item_no}")
else:
    print("No such row was found.")   