import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# gru_outputs = open("gru_outputs.csv").read()
# targets = open("targets.csv").read()

with open("gru_outputs.csv") as file_name:
    gru_outputs = np.loadtxt(file_name, delimiter=",")
with open("targets.csv") as file_name:
    targets = np.loadtxt(file_name, delimiter=",")

# print(array)
gru_outputs_mod = [[]]
targets_mod = [[]]
gru_outputs_mod[0] = gru_outputs
targets_mod[0] = targets
print(gru_outputs_mod)
print(targets_mod)

plt.figure(figsize=(14,10))
# plt.subplot(2,2,1)
plt.plot(gru_outputs_mod[0][-200:], "-o", color="g", label="Predicted")
plt.plot(targets_mod[0][-200:], color="b", label="Actual")
plt.ylabel('PM 10')
plt.legend()

plt.show()