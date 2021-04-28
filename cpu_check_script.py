import psutil

def check(percent):
    usage=psutil.cpu_percent(10)
    return usage < percent

if not check(75):
    print("Ohhh Shit!!..Overloaded")
else:
    print("Woooww...Everything seems to Okay Man")
    print("Wonderfullll...")
