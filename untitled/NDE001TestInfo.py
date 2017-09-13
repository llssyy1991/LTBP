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
        self.readList   = []
        super(NDE001TestInfo, self).__init__(testinfo)

        # append data

        f = open(datapath, 'rb')

        reader = csv.reader(f)

        count = 0

        for row in reader:
            if count == 0:
                count += 1
                continue
            if float(row[2]) == -1:
                continue
            data_frame = dict()
            data_frame["XLocation"] = str(float(row[0]) * 0.00328084)
            data_frame["YLocation"] = str(float(row[1]) * 0.00328084)
            data_frame["ElectricalReading"] = row[2]
            data_list = ["YLocation", "XLocation", "ElectricalReading"]
            self.root.append(
                type("NDE001-Readings", (Node,), {"__init__": init})(data_frame, data_list).__ToNode__())

    # def __ToNode(self):
    #     return self.readList




if __name__ =="__main__":

    teinfo = TestInfo("test", "test", 66, 66, "George Washington")

    test = NDE001TestInfo(teinfo, "/home/lsy/Major Data Sets/George Washington Bus Bridge (Unit 3)/Region 01/ER/ER.ER")

    print tostring(test.root)