import pytest


@pytest.fixture
def clear_book_database():
    print('[FIXTURE] Удаляем все данные из базы данных')


@pytest.fixture
def fill_book_database():
    print('[FIXTURE] Создаем новые данные в базе данных')


@pytest.mark.usefixtures('clear_book_database', 'fill_book_database')
class TestLibrary:
    def test_read_book_from_library(self):
        ...

    def test_delete_book_from_library(self):
        ...
