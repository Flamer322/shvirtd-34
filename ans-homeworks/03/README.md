# Домашнее задание к занятию 3 «Использование Ansible»

## Описание плейбука

Этот плейбук выполняет установку и настройку ClickHouse, Vector и LightHouse на соответствующих хостах. Он скачивает необходимые дистрибутивы, устанавливает пакеты, настраивает конфигурационные файлы, проверяет их корректность и управляет службами.

## Установка и настройка ClickHouse

### Параметры

hosts: clickhouse  
become: true

### Хэндлеры

Restart Clickhouse  
Перезапускает службу ClickHouse для применения изменений конфигурации.

### Задачи

- Get clickhouse distrib  
  Скачивает дистрибутивы ClickHouse для архитектуры AMD64 в директорию /tmp  
  Теги: clickhouse, distr

- Update apt cache  
  Обновляет кэш пакетов APT  
  Теги: clickhouse, distr

- Install clickhouse packages  
  Устанавливает пакеты ClickHouse с использованием модуля APT  
  Теги: clickhouse, distr

- Configure ClickHouse listen host  
  Создаёт конфигурационный файл listen.xml, разрешающий ClickHouse принимать подключения со всех сетевых интерфейсов (0.0.0.0)  
  Теги: clickhouse, config  
  Notify: Restart Clickhouse

- Apply ClickHouse configuration changes  
  Выполняет все отложенные хэндлеры для применения изменений конфигурации  
  Теги: clickhouse, config

- Ensure clickhouse service is started  
  Запускает службу ClickHouse и добавляет её в автозагрузку  
  Теги: clickhouse, start service

- Wait for clickhouse-server to be ready  
  Ожидает, пока сервер ClickHouse станет доступен на порту 9000. Ожидание начинается через 10 секунд и продолжается не более 300 секунд  
  Теги: clickhouse, wait

- Create database  
  Создаёт базу данных logs в ClickHouse. Повторное выполнение не считается ошибкой, если база уже существует  
  Теги: clickhouse, db

## Установка и настройка Vector

### Параметры

hosts: vector  
become: true

### Хэндлеры

Хэндлеры отсутствуют.

### Задачи

- Get vector distrib  
  Скачивает дистрибутив Vector для архитектуры AMD64 в директорию /tmp  
  Теги: vector, distr

- Update apt cache  
  Обновляет кэш пакетов APT  
  Теги: vector, distr

- Install vector  
  Устанавливает пакет Vector из скачанного DEB-дистрибутива с использованием модуля APT  
  Теги: vector, distr

- Deploy vector configuration  
  Развёртывает конфигурационный файл Vector из шаблона Jinja2 templates/vector.yaml.j2 по указанному пути  
  Теги: vector, config

- Validate vector configuration  
  Проверяет корректность конфигурационного файла Vector с помощью команды vector validate. Задача не отмечается как изменяющая состояние системы  
  Теги: vector, config

- Ensure vector service is started  
  Запускает службу Vector и добавляет её в автозагрузку  
  Теги: vector, start service

## Установка и настройка LightHouse

### Параметры

hosts: lighthouse  
become: true

### Хэндлеры

Reload Nginx  
Перезагружает конфигурацию Nginx без полного перезапуска службы для применения изменений.

### Задачи

- Install unzip  
  Устанавливает утилиту unzip, необходимую для работы с ZIP-архивами  
  Теги: lighthouse, distr

- Get lighthouse static  
  Скачивает ZIP-архив репозитория LightHouse с GitHub и распаковывает его в директорию /opt. Если файл index.html уже существует в целевой директории, повторная распаковка не выполняется  
  Теги: lighthouse, distr

- Install nginx  
  Устанавливает веб-сервер Nginx  
  Теги: nginx, distr

- Deploy lighthouse nginx config  
  Развёртывает конфигурационный файл Nginx из шаблона Jinja2 templates/lighthouse.conf.j2 в /etc/nginx/sites-available/default  
  Теги: nginx, config  
  Notify: Reload Nginx

- Validate nginx configuration  
  Проверяет корректность конфигурации Nginx с помощью команды nginx -t. Задача не отмечается как изменяющая состояние системы  
  Теги: nginx, config

- Ensure nginx service is started  
  Запускает службу Nginx и добавляет её в автозагрузку  
  Теги: nginx, start service

## Переменные

### ClickHouse

clickhouse_version: Версия ClickHouse для установки.  
clickhouse_packages: Список пакетов ClickHouse для установки:

- clickhouse-common-static
- clickhouse-client
- clickhouse-server

### Vector

vector_version: Версия Vector для установки.  
vector_config_path: Путь к конфигурационному файлу Vector (/etc/vector/vector.yaml).

### LightHouse

lighthouse_directory: Путь к директории с распакованными статическими файлами LightHouse (/opt/lighthouse-master).  
