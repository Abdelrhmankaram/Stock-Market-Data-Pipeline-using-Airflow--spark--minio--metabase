from airflow.decorators import dag, task
from datetime import datetime

@dag(

)
def taskflow():

    @task
    def task_a():
        print('Task A')
        return 42

    @task
    def task_b(value):
        print('Task B')
        print(value)

    task_b(task_a())

taskflow()