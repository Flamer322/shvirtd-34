# Домашнее задание к занятию Использование Terraform в команде

### [Ссылка на на папку с кодом в отдельной ветке](https://github.com/Flamer322/ter-homeworks/tree/terraform-05/04/src)

## Задача 1

Конфигурация для работы tflint

![image](images/task-1-1.png)

Результаты проверки tflint и checkov

![image](images/task-1-2.png)
![image](images/task-1-3.png)
![image](images/task-1-4.png)
![image](images/task-1-5.png)

В проекте были обнаруженые следующие типы ошибок:

- использование default ветки как source модуля / не использование для этого тэга с версией или хэша коммита
- использование провайдеров без уточнения версии
- создание кластера БД без группы безопасности

## Задача 2

Созданный сервисный пользователь для работы с terraform

![image](images/task-2-1.png)

Для него добавлен authorized key

![image](images/task-2-2.png)

Создан файл с данными ключа

![image](images/task-2-3.png)

Конфигурация backend для terraform

![image](images/task-2-4.png)

Миграция state в S3

![image](images/task-2-5.png)

Ошибка доступа при блокировке state и принудильная разблокировка

![image](images/task-2-6.png)

## Задача 3

[Ссылка на PR](https://github.com/Flamer322/ter-homeworks/pull/1)

## Задача 4

Проверка правил валидации с верными значениями

![image](images/task-4-1.png)

Проверка правил валидации с неверными значениями

![image](images/task-4-2.png)

## Задача 5

Проверка различных значений для первой переменной

![image](images/task-5-1.png)

Проверка различных значений для второй переменной

![image](images/task-5-2.png)

## Задача 6

Конфигурация workflow для GitHub actions

![image](images/task-6-1.png)

Созданные ключи для использования в workflow

![image](images/task-6-2.png)

Заполненные переменные среды для GitHub actions в настройках репозитория

![image](images/task-6-3.png)

Отработавший workflow

![image](images/task-6-4.png)
![image](images/task-6-5.png)

[Ссылка на workflow](https://github.com/Flamer322/ter-homeworks/actions/runs/37664697727/job/112940829706)

## Задача 7

Файл провайдеров для модуля

![image](images/task-7-1.png)

Переменные модуля

![image](images/task-7-2.png)

Ресурсы для создания сервисного аккаунта, задания ему разрешений, создания его static access key и бакета со случайным суффиксом у имени

![image](images/task-7-3.png)

Output'ы с именем бакета, данными access key и примерами конфигураций aws и backend

![image](images/task-7-4.png)

Вывод output'ов в консоль

![image](images/task-7-5.png)

### [Ссылка на на папку с кодом в отдельной ветке](https://github.com/Flamer322/ter-homeworks/tree/terraform-05/04/src)
