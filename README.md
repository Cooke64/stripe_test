# Тестовое задание.

## Описание

Данный проект представляет собой онлайн магазин,в котором реализованы следующие **возможности**:
- По запросу на этот адрес http://127.0.0.1:8000/buy/id  получить Stripe Session Id для оплаты выбранного Item по его id.
- По запросу на этот адрес http://127.0.0.1:8000/item/id будет информация о выбранном Item и кнопка Buy.
## Технлологии

- Django
- Strip
- SQLite

## Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

```git clone git@github.com:Cooke64/stripe_test.git```

```cd ranks```

Cоздать и активировать виртуальное окружение:

```python -m venv env```

```venv/scripts/activate```

При необходимости обновить pip

```python -m pip install --upgrade pip```

Установить зависимости из файла requirements.txt:

```pip install -r requirements.txt```

Выполнить миграции:

```python manage.py migrate```

Создать файл e.env, в котором необходимо создать переменные:

- STRIPE_PUBLISHABLE_KEY
- STRIPE_SECRET_KEY

Запустить проект:

```python manage.py runserver```
