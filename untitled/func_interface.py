from basics import Equipments, inspectors, Inspectors, Personnel, TestInfo, BridgeInfo, Bridge, BridgeInformation, operationInfo
from NDE001TestInfo import NDE001TestInfo
from NDE004TestInfo import NDE004TestInfo
from NDE007TestInfo import NDE007TestInfo
from xml.etree.ElementTree import tostring
from LTBPOutPut import LTBPOutPut

def insert_inspector(firstname, surname, company):

    inspector = Inspectors(firstname, surname, company)
    inspectors.append(inspector)

def setTestInfo(TestDate,AirTemperature, DeckSurfaceTemperature, BridgeDeckThickness,TestSite):
    if len(inspectors) == 0:
        print "init inspector information first"
    personnel = Personnel(inspectors)
    global operationInfo

    operationInfo = TestInfo(TestDate, personnel, AirTemperature, DeckSurfaceTemperature, BridgeDeckThickness, TestSite)

def setBridgeInfo(ID, BridgeName, State):

    global Bridge
    Bridge = BridgeInfo(ID, BridgeName, State)


def GetOutPut( ER_DataPath, AA_DataPath, OutPath, Comment):

    BridgeChunk_ER   = BridgeInformation(Bridge)
    BridgeChunk_IE   = BridgeInformation(Bridge)
    BridgeChunk_USW  = BridgeInformation(Bridge)

    TestChunk_ER  = NDE001TestInfo(operationInfo, ER_DataPath)
    TestChunk_IE  = NDE004TestInfo(operationInfo, AA_DataPath, Comment)
    TestChunk_USW = NDE007TestInfo(operationInfo, AA_DataPath, Comment)

    output = OutPath + "/NDE001.xml"
    file = open(output, 'w')
    file.write(LTBPOutPut(BridgeChunk_ER, TestChunk_ER).output())

    output = OutPath + "/NDE004.xml"
    file = open(output, 'w')
    file.write(LTBPOutPut(BridgeChunk_IE, TestChunk_IE).output())

    output = OutPath + "/NDE007.xml"
    file = open(output, 'w')
    file.write(LTBPOutPut(BridgeChunk_USW, TestChunk_USW).output())







if __name__ == "__main__":

    from lxml import etree
    import StringIO
    xsd_path1 = '/home/lsy/Desktop/NDE001.xsd'
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
    doc = etree.parse(StringIO.StringIO(text))
    print schema.assertValid(doc)



    # setBridgeInfo("10","testing", "01")
    # insert_inspector("Siyuan", "Li", "infratek")
    # insert_inspector("Meng", "Xiao", "infratek")
    # Test = setTestInfo("2017-10-13", 20, 20, 2.2, "warren county")
    # GetOutPut("/home/lsy/Major Data Sets/George Washington Bus Bridge (Unit 3)/Region 01/ER/ER.ER",
    #           ["/home/lsy/Major Data Sets/George Washington Bus Bridge (Unit 3)/Region 01/AA/AA_0",
    #            "/home/lsy/Major Data Sets/George Washington Bus Bridge (Unit 3)/Region 01/AA/AA_1"], "/home/lsy/Desktop", "test")


    #


