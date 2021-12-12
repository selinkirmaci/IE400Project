# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 20:37:01 2021

@author: selin
"""
import gurobipy as gp
from gurobipy import GRB
# Create a Model instance
m = gp.Model()

#Add variables
#Dosage of drugs
X1 = m.addVar(vtype=GRB.CONTINUOUS, name="X1")
X2 = m.addVar(vtype=GRB.CONTINUOUS, name="X2")
X3 = m.addVar(vtype=GRB.CONTINUOUS, name="X3")
X4 = m.addVar(vtype=GRB.CONTINUOUS, name="X4")
X5 = m.addVar(vtype=GRB.CONTINUOUS, name="X5")
X6 = m.addVar(vtype=GRB.CONTINUOUS, name="X6")
X7 = m.addVar(vtype=GRB.CONTINUOUS, name="X7")

#Patient Feature
P1 = m.addVar(vtype=GRB.BINARY, name="P1")
P2 = m.addVar(vtype=GRB.BINARY, name="P2")
P3 = m.addVar(vtype=GRB.BINARY, name="P3")
P4 = m.addVar(vtype=GRB.BINARY, name="P4")
P5 = m.addVar(vtype=GRB.BINARY, name="P5")
P6 = m.addVar(vtype=GRB.BINARY, name="P6")
P7 = m.addVar(vtype=GRB.BINARY, name="P7")
P8 = m.addVar(vtype=GRB.BINARY, name="P8")
P9 = m.addVar(vtype=GRB.BINARY, name="P9")

#Drugs
Y1 = m.addVar(vtype=GRB.BINARY, name="Y1")
Y2 = m.addVar(vtype=GRB.BINARY, name="Y2")
Y3 = m.addVar(vtype=GRB.BINARY, name="Y3")
Y4 = m.addVar(vtype=GRB.BINARY, name="Y4")
Y5 = m.addVar(vtype=GRB.BINARY, name="Y5")
Y6 = m.addVar(vtype=GRB.BINARY, name="Y6")
Y7 = m.addVar(vtype=GRB.BINARY, name="Y7")

diff1 = m.addVar(vtype=GRB.CONTINUOUS, name="diff1")
abs1 = m.addVar(lb=0,vtype=GRB.CONTINUOUS, name="abs1")

m.addConstr(diff1 == X1-20,name = "diffConstraint1")
m.addGenConstrAbs(abs1,diff1,"absconstr1")

diff2 = m.addVar(vtype=GRB.CONTINUOUS, name="diff2")
abs2 = m.addVar(lb=0,vtype=GRB.CONTINUOUS, name="abs2")

m.addConstr(diff1 == X3-30,name = "diffConstraint2")
m.addGenConstrAbs(abs2,diff2,"absconstr2")

diff3 = m.addVar(vtype=GRB.CONTINUOUS, name="diff3")
abs3 = m.addVar(lb=0,vtype=GRB.CONTINUOUS, name="abs3")

m.addConstr(diff3 == X4-15,name = "diffConstraint3")
m.addGenConstrAbs(abs3,diff3,"absconstr3")


diff4 = m.addVar(vtype=GRB.CONTINUOUS, name="diff4")
abs4 = m.addVar(lb=0,vtype=GRB.CONTINUOUS, name="abs4")

m.addConstr(diff4 == X7-35,name = "diffConstraint4")
m.addGenConstrAbs(abs4,diff4,"absconstr4")

qualityOfLife = m.addVar(vtype=GRB.CONTINUOUS, name="qualityOfLife")
m.addConstr(qualityOfLife == -0.5*P1-0.5*P2 -12*P3-8*P4-5*P5-5*P6-1*P7-3*P8-2*P9
               -5*Y1-6*Y2-4*Y3-4*Y4-8*Y5-6*Y6-7*Y7
               +0.28*X1+0.3*X2+0.25*X3+0.17*X4+0.31*X5+0.246*X6+0.4*X7,name="qualityOfLifeContraint")

#SET OF
m.setObjective(abs1+abs2+abs3+abs4, GRB.MINIMIZE)

c1 = m.addConstr(Y1>=1)
c2 = m.addConstr(Y2<=0)
c3 = m.addConstr(Y3>=1)
c4 = m.addConstr(Y4>=1)
c5 = m.addConstr(Y5<=0)
c6 = m.addConstr(Y6<=0)
c7 = m.addConstr(Y7>=1)


c8 = m.addConstr(X1>=20*Y1)
c9 = m.addConstr(X1<=80*Y1)
c10 = m.addConstr(X2>=10*Y2)
c11 = m.addConstr(X2<=50*Y2)
c12 = m.addConstr(X3>=20*Y3)
c13 = m.addConstr(X3<=100*Y3)
c14 = m.addConstr(X4>=10*Y4)
c15 = m.addConstr(X4<=100*Y4)
c16 = m.addConstr(X5>=10*Y5)
c17 = m.addConstr(X5<=70*Y5)
c18 = m.addConstr(X6>=20*Y6)
c19 = m.addConstr(X6<=90*Y6)
c20 = m.addConstr(X7>=20*Y7)
c21 = m.addConstr(X7<=50*Y7)


c22 = m.addConstr(P1>=1)
c23 = m.addConstr(P2>=1)
c24 = m.addConstr(P3<=0)
c25 = m.addConstr(P4>=1)
c26 = m.addConstr(P5<=0)
c27 = m.addConstr(P6<=0)
c28 = m.addConstr(P7<=0)
c29 = m.addConstr(P8<=0)
c30 = m.addConstr(P9>=1)



#obejctive funtion treshold
c31 = m.addConstr(qualityOfLife>=35) 
m.optimize();
m.printAttr('X') #This prints the non-zero solutions found