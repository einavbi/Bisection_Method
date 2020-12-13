import math
#318231750 Einav Bitton
#316614320 Daniel Assayag

import sympy as sp
from mpmath import ln
from sympy import lambdify


def Bisection_Method(start_point,end_point,Ep,p):
    error =( -(ln((Ep) / (end_point - start_point))/ln(2)))
    count=0
    while (end_point-start_point)>Ep :
        if (count > error):
            print("this function dosent fit the Bisection Method ")
            break

        count=count+1
        c=(start_point+end_point)/2
        if ((p(start_point)*p(c))>0):
            start_point=c
        else:
            end_point=c
    return c



#Bisection_Method(1,2,0.0001,lambda x:x**3-x-1)




def derivative(f,x):
    my_f1=sp.diff(f,x)
    return lambdify(x, my_f1)




def Bisection_Method_derivative(start_point,end_point,num,p):
    Ep=0.0001
    x = sp.symbols('x')
    f=lambdify(x,p)#פונקציה מקורית

    splits=(abs(end_point-start_point))/num #רווח  בין הטווחים
    count=num
    P=derivative(p,x) #נכזרת
    pre=start_point
    nex=end_point
    start=start_point
    end=end_point
    while (count != 0):
        pre = f(start_point)
        count = count - 1
        start_point = start_point + splits
        nex = f(start_point)
        if (pre * nex < 0):
            root = Bisection_Method(start_point - splits, start_point, Ep, f)
            print(root)


    count = num
    while(count!=0):
        pre=P(start)
        count = count-1
        start=start+splits
        nex=P(start)
        if(pre*nex<0):
            root=Bisection_Method(start-splits,start, Ep,P)
            if(0==round(float(f(root)))):
                print(str(root))










x = sp.symbols('x')
f=x**4+x**3-3*x**2


Bisection_Method_derivative(-3,2,50,f)