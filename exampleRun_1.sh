
inputFileName="examples/test.fa"
#inputFileName="/media/nikos/DATA1_500/dsorf_2019/D-sORF_v1.0/sorfs.org_extract_CP_TIS_seq/sorf_only_fa/fa.fa"
#inputFileName="/home/perdikopn/nikos_on_raid/biothesis/github/TSS/15_dsorf_2019/D-sORF_v1.0/sorfs.org_extract_CP_TIS_seq/sorf_only_fa/fa.fa"
outputDir="2024_sorf_new/"
numOfProcess=4
mode=1 
startingPos=7  
bypassSignalPeptide="N"  ##default=N
configFileName="conf/sORFconfig.cfg"
simulateLength=0 ##0 or "" for no simulation
python DsORF_init.py $inputFileName $outputDir $numOfProcess $mode $startingPos $bypassSignalPeptide $configFileName $simulateLength

#inputDirName="output/7042018/"
workingDir=report/
#python reports_creator_180nt.py $inputDirName $workingDir
