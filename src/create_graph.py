import matplotlib.pyplot as plt




def check_rnti_option(rnti,user_options):
    #check rnti command filter option

    #if no filter selected then pass
    if(user_options.rnti1 is None):
        return False

    #elif r1 selected check filter
    elif(user_options.rnti1 and rnti == user_options.rnti1):
        return False

    #elif r2 selected check filter
    elif(user_options.rnti2 and rnti == user_options.rnti2):
        return False

    #else a filter has been selected but no match, continue
    else:
        return True




def dl_throughput_graph(data_sorted, min_timestamp,user_options):

    plt.figure()

    #enumerate each rnti with its data associated
    for rnti, data in data_sorted.items():

        #to calcul the dl throuhput we have to calcul the difference between 2 packets...
        previous_dl = 0
        
        #create two list to fulfill with the selected data that we need
        timestamp_list = []
        dl_throughput = []
        
        #check rnti command filter option
        if(check_rnti_option(rnti,user_options)):
            continue


        #plot each packet of the rnti
        for packet in data:

            timestamp = round((int(packet[5]) - min_timestamp)/1000)

            #we match time option filter of the user
            if(timestamp < user_options.start or timestamp > user_options.end):
                previous_dl = int(packet[6])
                continue

            timestamp_list.append(timestamp)

            #we want MB/s
            dl_throughput.append((int(packet[6])-previous_dl)*8/1000000)

            #update the current dl throughput
            previous_dl = int(packet[6])

        plt.plot(timestamp_list,dl_throughput, marker='o', label=rnti,markersize=3)


    plt.legend()
    plt.xlabel("Time in second")
    plt.ylabel("DL throughput in MB/s")
    plt.title("DL throughput graph")

    #save graph
    plt.savefig("graph/DL_throughput.png")

    plt.close()



def ul_throughput_graph(data_sorted,min_timestamp,user_options):

    plt.figure()

    #enumerate each rnti with its data associated
    for rnti, data in data_sorted.items():

        #to calcul the dl throuhput we have to calcul the difference between 2 packets...
        previous_ul = 0
        
        #create two list to fulfill with the selected data that we need
        timestamp_list = []
        dl_throughput = []
        
        #check rnti command filter option
        if(check_rnti_option(rnti,user_options)):
            continue


        #plot each packet of the rnti
        for packet in data:

            timestamp = round((int(packet[5]) - min_timestamp)/1000)

            #we match time option filter of the user
            if(timestamp < user_options.start or timestamp > user_options.end):
                previous_ul = int(packet[9])
                continue

            timestamp_list.append(timestamp)

            #we want MB/s
            dl_throughput.append((int(packet[9])-previous_ul)*8/1000000)

            #update the current ul throughput
            previous_ul = int(packet[9])

        plt.plot(timestamp_list,dl_throughput, marker='o', label=rnti,markersize=3)


    plt.legend()
    plt.xlabel("Time in second")
    plt.ylabel("UL throughput in MB/s")
    plt.title("UL throughput graph")

    #save graph
    plt.savefig("graph/UL_throughput.png")

    plt.close()



def rsrq_graph(data_sorted,min_timestamp,user_options):

    plt.figure()

    #enumerate each rnti with its data associated
    for rnti, data in data_sorted.items():
        
        #create two list to fulfill with the selected data that we need
        timestamp_list = []
        rssi = []
        
        #check rnti command filter option
        if(check_rnti_option(rnti,user_options)):
            continue


        #plot each packet of the rnti
        for packet in data:

            timestamp = round((int(packet[5]) - min_timestamp)/1000)

            #we match time option filter of the user
            if(timestamp < user_options.start or timestamp > user_options.end):
                continue

            timestamp_list.append(timestamp)

            rssi.append(float(packet[16]))

        plt.plot(timestamp_list,rssi, marker='o', label=rnti,markersize=1)


    plt.legend()
    plt.xlabel("Time in second")
    plt.ylabel("RSRQ in dBm")
    plt.title("RSRQ graph")

    #save graph
    plt.savefig("graph/RSRQ_graph.png")

    plt.close()



