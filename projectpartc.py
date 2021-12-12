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

condition = m.addVar(vtype=GRB.BINARY, name="condition")


qualityOfLife = m.addVar(vtype=GRB.CONTINUOUS, name="qualityOfLife")
m.addConstr(qualityOfLife == -0.5*P1-0.5*P2 -12*P3-8*P4-5*P5-5*P6-1*P7-3*P8-2*P9
               -5*Y1-6*Y2-4*Y3-4*Y4-8*Y5-6*Y6-7*Y7
               +0.28*X1+0.3*X2+0.25*X3+0.17*X4+0.31*X5+0.246*X6+0.4*X7,name="qualityOfLifeContraint")


cost = m.addVar(vtype=GRB.CONTINUOUS, name="cost")
m.addConstr(cost == 25*Y1+ 50*Y1+10*Y3+25*Y4+20*Y5+30*Y6+40*Y7+
            1*X1+2*X2+1*X3+3*X4+2*X5+1*X6+1*X7,name="COSTcONSTRint")

#SET OF
m.setObjective(cost, GRB.MINIMIZE)

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


c31 = m.addConstr(X1+X2 <= 70)
c32 = m.addConstr(X1+X2 >= 50)
c33 = m.addConstr(Y4+Y6 <= Y7+Y5+1);
c34 = m.addConstr(1-Y5<=condition);
c35 = m.addConstr(X3-25<=1-condition);

#obejctive funtion treshold
c40 = m.addConstr(qualityOfLife>=35) 
m.optimize();
m.printAttr('X') #This prints the non-zero solutions found