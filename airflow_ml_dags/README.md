# Homework 3
## Ермаков Василий
<p>
    Поднятый airflow для обработки постоянно поступающих данных.
</p>
Примечание: все команды выполняются из директории ml_airflow

### Предустановка
```commandline
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export DATA_DIR=$(pwd)/data
export FERNET_KEY=$(python3 -c "from cryptography.fernet import Fernet; FERNET_KEY = Fernet.generate_key().decode(); print(FERNET_KEY)")
```

### Запуск Airflow
```commandline
docker-compose up --build
```
<p>
UI Airflow доступен по http://localhost:8080
</p>
<p>
логин: admin
пароль: admin
</p>

![All dags](https://github.com/nokrolikno/Images/raw/main/all_dags.png)

Далее запустить даги generate_data, predict и train
![generate_data](https://github.com/nokrolikno/Images/raw/main/generate_data.png)
![predict](https://github.com/nokrolikno/Images/raw/main/predict.png)
![train](https://github.com/nokrolikno/Images/raw/main/train.png)

### Самооценка
<ol>
    <li value="0"> Локально поднимается Airflow, используя docker compose;
    <li> Реализован dag, который генерирует данные для обучения модели (5 баллов);
    <li> Реализован dag, который обучает модель еженедельно, используя данные за текущий день. В пайплайне 5 стадий (10 баллов);
    <li> Реализован dag, который использует модель ежедневно. Используется актуальная модель из data/model (5 баллов);
    <li> Все даги реализованы с помощью DockerOperator. Каждая таска запускается в собственном контейнере со своими зависимостями (10 баллов);
    <li> Проведена самооценка (1 балл);
</ol>
<p>Дополнительные баллы:</p>
<ol>
    <li value="6">Реализованы сенсоры на то, что данные готовы для дагов тренировки и обучения (3 балла);</li>
    <li value="10">Настроен алерт на случай падения дага (3 балла)</li>
</ol>

Итого: 37 баллов.