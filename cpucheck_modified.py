import psutil

def check(percent):
    usage=psutil.cpu_percent(10)
    return usage < percent

if not check(75):
    print("Ohhh Shit!!..Overloaded")
    print("Shut the System off or Kill the Process before it kills your system")
else:
    print("Woooww...Everything seems to Okay Man")
