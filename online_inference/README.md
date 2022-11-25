# Homework 2
## Ермаков Василий
<p>
    Обертка для проекта обучения модели и предсказания сердечных заболеваний. Вид пригодный для использования онлайн.
</p>

Примечание: все команды выполняются из директории online_inference
### Предустановка
```commandline
python3 -m venv .venv
source .venv/bin/activate
pip install .
export URL_TO_MODEL="https://drive.google.com/file/d/1zf5TWzifzDIS8Fl_kN4gunKPW42xJcva/view?usp=share_link"
```
Примечание: В переменную окружение помещается ссылка на google drive модели.

### Запуск сервера
```commandline
cd rest_service
uvicorn main:app
```

### Тестирования endpoint /predict
```commandline
pytest rest_service/tests.py
```

### Сгенерировать запросы к серверу
```commandline
python3 make_requests/generate_data.py
python3 make_requests/make_requests.py --ip <ip, default=127.0.0.1> --port <port, default=8000>
Например:
python3 make_requests/make_requests.py --ip 127.0.0.1 --port 8000
```

### Создать докер образ
```commandline
docker build -t nokrolikno/ml_web_service:v1 .
```

### Пулл docker image из docker hub
```commandline
docker pull nokrolikno/ml_web_service:v1
```

### Запуск web сервиса в докере
```commandline
docker run -p 8000:8000 nokrolikno/ml_web_service:v1
```

### Запросы к активному серверу в docker
```commandline
python3 make_requests/generate_data.py
python3 make_requests/make_requests.py --ip 0.0.0.0 --port 8000
```

### Самооценка
<ol>
    <li> Обернул inference модели в rest сервис на FastAPI, есть endpoint /predict (3 балла);
    <li> Присутствует endpoint /health, который возвращает 200, когда модель готова к работе (1 балл);
    <li> Написан unittest для /predict (3 балла);
    <li> Написан скрипт, который делает запросы к сервису (2 балла);
    <li> Написан Dockerfile. На его основе собирается образ и запускается локально контейнер с web сервисом. Dockerfile закоммичен, в README описана команда сборки (4 балла);
    <li> Образ опубликован в docker hub
https://hub.docker.com/layers/nokrolikno/ml_web_service/v1/images/sha256-e38b9d0f4d1141c3b7be9c57b9178bec8c2c38e87cb518e26a7b9adc56f858e6?context=repo (2 балла);
    <li> В README описаны команды docker pull/run (1 балл);
    <li> Проведена самооценка (1 балл);
</ol>
<p>Дополнительные баллы:</p>
<ul>
    <li>Сервис скачивает модель из google drive, ссылка передается через переменную окружения (2 балла);</li>
</ul>

Итого: 19 баллов.