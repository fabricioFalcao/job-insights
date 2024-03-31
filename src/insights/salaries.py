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
        # Check if min_salary and max_salary keys are present in the job dictionary
        if "min_salary" not in job or "max_salary" not in job:
            raise ValueError(
                "min_salary or max_salary keys are missing in the dictionary"
            )

        # Extract min_salary and max_salary values from the job dictionary
        min_salary = job["min_salary"]
        max_salary = job["max_salary"]

        # Convert min_salary and max_salary to integers if they are numeric strings
        if isinstance(min_salary, str) and min_salary.isdigit():
            min_salary = int(min_salary)
        if isinstance(max_salary, str) and max_salary.isdigit():
            max_salary = int(max_salary)

        # Check if min_salary and max_salary are numeric
        if not (isinstance(min_salary, int) and isinstance(max_salary, int)):
            raise ValueError("min_salary or max_salary values are not numeric")

        # Convert salary parameter to integer if it's a string
        if isinstance(salary, str):
            if not salary.isdigit():
                raise ValueError("salary parameter is not numeric")
            salary = int(salary)

        # Check if min_salary is greater than max_salary
        if min_salary > max_salary:
            raise ValueError("min_salary is greater than max_salary")

        # Check if salary parameter is numeric
        if not isinstance(salary, int):
            raise ValueError("salary parameter is not numeric")

        # Check if salary is within the salary range
        return min_salary <= salary <= max_salary

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
