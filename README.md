# Sprint_4
## Юнит-тестирование

## BooksCollector: Автотесты
Этот проект реализует класс BooksCollector, который позволяет управлять коллекцией книг: добавлять их, устанавливать жанры, добавлять в избранное и получать списки книг по жанрам и возрастным ограничениям.

---
# Реализованные автотесты:

## Тесты инициализации: 
`test_init_sets_up_empty_and_default_values` - проверка, что при создании объекта поля `books_genre`, `favorites`, `genre` и `genre_age_rating` инициализируются правильно. 

## Тесты метода `add_new_book`:
`test_add_new_book_various_names` - книга добавляется, если имя валидное. Не добавляется, если имя пустое или длина больше 40 символов.
`test_add_duplicate_book_only_once` - повторное добавление одной и той же книги не дублирует её.

## Тесты метода `set_book_genre`:
`test_set_book_genre_valid_for_existing_book` - установка жанра успешна, если книга существует и жанр допустим.

## Тесты метода `get_book_genre`:

Проверка через `test_get_book_genre_by_name_returns_correct_genre` - выводит жанр книги по её имени.

## Тест метода `get_books_with_specific_genre`:

`test_get_books_with_specific_genre` - возвращает список книг с заданным жанром. Возвращает пустой список, если жанр не найден.

## Тест метода `get_books_genre`:

`test_get_books_genre_returns_dict` - возвращает актуальный словарь всех добавленных книг и их жанров.

## Тест метода `get_books_for_children`:

`test_get_books_for_children_excludes_age_restricted` - исключает книги с жанрами из `genre_age_rating` (например, "Ужасы").

## Тест метода `add_book_in_favorites`:

`test_add_book_in_favorites_once` - книга добавляется в favorites, если она есть в `books_genre`. Повторное добавление не дублирует книгу.

`test_add_non_existing_book_to_favorites` - книга не добавляется, если её нет в `books_genre`.

## Тест метода `delete_book_from_favorites`:

`test_delete_book_from_favorites_removes_book` - удаляет книгу из списка `favorites`, если она там есть. 

## Тест метода `get_list_of_favorites_books`:

`test_get_list_of_favorites_books_returns_correct_list` - возвращает список избранных книг.

---
