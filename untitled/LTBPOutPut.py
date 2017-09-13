from xml.etree.ElementTree import Element, tostring, SubElement
from xml.dom import minidom

class LTBPOutPut():

    def __init__(self, bridgeInfo, NDEtestInfo, NDEreading = None):

        protocol = NDEtestInfo.root.tag[0:6]
        print protocol
        bridgeInfo.data["ltbpcmn:ProtocolName"] = protocol
        bridgeInfo.list.append("ltbpcmn:ProtocolName")
        self.root = Element(protocol)
        self.root.attrib["xmlns:ltbpcmn"] = "http://www.fhwa.dot.gov/research/tfhrc/programs/infrastructure/structures/ltbp/xml/LTBPCommonTypes"
        self.root.attrib["xmlns:xsi"] = "http://www.w3.org/2001/XMLSchema-instance"
        self.root.append(bridgeInfo.__ToNode__())
        self.root.append(NDEtestInfo.__ToNode__())
        # for element in NDEtestInfo.readList:
        #     self.root.append(element)

    def output(self):

        rough_string = tostring(self.root)
        reparse = minidom.parseString(rough_string)

        return reparse.toprettyxml(indent='\t')






