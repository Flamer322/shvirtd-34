# Домашнее задание к занятию «Введение в Terraform»

## Задача 0

Склонированный проект, установленные terraform и docker

![image](images/task-0.png)

## Задача 1

Установка зависимостей terraform

![image](images/task-1-1.png)

Файл terraform для секретов в проекте - personal.auto.tfvars

![image](images/task-1-2.png)

Содержимое ресурса random_password в terraform.tfstate

![image](images/task-1-3.png)

Ошибки в конфигурации - недостающий label с именем ресурса и некорректное имя ресурса

![image](images/task-1-4.png)

Ошибки в конфигурации - неправильное имя ресурса с паролем и неправильное имя атрибута с результатом

![image](images/task-1-5.png)

Исправленная конфигурация, успешное выполнение и вывод `docker ps`

![image](images/task-1-6.png)

Изменённое имя контейнера и вывод `docker ps`  
Ключ `-auto-approve` может быть использован для автоматизации, так как с ним не требуется подтверждение действия. Однако при его использовании можно применить ошибочную конфигурацию, не имея возможности отреагировать на план изменений

![image](images/task-1-7.png)

Уничтожение созданных ресурсов и содержимое terraform.tfstate

![image](images/task-1-8.png)

Docker-образ не удаляется из-за флага `keep_locally`. При его установке в `true`, terraform не удаляет образ даже при удалении ресурсов проекта

![image](images/task-1-9.png)
![image](images/task-1-10.png)

## Задача 2

Создание ВМ в yandex cloud при помощи terraform  
Конфигурация для создания ВМ - [main.tf](src/yandex-cloud/main.tf)

![image](images/task-2-1.png)

Установка docker на созданной ВМ

![image](images/task-2-2.png)

Запуск контейнера на ВМ при помощи terraform и удалённого docker контекста  
Конфигурация для запуска контейнера - [main.tf](src/docker/main.tf)

![image](images/task-2-3.png)

Проверка env переменных внутри контейнера

![image](images/task-2-4.png)

## Задача 3

Выполненение кода при помощи opentofu (предварительно были переустановлены зависимости при помощи `tofu init`)

![image](images/task-3-1.png)
![image](images/task-3-2.png)
