Enhancer Journal Club: Locus-specific editing of histone modifications at endogenous enhancers.
###############################################################################################
:date: 2013-10-31 20:51
:author: Rob Beagrie
:tags: Enhancers, Journal Club, gene expression, histone modifications, Journal Club
:slug: enhancer-journal-club-locus-specific-editing-of-histone-modifications-at-endogenous-enhancers

Moving away from enhancer/promoter looping for a little while, I came
across this nice paper from the Bernstein lab at the Howard Hughes
Medical Institute. This paper is about assigning enhancers to their
cognate genes, and also has some interesting implications for the
causality of histone modifications on active enhancers.

A non-technical summary is available at ScienceGist:
http://sciencegist.com/doi/10.1038/nbt.2701

The abstract for the paper is as follows:

    Mammalian gene regulation is dependent on tissue-specific enhancers
    that can act across large distances to influence transcriptional
    activity. Mapping experiments have identified hundreds of thousands
    of putative enhancers whose functionality is supported by cell
    type–specific chromatin signatures and striking enrichments for
    disease-associated sequence variants. However, these studies did not
    address the in vivo functions of the putative elements or their
    chromatin states and did not determine which genes, if any, a given
    enhancer regulates. Here we present a strategy to investigate
    endogenous regulatory elements by selectively altering their
    chromatin state using programmable reagents. Transcription
    activator–like (TAL) effector repeat domains fused to the LSD1
    histone demethylase efficiently remove enhancer-associated chromatin
    modifications from target loci, without affecting control regions.
    We find that inactivation of enhancer chromatin by these fusion
    proteins frequently causes downregulation of proximal genes,
    revealing enhancer target genes. Our study demonstrates the
    potential of epigenome editing tools to characterize an important
    class of functional genomic elements.

First of all, I think the technology and methodology of the paper is
extremely exciting. Since custom designed DNA binding proteins started
to become common for genome editing, it has only been a matter of time
before people start using the techniques to do some really cool
molecular biology, and I think we are going to see some really exciting
work in this area over the next decade or so. Papers using synthetic
fusion proteins to study enhancer mechanisms in more molecular detail
than was previously possible have started to trickle out recently, my
favourite being Gert Blobel's demonstration that enhancer/promoter
looping can induce gene expression
(http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3372860/).

In this paper, Mendenhall et al. fuse an engineered TAL effector DNA
binding domain to the chromatin modifier LSD1. By designing the TALE
domain to bind to a predicted enhancer sequence, they can do in vivo
targeting of H3K4 demethylase activity. This is great for enhancers as
H3K4me1 and H3K4me2 are two of the marks commonly used to identify
putative enhancer regions which are active in any specific cell line.
For 40 tested LSD1/TALE fusion constructs targeted to different
enhancers, they find that 26 show a more than 2 fold reduction in either
H3K4me2 or H3K27Ac. This is a nice validation that the method appears to
be reasonably efficient, but one interesting point here is that the
effect on H3K27 acetylation seems to be larger than that on H3K4me2.
This most likely indicates that LSD1 is recruiting additional proteins
with HDAC activity, but the possibility remains that H3K4 methylation
may lie upstream of this acetylation.

Having established that they are able to 'edit' the histone
modifications at 26 putative enhancer loci, they then choose 9 of their
constructs and look for changes in local gene expression using "a
modified RNA-seq procedure termed 3' digital gene expression (3'DGE)". 
Of these nine, they found significantly downregulated genes in four
cases. The paper is a little confusing here, as the main figure legend
says the results are for "the closest expressed upstream and downstream
genes", but the methods say they examined the three closest upsteam and
three closest downstream genes, and the supplementary figure actually
shows between 10 and 25 genes measured per targetting construct. In any
case, there is plenty of literature showing that enhancers can act over
really quite large distances and since they measured expression from the
whole transcriptome it would be nice to see, for example, the expression
of all genes within a megabase. Perhaps this might explain why they only
identify candidates in four out of nine cases.

All in all, I really like this paper. It's nice to see a mechanistic
identification of enhancer target genes, although some would argue that
targeting eRNAs with an shRNA would have the same effect and would be
potentially quicker/cheaper for identifying enhancer targets on a wider
scale. I think the paper would benefit from really nailing down the
order of causality - since the LSD1 construct seems to be interfering
with H3K27 acetylation, it seems likely that the observed effects depend
upon recruitment of other factors, at least in part. The question is
which effects are due to the change in H3K4 demethylation and which are
due to recruitment of extra factors by LSD1. Here I think it would have
been really nice to have a catalytically inactive LSD1 fused to a TALE
domain. If you saw no effect on gene expression with this construct, I
think you would have very strong evidence that H3K4me2 actually plays a
causal role in determining enhancer activity.

Original paper available at:
http://www.nature.com/nbt/journal/vaop/ncurrent/full/nbt.2701.html

As always, let me know what you think about this paper in the comments!
