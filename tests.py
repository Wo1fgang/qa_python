from main import BooksCollector
import pytest


@pytest.fixture
def collector():
    return BooksCollector()


class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('book_name, expected_length', [
        ('Невероятно длинное название книги, чтобы оно было длиннее сорока одного символа', 0),
        ('', 0),
        ('Новая книга', 1),
    ])
    def test_add_new_book_with_different_names(self, collector, book_name, expected_length):
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == expected_length

    def test_set_book_genre(self, collector):
        collector.add_new_book('Новая книга')
        collector.set_book_genre('Новая книга', 'Ужасы')
        assert collector.books_genre == {'Новая книга': 'Ужасы'}

    def test_get_book_genre(self, collector):
        collector.add_new_book('Новая книга')
        collector.set_book_genre('Новая книга', 'Ужасы')
        assert collector.books_genre.get('Новая книга') == 'Ужасы'

    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book('Новая книга')
        collector.set_book_genre('Новая книга', 'Ужасы')
        collector.add_new_book('Новая книга #2')
        collector.set_book_genre('Новая книга #2', 'Ужасы')
        assert collector.get_books_with_specific_genre('Ужасы') == ['Новая книга', 'Новая книга #2']

    def test_books_genre(self, collector):
        collector.add_new_book('Новая книга')
        collector.set_book_genre('Новая книга', 'Ужасы')
        assert collector.get_books_genre() == {'Новая книга': 'Ужасы'}

    def test_get_books_for_children(self, collector):
        collector.add_new_book('Новая книга')
        collector.set_book_genre('Новая книга', 'Ужасы')
        collector.add_new_book('Новая книга #2')
        collector.set_book_genre('Новая книга', 'Фантастика')
        assert len(collector.get_books_for_children()) == 1

    def test_add_book_in_favourites(self, collector):
        collector.add_new_book('Новая книга')
        collector.add_book_in_favorites('Новая книга')
        assert collector.favorites == ['Новая книга']

    def test_delete_book_from_favourites(self, collector):
        collector.add_new_book('Новая книга #1')
        collector.add_book_in_favorites('Новая книга #1')
        collector.add_new_book('Новая книга #2')
        collector.add_book_in_favorites('Новая книга #2')
        collector.delete_book_from_favorites('Новая книга #2')
        assert collector.favorites == ['Новая книга #1']

    def test_get_list_of_favourites_books(self, collector):
        collector.add_new_book('Новая книга')
        collector.add_book_in_favorites('Новая книга')
        collector.add_new_book('Новая книга #2')
        collector.add_book_in_favorites('Новая книга #2')
        assert collector.favorites == ['Новая книга', 'Новая книга #2']
