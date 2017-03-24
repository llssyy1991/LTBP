from basics import Node, init, TestInfo, Equipments
from xml.etree.ElementTree import Element, tostring, SubElement
import csv
from TestNode import TestNode

class NDE001TestInfo(TestNode):
    # interface for ER

    __rootTag   = "NDE001-TestInfo"
    __Equipment = "ER"

    def __init__(self, testinfo, datapath):

        self.rootTag    = self.__rootTag
        self.Equip      = self.__Equipment
        super(NDE001TestInfo, self).__init__(testinfo)

        # append data

        f = open(datapath, 'rb')

        reader = csv.reader(f)

        for row in reader:

            data_frame = dict()
            data_frame["XLocation"] = row[0]
            data_frame["YLocation"] = row[1]
            data_frame["ElectricalReading"] = row[2]
            data_list = ["YLocation", "XLocation", "ElectricalReading"]
            self.root.append(
                type("NDE001-Readings", (Node,), {"__init__": init})(data_frame, data_list).__ToNode__())




if __name__ =="__main__":

    teinfo = TestInfo("test", "test", "test", "test", "test",66)

    test = NDE001TestInfo(teinfo, "/home/lsy/Desktop/ER.ER")

    print tostring(test.root)