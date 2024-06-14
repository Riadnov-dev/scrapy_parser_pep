import csv
import os
from pathlib import Path

from scrapy.utils.project import get_project_settings

BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:
    def open_spider(self, spider):
        self.pep_count = {}
        self.settings = get_project_settings()
        self.results_dir = BASE_DIR / "results"
        os.makedirs(self.results_dir, exist_ok=True)
        self.summary_filepath = (
            self.results_dir
            / f"status_summary_{self.settings.get('NOW_TIME')}.csv"
        )

    def close_spider(self, spider):
        total_count = sum(self.pep_count.values())
        with open(
            self.summary_filepath, "w", newline="", encoding="utf-8"
        ) as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Status", "Количество"])
            for status, count in self.pep_count.items():
                writer.writerow([status, count])
            writer.writerow(["Total", total_count])

    def process_item(self, item, spider):
        status = item["status"]
        if status in self.pep_count:
            self.pep_count[status] += 1
        else:
            self.pep_count[status] = 1
        return item
