# -*- coding: utf-8 -*-

###########################################################################
#
# This file is a collection of constants and utility functions used for
# processing data in the process data window.
#
###########################################################################

from matplotlib import cm
import os
import csv

# dictionary keys for graph types
GPR_DEPTH_MAP = "Cover Depth Map"
GPR_TIME_MAP = "Time Map"
GPR_AMP_MAP = "Amplitude Map"
GPR_MODELA = "Depth Corrected Amplitude"
GPR_MODELB = "Depth Corrected B"
GPR_DEBUG_MAP = "Debug Scan Indices" #plots the scan #s, for testing plots. Should result in smooth gradients.            
gpr_graph_types = [GPR_AMP_MAP, GPR_MODELA, GPR_DEPTH_MAP]

AA_DOMINANT_FREQUENCY_MAP = "Impact Echo"
AA_CONCRETE_MODULUS_MAP = "USW"
aa_graph_types = [AA_DOMINANT_FREQUENCY_MAP, AA_CONCRETE_MODULUS_MAP]

ER_RESISTIVITY_MAP = "Resistivity"
er_graph_types = [ER_RESISTIVITY_MAP]

LAYER_MAP = "Combined Layers"

GPR = 0
AA = 1
CAM = 2
ER = 3

graph_colormap = dict()
graph_valmin = dict()
graph_valmax = dict()
graph_units = dict()

graph_colormap[AA_DOMINANT_FREQUENCY_MAP] = cm.rainbow_r
graph_valmin[AA_DOMINANT_FREQUENCY_MAP] = 2000
graph_valmax[AA_DOMINANT_FREQUENCY_MAP] = 20000
graph_units[AA_DOMINANT_FREQUENCY_MAP] = "Hz"

graph_colormap[AA_CONCRETE_MODULUS_MAP] = cm.rainbow_r
graph_valmin[AA_CONCRETE_MODULUS_MAP] = 2000
graph_valmax[AA_CONCRETE_MODULUS_MAP] = 6000
graph_units[AA_CONCRETE_MODULUS_MAP] = "Ksi"

graph_colormap[ER_RESISTIVITY_MAP] = cm.rainbow_r
graph_valmin[ER_RESISTIVITY_MAP] = 0
graph_valmax[ER_RESISTIVITY_MAP] = 100
graph_units[ER_RESISTIVITY_MAP] = u"k\u03A9cm"

graph_colormap[GPR_AMP_MAP] = cm.rainbow_r
graph_colormap[GPR_MODELA] = cm.rainbow_r
graph_colormap[GPR_MODELB] = cm.rainbow_r
graph_colormap[GPR_DEPTH_MAP] = cm.rainbow_r
graph_units[GPR_AMP_MAP] = "dB"
graph_units[GPR_MODELA] = "dB"
graph_units[GPR_MODELB] = "dB"
graph_units[GPR_DEPTH_MAP] = "mm"

graph_colormap[LAYER_MAP] = cm.Greys

def csv_from_type(project_path, graph_type):
    if project_path is None or not os.path.isdir(project_path):
        return ""
    if graph_type in gpr_graph_types:
        return project_path+"\\GPR\\"+graph_type+".csv"
    elif graph_type in aa_graph_types:
        return project_path+"\\AA\\"+graph_type+".csv"
    elif graph_type in er_graph_types:
        return project_path+"\\ER\\"+graph_type+".csv"
    else:
        return ""
    
def type_from_csv(csv_file):
    filename = os.path.basename(csv_file)
    return filename[:filename.index(".")]

AA_META_IE_X = "ie_x"
AA_META_IE_Y = "ie_y"
AA_META_USW_X = "usw_x"
AA_META_USW_Y = "usw_y"
AA_META_WAVEFORM_COUNT = "num_rows"
AA_META_SENSOR_COUNT = "num_cols"
AA_META_FREQUENCY = "freq"
AA_META_SENSOR_DIST = "dist"
def aa_csv_metadata(csv_file):
    f = open(csv_file, 'r')
    metadata = dict()
    count = 0
    reader = csv.reader(f)
    for line in reader:
        count += 1
        if count == 1:
            metadata[AA_META_IE_X] = list(line)
        elif count == 2:
            metadata[AA_META_IE_Y] = list(line)
        elif count == 3:
            metadata[AA_META_USW_X] = list(line)
        elif count == 4:
            metadata[AA_META_USW_Y] = list(line)
        elif count == 5:
            if len(line) > 1:
                metadata[AA_META_FREQUENCY] = 0.000004 # malformed data, use default instead.
            else:
                metadata[AA_META_FREQUENCY] = float(line[0])
        elif count == 6:
            if len(line) > 1:
                metadata[AA_META_SENSOR_COUNT] = 16 # malformed data, use default instead.
            else:
                metadata[AA_META_SENSOR_COUNT] = int(line[0])
        elif count == 7:
            if len(line) > 1:
                metadata[AA_META_WAVEFORM_COUNT] = 512 # malformed data, use default instead.
            else:
                metadata[AA_META_WAVEFORM_COUNT] = int(line[0])
        else:
            break
    f.close()
    metadata[AA_META_SENSOR_DIST] = 0.1335
    #metadata[AA_META_SENSOR_DIST] = 0.15 # ltbp
    return metadata