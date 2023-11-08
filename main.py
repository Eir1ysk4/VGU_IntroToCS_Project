from scheduler import *
from task1 import *
from task5 import *

scheduler = Scheduler()
scheduler.SCH_Init()

task1 = Task1()
task5 = Task5()


scheduler.SCH_Add_Task(task1.Task1_Run(), 1000, 5000)
print(task1.result_text)
scheduler.SCH_Add_Task(task5.Task5_Run(task1.result_text), 1000, 5000)

while True:
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    time.sleep(0.1)
