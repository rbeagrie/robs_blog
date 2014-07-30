Enhancer Journal Club: Global view of enhancer–promoter interactome in human cells
##################################################################################################################
:date: 2014-07-31 09:00
:author: Rob Beagrie
:tags: Enhancers, Journal Club
:slug: enhancer-journal-club-global-view-of-enhancer-promoter-interactome-in-human-cells

One of the key hypotheses which is driving interest in enhancer biology right
now is that mutations in enhancer sequences may cause medically relevant
changes in gene expression (e.g. in cancer). There has been a great deal of
progress in recent years towards high throughput identification of enhancers,
genome sequencing and measurement of gene expression (e.g. by RNA-seq).  In
order to show a correlation between sequence variation in enhancers to gene
expression, the missing piece of the puzzle is a way to link predicted
enhancers with their target promoters. The paper I'll be discussing this month
contains a nice summary of the currently used methods, as well as some fairly
rigorous comparisons between the possible approaches. The article is called
"Global view of enhancer–promoter interactome in human cells" and comes from
the Tan lab at the University of Iowa.

The original paper can be found at
<http://www.pnas.org/content/111/21/E2191.long>. The abstract for the paper is
as follows:

    Enhancer mapping has been greatly facilitated by various genomic marks
    associated with it. However, little is available in our tool- box to link
    enhancers with their target promoters, hampering mechanistic understanding
    of enhancer–promoter (EP) interac- tion. We develop and characterize
    multiple genomic features for distinguishing true EP pairs from
    noninteracting pairs. We inte- grate these features into a probabilistic
    predictor for EP interac- tions.  Multiple validation experiments
    demonstrate a significant improvement over state-of-the-art approaches.
    Systematic analy- ses of EP interactions across 12 cell types reveal
    several global features of EP interactions: (i) a larger fraction of EP
    interactions are cell type specific than enhancers; (ii) promoters
    controlled by multiple enhancers have higher tissue specificity, but the
    regulat- ing enhancers are less conserved; (iii) cohesin plays a role in
    me- diating tissue-specific EP interactions via chromatin looping in a
    CTCF-independent manner. Our approach presents a systematic and effective
    strategy to decipher the mechanisms underlying EP communication.

The first step in their analysis is to identify promoters and enhancers in
their 12 cell types. For promoters, they use the GENCODE annotation of
transcripts and for enhancers they use their own previously published method
(`CSI-ANN <http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2887052/>`_) to detect
enhancers based on H3K4me1, H3K4me3 and H3K27Ac. Once they have their
enhancer/promoter lists they identify "real" pairs using ChIA-PET data.

The next step is to describe features of the enhancer/promoter (E/P) pairs that
distinguish "real" pairs from random pairs. They use the following four
characteristics:

1. In real E/P pairs, the ChIP signal of the enhancer correlates with
   transcription at the promoter across the 12 cell types.
2. In real E/P pairs, the expression of transcription factors that bind to the
   enhancer correlates with transcription at the promoter.
3. Real E/P pairs show higher co-evolution of DNA sequence, or higher
   conservation of their relative position (synteny).
4. Real E/P pairs tend to be closer to each other.

For each of the characteristics, they check for statistically robust
differences between the real pairs and random non-pairs, then combine the four
measures using a random-forest classifier. This forms the basis of their
approach, which they call IM-PET. They compare IM-PET to the "nearest-promoter"
approach (which is still what most people use in a pinch) and to three other
published algorithms. The ROC curves are relatively impressive when they use
the original ChIA-PET data from K562 and MCF7 cells for validation, but
actually the approaches appear to perform more similarly when newer ChIA-PET or
high resolution Hi-C datasets are used.

Whilst their analyses do seem to support their method as the best compromise
between precision and recall, I wonder whether their "nearest promoter"
comparison is fair. It would have been better to use the nearest active
promoter as a control, as it seems a reasonable assumption that an inactive
gene cannot be the target of an active enhancer. Even using this comparison,
their approach would likely compare favourably as "nearest x" can only ever
predict one target for each enhancer, and will therefore have lots of false
negatives. I think the most interesting comparison would have been against the
assumption that enhancers contact all active promoters within a certain
distance, or even better, all active promoters within the same topological
domain. Another way of putting this question is, how often does IM-PET predict
that an active promoter is not a target for a nearby enhancer? I can't see any
examples of this in the UCSC tracks from the paper, at least.


