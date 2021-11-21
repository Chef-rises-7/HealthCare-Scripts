import matplotlib.pyplot as plt
import json


avgs = []
index = []

for i in range(1,3):
  f = open("test"+str(500*i)+".json")
  RTT = json.loads(f.read())
  rtt = RTT["results"][0]["times"]
  avgs.append(sum(rtt)/len(rtt))
  index.append(500*i)

plt.plot(index,avgs,"r-")
plt.xlabel("Number of requests")
plt.ylabel("Average RTT")
plt.show()

for i in range(1,3):
  print(str(i*500)+" requests: "+str(round(avgs[i-1],2))+"ms")
