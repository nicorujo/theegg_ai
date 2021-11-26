#!/usr/bin/env python
# coding: utf-8

# In[10]:


ataque_p=25
ataque_j=15
ataque_p=55
ataque_j=45
vida_p=100
vida_j=100
turno=1

while (vida_p>0) and (vida_j>0):
    if turno==1:
        vida_j=vida_j-ataque_p
        turno=0
    else:
        vida_p=vida_p-ataque_j
        turno=1
if vida_p<0:
    print("Jigglipuff ha ganado")
else:
    print("Pikachu ha ganado")

