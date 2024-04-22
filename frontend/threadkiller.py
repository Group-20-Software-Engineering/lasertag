import ctypes
import threading
import time

def target():
    while True:
        print("Thread is running")
        time.sleep(1)

def terminate_thread(thread):
    if not thread.is_alive():
        return

    exc = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread.ident), exc)

    if res == 0:
        raise ValueError("Nonexistent thread ID")
    elif res > 1:
        # If it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect
        ctypes.pythonapi.PyThreadState_SetAsyncExc(thread.ident, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")

thread = threading.Thread(target=target)
thread.start()
time.sleep(5)

terminate_thread(thread)  # Force terminate the thread
thread.join()

print("Thread was terminated")
