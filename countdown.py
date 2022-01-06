import time 
def countdown_timer(t):
    while t>=1:
        print("{:02d}:{:02d}".format(0,t))
        time.sleep(1)
        t-=1
    return "Times up!!!"
set_timer=int(input("set timer for countdown: "))
print(countdown_timer(set_timer))
