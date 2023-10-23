
from joblib import load
import matplotlib.pyplot as plt
import numpy as np

data = load('TempPDF/AllIndex.joblib')
data = [item * 100 for item in data]

label_name = ['Community', 'Air Pollution', 
            'Greenhouse Gas', 'Water Consumption', 
            'Mining Consumption',
            'Work Environment', 
            'Safety and Health', 'Human Rights', 
            'Governance Risk', 'Production Cost',
            'Domestic Job Creation', 'Economic Ripple Effect',
            'Domestic Reflux Rate']

x_lable = [item + " (%)" for item in label_name]

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(29.7, 21), dpi=300, subplot_kw=dict(polar=True))

angles = np.linspace(0, 2 * np.pi, len(data), endpoint=False).tolist()
angles += angles[:1]  # Repeat the first angle to close the circle
x_lable = x_lable + [x_lable[0]]
data = data + [data[0]]  # Repeat the first data point to match the length of angles
colors = plt.cm.get_cmap('rainbow', len(data))
ax.bar(angles, data, color=colors(range(len(data))), width=2 * np.pi / len(data))
ax.set_xticks(angles)
ax.set_xticklabels(x_lable, fontsize=18, fontweight='bold')
ax.set_yticklabels(ax.get_yticks(), fontsize=18, fontweight='bold')

fig.savefig("Results/Tendency.jpg", bbox_inches='tight')
