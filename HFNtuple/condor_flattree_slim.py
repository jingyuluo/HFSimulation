#submit batch jobs for selection plots

import sys, os
import shutil
import getpass
import glob
import argparse
import subprocess
#set paths

parser = argparse.ArgumentParser(description='Submit condor jobs')
parser.add_argument('-i', "--input", default="", help="The input directory where the analyzer output trees are")
parser.add_argument('-o', "--output", default="", help="The output directory for flat trees")
parser.add_argument("-a","--abs", default=False, action="store_true", help="use absolute path") 
parser.add_argument("-r","--reweight", default="", help="The pileup reweight function")
parser.add_argument("-d", "--depth", type=int, default=1, help="The depth of the HF fiber")
parser.add_argument("-e","--eos", default="", help="EOS path to copy to")
parser.add_argument("--r3mm", default=False, action="store_true", help="Reweight 1mm sample to 3mm sample")
parser.add_argument("--r30mm", default=False, action="store_true", help="Reweight 10mm sample to 30mm sample")
parser.add_argument("--r300mm", default=False, action="store_true", help="Reweight 100mm sample to 300mm sample")
parser.add_argument("--r3000mm", default=False, action="store_true", help="Reweight 1000mm sample to 3000mm sample")
parser.add_argument("-p", "--perjob", default=10, type=int, help="Files per job")
parser.add_argument("-s", "--sub", default=False, action="store_true")

args=parser.parse_args()

current=os.getcwd()
basefolder=args.input
bashjob="flat.csh"
pathbashjob="{0}/{1}".format(current, bashjob)
pyscript="HF_Calc.py"
pathpyscript="{0}/{1}".format(current, pyscript)
eospath = args.eos
nperj = args.perjob
root_files = glob.glob("{0}/*.root".format(basefolder))
filegroups = {}
icount=1
currgroup = ""

if args.abs:
    root_files=glob.glob("/eos/uscms{0}/*/000*/*.root".format(basefolder))
    #root_files = subprocess.check_output(["eosls", "{0}/*.root".format(basefolder)])
for rootfile in root_files:
    rawfile = rootfile
    print("+look at the root file: {0}".format(rootfile))
    if args.abs:
        rootfile=rootfile[rootfile.find("/store"): ]
        rootfile="root://cmseos.fnal.gov/"+rootfile
    #rootfile = rootfile.lstrip("/eos/uscms")
    if currgroup!="":
        currgroup+=","+rootfile
    else:
        currgroup+=rootfile

    if icount%nperj==0: #or rawfile==root_files[-1]:
        filegroups[icount/nperj]=currgroup
        currgroup=""
    if rawfile == root_files[-1]:
        filegroups[icount/nperj+1]=currgroup
    icount+=1

for key in filegroups.keys():
 
    #folder0 = rootfile.split("/")[-1].rstrip(".root")
    #folder1 = rootfile.split("/")[-2]
    folder0 = "output_"+str(key)
    folder = args.output+"/"
    if not os.path.isdir(folder): os.mkdir(folder)
    folder = folder+folder0
    if not os.path.isdir(folder): os.mkdir(folder)

    os.chdir(folder)

    shutil.copyfile(pathpyscript, pyscript)
    shutil.copyfile(pathbashjob, bashjob)

    if args.reweight!="":
        REWEIGHT="--reweight="+args.reweight
    else:
        REWEIGHT='--reweight='

    FIBER = "--depth="+str(args.depth)
    
    if args.r3mm:
        R3MM = "--r3mm"
    else: 
        R3MM = ""
    
    if args.r30mm:
        R30MM = "--r30mm"
    else:
        R30MM = ""

    if args.r300mm:
        R300MM = "--r300mm"
    else:
        R300MM = ""

    if args.r3000mm:
        R3000MM = "--r3000mm"
    else: 
        R3000MM = ""

    condor_filename="analyze_condor_{0}".format(folder0)
    fcondor=open(condor_filename, "w")
    fcondor.write("Executable = {0}\n".format(bashjob))
    fcondor.write("Universe = vanilla\n")
    fcondor.write("transfer_input_files = {0}\n".format(pyscript))
    fcondor.write("should_transfer_files = YES\n")
    fcondor.write("Output = {0}/{1}/run_{2}.out\n".format(current, folder, folder0))
    fcondor.write("Error  = {0}/{1}/run_{2}.err\n".format(current, folder, folder0))
    fcondor.write("Log    = {0}/{1}/run_{2}.log\n".format(current, folder, folder0))
    if args.abs:
        #rootfile="root://cmsxrootd.fnal.gov/"+rootfile
        fcondor.write("Arguments = {0} {1} {2} {3} {4}\n".format(pyscript, filegroups[key], folder0, eospath, FIBER))
    else:
        fcondor.write("Arguments = {0} {1} {2} {3} {4}\n".format(pyscript, current+"/"+rootfile, folder0, eospath, FIBER))
    fcondor.write("Queue\n")
    fcondor.close()
    
    os.system("chmod +x flat.csh HF_Calc.py analyze_condor_{0}".format(folder0))
    if args.sub:
        os.system("condor_submit analyze_condor_{0}".format(folder0))
 
    os.chdir(current)
