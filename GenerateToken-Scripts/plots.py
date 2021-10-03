import matplotlib.pyplot as plt
import statistics
import json

f = open("load_test_results_1.json")
RTT = json.loads(f.read())

rtt = RTT["results"][0]["times"]
index = [i for i in range(1,len(rtt)+1)]

std = statistics.stdev(rtt)
avg = sum(rtt)/len(rtt)
print("Standard Deviation: ",std)
print("Average: ",avg)

fig1 = plt.figure(figsize=(20,10))
plt.bar(index[:200],rtt[:200],color="g")
plt.savefig("plot1.png")
plt.xlabel("RTT")
plt.ylabel("Request No")
plt.show()

fig2 = plt.figure(figsize=(20,10))
plt.bar(index[200:400],rtt[200:400],color="g")
plt.savefig("plot2.png")
plt.xlabel("RTT")
plt.ylabel("Request No")
plt.show()

fig3 = plt.figure(figsize=(20,10))
plt.bar(index[400:600],rtt[400:600],color="g")
plt.savefig("plot3.png")
plt.xlabel("RTT")
plt.ylabel("Request No")
plt.show()

fig4 = plt.figure(figsize=(20,10))
plt.bar(index[600:800],rtt[600:800],color="r")
plt.savefig("plot4.png")
plt.xlabel("RTT")
plt.ylabel("Request No")
plt.show()

fig5 = plt.figure(figsize=(20,10))
plt.bar(index[800:1000],rtt[800:1000],color="r")
plt.savefig("plot5.png")
plt.xlabel("RTT")
plt.ylabel("Request No")
plt.show()
