import pulp

modelo = pulp.LpProblem("Problema_Agricola", pulp.LpMaximize)

x = pulp.LpVariable("Tomate", lowBound=0, cat="Integer")
y = pulp.LpVariable("Trigo", lowBound= 0, cat="Integer")


modelo += 300 * x + 200 * y       #função objetivo

modelo += x + y <= 80             #restrição de hectares
modelo += 40 * x + 20*y <= 2000   #restrição de mão de obra
modelo += 8 * x <= 320            #restrição água tomate

modelo.solve()                #função do pulp que resolve as coisa

print("Status: ", pulp.LpStatus[modelo.status])
print("n/Tomates plantados: ", x.varValue)
print("n/Trigo plantado: ", y.varValue)
print("n/Lucro maximo:", pulp.value(modelo.objective)) 
