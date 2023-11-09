# TODO решите задачу
import json
def task() -> float:
    file = "input.json"
        #прочитаем файл JSON
    with open(file,'rt') as f:
        #десериализация
        json_data = json.load(f)
        #подсчет суммы
    sum_data = sum([item["score"] * item["weight"] for item in json_data])
    round_sum = round(sum_data, 3)
    return round_sum

print(task())


