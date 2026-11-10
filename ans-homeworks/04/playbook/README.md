# Ansible Playbook

## Описание

Данный playbook автоматизирует установку и настройку следующих компонентов:

- ClickHouse — база данных для хранения и обработки логов;
- Vector — инструмент для сбора, обработки и передачи данных наблюдаемости;
- LightHouse — веб-интерфейс для ClickHouse.

Для каждого из них используется отдельная Ansible-роль.

## Требования

- Ansible Core
- SSH-доступ к целевым хостам
- Поддерживаемые дистрибутивы Linux

## Роли

| Роль | Репозиторий | Описание |
| --- | --- | --- |
| ClickHouse | [ansible-clickhouse](https://github.com/AlexeySetevoi/ansible-clickhouse) | Устанавливает и настраивает ClickHouse |
| Vector | [vector-role](https://github.com/flamer322/vector-role) | Устанавливает и настраивает Vector |
| LightHouse | [lighthouse-role](https://github.com/flamer322/lighthouse-role) | Разворачивает LightHouse |

## Использование

Установка ролей:

```bash
ansible-galaxy install -r requirements.yml
```

Запуск playbook:

```bash
ansible-playbook -i inventory/prod.yml site.yml
```
