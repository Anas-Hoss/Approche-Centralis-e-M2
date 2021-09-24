# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 17:40:18 2021

@author: hossi
"""
import numpy as np
#Définition des taux d'arrivées:

Taux_Arrivée_1=2
Taux_Arrivée_2=2
#Définition des taux de services:

Taux_Service_1=10
Taux_Service_2=10
Taux_Service_3=10
#Définition des tailles des files d'attente par noeud:

Taille_File_1=2
Taille_File_2=2
Taille_File_3=2
Taille_File_4=2
Taille_File_5=2
#Définition de l'ensemble d'états par noeud:

Liste_action_totale=(0,0.25,0.5,0.75)
Etats=[]
for i in range(Taille_File_1+1):
    for j in range(Taille_File_2+1):
          for k in range(Taille_File_3+1):
              for l in range(Taille_File_4+1):
                      for z in Liste_action_totale:
                          for c in Liste_action_totale:
                              for p in Liste_action_totale:
                                  for x in Liste_action_totale:
                                           Etats.append((i,z,j,min(p,0.75-z))+(k,c,l,min(x,0.75-c)))
print("L'ensemble d'états est:",Etats)
print("Le nombre d'états est:",len(Etats))

#Définition des actions:
Actions={}
for k in Etats:
    Actions[k]=('Auguementer','Diminuer','Garder')

#Définition des rewards lorsqu'on effectue une action "a" à partir de l'état "s":
Taille_Maximum_11=1
Taille_Maximum_12=1
Taille_Maximum_21=1
Taille_Maximum_22=1
def Reward(s,a):
    if a=='Auguementer':
      if s[0]-Taille_Maximum_11<0 and s[2]-Taille_Maximum_12<0 and s[4]-Taille_Maximum_21<0 and s[6]-Taille_Maximum_22<0 :
         return -5
      if s[0]-Taille_Maximum_11>0 and s[2]-Taille_Maximum_12>0 and s[4]-Taille_Maximum_21>0 and s[6]-Taille_Maximum_22>0 :
         return 5
      if s[0]-Taille_Maximum_11>0 and s[2]-Taille_Maximum_12<0 and s[4]-Taille_Maximum_21<0 and s[6]-Taille_Maximum_22<0 :
         return -3
      if s[0]-Taille_Maximum_11>0 and s[2]-Taille_Maximum_12>0 and s[4]-Taille_Maximum_21<0 and s[6]-Taille_Maximum_22<0 :
         return -1
      if s[0]-Taille_Maximum_11>0 and s[2]-Taille_Maximum_12>0 and s[4]-Taille_Maximum_21>0 and s[6]-Taille_Maximum_22<0 :
         return 1
      if s[0]-Taille_Maximum_11>0 and s[2]-Taille_Maximum_12>0 and s[4]-Taille_Maximum_21>0 and s[6]-Taille_Maximum_22>0 :
         return 3
      else:
         return 0
    if a=='Diminuer':
      if s[0]-Taille_Maximum_11<0 and s[2]-Taille_Maximum_12<0 and s[4]-Taille_Maximum_21<0 and s[6]-Taille_Maximum_22<0 :
         return 5
      if s[0]-Taille_Maximum_11>0 and s[2]-Taille_Maximum_12>0 and s[4]-Taille_Maximum_21>0 and s[6]-Taille_Maximum_22>0 :
         return -5
      if s[0]-Taille_Maximum_11>0 and s[2]-Taille_Maximum_12<0 and s[4]-Taille_Maximum_21<0 and s[6]-Taille_Maximum_22<0 :
         return 3
      if s[0]-Taille_Maximum_11>0 and s[2]-Taille_Maximum_12>0 and s[4]-Taille_Maximum_21<0 and s[6]-Taille_Maximum_22<0 :
         return 1
      if s[0]-Taille_Maximum_11>0 and s[2]-Taille_Maximum_12>0 and s[4]-Taille_Maximum_21>0 and s[6]-Taille_Maximum_22<0 :
         return -1
      if s[0]-Taille_Maximum_11>0 and s[2]-Taille_Maximum_12>0 and s[4]-Taille_Maximum_21>0 and s[6]-Taille_Maximum_22>0 :
         return -3
      else:
         return 0  
    if a=='Garder':
      if s[0]-Taille_Maximum_11<0 and s[2]-Taille_Maximum_12<0 and s[4]-Taille_Maximum_21<0 and s[6]-Taille_Maximum_22<0 :
         return 5
      if s[0]-Taille_Maximum_11>0 and s[2]-Taille_Maximum_12>0 and s[4]-Taille_Maximum_21>0 and s[6]-Taille_Maximum_22>0 :
         return -5
      else:
         return 0  
     
#Définition de la matrice de transition:
Facteur_Uniformisation=Taux_Arrivée_1 + Taux_Arrivée_2 + Taux_Service_1 + Taux_Service_2
print("Le facteur d'uniformisation est:",Facteur_Uniformisation)

def Prob_Transition(s_suivant,s_actuel,a):
  if a=='Auguementer':

                           #Arrivée file 1 slice 1 
     if s_suivant[0]==s_actuel[0]+1  and s_suivant[2]==s_actuel[2] and s_suivant[4]==s_actuel[4] and s_suivant[6]==s_actuel[6]  and s_suivant[1]==min(max(s_actuel[1]+0.25,0),0.75) and s_suivant[3]==min(s_actuel[3],(0.75-s_actuel[1])) and s_suivant[5]==min(max(s_actuel[5]+0.25,0),0.75) and s_suivant[7]==min(s_actuel[7],(0.75-s_actuel[5])) :
        return Taux_Arrivée_1/Facteur_Uniformisation

                           #Arrivée file 1 slice 2
     if s_suivant[0]==s_actuel[0]  and s_suivant[2]==s_actuel[2]+1 and s_suivant[4]==s_actuel[4] and s_suivant[6]==s_actuel[6]  and s_suivant[1]==min(max(s_actuel[1]+0.25,0),0.75) and s_suivant[3]==min(s_actuel[3],(0.75-s_actuel[1])) and s_suivant[5]==min(max(s_actuel[5]+0.25,0),0.75) and s_suivant[7]==min(s_actuel[7],(0.75-s_actuel[5])) :
        return Taux_Arrivée_2/Facteur_Uniformisation

                           #Service de slice 1 num 1
     if s_suivant[0]==s_actuel[0]-1  and s_suivant[2]==s_actuel[2] and s_suivant[4]==s_actuel[4]+1 and s_suivant[6]==s_actuel[6]  and s_suivant[1]==min(max(s_actuel[1]+0.25,0),0.75) and s_suivant[3]==min(s_actuel[3],(0.75-s_actuel[1])) and s_suivant[5]==min(max(s_actuel[5]+0.25,0),0.75) and s_suivant[7]==min(s_actuel[7],(0.75-s_actuel[5])) :
        return Taux_Service_1*s_actuel[1]/Facteur_Uniformisation

                           #Service de slice 2 num 1
     if s_suivant[0]==s_actuel[0]  and s_suivant[2]==s_actuel[2]-1 and s_suivant[4]==s_actuel[4] and s_suivant[6]==s_actuel[6]+1  and s_suivant[1]==min(max(s_actuel[1]+0.25,0),0.75) and s_suivant[3]==min(s_actuel[3],(0.75-s_actuel[1])) and s_suivant[5]==min(max(s_actuel[5]+0.25,0),0.75) and s_suivant[7]==min(s_actuel[7],(0.75-s_actuel[5])) :
        return Taux_Service_1*s_suivant[3]/Facteur_Uniformisation

                           #Service de slice 1 num 2
     if s_suivant[0]==s_actuel[0]  and s_suivant[2]==s_actuel[2] and s_suivant[4]==s_actuel[4]-1 and s_suivant[6]==s_actuel[6] and s_suivant[1]==min(max(s_actuel[1]+0.25,0),0.75) and s_suivant[3]==min(s_actuel[3],(0.75-s_actuel[1])) and s_suivant[5]==min(max(s_actuel[5]+0.25,0),0.75) and s_suivant[7]==min(s_actuel[7],(0.75-s_actuel[5])) :
        return Taux_Service_2*s_suivant[5]/Facteur_Uniformisation

                          #Sortie de slice 2 vers l'extérieur
     if s_suivant[0]==s_actuel[0]  and s_suivant[2]==s_actuel[2] and s_suivant[4]==s_actuel[4] and s_suivant[6]==s_actuel[6]-1  and s_suivant[1]==min(max(s_actuel[1]+0.25,0),0.75) and s_suivant[3]==min(s_actuel[3],(0.75-s_actuel[1])) and s_suivant[5]==min(max(s_actuel[5]+0.25,0),0.75) and s_suivant[7]==min(s_actuel[7],(0.75-s_actuel[5])) :
        return Taux_Service_2*s_suivant[7]/Facteur_Uniformisation


                          #Les diagonales
     if s_suivant==s_actuel:
        return 1-(Taux_Service_2*s_suivant[7]/Facteur_Uniformisation +Taux_Service_2*s_suivant[5]/Facteur_Uniformisation+ Taux_Service_1*s_suivant[3]/Facteur_Uniformisation 
                  + Taux_Service_1*s_actuel[1]/Facteur_Uniformisation + Taux_Arrivée_2/Facteur_Uniformisation + Taux_Arrivée_1/Facteur_Uniformisation)
                          #Sinon
     else:
        return 0
    

  if a=='Diminuer':
    
                           #Arrivée file 1 slice 1 
     if s_suivant[0]==s_actuel[0]+1  and s_suivant[2]==s_actuel[2] and s_suivant[4]==s_actuel[4] and s_suivant[6]==s_actuel[6]  and s_suivant[1]==min(max(s_actuel[1]-0.25,0),0.75) and s_suivant[3]==min(s_actuel[3],(0.75-s_actuel[1])) and s_suivant[5]==min(max(s_actuel[5]-0.25,0),0.75) and s_suivant[7]==min(s_actuel[7],(0.75-s_actuel[5])) :
        return Taux_Arrivée_1/Facteur_Uniformisation

                           #Arrivée file 1 slice 2
     if s_suivant[0]==s_actuel[0]  and s_suivant[2]==s_actuel[2]+1 and s_suivant[4]==s_actuel[4] and s_suivant[6]==s_actuel[6]  and s_suivant[1]==min(max(s_actuel[1]-0.25,0),0.75) and s_suivant[3]==min(s_actuel[3],(0.75-s_actuel[1])) and s_suivant[5]==min(max(s_actuel[5]-0.25,0),0.75) and s_suivant[7]==min(s_actuel[7],(0.75-s_actuel[5])) :
        return Taux_Arrivée_2/Facteur_Uniformisation

                           #Service de slice 1 num 1
     if s_suivant[0]==s_actuel[0]-1  and s_suivant[2]==s_actuel[2] and s_suivant[4]==s_actuel[4]+1 and s_suivant[6]==s_actuel[6]  and s_suivant[1]==min(max(s_actuel[1]-0.25,0),0.75) and s_suivant[3]==min(s_actuel[3],(0.75-s_actuel[1])) and s_suivant[5]==min(max(s_actuel[5]-0.25,0),0.75) and s_suivant[7]==min(s_actuel[7],(0.75-s_actuel[5])) :
        return Taux_Service_1*s_actuel[1]/Facteur_Uniformisation

                           #Service de slice 2 num 1
     if s_suivant[0]==s_actuel[0]  and s_suivant[2]==s_actuel[2]-1 and s_suivant[4]==s_actuel[4] and s_suivant[6]==s_actuel[6]+1  and s_suivant[1]==min(max(s_actuel[1]-0.25,0),0.75) and s_suivant[3]==min(s_actuel[3],(0.75-s_actuel[1])) and s_suivant[5]==min(max(s_actuel[5]-0.25,0),0.75) and s_suivant[7]==min(s_actuel[7],(0.75-s_actuel[5])) :
        return Taux_Service_1*s_suivant[3]/Facteur_Uniformisation

                           #Service de slice 1 num 2
     if s_suivant[0]==s_actuel[0]  and s_suivant[2]==s_actuel[2] and s_suivant[4]==s_actuel[4]-1 and s_suivant[6]==s_actuel[6] and s_suivant[1]==min(max(s_actuel[1]-0.25,0),0.75) and s_suivant[3]==min(s_actuel[3],(0.75-s_actuel[1])) and s_suivant[5]==min(max(s_actuel[5]-0.25,0),0.75) and s_suivant[7]==min(s_actuel[7],(0.75-s_actuel[5])) :
        return Taux_Service_2*s_suivant[5]/Facteur_Uniformisation

                          #Sortie de slice 2 vers l'extérieur
     if s_suivant[0]==s_actuel[0]  and s_suivant[2]==s_actuel[2] and s_suivant[4]==s_actuel[4] and s_suivant[6]==s_actuel[6]-1  and s_suivant[1]==min(max(s_actuel[1]-0.25,0),0.75) and s_suivant[3]==min(s_actuel[3],(0.75-s_actuel[1])) and s_suivant[5]==min(max(s_actuel[5]-0.25,0),0.75) and s_suivant[7]==min(s_actuel[7],(0.75-s_actuel[5])) :
        return Taux_Service_2*s_suivant[7]/Facteur_Uniformisation

                          #Les diagonales
     if s_suivant==s_actuel:
        return 1-(Taux_Service_2*s_suivant[7]/Facteur_Uniformisation +Taux_Service_2*s_suivant[5]/Facteur_Uniformisation
                  + Taux_Service_1*s_suivant[3]/Facteur_Uniformisation + Taux_Service_1*s_actuel[1]/Facteur_Uniformisation + Taux_Arrivée_2/Facteur_Uniformisation 
                  + Taux_Arrivée_1/Facteur_Uniformisation)
                          #Sinon
     else:
        return 0
        

  if a=='Garder':
    
                           #Arrivée file 1 slice 1 
     if s_suivant[0]==s_actuel[0]+1  and s_suivant[2]==s_actuel[2] and s_suivant[4]==s_actuel[4] and s_suivant[6]==s_actuel[6]  and s_suivant[1]==min(max(s_actuel[1],0),0.75) and s_suivant[3]==min(s_actuel[3],(0.75-s_actuel[1])) and s_suivant[5]==min(max(s_actuel[5],0),0.75) and s_suivant[7]==min(s_actuel[7],(0.75-s_actuel[5])) :
        return Taux_Arrivée_1/Facteur_Uniformisation

                           #Arrivée file 1 slice 2
     if s_suivant[0]==s_actuel[0]  and s_suivant[2]==s_actuel[2]+1 and s_suivant[4]==s_actuel[4] and s_suivant[6]==s_actuel[6]  and s_suivant[1]==min(max(s_actuel[1],0),0.75) and s_suivant[3]==min(s_actuel[3],(0.75-s_actuel[1])) and s_suivant[5]==min(max(s_actuel[5],0),0.75) and s_suivant[7]==min(s_actuel[7],(0.75-s_actuel[5])) :
        return Taux_Arrivée_2/Facteur_Uniformisation

                           #Service de slice 1 num 1
     if s_suivant[0]==s_actuel[0]-1  and s_suivant[2]==s_actuel[2] and s_suivant[4]==s_actuel[4]+1 and s_suivant[6]==s_actuel[6]  and s_suivant[1]==min(max(s_actuel[1],0),0.75) and s_suivant[3]==min(s_actuel[3],(0.75-s_actuel[1])) and s_suivant[5]==min(max(s_actuel[5],0),0.75) and s_suivant[7]==min(s_actuel[7],(0.75-s_actuel[5])) :
        return Taux_Service_1*s_actuel[1]/Facteur_Uniformisation

                           #Service de slice 2 num 1
     if s_suivant[0]==s_actuel[0]  and s_suivant[2]==s_actuel[2]-1 and s_suivant[4]==s_actuel[4] and s_suivant[6]==s_actuel[6]+1  and s_suivant[1]==min(max(s_actuel[1],0),0.75) and s_suivant[3]==min(s_actuel[3],(0.75-s_actuel[1])) and s_suivant[5]==min(max(s_actuel[5],0),0.75) and s_suivant[7]==min(s_actuel[7],(0.75-s_actuel[5])) :
        return Taux_Service_1*s_suivant[3]/Facteur_Uniformisation

                           #Service de slice 1 num 2
     if s_suivant[0]==s_actuel[0]  and s_suivant[2]==s_actuel[2] and s_suivant[4]==s_actuel[4]-1 and s_suivant[6]==s_actuel[6]  and s_suivant[1]==min(max(s_actuel[1],0),0.75) and s_suivant[3]==min(s_actuel[3],(0.75-s_actuel[1])) and s_suivant[5]==min(max(s_actuel[5],0),0.75) and s_suivant[7]==min(s_actuel[7],(0.75-s_actuel[5])) :
        return Taux_Service_2*s_suivant[5]/Facteur_Uniformisation

                          #Sortie de slice 2 vers l'extérieur
     if s_suivant[0]==s_actuel[0]  and s_suivant[2]==s_actuel[2] and s_suivant[4]==s_actuel[4] and s_suivant[6]==s_actuel[6]-1  and s_suivant[1]==min(max(s_actuel[1],0),0.75) and s_suivant[3]==min(s_actuel[3],(0.75-s_actuel[1])) and s_suivant[5]==min(max(s_actuel[5],0),0.75) and s_suivant[7]==min(s_actuel[7],(0.75-s_actuel[5])) :
        return Taux_Service_2*s_suivant[7]/Facteur_Uniformisation

                          #Les diagonales
     if s_suivant==s_actuel:
        return 1-(Taux_Service_2*s_suivant[7]/Facteur_Uniformisation +Taux_Service_2*s_suivant[5]/Facteur_Uniformisation
                  + Taux_Service_1*s_suivant[3]/Facteur_Uniformisation + Taux_Service_1*s_actuel[1]/Facteur_Uniformisation + Taux_Arrivée_2/Facteur_Uniformisation 
                  + Taux_Arrivée_1/Facteur_Uniformisation)
                          #Sinon
     else:
        return 0

gamma=0.9
def value_iteration(S,A,P,R):
    V={s:0 for s in S}
    optimal_policy={s:0 for s in S}
    while True :
        oldV = V.copy()
        for s in S:
            Q={}
            for a in A[s]:
                Q[a]=R(s,a)+gamma*sum(P(s_next,s,a)*oldV[s_next] for s_next in S)
            V[s]=max(Q.values())
            if V[s] >= oldV[s]:
              oldV[s] = V[s]
            optimal_policy[s]=max(Q,key=Q.get)
        if all(V[s]==oldV[s] for s in S):
           break
    return V,optimal_policy           
V1,P1=value_iteration(Etats, Actions,Prob_Transition,Reward)
print(V1)
print()
print(P1)