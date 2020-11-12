#!/bin/csh

#pyscript=$1
#inputfile=$2
#outputname=$3
#Jet/Displaced Trigger = $4
#Data/MC=$5
#Control/Signal=$6
#Blind/Not=$7
#isMC=$8
#Reweight=$9

source /cvmfs/cms.cern.ch/cmsset_default.csh
setenv ROOTSYS /cvmfs/cms.cern.ch/slc6_amd64_gcc472/lcg/root/5.32.00-cms
setenv PATH $ROOTSYS/bin:$PATH
set current=`pwd`
echo $current
scram p CMSSW CMSSW_7_6_2
cd CMSSW_7_6_2
cmsenv
rm -r CMSSW_7_6_2
cd $current
#xrdcp root://cmseos.fnal.gov//store/user/jluo/Reweight/new_ratio_likelihood_inclusive.root ./
#xrdcp root://cmseos.fnal.gov//store/user/jluo/Reweight/Run2016G_PUMoriond17.root ./
#xrdcp root://cmseos.fnal.gov//store/user/jluo/Reweight/Pileup_reweight_2017.root ./
#xrdcp root://cmseos.fnal.gov//store/user/jluo/Reweight/Pileup_reweight_2018.root ./
#xrdcp root://cmseos.fnal.gov//store/user/jluo/Reweight/Pileup_reweight_2018_80mb.root ./
#xrdcp root://cmseos.fnal.gov//store/user/jluo/Reweight/Pileup_reweight_2018_78mb.root ./
#cd $6
#eos root://cmseos.fnal.gov mkdir $5
#eosmkdir -p $5
setenv LD_LIBRARY_PATH $ROOTSYS/lib/:$LD_LIBRARY_PATH
echo $LD_LIBRARY_PATH
python $1 -f $2 -o $3  
#rm new_ratio_likelihood_inclusive.root
#rm Run2016G_PUMoriond17.root
#rm Pileup_reweight_2017.root 
#rm Pileup_reweight_2018.root 
#rm Pileup_reweight_2018_80mb.root
#rm Pileup_reweight_2018_78mb.root
xrdcp *.root root://cmseos.fnal.gov/$4
rm *.root 
