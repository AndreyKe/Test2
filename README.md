# Валидатор кодовой фразы с GUI.

## Запуск
Для установки зависимостей в виртуальном окружении:
```bash
python3 -m venv venv
source venv/bin/activate
```
Установка фреймворка для GUI:
```bash
pip install PyQt5
```
Запуск приложения:
```bash
python3 app.py
```
## Структура проекта

```bash
.
├── app.py  - точка входа
├── controller
│   ├── __init__.py
│   └── secret_controller.py - контроллер секретов
├── model
│   ├── __init__.py
│   └── secret_model.py - модель секретов
└── view
    ├── __init__.py
    └── main_window.py - интерфейс приложения
```

## Описание работы
- При запуске приложения генерируетс секретный ключ, его можно увидеть в терминале
- Пользователю нужно ввести последние два символа, подразумевается, что он должен знать код
  - Если пользователь нажимает кнопку "Ok": 
    - Если введен правильный код, то выводится статус "Correct!"
    - Если введен неправильный код, то выводится статус "Error!"
  - Если пользователь наижимает кнопку "Cancel":
    - Все коментарии и введеный код сбрасываются
