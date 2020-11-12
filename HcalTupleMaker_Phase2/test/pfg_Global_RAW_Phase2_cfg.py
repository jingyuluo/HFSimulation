#------------------------------------------------------------------------------------
# Imports
#------------------------------------------------------------------------------------
import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Eras import eras
import FWCore.ParameterSet.VarParsing as VarParsing

#------------------------------------------------------------------------------------
# Options
#------------------------------------------------------------------------------------
options = VarParsing.VarParsing()

options.register('skipEvents',
                 0, # default value
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.int,
                 "Number of events to skip")

options.register('processEvents',
                 -1, # default value
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.int,
                 "Number of events to process")

options.register('inputFiles',
                 "file:/uscms_data/d3/jluo/work/CMSSW_simulation/CMSSW_11_1_0_pre6/src/singleneu_gun_forHFtest_step1.root",#"file:/eos/uscms/store/user/lpcbril/MC_test/HFSim_RAWSIM/HFSim_Phase2/SingleNeutrino_forHF_RAWSIM_phase2/200516_013215/0001/singleneu_gun_forHFtest_step1_1330.root",#"root://cmsxrootd.fnal.gov//store/relval/CMSSW_10_6_0_patch2/RelValNuGun/GEN-SIM-RECO/PU25ns_106X_upgrade2023_realistic_v3_2023D42PU200-v1/10001/D01AF9AB-548A-2A45-B288-4A7A86ABF4C3.root",#"file:/eos/uscms/store/user/lpcbril/MC_test/HFSim_FEVT/HFSim_Run3/SingleNeutrino_forHF_FEVT/191215_201235/0000/HFSimulation_Run3_FEVT_976.root",#"root://eoscms.cern.ch//eos/cms/store/group/dpg_hcal/comm_hcal/USC/USC_268238.root",#"root://cmsxrootd.fnal.gov//store/express/Commissioning2017/ExpressPhysics/FEVT/Express-v1/000/293/591/00000/F45D88B0-A234-E711-B36A-02163E01A6B2.root", # default value
                 VarParsing.VarParsing.multiplicity.list,
                 VarParsing.VarParsing.varType.string,
                 "Input files")

options.register('outputFile',
                 "HcalTupleMaker.root", # default value
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.string,
                 "Output file")

options.parseArguments()

print " "
print "Using options:"
print " skipEvents    =", options.skipEvents
print " processEvents =", options.processEvents
print " inputFiles    =", options.inputFiles
print " outputFile    =", options.outputFile
print " "

#------------------------------------------------------------------------------------
# Declare the process and input variables
#------------------------------------------------------------------------------------
process = cms.Process('PFG',eras.Run2_2017)

#------------------------------------------------------------------------------------
# Get and parse the command line arguments
#------------------------------------------------------------------------------------
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.processEvents) )

process.source = cms.Source(
    "PoolSource",
    fileNames  = cms.untracked.vstring(options.inputFiles),
    skipEvents = cms.untracked.uint32(options.skipEvents)
    )

process.TFileService = cms.Service(
    "TFileService",
    fileName = cms.string(options.outputFile)
    )

#------------------------------------------------------------------------------------
# import of standard configurations
#------------------------------------------------------------------------------------
process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(1000)
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.Reconstruction_Data_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('RecoMET.METProducers.hcalnoiseinfoproducer_cfi')
process.load("CommonTools.RecoAlgos.HBHENoiseFilter_cfi")
process.load("CommonTools.RecoAlgos.HBHENoiseFilterResultProducer_cfi")
process.load("CondCore.CondDB.CondDB_cfi")
#process.load('RecoLocalCalo.Configuration.RecoLocalCalo_Cosmics_cff')
process.load("RecoLocalCalo.Configuration.hcalLocalReco_cff")
#process.load("EventFilter.HcalRawToDigi.HcalRawToDigi_cfi")
#------------------------------------------------------------------------------------
# Set up our analyzer
#------------------------------------------------------------------------------------
process.load("HCALPFG.HcalTupleMaker.HcalTupleMaker_cfi") # loads all modules
process.load("HCALPFG.HcalTupleMaker.HcalTupleMaker_Trigger_cfi")
## set desired parameters, for example:
process.hcalTupleHFDigis.DoEnergyReco = False
process.hcalTupleHFDigis.FilterChannels = False
process.hcalTupleHBHERecHits.source = cms.untracked.InputTag("hbheplan1")
process.hcalTupleHBHEDigis.recHits = cms.untracked.InputTag("hbheplan1")
process.hcalTupleHBHEDigis.DoEnergyReco = cms.untracked.bool(False)
process.hcalTupleHFDigis.ChannelFilterList = cms.untracked.VPSet(
    # Notice only channels listed here will be saved, if the FilterChannels flag is set to true
    cms.PSet(iEta = cms.int32(29), iPhi = cms.int32(39), depth = cms.int32(1)),
    )

from Configuration.StandardSequences.RawToDigi_cff import *
process.CustomizedRawToDigi = cms.Sequence(
        gtDigis*
        #siPixelDigis*
        #siStripDigis*
        #ecalDigis*
        #ecalPreshowerDigis*
        hcalDigis
        #muonDTDigis*
        #muonCSCDigis*
        #muonRPCDigis*
        #castorDigis*
        #scalersRawToDigi*
        #tcdsDigis
)

