import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET
import argparse

def xml_to_csv(path, args):
    txt_path = args.output
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        k=0
        for member in root.findall('object'):
            name = (xml_file.split("\\")[1]).split(".")[0]
            if k==0:
                with open(txt_path, "a") as file:
                    text = name
                    file.write(text)
                    #print(file_name)
                file.close()
                k=k+1
            else:
                with open(txt_path, "a") as file:
                    pass
                    #print(file_name)
                file.close()
        with open(txt_path, "a") as file:
            file.write("\n")
            #print(file_name)
        file.close()
    return 0


parser = argparse.ArgumentParser(description='original data to voc text')
parser.add_argument('--xml', type=str, default=None, metavar='N',
                    help='xml file path')
parser.add_argument('--output', type=str, default='train123.txt', metavar='N',
                    help='output file name')
def main():
    args = parser.parse_args()
    image_path = args.xml
    xml_to_csv(image_path,args)
    print('Successfully converted xml to text.')

if __name__ == '__main__':
    main()