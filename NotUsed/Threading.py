import threading
GState = True
def hi():
    global GState
    print(hi)
    while GState:
        print(1)



def foo():
    global GState
    print ("foo")
    GState = False



threads= []

t = threading.Thread(target=hi)
t2 = threading.Thread(target=foo)
t.daemon = False
threads.append(t)
threads.append(t2)
threads[0].start()
threads[1].start()





threads[1].join()
threads[0].join()   

