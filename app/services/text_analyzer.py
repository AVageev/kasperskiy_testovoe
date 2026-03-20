import re
from collections import defaultdict
from openpyxl import Workbook
import pymorphy3

morph = pymorphy3.MorphAnalyzer()

WORD_REGEX = re.compile(r"[а-яА-Яa-zA-Z]+")


def normalize(word: str) -> str:
    return morph.parse(word)[0].normal_form


def process_file(file):
    stats = defaultdict(lambda: {"total": 0, "per_line": []})

    line_index = 0

    for raw_line in file.file:
        line = raw_line.decode("utf-8", errors="ignore")

        words = WORD_REGEX.findall(line.lower())
        line_counter = defaultdict(int)

        for word in words:
            norm = normalize(word)
            line_counter[norm] += 1

        # 1. Добавляем 0 всем уже известным словам
        for word in stats:
            stats[word]["per_line"].append(0)

        # 2. Обрабатываем слова в текущей строке
        for word, count in line_counter.items():
            if word not in stats:
                # создаём новый список с нулями для предыдущих строк
                stats[word]["per_line"] = [0] * line_index
                stats[word]["per_line"].append(count)
                stats[word]["total"] = count
            else:
                # обновляем последнее значение
                stats[word]["per_line"][-1] = count
                stats[word]["total"] += count

        line_index += 1

    save_to_excel(stats)


def save_to_excel(stats: dict):
    wb = Workbook()
    ws = wb.active
    ws.title = "Report"

    ws.append(["Словоформа", "Общее количество", "По строкам"])

    for word, data in stats.items():
        ws.append([
            word,
            data["total"],
            ",".join(map(str, data["per_line"]))
        ])

    wb.save("report.xlsx")
