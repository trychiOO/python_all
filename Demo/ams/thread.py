import threading
from threading import current_thread
def fun (args,args1):
    print('%s %s'%(args,args1))
for i in range(1,7,1)
    t = threading.Thread(target=fun,args=(i ,i+1))
    t.start()