"""
Модуль расчёта стоимости тетрадей и обложек.
Содержит чистую функцию, которую можно тестировать без GUI.
"""


def calculate_total(count: int, price_tetr: float, price_obloz: float) -> float:
    """
    Рассчитывает итоговую стоимость заказа.

    Args:
        count: количество тетрадей (и обложек)
        price_tetr: цена одной тетради в рублях
        price_obloz: цена одной обложки в рублях

    Returns:
        Итоговая сумма в рублях

    Raises:
        ValueError: если переданы отрицательные значения
        TypeError: если переданы нечисловые значения
    """
    if not isinstance(count, (int, float)):
        raise TypeError("Количество должно быть числом")
    if not isinstance(price_tetr, (int, float)):
        raise TypeError("Цена тетради должна быть числом")
    if not isinstance(price_obloz, (int, float)):
        raise TypeError("Цена обложки должна быть числом")

    if count < 0:
        raise ValueError("Количество не может быть отрицательным")
    if price_tetr < 0:
        raise ValueError("Цена тетради не может быть отрицательной")
    if price_obloz < 0:
        raise ValueError("Цена обложки не может быть отрицательной")

    total = (price_tetr + price_obloz) * count
    return round(total, 2)


def format_result(total: float, count: int) -> str:
    """
    Форматирует результат для отображения.

    Args:
        total: итоговая сумма
        count: количество тетрадей

    Returns:
        Строка с отформатированным результатом
    """
    return f"Итого: {total:,.2f} ₽ | Тетрадей: {count} | Обложек: {count}"