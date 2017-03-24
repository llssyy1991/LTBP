from basics import Node, init, TestInfo, Equipments, TestNode
from xml.etree.ElementTree import Element, tostring, SubElement
import csv

class NDE004TestInfo(TestNode):

    __rootTag = "NDE001-TestInfo"
    __Equipment = "ER"

    def __init__(self, testinfo, datapath):



        # append data

        f = open(datapath, 'rb')

        reader = csv.reader(f)

        for row in reader:
            data_frame = dict()
            data_frame["XLocation"] = row[0]
            data_frame["YLocation"] = row[1]
            data_frame["ElectricalReading"] = row[2]
            self.root.append(
                type("NDE001-Readings", (Node,), {"__init__": init})(data_frame, list = data_list).__ToNode__())