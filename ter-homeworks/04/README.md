# Домашнее задание к занятию «Продвинутые методы работы с Terraform»

### [Ссылка на на папку с кодом в отдельной ветке](https://github.com/Flamer322/ter-homeworks/tree/terraform-04/04/src)

## Задача 1

Шаблон cloud-init `cloud-init.yaml.tpl` с добавленным ssh ключём и установкой nginx

![image](images/task-1-1.png)

Использование шаблона с ssh ключём и ресурсы ВМ с `labels` в terraform (скриншот сделан чуть позже)

![image](images/task-1-2.png)

Проверка nginx на ВМ после `terraform apply`

![image](images/task-1-3.png)

Созданные ВМ в веб-интерфейсе

![image](images/task-1-4.png)

Вывод модуля в `terraform console`

![image](images/task-1-5.png)

## Задача 2

Провайдеры созданного модуля

![image](images/task-2-1.png)

Переменные

![image](images/task-2-2.png)

Создание сети и подсети

![image](images/task-2-3.png)

Передача сети и подсети в output

![image](images/task-2-4.png)

Вывод информации модуля в `terraform console`

![image](images/task-2-5.png)

Применение созданного модуля

![image](images/task-2-6.png)

Замена ранее используемых сети и подсети на информацию из модуля

![image](images/task-2-7.png)

Сгенерированная документация

![image](images/task-2-8.png)

## Задача 3

Список ресурсов в стейте и удаление модулей vm и vpc

![image](images/task-3-1.png)

Импорт удалённых модулей

![image](images/task-3-2.png)
![image](images/task-3-3.png)
![image](images/task-3-4.png)

Вывод `terraform plan` после импорта

![image](images/task-3-5.png)

## Задача 4

Изменённые переменные модуля для создания нескольких подсетей

![image](images/task-4-1.png)

Создание нескольких подсетей при помощи for_each

![image](images/task-4-2.png)

Изменение output для выдачи всех созданных подсетей

![image](images/task-4-3.png)

Изменённые переменные в проекте

![image](images/task-4-4.png)

Передача переменных в модуль

![image](images/task-4-5.png)

Передача всех подсетей из модуля в создаваемые ВМ

![image](images/task-4-6.png)

Вывод `terraform plan`

![image](images/task-4-7.png)
![image](images/task-4-8.png)
![image](images/task-4-9.png)
![image](images/task-4-10.png)
![image](images/task-4-11.png)

Созданная сеть и её подсети

![image](images/task-4-12.png)

Созданные ВМ

![image](images/task-4-13.png)

## Задача 5

Переменные в модуле для кластера mysql

![image](images/task-5-1.png)

Создание кластера в модуле

![image](images/task-5-2.png)

Выдача кластера в output модуля

![image](images/task-5-3.png)

Переменные в модуле для создания БД и пользователя в кластере

![image](images/task-5-4.png)

Создание БД и пользователя

![image](images/task-5-5.png)

Переменные для модулей в проекте

![image](images/task-5-6.png)

Использование модулей в проекте

![image](images/task-5-7.png)

`terraform plan` с `ha=false`

![image](images/task-5-8.png)
![image](images/task-5-9.png)

Результат `terraform apply`

![image](images/task-5-10.png)

Созданный кластер в веб-интерфейсе

![image](images/task-5-11.png)

Хосты в кластере

![image](images/task-5-12.png)

`ha=true`

![image](images/task-5-13.png)

Вывод `terraform plan`

![image](images/task-5-14.png)

Результат `terraform apply`

![image](images/task-5-15.png)

Изменённый кластер в веб-интерфейсе

![image](images/task-5-16.png)

Хосты в кластере

![image](images/task-5-17.png)

## Задача 6

Переменные для s3 бакета

![image](images/task-6-1.png)

Код для создания бакета с использованием модуля из git

![image](images/task-6-2.png)

Конфигурация провайдеров

![image](images/task-6-3.png)

Вывод `terraform apply`

![image](images/task-6-4.png)
![image](images/task-6-5.png)

Созданный бакет в веб-интерфейсе

![image](images/task-6-6.png)

## Задача 7

docker-compose с vault

![image](images/task-7-1.png)

Создание нового секрета

![image](images/task-7-2.png)

Переменные для vault

![image](images/task-7-3.png)

Провайдер для vault

![image](images/task-7-4.png)

Код для добавления нового секрета и чтения его и ранее созданного вручную

![image](images/task-7-5.png)

Вывод `terraform apply`

![image](images/task-7-6.png)

Созданный секрет в интерфейсе vault

![image](images/task-7-7.png)

## Задача 8

Переменные отдельного root-модуля для vpc

![image](images/task-8-1.png)

Провайдеры vpc

![image](images/task-8-2.png)

Код для создания vpc с использованием локального модуля

![image](images/task-8-3.png)

output с сетью и подсетями

![image](images/task-8-4.png)

Вывод `terraform apply` в root-модуле vpc

![image](images/task-8-5.png)
![image](images/task-8-6.png)

Переменные отдельного root-модуля для vm

![image](images/task-8-7.png)

Провайдеры vm

![image](images/task-8-8.png)

Код для создания vm с использованием модуля из git и terraform remote state

![image](images/task-8-9.png)

Вывод `terraform apply`

![image](images/task-8-10.png)
![image](images/task-8-11.png)

Созданные ресурсы в веб-интерфейсе

![image](images/task-8-12.png)

### [Ссылка на на папку с кодом в отдельной ветке](https://github.com/Flamer322/ter-homeworks/tree/terraform-04/04/src)
