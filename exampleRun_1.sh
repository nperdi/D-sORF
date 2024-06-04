
inputFileName="examples/test.fa"

outputDir="2024_sorf_new/"
numOfProcess=4
mode=1 
startingPos=7  
bypassSignalPeptide="N"  ##default=N
configFileName="conf/sORFconfig.cfg"
simulateLength=0 ##0 or "" for no simulation
python DsORF_init.py $inputFileName $outputDir $numOfProcess $mode $startingPos $bypassSignalPeptide $configFileName $simulateLength
