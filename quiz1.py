import numpy as np
import matplotlib.pyplot as plt
from sklearn.utils import resample

N = 5000 #poblacion

theta = 34 #parametro
n_space = [50, 100, 1000]#tamanos de muestra

for n in n_space:
    vec_theta_1 = []
    vec_theta_2 = []
    for i in range(10000):
        poblacion = [x for x in range(theta)]
        samples = resample(poblacion, n_samples=n, replace=True)#seleccion de muestra
        #calcular estimadores
        theta_1 = max(samples)
        theta_2 = 2 * np.mean(samples)
        vec_theta_1.append(theta_1)
        vec_theta_2.append(theta_2)

    #Generar histogramas
    plt.clf()
    plt.hist(vec_theta_1)
    plt.title("Histogram for $\\theta_1$ and n={}".format(n))
    plt.ylabel("Frecuencia")
    plt.xlabel("$\\theta_1$")
    plt.savefig(f"theta1_n{n}.png")

    plt.clf()
    plt.hist(vec_theta_2)
    plt.title("Histogram for $\\theta_2$ and n={}".format(n))
    plt.ylabel("Frecuencia")
    plt.xlabel("$\\theta_2$")
    plt.savefig(f"theta2_n{n}.png")