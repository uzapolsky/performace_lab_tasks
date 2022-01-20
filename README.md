## Решение тестовых заданий PerformanceLab

Все решения запускаются с отправкой данных в виде **аргументов командной строки**.

### Примеры

```sh
python3 task1/task1.py 5 4
python3 task2/task2.py file1.txt file2.txt
python3 task3/task3.py values.json tests.json
python3 task4/task4.py file.txt
```

Для уточнения аргументов можно вызвать справку:

```sh
python3 task3/task3.py -h
```

Вывод:

```sh
usage: task3.py [-h] values_file tests_file

positional arguments:
  values_file  filepath to tests results json
  tests_file   filepath to report structure json
```
