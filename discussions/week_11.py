import seaborn as sns
import matplotlib.pyplot as plt

# Q1
penguins = sns.load_dataset("penguins")
sns.histplot(data=penguins, x="bill_depth_mm")
plt.show()

# Q2
# The histplot() function automatically drops NAs
penguins_not_null = penguins[penguins["bill_depth_mm"].notnull()]
sns.histplot(data=penguins_not_null, x="bill_depth_mm")
# This figure will be identical to the previous one
plt.show()

# Q3
# Use the "color" argument
sns.histplot(data=penguins, x="bill_depth_mm", color="red")
plt.show()

# Q4
# A scatterplot is a good visualization for two continuous features
sns.scatterplot(data=penguins, x="bill_depth_mm", y="body_mass_g")
plt.show()

# Q5
sns.pairplot(penguins)
plt.show()

# Q6
sns.set_theme(rc={"figure.figsize": (6,6)})
sns.scatterplot(data=penguins, x="bill_depth_mm", y="body_mass_g")
plt.show()