from typing import List, Optional

def calculate_average(numbers: List[float]) -> Optional[float]:
    """
    Возвращает среднее арифметическое элементов списка чисел.
    Если список пустой, возвращает None.
    """
    if not numbers:
        return None
    return sum(numbers) / len(numbers)