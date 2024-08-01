# apitestingfwpy

Данный репозиторий основан на [видео-уроке](https://youtu.be/_6ib59ddHnA).

Простой фреймворк тестирования API https://restful-api.dev реализованный на Python 3.12 с использованием [PyTest](https://docs.pytest.org/en/stable/) и [Poetry](https://python-poetry.org).

Сервис https://restful-api.dev использует вот такую JSON-структуру данных:

```json
{
    "name": "Apple MacBook Air 16",
    "data": {
        "year": 2016,
        "price": 900.00,
        "CPU model": "Intel Core i3",
        "Hard disk size": "128 GB"
    }
}
```

## Locally testing

1. Клонировать данный репозиторий и перейти в него:

```shell
git clone git@github.com:jtprogru/apitestingfwpy.git
cd apitestingfwpy
```

2. Установить зависимости:

```shell
poetry install --no-root
```

3. Выполнить запуск всех тестов:

```shell
poetry run pytest -v
```

## License

[Apache License 2.0](LICENSE)
