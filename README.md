# task-manager

## Запуск unit тестов:
Команды выполнять из папки проекта
```
pytest unit_tests.py
```

## Запуск интеграционных тестов
Команды выполнять из папки проекта
```
python -m uvicorn main:app --reload
pytest integration_tests.py
```
