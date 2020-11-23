# control_seq_gen

**Overview**
<p> Generates a set of control sequences from a set of reference sequences that are passed in. The goal is to maintain the statistical parameters (i.e. nucleotide composition) of the reference sequences without recapitulating the sites of interest. </p>
 
 **How it works**
 <p> All of the reference seqeunces are concatenated into one string. Random units are resampled from the conglomerate stirng and concatenated to make a control sequence. </p>
 
 **Usage** <br>
 ###### Method 1 - manually pass in paramters
 `cs_gen()`
 <p>The parameters can be passed directly into the function. It will return the set of control sequences:</p>
 
 Parameter | Default | Desrciption
 ---|---|---
 `fasta_files` | input.fasta | path to a FASTA file containing the set of reference sequences to pull from to make the control sequences.
 `output_file` | data/cs_gen.fasta | path to the output file where generated control set will be written.
 `output_descrip` | Control sequence | THe description that is attached to each of the generated sequences in the output FASTA 
 `mark_param` | 5 | _Markovnikov parameter_, the length of the resampling unit. (i.e. 5 -> fragments of length 5 will be selected)
 `length` | 1000 | The length of each individual control sequence
 `num_seq` | 100 | The number of control sequences to be returned. 
 
 ###### Method 2 - load parameters from file
`cs_genj()` 
 <p>An input JSON file is parsed for the parameters. JSON file layout: </p>
 
 ```JSON 
     {
        "fasta_files" : ["data/input.fasta", "data/input2.fasta"],
        "output_file" : "cs_gen.fasta",
        "output_descrip" : "Control Sequence",
        "mark_param": 5,
        "length" : 10,
        "num_seq" : 10
    }
 ```
