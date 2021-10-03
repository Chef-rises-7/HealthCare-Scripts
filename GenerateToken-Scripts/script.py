import json
import string
import random
# phone_numbers = []
# for i in range(1,1001):
#     phone_numbers.append(i)

res = []
ben_id_counter = 1


for i in range(0,1000):
    final_obj={}
    final_obj["beneficiaries"] = []
    final_obj["phone_number"] = i
    final_obj["doses"] = {}

    for j in range(4):
        ben = {}
        ben["beneficiary_reference_id"] = str(ben_id_counter)
        ben["name"] = ''.join(random.choices(string.ascii_uppercase +string.digits, k = 5))
        ben["birth_year"] = "1995"
        ben["gender"] = "Male"
        ben["mobile_number"] = str(i)
        ben["photo_id_type"] = "Driving License"
        ben["photo_id_number"] = "99999"
        ben["comorbidity_ind"] = "Y"
        ben["vaccination_status"] = "Not Vaccinated"
        ben["vaccine"] = "covishield"
        ben["dose1_date"] = "25-08-2021"
        ben["dose2_date"] = ""
        final_obj["beneficiaries"].append(ben)
        final_obj["doses"][str(ben_id_counter)] = "dose1"
        ben_id_counter=ben_id_counter + 1

    res.append(final_obj)

ben_id_counter = 1
for i in range(600,800):
    temp_ben_id = res[i]["beneficiaries"][1]["beneficiary_reference_id"]
    res[i]["beneficiaries"][1]["beneficiary_reference_id"] = ben_id_counter
    # print(temp_ben_id)
    del res[i]["doses"][temp_ben_id]
    res[i]["doses"][str(ben_id_counter)] = "dose1"
    ben_id_counter = ben_id_counter + 1
print(len(res))

for i in range(800,1000):
    del res[i]["beneficiaries"][1]["name"]

json_res = json.dumps(res)

with open("data.json","w") as fs:
    fs.write(json_res)






