from scipy.optimize import linprog

c = [-300, -200]                   #coeficientes da função objetivo         
A_ub = [[1,1],[40,20],[8, 0]]      #coeficientes das restrições
b_ub = [80, 2000, 320]             #valores máximos que cada restrição pode ter

res = linprog(c, 
              A_ub=A_ub, 
              b_ub=b_ub, method="highs", 
              bounds=([0, None], [0, None]), 
              integrality=[1,1])

print("Quantidade plantada: ", res.x, 
      "\nLucro total: ", -res.fun)