from basics import Equipments, inspectors, Inspector, Personnel, TestInfo, BridgeInfo, Bridge, BridgeInformation, operationInfo
from NDE001TestInfo import NDE001TestInfo
from xml.etree.ElementTree import tostring
from LTBPOutPut import LTBPOutPut

def insert_inspector(firstname, surname, company):

    inspector = Inspector(firstname, surname, company)
    inspectors.append(inspector)

def setTestInfo(TestDate,AirTemperature, DeckSurfaceTemperature, TestSite):

    if len(inspectors) == 0:

        print "init inspector information first"

    personnel = Personnel(inspectors)

    global operationInfo

    operationInfo = TestInfo(TestDate, personnel, AirTemperature, DeckSurfaceTemperature, TestSite)

def setBridgeInfo(ID, BridgeName, State):

    global Bridge

    Bridge = BridgeInfo(ID, BridgeName, State)


def GetOutPut( DataPath, OutPath):

    BridgeChunk = BridgeInformation(Bridge)
    TestChunk = NDE001TestInfo(operationInfo, DataPath)

    output = OutPath + "/NDE001.xml"

    file = open(output, 'w')

    file.write(LTBPOutPut(BridgeChunk, TestChunk).output())





if __name__ == "__main__":

    from lxml import etree
    import StringIO
    xsd_path1 = '/home/lsy/NDE001.xsd'
    xsd_path2 = '/home/lsy/LTBPCommonTypes.xsd'
    xml_path = '/home/lsy/Desktop/NDE001.xml'

    def validate(xmlparser, xmlfilename):
        try:
            with open(xmlfilename, 'r') as f:
                etree.fromstring(f.read(), xmlparser)
            return True
        except etree.XMLSchemaError:
            return False

    xsd_1 = open(xsd_path1, 'r')
    text = xsd_1.read()
    test = StringIO.StringIO(text)
    schema_doc = etree.parse(test)
    schema = etree.XMLSchema(schema_doc)

    valid = open(xml_path, 'r')
    text = valid.read()
    print text
    doc = etree.parse(StringIO.StringIO(text))
    print schema.validate(doc)

    # setBridgeInfo("10","testing", "NJ")
    # insert_inspector("Siyuan", "Li", "infratek")
    # insert_inspector("Meng", "Xiao", "infratek")
    # Test = setTestInfo("10.12", 20, 20, "warren county")
    # GetOutPut("/home/lsy/Desktop/ER.ER", "/home/lsy/Desktop")





