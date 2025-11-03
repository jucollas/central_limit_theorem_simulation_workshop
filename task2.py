
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

from task1 import generate_numbers_normal, average, variance

def generate_samples(num_samples,  len_sample, avg_expected, var_expected):
  samples = []
  for _ in range(num_samples):
    samples.append(generate_numbers_normal(avg_expected, var_expected, len_sample))
  return samples


def grafix(avg_of_samples, var_of_samples, avg_expected, var_expected, len_samples):
  plt.figure(figsize=(7,4))
  sns.histplot(var_of_samples, kde=True, color='skyblue')
  plt.title('Distribución de varianza estimada (500 muestras)')
  plt.xlabel('Varianza estimada')
  plt.ylabel('Frecuencia')
  plt.show()

  # --- (c) Distribución de medias estimadas ---
  plt.figure(figsize=(7,4))
  sns.histplot(avg_of_samples, kde=True, color='lightgreen')
  plt.title('Distribución de media estimada (500 muestras)')
  plt.xlabel('Media estimada')
  plt.ylabel('Frecuencia')
  plt.show()

  # --- (d) Comparación con Teorema Central del Límite ---
  plt.figure(figsize=(7,4))
  sns.histplot(avg_of_samples, kde=True, stat='density', color='lightcoral', label='Distribución simulada')

  # Curva normal teórica según TCL
  x = np.linspace(min(avg_of_samples), max(avg_of_samples), 200)
  pdf = norm.pdf(x, avg_expected, np.sqrt(var_expected/len_samples))
  plt.plot(x, pdf, 'k--', label='Distribución normal teórica')

  plt.title('Comparación: medias simuladas vs. Teorema Central del Límite')
  plt.xlabel('Media estimada')
  plt.ylabel('Densidad')
  plt.legend()
  plt.show()

def main():
  num_samples = 500
  len_sample = 150
  avg_expected = 5
  var_expected = 1.2
  samples = generate_samples(num_samples,  len_sample, avg_expected, var_expected)
  avg_of_samples = list(map(average, samples))
  var_of_samples = list(map(variance, samples))
  grafix(avg_of_samples, var_of_samples, avg_expected, var_expected, len_sample)
main()