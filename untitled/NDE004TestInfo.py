from basics import Node, init, TestInfo, Equipments
from xml.etree.ElementTree import Element, tostring, SubElement
from process_static_parameter import aa_csv_metadata, AA_META_SENSOR_COUNT,\
    AA_META_WAVEFORM_COUNT, AA_META_FREQUENCY
from TestNode import TestNode
import numpy
import csv
import base64
import os

class NDE004TestInfo(TestNode):

    __rootTag   = "NDE004-TestInfo"
    __Equipment = "IE"

    def __init__(self, testinfo, datapathList, comment):

        self.rootTag = self.__rootTag
        self.Equip   = self.__Equipment
        super(NDE004TestInfo, self).__init__(testinfo)

        for datapath in datapathList:

            self.dataIn, _, _ = self.GetData(datapath)
            self.GetLocation(datapath)
            count     = 0

            for rowNum in (1, 2, 7, 8, 9, 10, 15, 16):
                data_frame = dict()
                data_frame["XLocation"] =  str(float(self.x[count]) * 0.00328084)
                data_frame["YLocation"] =  str(float(self.y[count]) * 0.00328084)
                data_list               =  ["YLocation", "XLocation"]
                data_node               =  \
                    type("NDE004-Readings", (Node,), {"__init__": init})(data_frame, list=data_list).__ToNode__()
                data_file               =  ""
                col1                    =  self.dataIn["set_" + str(rowNum)]
                count                   += 1

                for i in range(512):
                    data_file    = data_file + str(col1[i]) + '\n\r'

                data_fileBase64  = base64.b64encode(data_file)
                dataRoot         = Element("DataCollectionFile")
                subDataFile      = SubElement(dataRoot, "File")
                subDataFile.text = data_fileBase64
                subFileName      = SubElement(dataRoot, "FileName")
                subFileName.text = os.path.basename(datapath) + str(count) + "IE"
                subFileComment = SubElement(dataRoot, "Comment")
                subFileComment.text = comment
                data_node.append(dataRoot)

                self.root.append(data_node)

    def GetData(self, filename):
        print filename
        meta = aa_csv_metadata(filename)
        read_data = numpy.genfromtxt(filename, dtype=None, delimiter=',',
                                     usecols=range(meta[AA_META_SENSOR_COUNT]), skip_header=7)
        read_data = zip(*read_data[::1])
        data_in   = dict()
        for i in range(meta[AA_META_SENSOR_COUNT]):
            data_in['set_' + str(i + 1)] = [0] + list(read_data[i])
        return data_in, meta[AA_META_FREQUENCY], meta[AA_META_WAVEFORM_COUNT]

    def GetLocation(self, filename):
        file   = open(filename)
        reader = csv.reader(file, delimiter = ',')
        # USW location information
        self.x = next(reader)
        self.y = next(reader)