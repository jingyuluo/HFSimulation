import FWCore.ParameterSet.Config as cms

hcalTupleEvent = cms.EDProducer("HcalTupleMaker_Event", 
   puinfo = cms.untracked.InputTag('addPileupInfo') 
)
