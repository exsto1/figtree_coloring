from matplotlib import pyplot as plt

data = open("files/4_ch/CL0057_no_RHH_ali.nexus.mcmc").readlines()
data = [i for i in data if "[" not in i]
data = data[1:]
data = [i.split("\t") for i in data]

x_data = []
y_data = []
for i in data:
    x_data.append(float(i[0]))
    y_data.append(float(i[-1]))


min_gen = 1000000
min_index = None
for i in range(len(x_data)):
    if x_data[i] > min_gen:
        min_index = i
        break


plt.figure(figsize=(15, 8))
plt.title("Average standard deviation of split frequencies\n4 chains long run")
plt.xlabel("Generation")
plt.ylabel("Standard deviation")
plt.plot(x_data[min_index:], y_data[min_index:])
plt.savefig("plot_4.svg")
plt.tight_layout()
plt.show()
