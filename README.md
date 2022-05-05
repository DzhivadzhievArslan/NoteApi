# Развертывание на локальной машине
1. Создаем виртуальное окружение: python3 -m venv flask_venv
2. Активируем venv: source flask_venv/bin/activate
3. Устанавливаем зависимости: pip install -r requirements.txt
4. Создать переменную окружения: export DATABASE_URL=<path_to_db>
5. Создаем локальную БД: flask db upgrade
6. Запуск проекта: flask run

# Миграции
1. Активировать миграции: flask db init
2. Создать миграцию: flask db migrate -m "comment"
3. Применить миграции: flask db upgrade