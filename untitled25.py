# -*- coding: utf-8 -*-
"""Untitled25.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GkcxPjtRjhpk1ylA9h74Oysv83fE0SFW
"""

# Google Colabda tasodifiy nuqtalar uchun scatter grafik
import numpy as np
import matplotlib.pyplot as plt

# Tasodifiy nuqtalar yaratish
np.random.seed(42)  # Natijani qayta tiklash uchun
x = np.random.rand(100) * 10  # X koordinatalari (0 dan 10 gacha)
y = np.random.rand(100) * 10  # Y koordinatalari (0 dan 10 gacha)
sizes = np.random.rand(100) * 300  # Nuqta kattaligi (radius)
colors = np.random.rand(100)  # Har bir nuqta uchun rang

# Scatter grafikni chizish
plt.figure(figsize=(8, 6))
scatter = plt.scatter(x, y, s=sizes, c=colors, cmap='viridis', alpha=0.7, edgecolor='k')
plt.colorbar(scatter, label='Rang qiymati')  # Ranglar shkalasi
plt.title('Tasodifiy nuqtalar scatter grafigi')
plt.xlabel('X koordinata')
plt.ylabel('Y koordinata')
plt.grid(True)
plt.show()