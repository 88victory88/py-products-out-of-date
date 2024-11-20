import unittest
from unittest.mock import patch
import datetime
from app.main import outdated_products  # Импортируем функцию для тестирования


class TestOutdatedProducts(unittest.TestCase):
    @patch("app.main.datetime")
    def test_outdated_products(self, mock_datetime: datetime) -> any:
        mock_datetime.date.today.return_value = datetime.date(2022, 2, 5)

        # Пример данных
        products = [
            {"name": "salmon",
             "expiration_date": datetime.date(2022, 2, 10),
             "price": 600},
            {"name": "chicken",
             "expiration_date": datetime.date(2022, 2, 5),
             "price": 120},
            {"name": "duck",
             "expiration_date": datetime.date(2022, 2, 1),
             "price": 160},
        ]

        # Ожидаемый результат
        expected = ["duck"]

        # Проверяем функцию
        result = outdated_products(products)
        self.assertEqual(result, expected)

    @patch("app.main.datetime")
    def test_no_outdated_products(self, mock_datetime: datetime) -> any:
        mock_datetime.date.today.return_value = datetime.date(2022, 2, 1)

        products = [
            {"name": "salmon",
             "expiration_date": datetime.date(2022, 2, 10),
             "price": 600},
            {"name": "chicken",
             "expiration_date": datetime.date(2022, 2, 5),
             "price": 120},
        ]

        expected = []  # Никто не просрочен
        result = outdated_products(products)
        self.assertEqual(result, expected)

    @patch("app.main.datetime")
    def test_all_outdated_products(self, mock_datetime: datetime) -> any:
        mock_datetime.date.today.return_value = datetime.date(2022, 3, 1)

        products = [
            {"name": "salmon",
             "expiration_date": datetime.date(2022, 2, 10),
             "price": 600},
            {"name": "chicken",
             "expiration_date": datetime.date(2022, 2, 5),
             "price": 120},
        ]

        expected = ["salmon", "chicken"]  # Все просрочены
        result = outdated_products(products)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
