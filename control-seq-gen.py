#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 17:34:29 2020

@author: ichaudr
"""

'''
Generates cotnrol sequences for motif analysis. Goal is to maintain the
statistical parameters of the input sequences without recapitulating the sites
of interest. (i.e maintaining nucleotide composition). 

'''

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import random
import json


#Control Sequence (cs) generator
#Resamples a set of references sequences to generate a set of control sequences. 
#Parameters:
    # fasta_files: array of file names stored as strings, these files hold the reference seqeunces
    # output_file: string, file name (.fasta) that holds the generated control sequences
    # output_descrip: string, the description stored with each generated sequence in the ouput FASTA file.
    # mark_param: int, the size of the resampling unit (i.e 5 -> 5 residues will be selected at a time)
    # length: int, the length of each control sequence generated
    # num_seq: int, the number of control sequences needed
def cs_gen(fasta_files=["input.fasta"], output_file="data/cs_gen.fasta", output_descrip="Control sequence" 
           ,mark_param=5, length=1000, num_seq=100):
    
    
    #The sequences from all the input files are concatenated into one string
    #that can be resampled. 
    total_concat = ""
    for file in fasta_files:
        for record in SeqIO.parse(file, "fasta"):
            total_concat += record.seq
            
            
    #Error handeling
    if mark_param > len(total_concat):
        raise Exception("mark_param > length of reference seq")
    if mark_param > length:
        raise Exception("mark_param > length of output seq")
    
    
    #Holds the final set of control sequences as a Sequence records
    cs_set = []
    
    #The number resampling interations needed per sequence.
    #If the mark_param is not a perfect factor of the length, an addtional
    # iteration is added to compensate. 
    iterate_count = int(length / mark_param)
    
    if length % mark_param != 0:
        iterate_count += 1
    
    
    for i in range(num_seq):
        #Hold the current control sequence that is being generated.
        curr_cs = []
        
        #For each iteration of the resampling, a random position in the
        # conglomarate of all the input reference sequences is selected as the 
        # starting position. 
        for j in range(iterate_count):
            start_pos = random.randint(0, len(total_concat) - mark_param)
            curr_cs.append(str(total_concat[start_pos:start_pos+mark_param]))
               
        #Makes a SeqRecord of the current control sequence
        cs_rec = SeqRecord(Seq(''.join(curr_cs)), id=("controlSeq" + str(i)), name="cs", description=output_descrip)
        cs_set.append(cs_rec)
        
    #Writes all control sequence records to the output file
    SeqIO.write(cs_set, output_file, "fasta")    
     
    return cs_set


#A wrapper function for cs_gen() that takes the inputs as a .json file
# .json file format:
    # {
    #   "fasta_files" : ["input.fasta", "input2.fasta"],
    #   "output_file" : "cs_gen.fasta",
    #   "output_descrip" : "Control Sequence",
    #   "mark_param": 5,
    #   "length" : 10,
    #   "num_seq" : 10    
    # }
def cs_genj(json_file="input.json"):
    params = json.load(open(json_file))
    return cs_gen(params["fasta_files"], 
           params["output_file"], 
           params["output_descrip"], 
           params["mark_param"], 
           params["length"], 
           params["num_seq"])
            
        
cs_genj()