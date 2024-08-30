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





import os
from openpyxl import load_workbook

# Cross-platform imports for file locking
try:
    import fcntl  # Unix-based systems
except ImportError:
    fcntl = None

try:
    import msvcrt  # Windows
except ImportError:
    msvcrt = None

class FileLock:
    def __init__(self, filepath):
        self.filepath = filepath
        self.file = None

    def lock(self):
        """Locks the file to prevent access by other programs."""
        self.file = open(self.filepath, 'r+')
        if fcntl:  # Unix-based locking
            fcntl.flock(self.file, fcntl.LOCK_EX)
        elif msvcrt:  # Windows locking
            msvcrt.locking(self.file.fileno(), msvcrt.LK_NBLCK, 1024)

    def unlock(self):
        """Unlocks the file."""
        if self.file:
            if fcntl:
                fcntl.flock(self.file, fcntl.LOCK_UN)
            elif msvcrt:
                msvcrt.locking(self.file.fileno(), msvcrt.LK_UNLCK, 1024)
            self.file.close()
            self.file = None

def find_and_fill_next_item_no(workbook_path, values):
    """
    Finds the first empty row in columns B to F and inserts the provided values.

    :param workbook_path: Path to the Excel workbook.
    :param values: A list of values to insert into columns B to F.
    :return: The item number from column A if a row was found, else None.
    """
    # Lock the file before processing
    lock = FileLock(workbook_path)
    lock.lock()

    try:
        # Load the workbook and select the active worksheet
        workbook = load_workbook(workbook_path)
        sheet = workbook.active

        # Initialize variable to store the value from column A
        next_item_no = None

        # Iterate through the rows to find the first one where columns B to F are empty
        for row in sheet.iter_rows(min_row=1):
            if all(cell.value is None for cell in row[1:6]):  # Checking columns B to F
                next_item_no = row[0].value  # Get value from column A
                # Insert values into columns B to F
                for idx, value in enumerate(values):
                    row[idx + 1].value = value
                break

        # Save the workbook with the updated values
        workbook.save(workbook_path)

    finally:
        # Unlock the file after processing
        lock.unlock()

    return next_item_no