def sinr_graph(data_sorted,min_timestamp,user_options):

    plt.figure()

    #enumerate each rnti with its data associated
    for rnti, data in data_sorted.items():
        
        #create two list to fulfill with the selected data that we need
        timestamp_list = []
        rsrp = []
        
        #check rnti command filter option
        if(check_rnti_option(rnti,user_options)):
            continue


        #plot each packet of the rnti
        for packet in data:

            timestamp = round((int(packet[5]) - min_timestamp)/1000)

            #we match time option filter of the user
            if(timestamp < user_options.start or timestamp > user_options.end):
                continue

            timestamp_list.append(timestamp)

            rsrp.append(float(packet[17]))

        plt.plot(timestamp_list,rsrp, marker='o', label=rnti,markersize=1)


    plt.legend()
    plt.xlabel("Time in second")
    plt.ylabel("SINR in dBm")
    plt.title("SINR graph")

    #save graph
    plt.savefig("graph/SINR_graph.png")

    plt.close()



def rsrp_graph(data_sorted,min_timestamp,user_options):

    plt.figure()

    #enumerate each rnti with its data associated
    for rnti, data in data_sorted.items():
        
        #create two list to fulfill with the selected data that we need
        timestamp_list = []
        rssi = []
        
        #check rnti command filter option
        if(check_rnti_option(rnti,user_options)):
            continue


        #plot each packet of the rnti
        for packet in data:

            timestamp = round((int(packet[5]) - min_timestamp)/1000)

            #we match time option filter of the user
            if(timestamp < user_options.start or timestamp > user_options.end):
                continue

            timestamp_list.append(timestamp)

            rssi.append(float(packet[18]))

        plt.plot(timestamp_list,rssi, marker='o', label=rnti,markersize=1)


    plt.legend()
    plt.xlabel("Time in second")
    plt.ylabel("RSRP in dBm")
    plt.title("RSRP graph")

    #save graph
    plt.savefig("graph/RSRP_graph.png")

    plt.close()

def rssi_graph(data_sorted,min_timestamp,user_options):

    plt.figure()

    #enumerate each rnti with its data associated
    for rnti, data in data_sorted.items():
        
        #create two list to fulfill with the selected data that we need
        timestamp_list = []
        rssi = []
        
        #check rnti command filter option
        if(check_rnti_option(rnti,user_options)):
            continue


        #plot each packet of the rnti
        for packet in data:

            timestamp = round((int(packet[5]) - min_timestamp)/1000)

            #we match time option filter of the user
            if(timestamp < user_options.start or timestamp > user_options.end):
                continue

            timestamp_list.append(timestamp)

            rssi.append(float(packet[19]))

        plt.plot(timestamp_list,rssi, marker='o', label=rnti,markersize=1)


    plt.legend()
    plt.xlabel("Time in second")
    plt.ylabel("RSSI in dBm")
    plt.title("RSSI graph")

    #save graph
    plt.savefig("graph/RSSI_graph.png")

    plt.close()






def pucchSnr_graph(data_sorted,min_timestamp,user_options):

    plt.figure()

    #enumerate each rnti with its data associated
    for rnti, data in data_sorted.items():
        
        #create two list to fulfill with the selected data that we need
        timestamp_list = []
        pucchsnr = []
        
        #check rnti command filter option
        if(check_rnti_option(rnti,user_options)):
            continue


        #plot each packet of the rnti
        for packet in data:

            timestamp = round((int(packet[5]) - min_timestamp)/1000)

            #we match time option filter of the user
            if(timestamp < user_options.start or timestamp > user_options.end):
                continue

            timestamp_list.append(timestamp)

            pucchsnr.append(float(packet[21]))

        plt.plot(timestamp_list,pucchsnr, marker='o', label=rnti,markersize=1)


    plt.legend()
    plt.xlabel("Time in second")
    plt.ylabel("Pucch Snr in dB")
    plt.title("Pucch Snr graph")

    #save graph
    plt.savefig("graph/PucchSnr_graph.png")

    plt.close()



def puschSnr_graph(data_sorted,min_timestamp,user_options):

    plt.figure()

    #enumerate each rnti with its data associated
    for rnti, data in data_sorted.items():
        
        #create two list to fulfill with the selected data that we need
        timestamp_list = []
        puschsnr = []
        
        #check rnti command filter option
        if(check_rnti_option(rnti,user_options)):
            continue


        #plot each packet of the rnti
        for packet in data:

            timestamp = round((int(packet[5]) - min_timestamp)/1000)

            #we match time option filter of the user
            if(timestamp < user_options.start or timestamp > user_options.end):
                continue

            timestamp_list.append(timestamp)

            puschsnr.append(float(packet[22]))

        plt.plot(timestamp_list,puschsnr, marker='o', label=rnti,markersize=1)


    plt.legend()
    plt.xlabel("Time in second")
    plt.ylabel("Pusch Snr in dB")
    plt.title("Pusch Snr graph")

    #save graph
    plt.savefig("graph/PuschSnr_graph.png")

    plt.close()