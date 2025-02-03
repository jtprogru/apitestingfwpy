# API Testing Framework Python

[![PyLint](https://github.com/jtprogru/apitestingfwpy/actions/workflows/pylint.yaml/badge.svg?branch=main)](https://github.com/jtprogru/apitestingfwpy/actions/workflows/pylint.yaml)
[![PyTest](https://github.com/jtprogru/apitestingfwpy/actions/workflows/pytest.yaml/badge.svg?branch=main)](https://github.com/jtprogru/apitestingfwpy/actions/workflows/pytest.yaml)

Данный репозиторий основан на [видео-уроке](https://youtu.be/_6ib59ddHnA).

Простой фреймворк тестирования API <https://restful-api.dev> реализованный на Python 3.12 с использованием [PyTest](https://docs.pytest.org/en/stable/) и [uv](https://docs.astral.sh/uv/).

Сервис <https://restful-api.dev> использует вот такую JSON-структуру данных:

```json
{
  "id": "7",
  "name": "Apple MacBook Pro 16",
  "data": {
    "year": 2019,
    "price": 1849.99,
    "CPU model": "Intel Core i9",
    "Hard disk size": "1 TB"
  },
  "createdAt": "2022-11-21T20:06:23.986Z"
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
task install
```

3. Выполнить запуск всех тестов:

```shell
task test
```

### Info

Важно учитывать, что сервис <https://restful-api.dev> имеет ограничения в 100 запросов в 1 день на IP.

Мысли для тренировки навыка написания кода зафиксированы в отдельном файле – [TODOs](TODOs.md).

## License

[Apache License 2.0](LICENSE)
