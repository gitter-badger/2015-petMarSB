Background
==========

Some biological background on sea lamprey, and why we care about them:
ancestral jawed vertebrate, invasive species interest, regenerative
capabilities, programmed genome rearrangement (PGR). This drives
interest in a complete sea lamprey transcriptomic reference. [Cite:
lamprey genome paper, more provided by weiming]

Background on NGS / RNAseq tech enabling deep mRNA sequencing. Lack of a
complete reference due to PGR necessitates de novo assembly. De novo
projects challenging because of difficulty in validation, data volume,
data integrity. [Cite: ...]

Reproducibility crisis: many methods for pre-processing, assembly, and
post-processing, but many difficult to replicate. Lack of documented
tools, versions, parameters, source code for scripts. Demonstration of
effective reproducible pipelines from start to finish. [Cite:
assemblathon, mr-c, ...]

Goal: deeply characterize the sea lamprey transcriptome; produce a
valuable resource for researchers; demonstrate efficacy of de novo
approach for many-sample data; show open, reproducible pipelines.

Data Description
================

Section should include information on sea lamprey sample prep where
available, table of sample descriptions including read lengths, insert
sizes, sequencing technology, tissue type, and conditions. Also includes
accessions.

[Table 1, samples]

Analyses
========

Assembly
--------

We find 73.93% of annotations to be covered by a transcript from lamp10.
Breaking down this percentage by feature type reveals that the results
are biased by the inclusion of gene and transcripts features, both of
which tend to contain large stretches of intronic sequence unlikely to
be covered above our chosen cutoff by any transcript. When we consider
only exons, 80.71% are covered, exons being a basic feature of mRNAs.

| lrr & lamp00 & lamp10
| CDS & 0.919196 & 0.814513
| UTR & 0.957400 & 0.862251
| exon & 0.896378 & 0.807120
| gene & 0.051323 & 0.147640
| start\_codon & 0.960101 & 0.857505
| stop\_codon & 0.636520 & 0.903922
| transcript & 0.048511 & 0.138392

Conversely, 29.72% of transcripts are covered by a single feature, while
99.89% of transcripts are covered in lamp00. We find the latter number
encouraging; one would expect almost all transcripts in lamp00 to be
covered by a single feature, as it was derived directly from the
annotations, while previous evidence suggests that lamp10 is a superset
of lamp00, thus explaining the disparity. Examining the extend to which
our overlaps are a superset, we can break down transcript genome
homologies by whether each transcript has only a homology, or both a
homology and an annotation overlap, as follows.

| llrr & assembly & num & prop
| presence & & &
| +genome+ann & lamp00 & 11476 & 0.998868
| +genome+ann & lamp10 & 212606 & 0.297208
| +genome-ann & lamp00 & 0 & 0.000000
| +genome-ann & lamp10 & 311949 & 0.436082

With so many transcripts having alignments to the genome but no
corresponding annotation, it would be valuable to further understand
which of these transcripts have protein homologies to other databases.
In particular, lamprey’s uniquely valuable position in vertebrate
evolution drives questions regarding loss and gain of genes within
gnathostomes. To that end, we have subdivided these transcripts based on
their homologies and orthologies with both zebrafish and amphioxus.

| llrr braflo\_best\_hom & danrer\_best\_hom & no\_ann & has\_ann
| True & True & 36605 & 10293
| True & False & 847 & 873
| False & True & 7196 & 4445
| False & False & 167958 & 296338

| llrr danrer\_ortho & braflo\_ortho & no\_ann & has\_ann
| True & True & 3664 & 833
| True & False & 2450 & 892
| False & True & 1255 & 437
| False & False & 205237 & 309787

Futher, % of the genome is covered by annotations, while % is covered by
alignments from lamp10; % of transcripts have any alignment to the
genome.

We also find that % of transcript alignments entirely contain an
annotation, increasing the annotation size by %. % of extensions are
supported by homology to a known protein. % of transcript alignments are
entirely contained by an annotation.

Pooled Assembly Discovers Novel Transcripts
-------------------------------------------

Many-Sample Comparison
----------------------

Include heatmaps, bar charts of unique gene content.

Discussion
==========

Methods
=======

In order to assess the completeness of our de Novo transcriptome
assembly (lamp10), we have compared the alignment of the generated
transcripts against the existing genome annotations released with
Pmarinus v7.0.75. First, we use blastn to align transcripts to the
genome, using parameters \`-evalue 1e-6\`. Then, we use the coordinates
from the annotation and the corresponding coordinates from the
alignments to calculate the proportion of annotated sequence overlapped,
proportion of transcripts overlapped, and the respective proportions of
non-overlapped sequence and transcripts. We consider an annotated region
to be overlapped by a trancript if it is at least 90 We give particular
attention to alignments which entirely contain annotated regions, as
these suggest extensions to existing annotations. When these alignments
are from transcripts with homology evidence from other species, we
consider them to represent putative extensions [note: maybe not
necessary to establish validity, instead just report the numbers].
Further, alignments which are entirely contained within an annotation
suggest either an overly aggressive prediction in the genome, or an
incompletely assembled transcript.

Pre-processing
--------------

Trinity Assembly
----------------

Post-processing
---------------
