
inputFileName="/mnt/raid1/perdikopn/projects/dsorf/2022_ver_june/data/otherTestingDataset/datasets/Testing_Sets/CPPred/Human-sORF-Testing/Homo38.small_ncrna_test.fa"
##inputFileName="/home/perdikopn/nikos_on_raid/biothesis/github/TSS/12_ECCB_PAPER/v9/createTrainingDataSets/sORFS_simulated_DataSets/POSITIVE/Positive_sORFs_from_start_of_proteinSeq_70-300/sorfSimulatedWithOutPeptide.fa"
#inputFileName="/home/perdikopn/nikos_on_raid/biothesis/github/TSS/12_ECCB_PAPER/v9/createTrainingDataSets/sORFS_simulated_DataSets/NEGATIVE/extract_negative_sorfs_set_bypassing_2000_from_TSS_210ntLength_15.000/negativeSORFSeq.fa"
#inputFileName="/home/perdikopn/Desktop/LINK_ECCB_PAPER/v9/createTrainingDataSets/sORFS_simulated_DataSets/NEGATIVE/extract_negative_sorfs_set_bypassing_2000_from_TSS_210ntLength_200.000/negativeSORFSeq.fa"
outputDir="202_CPPred_negative_sorfs/"
numOfProcess=40
mode=2  #1 COMB , 2 CP , 3 TIS 
startingPos=0  ## this this the place of TIS codon in the sequece
bypassSignalPeptide="N"  ##default=N
configFileName="conf/sORFconfig.cfg"
simulateLength=0 ##0 or "" for no simulation
python DsORF_init.py $inputFileName $outputDir $numOfProcess $mode $startingPos $bypassSignalPeptide $configFileName $simulateLength

# inputDirName="output/7042018/"
# workingDir=report/
#python reports_creator_180nt.py $inputDirName $workingDir


# if   (mode==1)  : modelClass = "COMB"
# elif (mode==2)  : modelClass = "CP"
# elif (mode==3)  : modelClass = "TIS"
