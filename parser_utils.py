import re
from datetime import datetime


def extract_data_from_description(description: str) -> tuple:
    """
    Извлекает данные (ФИО, название темы и дату) из строки с помощью регулярного выражения.
    
    Args:
        description (str): Строка, содержащая ФИО, название темы и дату в формате "гггг.мм.дд".

    Returns:
        tuple: Кортеж, содержащий ФИО, название темы и строку с датой.
        
    Raises:
        ValueError: Если строка не соответствует ожидаемому формату.
    """
    pattern = r'"(.*?)"\s+"(.*?)"\s+(\d{4}\.\d{2}\.\d{2})'
    match = re.search(pattern, description)

    if not match:
        raise ValueError(
            "Строка должна содержать полное ФИО, название темы и дату выдачи."
        )

    return match.group(1).strip(), match.group(2).strip(), match.group(3).strip()


def parse_date(issue_date_str: str) -> datetime:
    """
    Преобразует строку с датой в объект datetime.
    
    Args:
        issue_date_str (str): Строка, представляющая дату в формате "гггг.мм.дд".

    Returns:
        datetime: Объект даты.
        
    Raises:
        ValueError: Если формат даты некорректен.
    """
    try:
        return datetime.strptime(issue_date_str, '%Y.%m.%d')
    except ValueError:
        raise ValueError("Дата должна быть в формате гггг.мм.дд.")
