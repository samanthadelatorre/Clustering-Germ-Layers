#!C:\Users\Shonak\capstone_180a\Scripts\python.exe

import os
import sys
# import json

sys.path.insert(0, f"{os.path.join(sys.path[0], 'src')}")
sys.path.insert(0, 'src')
from selenium_functions import get_keywords, tcga_scrape, download_data


if __name__ == "__main__":
    args = sys.argv
    print('\n<> indicates an optional requirement\n')
    if len(args) == 1:
        print('Please specify function you want to use');

    elif 'createDict' in args[1]:
        print('After createDict specify Parameter.json <Data_dictionary.csv>')
        inp = input("Did your parameters fit this order? (y/n) \n")
        if inp.lower() != 'y': assert False, "Redo with correct order"

        if os.path.isfile(args[2]):
            if len(args) >= 4:
                get_keywords(args[2], args[3])
            else:
                get_keywords(args[2])
        else:
            print(f'{args[2]} does not exist')

    elif 'queryData' in args[1]:
        print('Order after queryData is Parameter.json Query.json ')
        inp = input("Did your parameters fit this order? (y/n) \n")
        if inp.lower() != 'y': assert False, "Redo with correct order"

        if os.path.isfile(args[2]) and os.path.isfile(args[3]):
            tcga_scrape(args[2], args[3])
        else:
            if os.path.isfile(args[2]) == False:
                print(f'{args[2]} does not exist')
            if os.path.isfile(args[3]) == False:
                print(f'{args[3]} does not exist')

    elif 'downloadData' in args[1]:
        print('Order after queryData is Parameter.json <[CSVs]>')
        print('CSVs can be obtained through * pattern or from json file.')
        print('However, make sure indicies in json file match.\n')

        print("Addition of command line patterns will override all manually " +
              "entered csv files from Parameters.json file,\n")

        inp = input("Did your parameters fit this order? (y/n) \n")
        if inp.lower() != 'y': assert False, "Redo with correct order"

        if os.path.isfile(args[2]):
            if len(args) >= 4:
                download_data(args[2], args[3:])
            else:
                download_data(args[2])
        else:
            if os.path.isfile(args[2]) == False:
                print(f'{args[2]} does not exist')

    else:
        print("Choices are currently only createDict, queryDict, and downloadData")