#------------------------------------------------------------------------------------
# FED numbers 
#------------------------------------------------------------------------------------
#process.hcalDigis.FEDs = cms.untracked.vint32(	1100, 1102, 1104, # HBHEa 
#                                              	1106, 1108, 1110, # HBHEb
#                                              	1112, 1114, 1116, # HBHEc
#                                              	1118, 1120, 1122, # HF
#                                              	1119, 1121, 1123  # HF
#					        724, 725, 726, 727, 728, 729, 730, 731, # HO
# 					        1134 # HcalLaser
#                                              )

#------------------------------------------------------------------------------------
# QIE10  Unpacker
#------------------------------------------------------------------------------------
process.qie10Digis = process.hcalDigis.clone()
process.qie10Digis.FEDs = cms.untracked.vint32(1118,1120,1122,1119,1121,1123)

#------------------------------------------------------------------------------------
# QIE11  Unpacker
#------------------------------------------------------------------------------------
process.qie11Digis = process.hcalDigis.clone()
#process.qie11Digis.InputLabel = cms.InputTag("source") 
#process.qie11Digis.FEDs = cms.untracked.vint32(1114)

#------------------------------------------------------------------------------------
# Specify Global Tag
#------------------------------------------------------------------------------------
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic_T15', '')

#process.GlobalTag.globaltag = '100X_mcRun2_asymptotic_v1'#'106X_mcRun3_2023_realistic_v3'#'90X_dataRun2_HLT_v1' 
print "GlobalTag = ", str(process.GlobalTag.globaltag).split("'")[1]
print " "


process.load("CondCore.DBCommon.CondDBCommon_cfi")
from CondCore.DBCommon.CondDBSetup_cfi import *
process.load("CondCore.CondDB.CondDB_cfi")
from CondCore.CondDB.CondDB_cfi import *

CondHcal = CondDB.clone(connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'))

process.hcaldb = cms.ESSource("PoolDBESSource",
            CondHcal, 
            toGet = cms.VPSet(cms.PSet(record = cms.string('HcalPedestalWidthsRcd'),
                                       tag = cms.string('HcalPedestalWidths_ADC_v8.00_mc_effective'),
                                       label = cms.untracked.string('effective') 
                                      ),
                              cms.PSet(record = cms.string('HcalPedestalsRcd'),
                                       tag = cms.string('HcalPedestals_ADC_v8.00_mc_effective'),
                                       label = cms.untracked.string('effective')
                                      )
                             )
            )

process.es_prefer_HCAL = cms.ESPrefer("PoolDBESSource", "hcaldb")
#------------------------------------------------------------------------------------
# Create Noise Filter
#------------------------------------------------------------------------------------
# Could be out of date, commented out in the main sequence, need to be fixed
process.hcalnoise.fillCaloTowers = cms.bool(False)
process.hcalnoise.fillTracks = cms.bool(False)
process.ApplyBaselineHBHENoiseFilter = cms.EDFilter(
    'BooleanFlagFilter',
    inputLabel = cms.InputTag('HBHENoiseFilterResultProducer','HBHENoiseFilterResult'),
    reverseDecision = cms.bool(False)
    )

#------------------------------------------------------------------------------------
# HcalTupleMaker sequence definition
#------------------------------------------------------------------------------------
process.tuple_step = cms.Sequence(
    ## Make HCAL tuples: Event info
    process.hcalTupleEvent*
    
    ## Make HCAL tuples: FED info
    #process.hcalTupleFEDs*
    
    ## Make HCAL tuples: digi info
    #process.hcalTupleHBHEDigis*
    #process.hcalTupleHODigis*
    #process.hcalTupleHFDigis*
    process.hcalTupleQIE10Digis* # for HF
    #process.hcalTupleQIE11Digis* # for HEP17
    
    ## Make HCAL tuples: reco info
    #process.hcalTupleHBHERecHits*
    #process.hcalTupleHFRecHits*
    #process.hcalTupleHORecHits*
    #process.hcalTupleHFRecHits*

    ## Make HCAL tuples: trigger info
    #process.hcalTupleTrigger*
    #process.hcalTupleTriggerPrimitives*
    #process.hcalTupleTriggerObjects*

    ## Package everything into a tree
    process.hcalTupleTree
)

#-----------------------------------------------------------------------------------
# Path and EndPath definitions
#-----------------------------------------------------------------------------------
process.preparation = cms.Path(
    ## Unpack digis from RAW
    process.RawToDigi*
    #process.CustomizedRawToDigi*
    #process.gtDigis*
    #process.hcalDigis*
    process.qie10Digis*
    #process.qie11Digis*
    
    ## reconstruction 
    #process.L1Reco*
    #process.reconstruction*
    #process.hcalLocalRecoSequence*
    
    ## Do energy reconstruction
    #process.horeco*
    #process.hfprereco*
    #process.hfreco*
    #process.hbheprereco*
    #process.hbheplan1*
    #process.hbhereco*
    
    ## For noise filter
    #process.hcalnoise*
    #process.HBHENoiseFilterResultProducer*
    #process.ApplyBaselineHBHENoiseFilter*
    
    ## Make the ntuples
    process.tuple_step
)

#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange('293765:264-293765:9999')
