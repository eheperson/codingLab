
import seaborn as sns
import matplotlib.pyplot as plt
#
# 	
# Plot univariate or bivariate histograms to show distributions of datasets.
penguins = sns.load_dataset("penguins")
sns.histplot(data=penguins, x="flipper_length_mm", hue="species", multiple="stack")
plt.show()
#
# Plot univariate or bivariate distributions using kernel density estimation.
sns.kdeplot(data=penguins, x="flipper_length_mm", hue="species", multiple="stack")
plt.show()