import csv
from datetime import datetime
from sql_utils import setup_db_connection, insert_students, create_db_tables

def read_csv_to_list(filename):
    with open(filename, newline='') as file:
        return list(csv.DictReader(file, delimiter=','))


def convert_all_dates(list_of_dicts, date_cols,
                      current_format='%d/%m/%Y',
                      expected_format='%Y-%m-%d'):
    for dict in list_of_dicts:
        for col in date_cols:
            try:
                str_to_date = datetime.strptime(dict[col], current_format)
                date_to_str = datetime.strftime(str_to_date, expected_format)
                dict[col] = date_to_str
            except ValueError:
                dict[col] = None
    return list_of_dicts


def check_integer_columns(list_of_dicts, int_cols):
    for dictionary  in list_of_dicts:
        for colum in int_cols:
            try:
                dictionary[colum] = int(dictionary[colum])
            except ValueError:
                dictionary [colum] = None
    return list_of_dicts
        


def check_values_in_valid_list(list_of_dicts, valid_items, col_name):
    for dictionary in list_of_dicts:
        if dictionary[col_name] not in valid_items:
            dictionary[col_name] = None
    return list_of_dicts


def drop_duplicate_ids(list_of_dicts):
    dictionary_ids = []
    new_dictionary_list = []
    for dictionary in list_of_dicts:
        if dictionary["id"] in dictionary_ids:
            pass
        else:
            dictionary_ids.append(dictionary["id"])
            new_dictionary_list.append(dictionary)
    return new_dictionary_list


def drop_rows_with_null(list_of_dicts):
    new_dictionary_list = []
    for dictionary in list_of_dicts:
        none_count = 0
        for key in dictionary:
            if not dictionary[key]:
                none_count += 1
        if none_count == 0:
            new_dictionary_list.append(dictionary)
    return new_dictionary_list


if __name__ == '__main__':
    connection = setup_db_connection()

    create_db_tables(connection)

    data_list = read_csv_to_list('messy-data.csv')

    # Sample data:
    #
    # id, name,       age, branch,           teacher, start_date, tel
    # 1,  John Smith, 19,  Computer Sciense, Mrs. X,  13/01/2020, 012345
    #
    # my_list = [
    #     {
    #         'id': 1,
    #         'name': 'John Smith',
    #         'age': None,
    #         'branch': 'Computer Sciense',
    #         'teacher': 'Mrs. X',
    #         'start_date': '13/01/2020',
    #         'tel': 012345
    #     },
    #     {...},
    #     {...},
    #     {...}
    # ]

    data_list = convert_all_dates(data_list, ['start_date'])
    data_list = check_integer_columns(data_list, ['id', 'age'])
    print(data_list)
    teacher_list = ['Mrs. X', 'Ms. Smith', 'Mr. G']
    data_list = check_values_in_valid_list(data_list, teacher_list, 'teacher')

    data_list = drop_duplicate_ids(data_list)
    data_list = drop_rows_with_null(data_list)

    insert_students(connection, data_list)

    connection.close()
