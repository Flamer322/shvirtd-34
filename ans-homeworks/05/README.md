# Домашнее задание к занятию 5 «Тестирование roles»

## Ссылки

### [Ссылка на тег с решением задания Molecule](https://github.com/Flamer322/vector-role/releases/tag/v1.0.1)

### [Ссылка на тег с решением задания Tox](https://github.com/Flamer322/vector-role/releases/tag/v1.0.2)

## Задание Molecule

Запуск `molecule test -s ubuntu_xenial` в директории с ролью clickhouse

![image](images/task-1-1.png)

Повторный запуск после правки синтаксиса в `molecule.yml`

![image](images/task-1-2.png)

Dockerfile и `molecule.yml` для тестирования vector-role

![image](images/task-1-3.png)

Выполнение роли в `converge.yml`

![image](images/task-1-4.png)

Исправление ошибок в tasks роли

![image](images/task-1-5.png)

Успешное выполнение converge и idempotence

![image](images/task-1-6.png)
![image](images/task-1-7.png)

Добавленные проверки в `verify.yml`

![image](images/task-1-8.png)

Успешное выполнение verify

![image](images/task-1-9.png)

Результаты тестирования

![image](images/task-1-10.png)

## Задание Tox

Первоначальный запуск `tox`

![image](images/task-2-1.png)

Конфигурация `prepare.yml` и `molecule.yml` для настройки контейнера и запуска облегчённого сценария

![image](images/task-2-2.png)

Выполнение роли в `converge.yml` и упрощённые проверки `verify.yml`

![image](images/task-2-3.png)

Исправление ошибок в tasks и handlers роли

![image](images/task-2-4.png)

Фиксация конкретных зависимостей в `tox.ini` для успешной работы с python3.9

![image](images/task-2-5.png)

Результаты тестирования

![image](images/task-2-6.png)

## Ссылки

### [Ссылка на тег с решением задания Molecule](https://github.com/Flamer322/vector-role/releases/tag/v1.0.1)

### [Ссылка на тег с решением задания Tox](https://github.com/Flamer322/vector-role/releases/tag/v1.0.2)
