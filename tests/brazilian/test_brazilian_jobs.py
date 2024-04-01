from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    translated_jobs = read_brazilian_file("tests/mocks/brazilians_jobs.csv")

    assert translated_jobs[0] == {
        "title": "Maquinista",
        "salary": "2000",
        "type": "trainee",
    }
