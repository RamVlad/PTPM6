"""
Модульные тесты для модуля calculator.py.
Проверяют функцию calculate_total и format_result.
"""
import pytest
from calculator import calculate_total, format_result


class TestCalculateTotal:
    """Тесты функции calculate_total"""

    def test_basic_calculation(self):
        """Базовый расчёт: 5 тетрадей по 30₽ + обложки по 10₽"""
        assert calculate_total(5, 30, 10) == 200.0

    def test_single_item(self):
        """Одна тетрадь"""
        assert calculate_total(1, 50, 20) == 70.0

    def test_zero_count(self):
        """Нулевое количество — итог 0"""
        assert calculate_total(0, 100, 50) == 0.0

    def test_zero_prices(self):
        """Нулевые цены — итог 0"""
        assert calculate_total(10, 0, 0) == 0.0

    def test_large_count(self):
        """Большое количество"""
        assert calculate_total(1000, 25.5, 12.5) == 38000.0

    def test_float_prices(self):
        """Дробные цены"""
        assert calculate_total(3, 29.99, 9.99) == 119.94

    def test_negative_count_raises(self):
        """Отрицательное количество должно вызывать ошибку"""
        with pytest.raises(ValueError):
            calculate_total(-1, 10, 5)

    def test_negative_price_tetr_raises(self):
        """Отрицательная цена тетради должна вызывать ошибку"""
        with pytest.raises(ValueError):
            calculate_total(5, -10, 5)

    def test_negative_price_obloz_raises(self):
        """Отрицательная цена обложки должна вызывать ошибку"""
        with pytest.raises(ValueError):
            calculate_total(5, 10, -5)

    def test_invalid_type_count_raises(self):
        """Неверный тип для количества"""
        with pytest.raises(TypeError):
            calculate_total("пять", 10, 5)

    def test_invalid_type_price_raises(self):
        """Неверный тип для цены"""
        with pytest.raises(TypeError):
            calculate_total(5, "десять", 5)


class TestFormatResult:
    """Тесты функции format_result"""

    def test_format_basic(self):
        """Базовое форматирование"""
        result = format_result(200.0, 5)
        assert "200.00 ₽" in result  # было "200,00 ₽"
        assert "Тетрадей: 5" in result
        assert "Обложек: 5" in result

    def test_format_zero(self):
        """Форматирование нулевого результата"""
        result = format_result(0.0, 0)
        assert "0.00 ₽" in result  # было "0,00 ₽"