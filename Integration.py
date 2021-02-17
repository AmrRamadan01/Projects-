
import math #in case you need to insert more notaions

#limits
lower=float(input("Please enter the lower limit of integration :")) #Lower limit ot the itegral
upper=float(input(" Please enter the upper limit of integration :")) #Upper limit of the integral

deltax=0.00001 #value of the increment 
i=None #Dummy counter

#The Riemann sum
integral=0
while i!=0 :

    if lower >= float(upper - deltax):
        break
    else:
        x = lower
        function = (float(x))
        integration = float(function) * float(deltax)

        lower = float(lower + deltax)
        integral = integral + integration

#Output
print('Integral (decimal value) = ',integral)
#Note!
## this is just an example in this case calculating the area under the curve of F(x)=X
### but it can be used with nonelementary integrls (that's why math library is imported)
