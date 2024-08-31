import _thread
import time

def planA(msg):
    count = 0
    while count < 5:
        print(f"Executing Plan A {count}th time - {msg}")
        count += 1
        time.sleep(2)


def planB(msg):
    count = 0
    while count < 5:
        print(f"Executing Plan B {count}th time - {msg}")
        count += 1
        time.sleep(2)


try:
    _thread.start_new_thread(planA, ("Executed",))
    _thread.start_new_thread(planB, ("Executed",))
except:
    print("Error")
time.sleep(12)
