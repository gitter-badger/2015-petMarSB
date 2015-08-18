Methods
=======

In order to assess the completeness of our de Novo transcriptome assembly (lamp10), we have compared the alignment of the generated transcripts against the existing genome annotations released with Pmarinus v7.0.75. First, we use blastn to align transcripts to the genome, using parameters `-evalue 1e-6`. Then, we use the coordinates from the annotation and the corresponding coordinates from the alignments to calculate the proportion of annotated sequence overlapped, proportion of transcripts overlapped, and the respective proportions of non-overlapped sequence and transcripts. We consider an annotated region to be overlapped by a trancript if it is at least 90% covered, with at least 98% identity [TODO: get better justification for these cutoffs other than "things Camille remembers reading"].

We give particular attention to alignments which entirely contain annotated regions, as these suggest extensions to existing annotations. When these alignments are from transcripts with homology evidence from other species, we consider them to represent putative extensions [note: maybe not necessary to establish validity, instead just report the numbers]. Further, alignments which are entirely contained within an annotation suggest either an overly aggressive prediction in the genome, or an incompletely assembled transcript. 

Results
=======

Using our 90% overlap / 98% identity heuristic, we find 71.4% of annotations to be covered by a transcript from lamp10. When we break this down by feature, we find that the the proportion is brought down by features of types transcript and gene, both of which include introns.

============   ===============
Feature Type   Prop Overlapped
============   ===============
CDS            0.789203
UTR            0.838308
exon           0.780100
gene           0.128880
start_codon    0.857505
stop_codon     0.903922
transcript     0.120501
============   ===============

 while 73%[dubious] of transcripts cover an annotation. Futher, []% of the genome is covered by annotations, while [%] is covered by alignments from lamp10; []% of transcripts have any alignment to the genome.

We also find that []% of transcript alignments entirely contain an annotation, increasing the annotation size by [blah]%. []% of extensions are supported by homology to a known protein. []% of transcipt alignments are entirely contained by an annotation.

[figure: bar chart of proportions; histogram of extension percentages or raw sequence lengths]

Discussion
===========


