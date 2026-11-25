# Домашнее задание к занятию 5. «Практическое применение Docker»

## Задача 1

Dockerfile с multistage сборкой

![image](images/task-1-1.png)

Запуск БД и приложения в docker

![image](images/task-1-2.png)

Запуск приложения при помощи venv

![image](images/task-1-3.png)

Изменённый код для управления названием таблицы - <https://github.com/Flamer322/shvirtd-example-python/blob/main/main.py>

Записи в новой таблице

![image](images/task-1-4.png)

## Задача 2

Результат сканирования

![image](images/task-2-1.png)
![image](images/task-2-2.png)

Файл отчёта - [vulnerabilities.csv](vulnerabilities.csv)

## Задача 3

Compose.yaml с include и сервисами web и db - <https://github.com/Flamer322/shvirtd-example-python/blob/main/compose.yaml>

Скриншот sql-запроса

![image](images/task-3.png)

## Задача 4

Ссылка на скрипт для установки и запуска - <https://github.com/Flamer322/shvirtd-example-python/blob/main/install.sh>  
Репозиторий скачивается в /opt/app, т.к. в /opt уже есть директория containerd

ВМ добавлена в ssh config

![image](images/task-4-1.png)

Контекст добавлен при помощи hostname из ssh config, список контекстов и результат удалённого docker ps -a

![image](images/task-4-2.png)

Скриншот sql-запроса в ВМ

![image](images/task-4-3.png)

Ссылка на fork - <https://github.com/Flamer322/shvirtd-example-python/tree/main>

## Задача 5

Ссылка на скрипт для бэкапа - <https://github.com/Flamer322/shvirtd-example-python/blob/main/backup.sh>  
Был использован отличный docker образ, который может работать с caching_sha2_password 

Crontab и созданные резервные копии

![image](images/task-5.png)

## Задача 6

Вывод dive

![image](images/task-6-1.png)

Сохранение образа docker, просмотр его слоёв

![image](images/task-6-2.png)
