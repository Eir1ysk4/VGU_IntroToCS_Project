import time

from scheduler import *
from task2 import *
from task3 import *
from task6 import Task6

scheduler = Scheduler()
scheduler.SCH_Init()

# task2 = Task2()
# task3 = Task3()
task6 = Task6()


scheduler.SCH_Add_Task(task6.Task6_Run, 1000, 5000)

#
# scheduler.SCH_Add_Task(task3.Task3_Run, 1000, 5000)
# scheduler.SCH_Add_Task(task2.Task2_Run, 1000, 5000)


while True:
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    time.sleep(0.1)
