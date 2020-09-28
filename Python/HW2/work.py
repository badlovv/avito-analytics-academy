from csv import reader, writer, Sniffer
from collections import defaultdict
from warnings import warn
from typing import List


def user_interface() -> int:
    """Asks user for a query"""
    print('1. Вывести все отделы')
    print('2. Вывести сводный отчёт по отделам')
    print('3. Сохранить сводный отчёт в виде csv-файла')
    q = None
    while q not in [1, 2, 3]:
        try:
            q = int(input('Номер запроса:'))
        except ValueError:
            print('Введите только число - 1, 2 или 3')
    return q


def main(q: int) -> None:
    """Handles users queries.
    1: print departments list;
    2: print departments summary;
    3: save departments summary to csv file.
    Asks user for the next query after successful execution.
    """
    employees = load_csv()
    dep_data = group_by(employees, "отдел", "оклад")
    try:
        if q == 1:
            departments_summary(dep_data, 'list_only')
        elif q == 2:
            departments_summary(dep_data, 'print')
        elif q == 3:
            departments_summary(dep_data, 'to_csv')
            print('Сводный отчет по отделам сохранен в csv-файл.')
        res = True
    except BaseException as e:
        warn(f'An error "{e}" occurred')
        res = False
    if res:
        again = None
        while again not in ['y', 'n', 'yes', 'no']:
            again = input('Запрос выполнен успешно. Выполнить новый запрос? [y/n]\n:')
        if again[0] == 'y':
            ans = user_interface()
            main(ans)
        else:
            return


def departments_summary(dep_data: dict, output: str = '') -> List[List]:
    """Computes salaries summary for each department
    and returns the data with header as a list of lists.
    Performs additional actions if output specified.
    """
    if output == 'list_only':
        print('Список отделов:')
        print('\n'.join(dep_data.keys()))

    header = ['Отдел', 'Численность', 'Вилка зарплат', 'Средняя зарплата']
    summary = []
    for i, (dep, vals) in enumerate(dep_data.items()):
        summary.append([dep])
        summary[i].append(len(vals))
        summary[i].append(f'{int(min(vals))}-{int(max(vals))}')
        summary[i].append(round(sum(vals)/len(vals), 2))
    h_summary = [header] + summary
    if output == 'print':
        print('Сводный отчет по отделам:')
        print_table(h_summary)
    elif output == 'to_csv':
        to_csv(h_summary)
    return h_summary


def group_by(data: List[List], by: str = 'отдел', field: str = 'оклад') -> dict:
    """Groups the 'field' column by categories in 'by' column from 'data'"""
    pos = col_position_handler(data[0], by, field)
    groups_data = defaultdict(list)
    for d in data[1:]:
        group = d[pos[0]].split('->')[0].strip()
        try:
            value = float(d[pos[1]].strip())
            groups_data[group].append(value)
        except ValueError:
            warn(f'Non-numeric data in column "{field}"!')
    return groups_data


def col_position_handler(header: list, by: str, field: str) -> list:
    """Returns positions of 'by' and 'field' in 'header' as a list.
    Used by group_by function.
    """
    positions = {}
    for i, h in enumerate(header):
        h = h.lower()
        if h == by.strip().lower():
            positions[0] = i
        elif h == field.strip().lower():
            positions[1] = i
    return list(positions.values())


def load_csv(path: str = 'employees.csv') -> List[List]:
    try:
        with open(path) as f:
            dialect = Sniffer().sniff(f.read(1024))
            f.seek(0)
            rdr = reader(f, dialect)
            return list(rdr)
    except FileNotFoundError:
        warn(f'File not found. Please, make sure to place {path} file in the directory!')
        exit(1)

def print_table(data: list) -> None:
    """Pretty print data in table-like format
    """
    row_format = "{:>20}|" * (len(data[0]))
    for line in data:
        print(row_format.format(*line))


def to_csv(data: List[List], path: str = 'summary.csv', delimiter: str = ',') -> None:
    with open(path, 'w', newline='') as f:
        wrtr = writer(f, delimiter=delimiter)
        wrtr.writerows(data)


if __name__ == '__main__':
    main(user_interface())
