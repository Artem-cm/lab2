from work_topic import WorkTopic
from parser_utils import extract_data_from_description, parse_date
from file_utils import read_descriptions_from_file


def create_work_topic(description: str) -> WorkTopic:
    """
    Создает объект WorkTopic на основе строки описания.
    
    Args:
        description (str): Строка, содержащая ФИО, название темы и дату выдачи.

    Returns:
        WorkTopic: Объект WorkTopic с заполненными данными.
    """
    student_name, topic_name, issue_date_str = extract_data_from_description(description)
    issue_date = parse_date(issue_date_str)
    return WorkTopic(student_name, topic_name, issue_date)


def main():
    """
    Основная функция программы. Читает список строк из файла, создает объекты WorkTopic для каждого студента и выводит их.
    """
    file_path = 'input.txt'
    descriptions = read_descriptions_from_file(file_path)

    for description in descriptions:
        try:
            work_topic = create_work_topic(description)
            print(work_topic)
        except ValueError as e:
            print(f"Ошибка в строке '{description}': {e}")


if __name__ == '__main__':
    main()
