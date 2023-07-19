import datetime

"""sort the data by rnti
The data structure is a dictionnary
Rnti name is the key,
The value is a list containing all the packet of the rnti
"""
def sort_rnti(data):
    
    sort_result = {}

    #deleting first line containing titles
    data.pop(0)

    for line in data:
        
        #get the rnti in our database
        rnti_name = line[0]

        #if it doesn't exist yet, create an entry
        if not rnti_name in sort_result:
            sort_result[rnti_name] = []

        #get the list
        rnti_tab = sort_result[rnti_name]

        rnti_tab.append(line)

    return sort_result

#To create a proper time axis and use the timestamp data
def find_minimum_timestamp(data_sorted):

    #We need to find a minimun, we start with our own timestamp as a max
    minimun_timestamp = int(datetime.datetime.now().timestamp() * 1000)

    for rnti, data in data_sorted.items():

        for packet in data:

            if int(packet[5]) < minimun_timestamp:
                minimun_timestamp = int(packet[5])

    return minimun_timestamp
