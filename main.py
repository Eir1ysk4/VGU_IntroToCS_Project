from scheduler import *
from task1 import *
from task2 import *
from task3 import *
from task4 import *
from task5 import *

scheduler = Scheduler()
scheduler.SCH_Init()

task1 = Task1()
task2 = Task2()
task3 = Task3()
task4 = Task4()
task5 = Task5()

scheduler.SCH_Add_Task(lambda: task1.Task1_Run(scheduler, task2), 1000, 1000000)
scheduler.SCH_Add_Task(lambda: task3.Task3_Run(scheduler, task4, task5), 1000, 4000)


while True:
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    time.sleep(0.1)
