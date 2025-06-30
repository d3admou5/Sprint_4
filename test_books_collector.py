import pytest
from main import BooksCollector

# Фикстура для создания нового экземпляра BooksCollector перед каждым тестом.
# Не выносил её в conftest.py, так как используется только в этом файле.

@pytest.fixture
def collector():
    return BooksCollector()

class TestBooksCollector:

# 1 Проверка: при инициализации все коллекции пусты, а жанры заданы по умолчанию
    def test_init_sets_up_empty_and_default_values(self, collector):
        assert collector.books_genre == {}
        assert collector.favorites == []
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

# 2 Проверка: добавление книги с разными названиями (валидное, пустое, слишком длинное)
    @pytest.mark.parametrize("name, expected", [
        ("Матрица", True), # допустимое имя - книга добавится
        ("", False), # пустая строка - не добавится
        ("А" * 41, False), # слишком длинное имя (>40 символов) - не добавится
    ])
    def test_add_new_book_various_names(self, collector, name, expected):
        collector.add_new_book(name)
        assert (name in collector.get_books_genre()) == expected

# 3 Проверка: повторное добавление одной и той же книги не создаёт дубликат
    def test_add_duplicate_book_only_once(self, collector):
        collector.add_new_book("Дюна")
        collector.add_new_book("Дюна") # вторая попытка
        books = collector.get_books_genre()
        assert list(books.keys()).count("Дюна") == 1

# 4 Проверка: установка жанра книги (исправлено)
    def test_set_book_genre_valid_for_existing_book(self, collector):
        collector.add_new_book("Матрица")
        collector.set_book_genre("Матрица", "Фантастика")
        assert collector.books_genre == {"Матрица": "Фантастика"}

# 4.1 Проверка: метод get_book_genre возвращает корректный жанр книги по её названию (исправил, добавил этот тест)
    def test_get_book_genre_by_name_returns_correct_genre(self, collector):
        collector.add_new_book("Матрица")
        collector.set_book_genre("Матрица", "Фантастика")
        assert collector.get_book_genre("Матрица") == "Фантастика"

# 5 Проверка: получаем список книг по жанру (исправлено)
    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book("Дюна")
        collector.add_new_book("Оно")
        collector.set_book_genre("Дюна", "Фантастика")
        collector.set_book_genre("Оно", "Ужасы")
        assert collector.get_books_with_specific_genre("Фантастика") == ["Дюна"]

# 6 Проверка: метод возвращает словарь всех книг
    def test_get_books_genre_returns_dict(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        assert collector.get_books_genre() == collector.books_genre

# 7 Проверка: фильтрация книг, подходящих детям
    def test_get_books_for_children_excludes_age_restricted(self, collector):
        collector.add_new_book("Оно")
        collector.add_new_book("Шрек")
        collector.set_book_genre("Оно", "Ужасы") # с возрастным рейтингом
        collector.set_book_genre("Шрек", "Мультфильмы") # можно детям
        assert collector.get_books_for_children() == ["Шрек"]

# 8 Проверка: можно добавить книгу в избранное только один раз
    def test_add_book_in_favorites_once(self, collector):
        collector.add_new_book("Дюна")
        collector.add_book_in_favorites("Дюна")
        collector.add_book_in_favorites("Дюна") # дублирование
        assert collector.get_list_of_favorites_books() == ["Дюна"]

# 9 Проверка: нельзя добавить в избранное книгу, которой нет
    def test_add_non_existing_book_to_favorites(self, collector):
        collector.add_book_in_favorites("Неизвестная") # нет в коллекции
        assert collector.get_list_of_favorites_books() == []

# 10 Проверка: удаление книги из избранного
    def test_delete_book_from_favorites_removes_book(self, collector):
        collector.add_new_book("Матрица")
        collector.add_book_in_favorites("Матрица")
        collector.delete_book_from_favorites("Матрица")
        assert collector.get_list_of_favorites_books() == []

# 11 Проверка: возврат актуального списка избранных книг
    def test_get_list_of_favorites_books_returns_correct_list(self, collector):
        collector.add_new_book("Шрек")
        collector.add_book_in_favorites("Шрек")
        assert collector.get_list_of_favorites_books() == ["Шрек"]
