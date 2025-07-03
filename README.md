# Пульт охраны  банка

Это сайт, который  можно подключить  к  удаленной  базе  данных с визитами  и  карточками пропуска  сотрудникв  банка.

## Как установить

1. Установите на компьютер `Python3`.

2. Скачайте все файлы проекта на свой компьютер.

```
https://github.com/IrinaQA423/django-orm-watching-storage-part-1-master.git
```

3. Установите зависимости.

```sh
pip install -r requirements.txt
```

### Где  хранить чувствительные данные?

В корне проекта создайте файл `.env` и поместите в него `DB_ENGINE`, `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `SECRET_KEY`.

![](https://github.com/IrinaQA423/gists1/blob/main/Screenshot_28.png?raw=true)

## Как запустить  программу?

1. Запустите файл `main.py`.

```sh
python main.py 
```

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org).
