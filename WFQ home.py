# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 13:22:51 2021

@author: hossi
"""
nbr_file=4
requis=[0 for i in range(nbr_file)]
attribuer=[0 for i in range(nbr_file)]
A=[0 for i in range(nbr_file)]
C=[0 for i in range(nbr_file)]
def WFQ (nbr_file,w,ta,bp,tp):
    for i in range(nbr_file):
        requis[i]=ta[i]*tp[i]
    print("la bande passante requise est:",requis)
    tot=sum(w[j] for j in range(nbr_file))
    for n in range(nbr_file):
        attribuer[n]=bp*(w[n]/tot)
    print("la bande passante offerte est:",attribuer)
    if requis[0] >= attribuer[0] and requis[1] >= attribuer[1] and requis[2] >= attribuer[2] and requis[3] >= attribuer[3]:
        return 'on va attribuer pour chaque file la bande passante :',attribuer
    if requis[0] <= attribuer[0] and requis[1] <= attribuer[1] and requis[2] <= attribuer[2] and requis[3] <= attribuer[3]:
        return 'on va attribuer pour chaque file la bande passante :',requis
    k=2
    while k < nbr_file +1 and bp != sum(B(l,k-1) for l in range(nbr_file)) :
        for x in range(nbr_file):
            A[x]=B(x,k)
            C[x]=requis[x]-A[x]
#        print('les attributions pour k=',k,'sont:' ,A)
#        print('le manque en bande passante pour k=',k,'sont:' ,C)
        k+=1
    return 'les attributions finales sont:' ,A,'le manque en bande passante est:' ,C

def B(i,k):
    if k==1:
        return min(requis[i],attribuer[i])
    return min(requis[i],B(i,k-1)+(bp-sum(B(l,k-1) for l in range(nbr_file)))*(w[i]/sum(w[l]*min(requis[l]-B(l,k-1),1) for l in range(nbr_file))))

w=[4,3,2,1]
ta=[1000,1050,1000,450]
bp=10000
tp=[3,3,3,3]
WFQ (nbr_file,w,ta,bp,tp)


        
        
    
    
    