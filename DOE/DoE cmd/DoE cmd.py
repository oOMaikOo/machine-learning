# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 19:22:07 2019

@author: maikloehn
maik.loehn@buehlermotor.com
Version : 0.0.1
"""
import dexpy.factorial
import dexpy.ccd
import dexpy.power
from statsmodels.formula.api import ols
from sys import exit
import pandas as pd
import evaluate_data as ev

print("########         ########        ##########             B")
print("#       #       #        #       #                     B B")
print("#        #      #        #       #                    B B B")
print("#         #     #        #       #                   B  B  B")
print("#         #     #        #       #######               B B")
print("#         #     #        #       #                    B B B  ")
print("#        #      #        #       #                   B  B  B")
print("#       #       #        #       #                      B   ")
print("########         ########        ##########             B   ")
print("")
print(" Menue:")
print(" 1. Neuen Versuchsplan erstellen")
#print("\t2. Bestehendes Versuchsplan fortsetzen")
print(" 3. Beenden")


factors_name = []
factors_result = []
dict_low = {}
dict_high = {}
i = 0
doe_design = pd.DataFrame()
x = ev.plots()

'''
###########
Start:
Menue
##########
'''
while True:
    try:
        menue = int(input(" Bitte eingeben : "))
        if menue == 1 or menue == 3:
            break
    except ValueError:
        print(" Falsche Eingabe!")
   
if menue == 2:
    #s = input("\tNamen des Versuchplanes eingeben : ")
    #doe_load_name = s+"_basis_doe.csv"
    #doe_design = doe_design.append(doe_design.from_csv(doe_load_name))
    #print(doe_design)
    pass

if menue >= 3:
    exit()
    
'''
###########
Menue
End
##########
'''
doe_name = input(" Bitte Namen für den neuen Versuchsplan eingeben : ")  
'''
###########
Start:
Genereate the factors
##########
'''
##### Input how many factors are to observe?
while True:
    try:
        factors = int(input(" Bitte die Anzahl der zu untersuchenden Faktoren eingeben (minimum 4) : "))
        if factors >= 4:
            break
    except ValueError:
        print(" Falsche Eingabe!")
        
##### Input for each factor a name!
for i in range(factors):
    s = str(input(" Bitte Faktor X"+str(i+1)+" benennen : "))
    factors_name.append(s) 

##### Input for each factor the upper and lower limit!
for i in range(factors):
    while True:
        try:
            dict_low[factors_name[i]] = float(input(" Bitte den niedrigsten Wert für Faktor "+factors_name[i]+" eingeben : "))
            dict_high[factors_name[i]] = float(input(" Bitte den hoechsten Wert für Faktor "+factors_name[i]+" eingeben : "))
            if dict_low[factors_name[i]] < dict_high[factors_name[i]]:
                break
            else:
                print(" # Der Wert für den Faktor "+factors_name[i]+" niedrig, war größer als der hoechste Wert # ")
        except ValueError:
            print(" Falsche Eingabe!")
'''
###########
Genereate the factors
End:
##########
'''
'''
###########
Start:
Genereate the design
##########
'''
doe_design = dexpy.factorial.build_factorial(factors, 2**(factors))

doe_design.columns = factors_name

twofi_model = "(" + '+'.join(doe_design.columns) + ")**2"
#test = dexpy.ccd.build_ccd(factors, alpha=1, center_points=1)
#test1 = dexpy.factorial.build_full_factorial(factors)
actual_design = dexpy.design.coded_to_actual(doe_design, dict_low, dict_high)
'''
###########
Genereate the design
End:
##########
'''

'''
###########
Start:
Save design and basis
##########
'''
save_file_design = doe_name+"_design_doe.csv"
save_file_basis = doe_name+"_basis_doe.csv"
actual_design.to_csv(save_file_design,sep='\t', encoding='utf-8')     
doe_design.to_csv(save_file_basis,sep='\t', encoding='utf-8')
#actual_design.to_csv("doe.csv",sep='\t', encoding='utf-8')
#doe_design.from_csv("Medtronic_basis_doe.csv")
print(actual_design)
print(doe_design)
print(" ###############################################")
print(" Aktuelles Design wurde automatisch gespeichert : "+save_file_design)
print(" Aktuelle Basis wurde automatisch gespeichert : "+save_file_basis)
'''
###########
Save design and basis
End
##########
'''

'''
###########
Start:
Menue
##########
'''
print(" Menue:")
print(" 1. Auswerung starten")
print(" 2. Beenden")
while True:
    try:
        menue = int(input(" Bitte eingeben : "))
        if menue < 3:
            break
    except ValueError:
        print(" Falsche Eingabe!")
if menue == 2:
    exit()
else:
    pass
'''
###########
Menue
End
##########
'''

'''
###########
Start:
Input results and evaluation
##########test
'''
for f in range(2**factors):
    while True:
        try:
            f = float(input(" Bitte das Ergebniss für den Lauf "+str(f)+" eingeben : "))
            factors_result.append(f)
            break
        except ValueError:
            print(" Falsche Eingabe!")


doe_design['Ergebniss'] = factors_result
actual_design['Ergebniss'] = factors_result
print("\t#################################################")
      
doe_design.to_csv(doe_name+"_doe_plan_with_result.csv",sep='\t', encoding='utf-8')
actual_design.to_csv(doe_name+"_actual_doe_plan_with_result.csv",sep='\t', encoding='utf-8')

lm = ols("Ergebniss ~" + twofi_model, data=doe_design).fit()
print(lm.summary2())

f_name = doe_name+"_actual_doe_plan_with_result.csv"

x.plot_interaction_plot(f_name)


pvalues = lm.pvalues[1:]
reduced_model = '+'.join(pvalues.loc[pvalues < 0.05].index)
lm = ols("Ergebniss ~" + reduced_model, data=doe_design).fit()
print(lm.summary2())
'''
###########
Input results and evaluation
End
##########
'''