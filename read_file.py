
import json
import numpy as np



path = 'qap25'
#path = 'qap50'

problem_name = 'qapStr.25.p75.1'


#permuation size
n = int(problem_name.split('.')[1])

#size of QUBO
N = n**2

file_path = path +'//'+problem_name +'obj_con.json'


with open(file_path) as json_file:
    coeffs = json.load(json_file)

#constant terms for first objective (constant_obj1), second objective (constant_obj2) and constraint (constant_con)
constant_obj1 = coeffs[problem_name]['constant_obj_1']
constant_obj2 = coeffs[problem_name]['constant_obj_2']
constant_con = coeffs[problem_name]['constant_con']

#QUBO matrix for first objective (qubo_obj1), second objective (qubo_obj2) and constraint (qubo_con)
qubo_obj1 = np.array(coeffs[problem_name]['coeffs_obj_1'])
qubo_obj2 = np.array(coeffs[problem_name]['coeffs_obj_2'])
qubo_con = np.array(coeffs[problem_name]['coeffs_con'])