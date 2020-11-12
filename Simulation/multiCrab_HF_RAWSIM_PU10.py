import subprocess
import sys, os
import argparse

from CRABClient.UserUtilities import config
from CRABAPI.RawCommand import crabCommand
from CRABClient.ClientExceptions import ClientException
from httplib import HTTPException

config = config()
config.General.transferOutputs = True
config.General.transferLogs = True
config.General.workArea = "crab_projects"

config.JobType.pluginName = 'Analysis' 
config.JobType.maxMemoryMB = 4000

#config.Data.outputPrimaryDataset = 'HFSim_Run3'
config.Data.inputDBS = 'phys03'

config.Data.splitting = 'FileBased'
#config.Data.splitting = 'Automatic'
config.Data.unitsPerJob = 1
#NJOBS = 5000
#config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/group/lpcbril/MC_test/HFSim_RAWSIM' 
config.Data.publication = True

config.Site.storageSite = 'T3_US_FNALLPC' 
config.Site.blacklist = ['T3_US_UCR']
#config.Site.whitelist = ['T3_US_Colorado', 'T2_US_Florida', 'T3_CH_PSI', 'T2_DE_RWTH']#['T2_CH_CERN', 'T2_US_*', 'T2_IT_Pisa','T2_UK_London_IC','T2_HU_Budapest', 'T2_IT_Rome', 'T2_IT_Bari', 'T2_IT_Legnaro', 'T2_FR_CCIN2P3', 'T2_FR_GRIF_LLR', 'T2_DE_DESY', 'T2_DE_RWTH', 'T2_UK_London_Brunel', 'T2_ES_CIEMAT', 'T2_ES_IFCA', 'T2_BE_IIHE']

config.JobType.psetName = "SingleNeutrino_forHF_step1_PU10_cfg.py" 
config.General.requestName = "SingleNeutrino_forHF_RAWSIM_PU10_phase2"
config.Data.outputDatasetTag = "SingleNeutrino_forHF_RAWSIM_PU10_phase2"
config.Data.inputDataset = "/HFSim_Phase2/jingyu-SingleNeutrino_forHF_GENSIM_phase2-9479ee7b0ee3ac9051dd1acaef42ec54/USER" 

#def produce_new_cfg(mass, life, lines):
#    file = open("StopToLB/StopToLB_M"+str(mass)+"_CTau"+str(life)+"mm_CP2_GENSIM.py", "w")
#    width = 0.0197327e-11/float(life)
#    #print width
#    for line in lines:
#        newline = line.replace("MMMM", str(mass)).replace("LLLL", str(life)).replace("XXXX", str(width))
#        file.write(newline)
#    file.close()

def submit(config):
    try:
        crabCommand('submit', config = config)
    except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
    except ClientException as cle:
        print "Failed submitting task: %s" % (cle)


#def sub_crab_job(mass, life):
#    config.General.requestName = 'StopToLB_M'+str(mass)+'_'+str(life)+'mm_CP2_GENSIM'
#    config.JobType.psetName = "StopToLB/StopToLB_M"+str(mass)+"_CTau"+str(life)+"mm_CP2_GENSIM.py"
#    config.Data.outputDatasetTag = 'StopToLB_M'+str(mass)+'_'+str(life)+'mm_CP2_GENSIM'
#    print "submit: Mass:",mass, "life:", life
submit(config)


#infile = open('StopToLB_MAAAA_ctauBBBB_TuneCP2_13TeV_pythia8_GENSIM.py')
#lines = infile.readlines()
#
#for m in [600, 800, 1000, 1200, 1400, 1600, 1800, 2000]:#[1400, 100, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000]:
#    for l in [1, 3, 10,30, 100, 300, 1000, 3000, 10000]:
##for m in [1000]:
##    for l in [1]: 
#        produce_new_cfg(m, l, lines)
#        sub_crab_job(m, l)

