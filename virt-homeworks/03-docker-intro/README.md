# Домашнее задание к занятию 4. «Оркестрация группой Docker контейнеров на примере Docker Compose»

## Задача 1

Ссылка в требуемом формате - <https://hub.docker.com/flamer322/custom-nginx/general>

## Задача 2

Скриншот консоли

![image](images/task-2.png)

## Задача 3

Контейнер останавливается при Ctrl+C в консоли, т.к. он прерывает процесс nginx, который обрабатывает контейнер

![image](images/task-3-1.png)

Проблема с curl после изменения вызывана тем, что nginx внутри контейнера слушает 81 порт, а docker пробрасывает 80

![image](images/task-3-2.png)

## Задача 4

Скриншот консоли

![image](images/task-4.png)

## Задача 5

Config контейнера custom-nginx

![image](images/task-5-1.png)

Скриншот portainer

![image](images/task-5-2.png)

Скриншот консоли

![image](images/task-5-3.png)
