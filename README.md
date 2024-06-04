D-sORF
---------------
D-sORF is an alignment-free data mining algorithm based on machine learning. The algorithm is based on the nucleotide composition of the ORF and the sequence information around the ATG start codon, called the translation initiation site (TIS). D-sORF distinguishes coding from non-coding transcripts and focuses on sequences with small ORFs. It provides a scoring system for predicting putative translating sORFs based on nucleotide context of three different windows (54, 99, and 180-nts) within ORFs and a 9-nts window around TIS of experimentally validated CDSs of protein-coding genes, compared to windows of similar size and location in negative sORFs.


Installation
---------------
1. Clone the repository from GitHub:
git clone https://github.com/nperdi/D-sORF.git

2. Go to D-sORF directory
  cd D-sORF

2. Create and activate a Conda virtual environment:
conda create --name dsorfEnv python=3.8
conda activate dsorfEnv

3. Install the required dependencies:
conda install scikit-learn=1.0.2

4. Run an example to check installation:
./exampleRun.sh

Usage
---------------
Run the program using the following command:
python DsORF_init.py $inputFileName $outputDir $numOfProcess $mode $startingPos $bypassSignalPeptide $configFileName $simulateLength
Parameters
inputFileName: Path to the input file containing genetic sequences.
outputDir: Directory where the output files will be saved.
numOfProcess: Number of processes to use for parallel processing.
mode: Mode of operation (e.g., 'batch', 'single').
startingPos: Starting position for dORF search.
bypassSignalPeptide: Flag to bypass signal peptide detection.
configFileName: Path to the configuration file.
simulateLength: Length to simulate the ORF.

Example
---------------
python DsORF_init.py examples/test.fa testOutput/ 4 1 8 N conf/sORFconfig.cfg  0

Acknowledgments
---------------
This program was developed by Nikos Perdikopanis.

Publication:
---------------
D-sORF: Accurate ab initio classification of experimentally detected sORFs .



