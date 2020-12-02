import pytest

# область действия - класс, стоит использовать там,
# где вызванные данные статичны, например БД
# браузер запускаем для каждой функции отдельно
# чтобы кэш не мешал тестированию
@pytest.fixture(scope="class")
def prepare_faces():
    print("^_^", "\n")
    yield
    print(":3", "\n")

# по умолчанию область действия (scope) это функция. куда вызвали, там и применится
@pytest.fixture()
def very_important_fixture():
    print(":)", "\n")

# автоматически вызывается в каждую функцию, не стоит злоупотрублять
@pytest.fixture(autouse=True)
def print_smiling_faces():
    print(":-Р", "\n")


class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        # какие-то проверки
        pass

    def test_second_smiling_faces(self, prepare_faces):
        # какие-то проверки
        pass