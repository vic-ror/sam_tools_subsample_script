# sam_tools_subsample_script
Automizes subsampling/downsampling of sequencing coverage depth ofsam files using samtools view and python.
Useful when working with sam files of different coverage, in order to make the comparison more equitable.

# How it works
In command line you should add the flags:
* -i = --input_file = Input file name/path
* -o = --output_file = Output file name/path
* -ic = --input_cov = Sequencing coverage of the input file
* -wc = --wanted_cov = Wanted sequencing coverage


