# Homework 1
## Ермаков Василий
<p>
    Production-ready проект для обучения и предсказания сердечных заболеваний.
    <br />
    Использование с помощью коммандной строки.
</p>

Примечание: все команды выполнять из директории `ml_project`

### Предустановка
```
python3 -m venv venv
source venv/bin/activate
pip install .
```
### Использование. Обучение
```commandline
python3 ml/pipeline.py <путь до конфига>
```
<p>Пример:</p>

```commandline
python3 ml/pipeline.py configs/train_config.yaml
```
### Использование. Предсказание
```commandline
python3 ml/predict.py <путь до фичей> <путь до модели> [-o <путь вывода>]>
```
<p>Пример:</p>

```commandline
python3 ml/predict.py data/test.csv models/model1.pkl -o predictions/my_predict.csv
```
Предупреждение: По умолчанию ```data/test.csv``` совпадает с ```data/train.csv```

### Запуск тестов
```commandline
coverage run --rcfile=tests/coverage_config.coveragerc tests/tests.py
coverage report -m
coverage html --rcfile=tests/coverage_config.coveragerc
```
### Организация проекта
```commandline
├── configs                         <- Configs for models
│   ├── train_config_2.yaml
│   └── train_config.yaml
├── data                            <- data for training and testing
│   ├── test.csv
│   └── train.csv
├── EDA                             <- notebook with research
│   ├── heart_cleveland_upload.csv
│   └── Heart_Disease_EDA.ipynb
├── metrics                         <- all metrics during train will upload here
├── ml                              <- main package of the project with code for
│                                      training and testing
│   ├── data                        <- class for handling data
│   ├── __init__.py
│   ├── model                       <- main model
│   ├── params                      <- dataclasses to parse config
│   ├── pipeline.py                 <- code for training
│   ├── predict.py                  <- code for prediction
├── models                          <- all model artifacts will upload here
│                                      during training
├── predictions                     <- prediction will upload here by default
├── Readme.md
├── requirements.txt                <- all dependances
├── setup.py
└── tests                           <- tests for code
```

### Основные архитектурные решения
Было решено поддерживать модульную структуру проекта для упрощения отладки и использования кода.
Также основная часть кода модели была выполнена в виде пакета для удобства обращения к ней извне (папка `ml`).
Сперва было проведено исследование в ноутбуке (папка `EDA`).
Поддерживается конфигурирования с помощью `yaml` файлов (папка `configs`), написаны тесты (папка `tests`).
Для реализации ml модели выбрана библиотека `sklearn`, для конфигурирования `marshmallow` + датаклассы, для тестирования `unittest`, для отчета о покрытии `coverage`.
Работа с консолью `click`, сериализация артефактов `pickle`.
Настроен `CI` для автоматического прогона тестов и сохранения артефактов на `GitHub Actions`.
