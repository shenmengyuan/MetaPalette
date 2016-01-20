#This will run each of the main scripts of MetaPalette and check the results with the pre-computed values

python ../src/Python/Train.py -i Data/FullFileNames.txt -o TestOutput -b bcalm -r `pwd` -j jellyfish -c count_in_file -t 4 -k 5 -s 4

#Write code to check if output makes sense

python ../src/Python/Classify.py -d TestOutput -o TestOutput -i Data/test-reads.fa -k default -j jellyfish -q query_per_sequence -Q C -y -x -t 4

#Write code to check if output makes sense

#Write plot code

#Check if plot output makes sense