def f_x(x):
    return float((x**3)+(2*x**2)+(10*x)-20)                         ## Put your f(x) function here

def f__x(x):
    return float(3*x**2+4*x+10)                                     ## Put your f'(x) function here


def g_x(x):
    return f_x(x)/f__x(x)                                           ## Put yout g_x function here


if __name__=='__main__':
    goal = 10^(-6)                                                  ## Put the goal here
    x=50                                                            ## Put the initial value of x here
    max_iteration = 500                                              ## Put the max iteration you want to achieve (exit parameter)

    gx = g_x(x)

    dispersion=x-gx
    i=0
    print("Iteration\tx\tg(x)\tdispersion")
    while (dispersion > 0.5*goal and i < max_iteration):
        print(str(i)+"\t"+str(x)+"\t"+str(gx)+"\t"+str(dispersion))
        x = gx
        gx=g_x(x)
        dispersion = x-gx
        i+=1
