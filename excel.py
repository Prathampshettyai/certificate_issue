import openpyxl

def fetch_data_from_xlsx(file_path):
    data_list = []  # Initialize an empty list to store the data
    wb = openpyxl.load_workbook(file_path)
    ws = wb.active
    for row in ws.iter_rows(values_only=True):
        data_list.append(row)  # Append each row to the list
    return data_list  # Return the list containing all the data

# Example usage

 # Print the data from the second row and second column
