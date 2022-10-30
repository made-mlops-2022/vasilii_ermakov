# Homework 1
## Ермаков Василий
<p>
    Production-ready проект для обучения модели и предсказания сердечных заболеваний.
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
or
ml_train <путь до конфига>
```
<p>Пример:</p>

```commandline
ml_train configs/train_config.yaml
```
### Использование. Предсказание
```commandline
python3 ml/predict.py <путь до фичей> <путь до модели> [-o <путь вывода>]
or
ml_predict <путь до фичей> <путь до модели> [-o <путь вывода>]
```
<p>Пример:</p>

```commandline
ml_predict data/test.csv models/model1.pkl -o predictions/my_predict.csv
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
├── linters                         <- configs for linters
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
Также основная часть кода модели была выполнена в виде пакета для удобства обращения к ней извне (папка `ml`). Добавлено несколько entry points для удобства использования.
Сперва было проведено исследование в ноутбуке (папка `EDA`).
Поддерживается конфигурирования с помощью `yaml` файлов (папка `configs`), написаны тесты (папка `tests`).
Для реализации ml модели выбрана библиотека `sklearn`, для конфигурирования `marshmallow` + датаклассы, для тестирования `unittest`, для отчета о покрытии `coverage`.
Работа с консолью `click`, сериализация артефактов `pickle`.
Настроен `CI` для автоматического прогона тестов и сохранения артефактов на `GitHub Actions`.
Для тестов генерируются синтетические данные собственной функцией.

### Самооценка
<ol>
    <li value="0"> В описании к пулл-реквесту описаны основные архитектурные решения (1 балл);
    <li> В пулл реквесте проведена самооценка (1 балл);
    <li> Исследование выполнено, ноутбук закоммичен (1 балл);
    <li> Написан класс для тренировки модели. Вызов оформлен как утилита командной строки. Инструкция в README есть (3 балла);
    <li> Написана функция predict (вызов оформлен как утилита командной строки), которая примет на вход артефакт от обучения, тестовую выборку (без меток) и запишет предикт по заданному пути, инструкция по вызову записана в readme (3 балла);
    <li> Проект имеет модульную структуру (2 балла);
    <li> Использованы логгеры (2 балла);
    <li> Написаны тесты на отдельные модули и на прогон обучения и predict (3 балла);
    <li> Для тестов генерируются синтетические данные собственной функцией (2 балла);
    <li> Обучение модели конфигурируется с помощью конфигов в yaml. Две корректные конфигурации закоммичено (3 балла);
    <li> Для сущностей из конфига используются датаклассы (2 балла);
    <li> Трансформер в модели используется, но вряд ли он кастомный; тестов на него нет (0 баллов);
    <li> Все зависимости в проекте зафиксированы (1 балл);
    <li> Настроен CI для прогона тестов, линтера на основе github actions (3 балла).
</ol>
<p>Дополнительные баллы:</p>
<ul>
    <li>Метрики логруются (1 балл);</li>
    <li>В модели выделено несколько entry points: ml_train и ml_predict (1 балл);</li>
    <li>Датасет добавлен под контроль версий (1 балл);</li>
</ul>
