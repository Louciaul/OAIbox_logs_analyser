import json
import csv
import argparse

# usage : python json_to_csv.py FILE.json FILE.csv

def json_to_csv():

    parser = argparse.ArgumentParser(description='Program description')

    # Adding Mandatory command line arguments
    parser.add_argument('json', help='targeted Json file to extract data')

    parser.add_argument('csv', help='targeted csv file')

    # Analysing command line arguments
    args = parser.parse_args()

    json_file = "json/" + args.json

    csv_file = "csv/" + args.csv
    
    #cleaning the data
    data = clear_data(json_file)

    #making the csv
    writing_csv(csv_file,data)



#Just to get a clean and nice dic
def setup_dic():
    dic = {}
    dic["rnti"] = None
    dic["id"] = None
    dic["frame"] = None
    dic["slot"] = None
    dic["pci"] = None
    dic["timestamp"] = None
    dic["dlBytes"] = None
    dic["dlMcs"] = None
    dic["dlBler"] = None
    dic["ulBytes"] = None
    dic["ulMcs"] = None
    dic["ulBler"] = None
    dic["ri"] = None
    dic["pmi"] = None
    dic["phr"] = None
    dic["pcmax"] = None
    dic["rsrq"] = None
    dic["sinr"] = None
    dic["rsrp"] = None
    dic["rssi"] = None
    dic["cqi"] = None        
    dic["pucchSnr"] = None
    dic["puschSnr"] = None

    return(dic)
    

#parsing each packet, 1 dic <-> 1 ue
def parsingdata(line, index_ue):
    dic = setup_dic()
    
    dic["rnti"] = index_ue["rnti"]
    dic["id"] = line["id"]
    dic["frame"] = line["frame"]
    dic["slot"] = line["slot"]
    dic["pci"] = line["pci"]
    dic["timestamp"] = line["timestamp"]
    dic["dlBytes"] = index_ue["dlBytes"]
    dic["dlMcs"] = index_ue["dlMcs"]
    dic["dlBler"] = index_ue["dlBler"]
    dic["ulBytes"] = index_ue["ulBytes"]
    dic["ulMcs"] = index_ue["ulMcs"]
    dic["ulBler"] = index_ue["ulBler"]
    dic["ri"] = index_ue["ri"]
    dic["pmi"] = index_ue["pmi"]
    dic["phr"] = index_ue["phr"]
    dic["pcmax"] = index_ue["pcmax"]
    dic["rsrq"] = index_ue["rsrq"]
    dic["sinr"] = index_ue["sinr"]
    dic["rsrp"] = index_ue["rsrp"]
    dic["rssi"] = index_ue["rssi"]
    dic["cqi"] = index_ue["cqi"]        
    dic["pucchSnr"] = index_ue["pucchSnr"]
    dic["puschSnr"] = index_ue["puschSnr"]
    
    return dic


#writing csv
def writing_csv(csv_file, data_cleared):

    headers = list(data_cleared[0].keys())

    with open(csv_file, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data_cleared)




#main function that start the process of parsing/clearing/writing

def clear_data(json_file):

    data_cleared = []
    # Loading json file
    with open(json_file, 'r') as json_file:
        data_json = json.load(json_file)

    for line in data_json:
        ues_tab = line["ues"]

        #deleting line without ue
        if not ues_tab:
            continue
        
        #creating a line for each eu in a packet
        for index_ue in ues_tab:
            dic = parsingdata(line,index_ue)
            
            data_cleared.append(dic)
    
    return data_cleared



json_to_csv()


