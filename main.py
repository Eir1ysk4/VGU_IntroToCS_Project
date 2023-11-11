from scheduler import *
from task1 import *
from task2 import *
from task4 import *
from task6 import Task6
from task5 import *

scheduler = Scheduler()
scheduler.SCH_Init()

task1 = Task1()
task2 = Task2()
task5 = Task5()
task4 = Task4()
task6 = Task6()

scheduler.SCH_Add_Task(task2.Task2_Run(), 1000, 5000)
scheduler.SCH_Add_Task(task1.Task1_Run(), 1000, 5000)
print(task1.result_text)
scheduler.SCH_Add_Task(task4.Task4_Run(), 1000, 5000)
scheduler.SCH_Add_Task(task6.Task6_Run(task4), 1000, 5000)
scheduler.SCH_Add_Task(task5.Task5_Run(task1.result_text), 1000, 5000)

while True:
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    time.sleep(0.1)
