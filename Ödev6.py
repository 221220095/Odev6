import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Koordinatları üretiyoruz burada
num_points = 1000
data = {
    'x': np.random.randint(0, 1001, num_points),
    'y': np.random.randint(0, 1001, num_points)
}

df = pd.DataFrame(data)

excel_path = 'kordinatlar.xlsx'
df.to_excel(excel_path, index=False)

#Excele kaydettikten sonra excelden randon üretilen noktaları okuyoruz

df = pd.read_excel(excel_path)

#Izgarayı bölüyoruz
grid_size = 200  # 200x200 ızgara
num_bins = 1000 // grid_size

# Koordinatları ızgaralara böldüm
df['x_bin'] = pd.cut(df['x'], bins=range(0, 1001, grid_size), labels=False)
df['y_bin'] = pd.cut(df['y'], bins=range(0, 1001, grid_size), labels=False)

colors = ['red', 'blue', 'green', 'purple', 'orange']

plt.figure(figsize=(10, 10))
for i in range(num_bins):
    for j in range(num_bins):
        color_index = (i + j) % 5  #5 satır ve sütunumuz olduğu için ayrı gruplandırma yaptım
        mask = (df['x_bin'] == i) & (df['y_bin'] == j)
        plt.scatter(df.loc[mask, 'x'], df.loc[mask, 'y'], color=colors[color_index])

plt.grid(True)
plt.title('Izgara')
plt.xlabel('X Kordinatı')
plt.ylabel('Y Kordinatı')
plt.savefig('Izgara.png') 
plt.show()
