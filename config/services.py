from datetime import datetime
from typing import Any


def my_print(message) -> Any:
    """For check the code."""

    # label on the print
    label = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    print(f'{label}: {message}')


def comparison_of_dates(date1: datetime, delta: int = 18, date2: datetime = datetime.now()) -> bool:
    """Определяет, больше ли date2 минус delta лет чем date1."""

    data2_year = date2.year - delta
    data2_month = date2.month
    data2_day = date2.day

    data1_year = date1.year
    data1_month = date1.month
    data1_day = date1.day

    if data1_year < data2_year:
        return True
    elif data1_year == data2_year:
        if data1_month < data2_month:
            return True
        elif data1_month == data2_month:
            if data1_day < data2_day:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
