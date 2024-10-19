import math
import numpy as np
import pandas as pd
from html.entities import entitydefs

## 5F85EBC4069BD362
## 只需要修改Frequency, Amplitude, Phase对应的值即可
## 根据第一幅图的内容, 填写第二幅图里面的表格  中文
data = {
    "Symbol": ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'],
    "Frequency": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    "Amplitude": [1.41, 2.83, 2.24, 2.24, 1.41, 2.83, 2.24, 2.24, 1.41, 2.83, 2.24, 2.24, 1.41, 2.83, 2.24, 2.24],
    "Phase": [45, 45, 63.43, 26.57, 135, 135, 153.43, 116.57, 225, 225, 243.43, 206.57, 315, 315, 333.43, 296.57]
}

df_encoding = pd.DataFrame(data)
df_encoding['X'] = df_encoding['Amplitude'] * np.cos(np.radians(df_encoding['Phase']))
df_encoding['Y'] = df_encoding['Amplitude'] * np.sin(np.radians(df_encoding['Phase']))

# Select only the Symbol, X, and Y columns for the output
df_coordinates = df_encoding[['Symbol', 'X', 'Y']]
print(df_coordinates)



def calculate_y(x_value):
    assert len(data['Frequency']) == len(data['Amplitude']) == len(data['Phase'])

    n_length = len(data['Amplitude'])
    y_value_lst = []
    for idx in range(n_length):
        y_value = data['Amplitude'][idx] * math.sin(2 * math.pi * (data['Frequency'][idx]) * x_value + (data['Phase'][idx] / 180 * math.pi))
        y_value = round(y_value, 2)
        y_value_lst.append(y_value)
    return y_value_lst



def print_formula():
    assert len(data['Frequency']) == len(data['Amplitude']) == len(data['Phase'])
    n_length = len(data['Amplitude'])
    y_formula_lst = []
    for idx in range(n_length):
        # angle = 180 / data['Phase'][idx]
        phase = f"{entitydefs['pi']} * {data['Phase'][idx]}/180"
        formula = f"y = {data['Amplitude'][idx]} * sin(2{entitydefs['pi']}x + {phase})"
        y_formula_lst.append(formula)

    return y_formula_lst



print('\n================================')
print("Compute Y value according X value")

print(calculate_y(0.3))
print("\n")
print(calculate_y(0.7))
print('\n=============================')
print('Print Formulas:\n')
formula_df = pd.DataFrame()
formula_df['Formula'] = print_formula()
print(formula_df)