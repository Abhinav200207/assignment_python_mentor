from prettytable import PrettyTable
import csv

def table_decorator(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        table = PrettyTable()
        if data:
            headers = data[0].keys()
            table.field_names = headers
            for row in data:
                table.add_row(row.values())
            print(table)
    return wrapper

@table_decorator
def display_csv(file_path):
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        return [row for row in reader]
