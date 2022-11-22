# Учебный проект по джанго
# Инструкция по установке
1. `python -v venv <venv_name>`
2. `activate source venv_name/bin/activate` (`deactivate`)
3. `pip install -r requirements.txt`
4. `python manage.py migrate`
Применяем миграции и создаем пустую базу даных
5. `python manage.py runserver
Запускаем сервер

#Полезные команды

1. `py-shell run: python manage.py shell_plus --ipython`