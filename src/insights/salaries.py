from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        return max(
            [
                int(job["max_salary"])
                for job in self.jobs_list
                if job["max_salary"].isdigit()
            ]
        )

    def get_min_salary(self) -> int:
        return min(
            [
                int(job["min_salary"])
                for job in self.jobs_list
                if job["min_salary"].isdigit()
            ]
        )

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        try:
            min_salary = int(job["min_salary"])
            max_salary = int(job["max_salary"])
            salary = int(salary)

            assert min_salary < max_salary

            return min_salary <= salary <= max_salary

        except (ValueError, TypeError, AssertionError, KeyError):
            raise ValueError("Invalid parameters provided")

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        filtered_jobs = list()
        for job in jobs:
            try:
                if self.matches_salary_range(job, salary):
                    filtered_jobs.append(job)

            except ValueError:
                continue

        return filtered_jobs
