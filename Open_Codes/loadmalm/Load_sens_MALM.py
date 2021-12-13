# -*- coding: utf-8 -*-
"""
Created on Thu May 28 08:01:49 2020

@author: Benjamin
"""

import pickle

def load_MALM_sens3d(filename=None):

    #file = open(filename, 'rb')
    #u = pickle._Unpickler(file)
    #u.encoding = 'latin1'
    #data = u.load()

    infile = open(filename,'rb')
    #data = pickle.load(infile,encoding='latin1')
    data = pickle.load(infile)
    infile.close()


    # SimName='M' + 'SoilR' + str(data['SoilR']) + 'AnoR' + str(data['AnoR']) + 'Z' + str(data['HWD'][0]) + 'W' + str(data['HWD'][1]) +  'D' + str(data['HWD'][2])
    SimName = None

    # different version of the pickle file
    if "HWDL" in data:
        maxdepth = data['HWDL'][2] * 1.5
    elif "HWD" in data:
        maxdepth = data['HWD'][2] * 1.5
    elif "HWDLs" in data:
        maxdepth = data['HWDLs'][2] * 1.5

    shape = data['shape']
    p1 = data['p12'][0]
    p2 = data['p12'][1]
    
    
    if "HWDL" in data:
        xyzu = data['XYU']
        xp, yp, z, U  = xyzu[:,0],  xyzu[:,1], xyzu[:,2],  xyzu[:,3]

        # return xp, yp, z, U, maxdepth, shape, p1, p2, SimName, data
    elif "HWD" in data:
        xyzu = data['uAz0_grid']
        xp, yp, z, U  = xyzu[:,0],  xyzu[:,1], xyzu[:,2],  xyzu[:,3]
        
    elif "HWDLs" in data:
        xyzu = data['XYU']
        xp, yp, z, U  = xyzu[:,0],  xyzu[:,1], xyzu[:,2],  xyzu[:,3]

        # return maxdepth, shape, p1, p2, SimName, data
    return xp, yp, z, U, maxdepth, shape, p1, p2, SimName, data


