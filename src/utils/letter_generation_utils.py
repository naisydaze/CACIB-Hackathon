from openpyxl import load_workbook

def find_and_fill_next_item(workbook_path, values):
    letter_ref = load_workbook(workbook_path)
    sheet = letter_ref.active

# Initialize variable to store the value from column A
    next_item_no = None

    # Iterate through the rows to find the first one where columns B and C are empty
    for row in sheet.iter_rows(min_row=1):
        # Check if all columns from B to CV (index 1 to 100) are empty
        if all(cell.value is None for cell in row[1:5]):
            next_item_no = row[0].value
        # Insert values into columns B to F
        for idx, value in enumerate(values):
            row[idx + 1].value = value
        break

    return next_item_no

