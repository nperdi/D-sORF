import os
import sys
sys.path.append('./lib')
from CP_features_extaction_module import *
from nMersDB import *
from fn_module import *


baseOutputDir="defaultOutput/"
currentPath=os.path.dirname(os.path.realpath(sys.argv[0]))+"/"

###DefaultValues Start
outputDir=""
configFileName="conf/sORFconfig.cfg"
numOfProcess=1 ##for parallel processing of module
mode=1  #if   (mode==1)  : modelClass = "COMB" elif (mode==2)  : modelClass = "CP" elif (mode==3)  : modelClass = "TIS"
bypassSignalPeptide="N"
signalPeptideBypaseMultiplier=0 ##select 0 to not bypassing signlal peptide zone
simulateLength=""
###DefaultValues End

if len(sys.argv)==8:
    #print ("argument are ok ")
    inputFileName   =sys.argv[1]
    outputDir       =sys.argv[2]
    numOfProcess    =sys.argv[3]
    mode            =sys.argv[4]
    startingPos     =sys.argv[5]
    signalPeptideBypaseMultiplier=sys.argv[6]
    configFileName=sys.argv[7]

if len(sys.argv)==9:
    #print ("argument are ok ")
    inputFileName   =sys.argv[1]
    outputDir       =sys.argv[2]
    numOfProcess    =sys.argv[3]
    mode            =sys.argv[4]
    startingPos     =sys.argv[5]
    signalPeptideBypaseMultiplier=sys.argv[6]
    configFileName=sys.argv[7]
    simulateLength=sys.argv[8]

if bypassSignalPeptide=="N":
    signalPeptideBypaseMultiplier=0
elif bypassSignalPeptide=="Y":
    signalPeptideBypaseMultiplier=3

print (signalPeptideBypaseMultiplier)


###read config file params
confDict=readConfigFile(configFileName)
outputStartingDir=confDict["outputStartingDir"]
outputStartingDir=currentPath+outputStartingDir
minLenLim=confDict["minLenLim"]
#########################
if (not outputStartingDir=="") and  (not outputStartingDir[-1:]=="/"):
    outputStartingDir=outputStartingDir+"/" 
inputFileName
if (not outputDir=="") and (not outputDir[-1:]=="/"):
    outputDir=outputDir+"/"

workingDir=outputStartingDir+outputDir
#print (workingDir)

command="mkdir -p "+workingDir
os.system(command)

#########################

command="python src/call_predict.py "+inputFileName+" "+workingDir+" "+str(signalPeptideBypaseMultiplier)+" "+str(startingPos)+" "+str(mode)+" "+str(numOfProcess)+" "+minLenLim+" "+configFileName +" "+inputFileName+" "+ simulateLength
print (command)
os.system(command)
    
print ("END")



