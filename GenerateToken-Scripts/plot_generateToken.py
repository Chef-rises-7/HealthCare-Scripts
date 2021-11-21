import matplotlib.pyplot as plt
import json

avgs = []
index = []
for i in range(1,11):
  f = open(str(200*i)+".json")
  RTT = json.loads(f.read())
  rtt = RTT["results"][0]["times"]
  avgs.append(sum(rtt)/len(rtt))
  index.append(200*i)



plt.plot(index,avgs,"r-")
plt.xlabel("Number of requests")
plt.ylabel("Average RTT")
plt.show()

for i in range(1,11):
  print(str(i*200)+" requests: "+str(round(avgs[i-1],2))+"ms")

import json
import string
import random

for k in range(500,1500,500):
  res = []
  ben_id_counter = 1
  for i in range(1,k+1):
      final_obj={}
      final_obj["phone_number"] = i
      res.append(final_obj) 
  json_res = json.dumps(res)
  with open("data" + "_" + str(k) + ".json","w") as fs:
      fs.write(json_res)

