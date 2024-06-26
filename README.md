D-sORF
---------------
D-sORF is an alignment-free data mining algorithm based on machine learning. The algorithm is based on the nucleotide composition of the ORF and the sequence information around the ATG start codon, called the translation initiation site (TIS). D-sORF distinguishes coding from non-coding transcripts and focuses on sequences with small ORFs. It provides a scoring system for predicting putative translating sORFs based on nucleotide context of three different windows (54, 99, and 180-nts) within ORFs and a 9-nts window around TIS of experimentally validated CDSs of protein-coding genes, compared to windows of similar size and location in negative sORFs.


Installation
---------------
1. Clone the repository from GitHub:
   
git clone https://github.com/nperdi/D-sORF.git

cd D-sORF

2. Create and activate a Conda virtual environment:

conda create --name dsorfEnv python=3.8

conda activate dsorfEnv

5. Install the required dependencies:
   
conda install scikit-learn=1.0.2

7. Run an example to check installation:
   
./exampleRun.sh

Usage
---------------
Run the program using the following command:

python DsORF_init.py $inputFileName $outputDir $numOfProcess $mode $startingPos $bypassSignalPeptide $configFileName $simulateLength
Parameters

inputFileName: Path to the input FASTA file containing genetic sequences.

outputDir: Directory where the output files will be saved. (will be created in D-sORF/output directory

numOfProcess: Number of processes to use for parallel processing.

mode: model used 
1 for TIS and CP combination,  
2 for  CP 
3 for TIS only 

startingPos: position of first letter of start codon (e.g. A of (A)TG ). In case there is an upstream regions of sequence

bypassSignalPeptide: Flag to bypass signal peptide region  
Y for bypass 
N(default) to not bypass 

configFileName: Path to the configuration file (for future extention  with models for other species).

simulateLength: Length of ORF to process. Default utilize all length for feature extraction


Example
---------------
python DsORF_init.py examples/test.fa testOutput/ 4 1 8 N conf/sORFconfig.cfg  0

Acknowledgments
---------------
This program was developed by Nikos Perdikopanis.

Publication:
---------------
D-sORF: Accurate ab initio classification of experimentally detected sORFs .



