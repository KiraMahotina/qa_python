from main import BooksCollector
import pytest
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    @pytest.mark.parametrize(
        "book_name",
        [
            "Гордость и предубеждение и зомби",
            "Нейромант",
            "Автостопом по галактике",
        ]
    )
    def test_add_new_book_valid_name(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()

    def test_add_new_book_duplicate_name(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_long_name(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби, Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize(
        "genre",
        [
            "Фантастика",
            "Ужасы",
            "Детективы",
            "Мультфильмы",
            "Комедии",
        ]
    )
    def test_set_book_genre_valid_genre(self, genre):
        collector = BooksCollector()
        collector.add_new_book('Книга с жанром')
        collector.set_book_genre('Книга с жанром', genre)
        assert collector.get_book_genre('Книга с жанром') == genre

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Жанр')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == ''

    @pytest.mark.parametrize(
        "book_name, genre, expected_genre",
        [
            ("Гордость и предубеждение и зомби", "Фантастика", "Фантастика"),
            ("Сияние", "Ужасы", "Ужасы"),
            ("1984", "Детективы", "Детективы"),
            ("Война и мир", "Эпопея", ""),
            ("Преступление и наказание", "Триллер", ""),
        ]
    )
    def test_get_book_genre_existing_book(self, book_name, genre, expected_genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        actual_genre = collector.get_book_genre(book_name)
        assert actual_genre == expected_genre

    def test_get_book_genre_non_existing_book(self):
        collector = BooksCollector()
        assert collector.get_book_genre('Несуществующая книга') == None

    @pytest.mark.parametrize(
        "genre, expected_books",
        [
            ("Фантастика", ['Гордость и предубеждение и зомби', 'Нейромант']),
            ("Ужасы", ['Сияние']),
            ("Детективы", []),
        ]
    )
    def test_get_books_with_specific_genre_existing_genre(self, genre, expected_books):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.add_new_book('Нейромант')
        collector.set_book_genre('Нейромант', 'Фантастика')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        assert collector.get_books_with_specific_genre(genre) == expected_books

    def test_get_books_with_specific_genre_non_existing_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.get_books_with_specific_genre('Ужасы') == []

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        assert collector.get_books_for_children() == ['Гордость и предубеждение и зомби']

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_not_in_books_genre(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' not in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_not_in_favorites(self):
        collector = BooksCollector()
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']