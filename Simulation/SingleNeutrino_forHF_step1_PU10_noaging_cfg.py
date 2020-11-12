# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step1 --filein file:singleneu_gun_forHF.root --fileout file:singleneu_gun_forHFtest_step1.root --mc --eventcontent RAWSIM --pileup AVE_175_BX_25ns --datatier GEN-SIM-RAW --conditions auto:phase2_realistic --step DIGI,L1,DIGI2RAW --beamspot HLLHC --geometry Extended2026D49 --era Phase2C9 --python_filename SingleNeutrino_forHF_step1_cfg.py --no_exec -n 5 --pileup_input das:/RelValMinBias_14TeV/CMSSW_11_1_0_pre4-110X_mcRun4_realistic_v3_2026D49noPU-v1/GEN-SIM --customise SLHCUpgradeSimulations/Configuration/aging.customise_aging_1000
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Phase2C9_cff import Phase2C9

process = cms.Process('DIGI2RAW',Phase2C9)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_POISSON_average_cfi')
process.load('Configuration.Geometry.GeometryExtended2026D49Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(5),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring('file:singleneu_gun_forHF.root'),
    inputCommands = cms.untracked.vstring(
        'keep *', 
        'drop *_genParticles_*_*', 
        'drop *_genParticlesForJets_*_*', 
        'drop *_kt4GenJets_*_*', 
        'drop *_kt6GenJets_*_*', 
        'drop *_iterativeCone5GenJets_*_*', 
        'drop *_ak4GenJets_*_*', 
        'drop *_ak7GenJets_*_*', 
        'drop *_ak8GenJets_*_*', 
        'drop *_ak4GenJetsNoNu_*_*', 
        'drop *_ak8GenJetsNoNu_*_*', 
        'drop *_genCandidatesForMET_*_*', 
        'drop *_genParticlesForMETAllVisible_*_*', 
        'drop *_genMetCalo_*_*', 
        'drop *_genMetCaloAndNonPrompt_*_*', 
        'drop *_genMetTrue_*_*', 
        'drop *_genMetIC5GenJs_*_*'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(

        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(1)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(1),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step1 nevts:5'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(1),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RAW'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    fileName = cms.untracked.string('file:singleneu_gun_forHFtest_step1.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.input.nbPileupEvents.averageNumber = cms.double(10.000000)
process.mix.bunchspace = cms.int32(25)
process.mix.minBunch = cms.int32(-12)
process.mix.maxBunch = cms.int32(3)
process.mix.input.fileNames = cms.untracked.vstring(['/store/relval/CMSSW_11_1_0_pre4/RelValMinBias_14TeV/GEN-SIM/110X_mcRun4_realistic_v3_2026D49noPU-v1/10000/F9058D88-F925-5A4C-9C6D-5FEC34B2E3EF.root', '/store/relval/CMSSW_11_1_0_pre4/RelValMinBias_14TeV/GEN-SIM/110X_mcRun4_realistic_v3_2026D49noPU-v1/10000/6960BEEB-2EAB-014F-A6AF-7C450BC5A26C.root', '/store/relval/CMSSW_11_1_0_pre4/RelValMinBias_14TeV/GEN-SIM/110X_mcRun4_realistic_v3_2026D49noPU-v1/10000/F5D71E28-A88E-6645-912A-4BB746C6F76F.root', '/store/relval/CMSSW_11_1_0_pre4/RelValMinBias_14TeV/GEN-SIM/110X_mcRun4_realistic_v3_2026D49noPU-v1/10000/5C975731-ECD9-3445-95A6-9806F7F5C85F.root', '/store/relval/CMSSW_11_1_0_pre4/RelValMinBias_14TeV/GEN-SIM/110X_mcRun4_realistic_v3_2026D49noPU-v1/10000/2E2154AD-F910-D74D-A006-50B9071760CD.root', '/store/relval/CMSSW_11_1_0_pre4/RelValMinBias_14TeV/GEN-SIM/110X_mcRun4_realistic_v3_2026D49noPU-v1/10000/C480DA4E-F840-1143-BF8B-76409F338F97.root', '/store/relval/CMSSW_11_1_0_pre4/RelValMinBias_14TeV/GEN-SIM/110X_mcRun4_realistic_v3_2026D49noPU-v1/10000/F6BD5BE8-6217-1948-98A7-0EDE9CF2A437.root', '/store/relval/CMSSW_11_1_0_pre4/RelValMinBias_14TeV/GEN-SIM/110X_mcRun4_realistic_v3_2026D49noPU-v1/10000/0D07A40F-A6AE-254E-B3EB-7190148073F0.root', '/store/relval/CMSSW_11_1_0_pre4/RelValMinBias_14TeV/GEN-SIM/110X_mcRun4_realistic_v3_2026D49noPU-v1/10000/2C55343C-757D-1541-AEEC-0DC2877AA905.root', '/store/relval/CMSSW_11_1_0_pre4/RelValMinBias_14TeV/GEN-SIM/110X_mcRun4_realistic_v3_2026D49noPU-v1/10000/0FF4F125-77A9-B449-99E1-79C5E3A2E6B3.root'])
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.L1simulation_step,process.digi2raw_step,process.endjob_step,process.RAWSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.aging
#from SLHCUpgradeSimulations.Configuration.aging import customise_aging_1000 

#call to customisation function customise_aging_1000 imported from SLHCUpgradeSimulations.Configuration.aging
#process = customise_aging_1000(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
