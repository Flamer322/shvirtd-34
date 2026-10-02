# Домашнее задание к занятию «Управляющие конструкции в коде Terraform»

### [Ссылка на коммит с кодом](https://github.com/Flamer322/ter-homeworks/commit/ba14ba430a8503adba9b9eed7bca08348f3a0233)

## Задача 1

Созданная группа безопасности в веб-интерфейсе

![image](images/task-1-2.png)

## Задача 2

Содержимое файла `count-vm.tf` с созданием ВМ при помощи `count`. ВМ добавлены в группу безопасности при помощи `network_interface.security_group_ids`

![image](images/task-2-1.png)

Содержимое файла `for_each-vm.tf` с созданием ВМ при помощи `for_each`. ВМ создаются после `count_vm` ВМ при помощи `depends_on`

![image](images/task-2-2.png)

Созданные ресурсы в веб-интерфейсе

![image](images/task-2-4.png)

## Задача 3

Содержимое файла `disk_vm.tf` с созданием ВМ `storage` и виртуальных дисков для неё

![image](images/task-3-1.png)

Диски созданной ВМ в веб-интерфейсе

![image](images/task-3-3.png)

## Задача 4

Содержимое файла `inventory.tf` для создания inventory-файла из шаблона

![image](images/task-4-1.png)

Содержимое шаблона `hosts.tftpl`

![image](images/task-4-2.png)

Содержимое результирующего файла `hosts.ini`

![image](images/task-4-3.png)

## Задача 5

Содержимое файла `output.tf` и вывод команды `terrafrom output`

![image](images/task-5.png)

## Задача 6

Содержимое файла `ansible.tf` для запуска `ansible-playbook` с `local-exec` и вывод при выполнении `terraform apply`

![image](images/task-6-1.png)

Изменение шаблона `hosts.ini` для использования внутренних ip при выключенном nat

![image](images/task-6-2.png)

Результирующий inventory-файл при выключенном nat

![image](images/task-6-3.png)

## Задача 7

Команда в `terraform console` для получения объекта без требуемых элементов

![image](images/task-7.png)

## Задача 8

Ошибки в шаблоне - закрывающая скобка для интерполяции в неправильном месте и пробел в свойстве ВМ `platform_id`. Дополнительно был добавлен перенос строки для корректных переносов в результате

![image](images/task-8-1.png)
![image](images/task-8-2.png)

Успешное выполнение `terraform apply`

![image](images/task-8-3.png)

Содержимое inventory-файла после выполнения

![image](images/task-8-4.png)

## Задача 9

Команды в `terraform console` для формирования требуемых списков

![image](images/task-9-1.png)
![image](images/task-9-2.png)
![image](images/task-9-3.png)

### [Ссылка на коммит с кодом](https://github.com/Flamer322/ter-homeworks/commit/ba14ba430a8503adba9b9eed7bca08348f3a0233)
