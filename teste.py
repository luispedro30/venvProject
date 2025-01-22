import pandas as pd
import matplotlib.pyplot as plt
print("Ambiente configurado corretamente!")
df = pd.DataFrame({'Coluna1': [1, 2], 'Coluna2': [3, 4]})
print(df)
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Teste de Plot")
plt.show()