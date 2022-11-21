import csv
import os
from typing import Dict, List, Set
from language_graph import create_plot
from language_analyzer import repo_languages

# Save language analyses in csv
def dump_language_data(path: str, headers: Set[str], langs: List[Dict[str, str]]) -> str:
    csv_path = path + ".csv"
    if os.path.exists(csv_path):
        os.remove(csv_path)

    with open(csv_path, 'w+', newline='') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        for lang in langs:
            writer.writerow(lang)
        file.close()


def analyze():
    (headers, langs, repo_name) = repo_languages()
    path = "./reports/" + repo_name + "-language"
    dump_language_data(path, headers, langs)
    create_plot(path)


analyze()
