#include "HCALPFG/HcalTupleMaker/interface/HcalTupleMaker_Event.h"
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Common/interface/EventBase.h"

HcalTupleMaker_Event::HcalTupleMaker_Event(const edm::ParameterSet& iConfig):
  PUInputTag (iConfig.getUntrackedParameter<edm::InputTag>("puinfo")) {
  produces <double> ("PU");
  produces <unsigned int> ( "run"    );
  produces <unsigned int> ( "event"  );
  produces <unsigned int> ( "ls"     );
  produces <unsigned int> ( "bx"     );
  produces <unsigned int> ( "orbit"  );
  puToken_ = consumes<std::vector<PileupSummaryInfo>>(PUInputTag);
}

void HcalTupleMaker_Event::
produce(edm::Event& iEvent, const edm::EventSetup& iSetup) {

  std::unique_ptr<double>         PU    (new double);
  std::unique_ptr<unsigned int >  run   ( new unsigned int(iEvent.id().run()        ) );
  std::unique_ptr<unsigned int >  event ( new unsigned int(iEvent.id().event()      ) );
  std::unique_ptr<unsigned int >  ls    ( new unsigned int(iEvent.luminosityBlock() ) );

  edm::EventBase const & eventbase = iEvent;
  std::unique_ptr<unsigned int >  bx    ( new unsigned int(eventbase.bunchCrossing() ) );
  std::unique_ptr<unsigned int >  orbit ( new unsigned int(eventbase.orbitNumber()   ) );
  edm::Handle<std::vector<PileupSummaryInfo >> PUInfo;
  iEvent.getByToken(puToken_, PUInfo);

  std::vector<PileupSummaryInfo>::const_iterator PVI; 
  for(PVI=PUInfo->begin(); PVI!=PUInfo->end(); ++PVI){
      int BX = PVI->getBunchCrossing();
      if (BX==0){
          *PU = PVI->getTrueNumInteractions();
          continue;
      }
  }
  
  iEvent.put(move( PU   ), "PU");
  iEvent.put(move( run  ), "run"   );
  iEvent.put(move( event), "event" );
  iEvent.put(move( ls   ), "ls"    );
  iEvent.put(move( bx   ), "bx"    );
  iEvent.put(move( orbit), "orbit" );

}
