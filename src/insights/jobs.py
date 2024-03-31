from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path) -> List[Dict]:
        with open(path, encoding="utf-8") as file:
            data = csv.DictReader(file)
            self.jobs_list = list(data)

    def get_unique_job_types(self) -> List[str]:
        return set(job["job_type"] for job in self.jobs_list)

    def filter_by_multiple_criteria(
        self, jobs_list, filter_criteria
    ) -> List[dict]:
        industry = filter_criteria["industry"]
        job_type = filter_criteria["job_type"]

        return [
            job
            for job in jobs_list
            if job["industry"] == industry and job["job_type"] == job_type
        ]
