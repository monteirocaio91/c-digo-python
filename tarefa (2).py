import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "EMPRESA:" ['A', 'B', 'C']
    "FATURAMENTO:" [24, 69, 102]
         }

df = pd.DataFrame(dados)

plt.figure(figsize=(8, 5))
plt.bar(df['EMPRESA'] df['FATURAMENTO'], color = 'yellow', alpha = 0.7)
plt.title('faturamento mensal')
plt.xlabel('EMPRESA')
plt.ylabel('FATURAMENTO')