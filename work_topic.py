from datetime import datetime


class WorkTopic:
    """Класс для хранения информации о студенте, теме работы и дате выдачи."""

    def __init__(self, student_name: str, topic_name: str, issue_date: datetime):
        self.student_name = student_name
        self.topic_name = topic_name
        self.issue_date = issue_date

    def __repr__(self) -> str:
        """Возвращает строку с полным ФИО, названием темы и датой выдачи."""
        return f"{self.student_name} {self.topic_name} {self.issue_date.strftime('%Y.%m.%d')}"
