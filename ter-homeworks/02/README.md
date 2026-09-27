# Домашнее задание к занятию «Основы Terraform. Yandex Cloud»

### [Ссылка на репозиторий с кодом](https://github.com/Flamer322/ter-homeworks/tree/main/02/src)

## Задача 1

Созданный сервисный аккаунт

![image](images/task-1-1.png)

Открытая часть ключа в `variables.tf`

![image](images/task-1-2.png)

Ошибки - некорректные значения `platform_id` и `cores`  
По [документации](https://yandex.cloud/ru/docs/compute/concepts/performance-levels#minmax-configurations) были выбраны подходящие значения `standard-v2` и `2` 

![image](images/task-1-3.png)  
![image](images/task-1-4.png)
![image](images/task-1-5.png)

Успешное создание ресурса

![image](images/task-1-6.png)

Созданный ресурс в веб-интерфейсе и результат `curl ifconfig.me`

![image](images/task-1-7.png)
![image](images/task-1-8.png)

Параметры `preemptible = true` и `core_fraction = 5` могут быть использованы в процессе обучения для создания дешёвых ВМ

## Задача 2

Созданные переменные с типами и значениями по умолчанию

![image](images/task-2-1.png)

Использованные переменные вместо хардкод-значений в `main.tf`

![image](images/task-2-2.png)

Вывод `terraform plan`

![image](images/task-2-3.png)

## Задача 3

Созданные переменные ресурсов в `vms_platform.tf`

![image](images/task-3-1.png)  
![image](images/task-3-2.png)

Созданные новые подсеть в зоне `ru-central1-b` и ВМ `netology-develop-platform-db`

![image](images/task-3-3.png)
![image](images/task-3-4.png)

Результат `terraform apply`

![image](images/task-3-5.png)

Созданные ВМ в веб-интерфейсе

![image](images/task-3-6.png)

## Задача 4

Содержимое `outputs.tf` и вывод `terraform output`

![image](images/task-4.png)

## Задача 5

Новые переменные для интерполяции в `locals`

![image](images/task-5-1.png)

Содержимое `locals.tf`

![image](images/task-5-2.png)

Использование `local` переменных в `main.tf`

![image](images/task-5-3.png)

Результат `terraform apply`

![image](images/task-5-4.png)

## Задача 6

Map-переменная с конфигами ВМ в `vms_platform.tf`

![image](images/task-6-1.png)

Map-переменная для блока `metadata` в `locals.tf`

![image](images/task-6-2.png)

Новые переменные в `main.tf`

![image](images/task-6-3.png)

Вывод `terraform plan`

![image](images/task-6-4.png)

## Задача 7

Необходимые команды и их выводы

![image](images/task-7.png)

## Задача 8

Описание переменной `test` и её типа и команда для вывода требуемой строки

![image](images/task-8.png)

## Задача 9

Создание ресурсов с включенным `nat`

![image](images/task-9-1.png)

Подключение по ssh и смена паролей на обеих ВМ

![image](images/task-9-2.png)

Выключение `nat`

![image](images/task-9-3.png)

Создание ресурса `nat_gateway` по примеру из документации и выполнение `terraform apply`

![image](images/task-9-4.png)

Подключение через серийную консоль и проверка доступа к интернету

![image](images/task-9-5.png)

### [Ссылка на репозиторий с кодом](https://github.com/Flamer322/ter-homeworks/tree/main/02/src)
