import threading
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

threadA = threading.Thread(target=planA, args=("Executed",))
threadB = threading.Thread(target=planB, args=("Executed",))


threadA.start()
threadB.start()


threadA.join()
threadB.join()

print("All threads completed.")
