import logging
from logging_1 import Runner
from logging_1 import Tournament
import unittest


class RunnerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.basicConfig(filename='runner_tests.log', level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s', filemode='w', encoding='UTF-8')
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            print(f'Тест: {test_key}')
            for key, value in test_value.items():
                print(f't{key}: {value.name}')

    def test_walk(self):
        try:
            runner = Runner("Иван", -5)  # Передаем отрицательную скорость
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning(f"Неверная скорость для Runner: {e}")

    def test_run(self):
        try:
            runner = Runner(123, 10)  # Передаем не строку в имя
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning(f"Неверный тип данных для объекта Runner: {e}")

    def test_turn1(self):
        turn_1 = Tournament(90, self.runner_1, self.runner_3)
        result = turn_1.start()
        self.assertTrue(result[max(result.keys())] == self.runner_3)
        self.all_results['Тест первого раунда'] = result

    def test_turn2(self):
        turn_2 = Tournament(90, self.runner_2, self.runner_3)
        result = turn_2.start()
        self.assertTrue(result[max(result.keys())] == self.runner_3)
        self.all_results['Тест второго раунда'] = result

    def test_turn3(self):
        turn_3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = turn_3.start()
        self.assertTrue(result[max(result.keys())] == self.runner_3)
        self.all_results['Тест третьего раунда'] = result


if __name__ == '__main__':
    unittest.main()
