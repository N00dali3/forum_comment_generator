import time
import json


menu = """
Forum Comments
==============
0: Exit
1: Display Comments
2: Add Comment
"""
filename = "step4_data.json"

try:
    fp = open(filename, 'r')
except:
    records = []
else:
    ds = json.load(fp)
    records = ds["records"]
    fp.close()

while True:
    print(menu)
    selection = input("Please choose option 0, 1, or 2 from the menu above: ")
    if selection == "0":
        print("Goodbye! Thank you for participating.")
        break
    
    elif selection == "1":
        print("""
Reader Comments
=================================================""")
        for record in records:
            print("-------------------------------------------------")
            print(f'{record["date"]} - {record["name"]}')
            print(f'{record["comment"]}\n')
            print("-------------------------------------------------")
        print("=================================================")
        
                
    elif selection == "2":
            current_time = time.ctime()
            nm = input("\nPlease enter your name: ")
            cmt = input("Please enter a one line comment: ")
            comment = {"date": current_time , "name": nm , "comment": cmt}
            records.append(comment)

ds = {"records": records}
fp = open(filename, "w")
json.dump(ds, fp)

fp.close()
    
    