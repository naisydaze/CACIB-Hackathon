from openpyxl import load_workbook
from filelock import FileLock

def find_next_item(workbook_path, values):

    # lock_path = workbook_path + '.lock'
    # lock = FileLock(lock_path)

    # # Acquire the file lock
    # with lock:
    #     print(f"Lock acquired for retrieving latest item no.")


    letter_ref = load_workbook(workbook_path)
    sheet = letter_ref.active

    min_row = 1
    max_row = 1000
# Initialize variable to store the value from column A
# # Iterate through the rows to find the first one where columns B and C are empty
    for row_number in range(min_row, max_row + 1):
        row = sheet[row_number]
        # if (row_number <2): next_item_no = '0001'
        # Check if all columns from B to CV (index 1 to 100) are empty
        if all(cell.value is None for cell in row[0:5]):
            previous_row = sheet[row_number -1]
            previous_item_no = previous_row[0].value
            print ("previous item no: {previous_item_no}")
            next_item_no = previous_item_no + 1
            print (next_item_no)
            print(row[0].row,)
            return row[0].row, next_item_no 
        # # Insert values into columns B to F
        # for idx, value in enumerate(values):
        #     row[idx + 1].value = value

    print("No empty row found.")
    return None, None  # If no empty row was found


def fill_next_item(workbook_path, row_number, next_item_no,  values):

    lock_path = workbook_path + '.lock'
    lock = FileLock(lock_path)

    # Acquire the file lock
    with lock:
        print(f"Lock acquired for filling row {row_number}.")
        # Load the workbook and select the active worksheet
        workbook = load_workbook(workbook_path)
        sheet = workbook.active

        # Insert values into columns B to F of the specified row
        for idx, value in enumerate(values):
            sheet.cell(row=row_number, column=1).value = next_item_no  # A iscolumn 1, for item no.
            print(next_item_no)
            sheet.cell(row=row_number, column=idx + 2).value = value  # B is column 2

        # Save the workbook with the updated values
    workbook.save(workbook_path)
    print(f"Row {row_number} filled and lock released.")    
