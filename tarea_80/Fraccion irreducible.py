#!/usr/bin/env python
# coding: utf-8

# In[160]:


#Se pide al usuario que introduzca el número, con las isntrucciones correspondientes:
n=input("Introduce un número entre 0.0001 y 0.9999 con un máximo de 4 decimales")


# In[161]:


#Se comrprueba que el número introducido tiene coma decimal correcta, para que funcione bien el programa:
error=0
try:
    n=float(n)
except ValueError:
    print('El número introducido no es correcto, utilice el punto como separador decimal')


# In[162]:


#Se comprueba si el número está en el rango solicitado:
if n <0.0001 or n > 0.9999:
        print(f"el número introducido se encuentra fuera del rango")

#Se comprueba si el número tiene 4 decimales, si tiene 4 o menos, se calcula la fracción:
if((n*100000)%10==0):
    numerador=n*10000
    denominador=10000
    for i in range(2,int(numerador+1)):
        while (numerador%i==0 and denominador%i==0):
            numerador=numerador/i
            denominador=denominador/i
else:
    print('El número introducido tiene más de 4 decimales')


# In[163]:


#Se muestra por pantalla la fracción calculada:
resultado=str(int(numerador))+'/'+str(int(denominador))3
print(resultado)


# In[ ]:




