import argparse
import csv

from sort_data import *
from create_graph import *

class Options:
    def __init__(self, start=0, end=1800, rnti1=None, rnti2=None):
        self.start = start
        self.end = end
        self.rnti1 = rnti1
        self.rnti2 = rnti2

user_options = Options()

#use clean data to create graph of download bytes with each RNTI
def start_graph(data_sorted,user_options):

    min_timestamp = find_minimum_timestamp(data_sorted)

    dl_throughput_graph(data_sorted, min_timestamp, user_options)

    ul_throughput_graph(data_sorted, min_timestamp, user_options)

    rsrq_graph(data_sorted,min_timestamp, user_options)

    sinr_graph(data_sorted,min_timestamp, user_options)

    rsrp_graph(data_sorted,min_timestamp, user_options)

    rssi_graph(data_sorted,min_timestamp, user_options)

    pucchSnr_graph(data_sorted,min_timestamp, user_options)

    puschSnr_graph(data_sorted,min_timestamp, user_options)



def main():

    parser = argparse.ArgumentParser(description='Program description')

    # Adding Mandatory command line arguments
    parser.add_argument('csv', help='targeted csv file to extract data')

    parser.add_argument('-s','--start',type=int, help="Start timer of data")

    parser.add_argument('-e','--end',type=int, help="End timer of data")

    parser.add_argument('-r1','--rnti1',type=str, help="Select one rnti")

    parser.add_argument('-r2','--rnti2',type=str, help="Select a second rnti (optionnal)")

    # Analysing command line arguments
    args = parser.parse_args()

    csv_file = args.csv

    if args.start:
        user_options.start = args.start
    
    if args.end:
        user_options.end = args.end
    
    if args.rnti1:
        user_options.rnti1 = args.rnti1
    
    if args.rnti2:
        user_options.rnti2 = args.rnti2

    with open(csv_file, 'r') as csv_data:
        data = list(csv.reader(csv_data))
         
    data_sorted = sort_rnti(data)
    start_graph(data_sorted,user_options)

main()
