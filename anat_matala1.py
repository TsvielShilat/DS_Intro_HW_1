def my_func(x1=None,x2=None,x3=None):
    try:
        x1 = float(x1)
        x2 = float(x2)
        x3 = float(x3)
    except:
        print("Error: parameters should be float")
        return None
    if (x1+x2+x3)==0:
        print("Not a number - denominater equals zero")
        return None
    value = (x1+x2+x3)*(x2+x3)*x3/(x1+x2+x3)
    return float(value)

def convert(hours=None,minutes=0):
    try:
        minutes = float(minutes)
        hours= float(hours)
    except:
        print("Input error!")
        return None
    if(hours <0 or minutes <0 or (hours==0 and minutes==0)):
        print("Input error!")
        return None
    return (hours*3600+minutes*60)