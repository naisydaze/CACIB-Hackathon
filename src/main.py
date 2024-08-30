from utils.letter_generation_utils import find_next_item, fill_next_item
from openpyxl import load_workbook
from filelock import FileLock


# Path to your workbook
workbook_path = '/Users/shanaisyuen/Downloads/Letter of Reference For Year 2024.xlsx'


lock_path = workbook_path + '.lock'
lock = FileLock(lock_path)
    
# Acquire the file lock
with lock:
    print ("insert message popup: 'Letter of reference is currently being locked and used by another User. Please wait for the process to end'")
    # Data retrieval (example)
    db_value = "Database Value"  # Replace with actual DB retrieval code
    user_input = "User Input"  # Replace with actual user input code


    letter_ref = load_workbook(workbook_path)
    sheet = letter_ref.active

    values_to_insert= [cell.value for cell in sheet[2]]


    print ( values_to_insert)
    # Values to insert into columns B to F (you can add more values as needed)
    # values_to_insert = [db_value, user_input, "Value 3", "Value 4", "Value 5"]
    # values_to_insert = [db_value, user_input, "Value 3", "Value 4", "Value 5"]

    # Find the next empty row
    row_number, next_item_no = find_next_item(workbook_path)

    extraction_done = ''# -- when WM's letter generation done, and ready to update letter of ref 

    if row_number :
        print(f"Next empty row found at: {row_number}, with item number: {next_item_no}")
        # Fill the row with the values
        fill_next_item(workbook_path, row_number, next_item_no, values_to_insert)
    else:
        print("No suitable row was found.")
    # Save the workbook with the updated values
    # letter_ref.save(workbook_path)
    # print(f"Row {row_number} filled and lock released.")  

            # Save the workbook with the updated values
