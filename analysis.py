import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("student_marks.csv", delimiter=",", skip_header=1)
marks = data[:, 1]

print("Mean:", np.mean(marks))
print("Median:", np.median(marks))
print("Variance:", np.var(marks))
print("Std Dev:", np.std(marks))

plt.hist(marks)
plt.xlabel("Marks")
plt.ylabel("Students")
plt.title("Marks Distribution")
plt.show()

plt.boxplot(marks)
plt.title("Box Plot")
plt.show()
