#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "store.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()


# Миграции - перенос моделей в базу данных
# python manage.py makemigrations - создает миграции
# python manage.py migrate - применяет миграции


# QuerySet - это список объектов модели, который можно фильтровать и сортировать.
# Методы QuerySet:
# get() - возвращает единственный объект модели, который соответствует фильтру, фильтр указывается в скобках
# create() - создает объект модели
# all() - возвращает все объекты модели
# filter() - возвращает отфильтрованные объекты модели
