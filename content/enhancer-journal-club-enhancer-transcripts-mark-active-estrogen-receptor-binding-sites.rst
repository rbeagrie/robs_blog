Enhancer Journal Club: Enhancer transcripts mark active estrogen receptor binding sites
#######################################################################################
:date: 2013-09-26 16:10
:author: rbeagrie
:category: Enhancers, Journal Club
:slug: enhancer-journal-club-enhancer-transcripts-mark-active-estrogen-receptor-binding-sites

Something rather contradictory for the Enhancer Journal Club series, the
Hah et al. paper, published in May from the Kraus lab at UT
Southwestern. This paper is really interesting because it has very
different conclusions to the previous three papers I've blogged about,
and I'm fascinated to see if and how the field can resolve these
discrepancies.

As always, I've posted a non-technical summary at ScienceGist:
http://sciencegist.com/gists/172

The abstract for this paper is as follows:

    We have integrated and analyzed a large number of data sets from a
    variety of genomic assays using a novel computational pipeline to
    provide a global view of estrogen receptor 1 (ESR1; a.k.a. ERα)
    enhancers in MCF-7 human breast cancer cells. Using this approach,
    we have defined a class of primary transcripts (eRNAs) that are
    transcribed uni- or bidirectionally from estrogen receptor binding
    sites (ERBSs) with an average transcription unit length of ∼3–5 kb.
    The majority are up-regulated by short treatments with estradiol
    (i.e., 10, 25, or 40 min) with kinetics that precede or match the
    induction of the target genes. The production of eRNAs at ERBSs is
    strongly correlated with the enrichment of a number of genomic
    features that are associated with enhancers (e.g., H3K4me1, H3K27ac,
    EP300/CREBBP, RNA polymerase II, open chromatin architecture), as
    well as enhancer looping to target gene promoters. In the absence of
    eRNA production, strong enrichment of these features is not
    observed, even though ESR1 binding is evident. We find that
    flavopiridol, a CDK9 inhibitor that blocks transcription elongation,
    inhibits eRNA production but does not affect other molecular
    indicators of enhancer activity, suggesting that eRNA production
    occurs after the assembly of active enhancers. Finally, we show that
    an enhancer transcription “signature” based on GRO-seq data can be
    used for de novo enhancer prediction across cell types. Together,
    our studies shed new light on the activity of ESR1 at its enhancer
    sites and provide new insights about enhancer function.

Like the Li et al. paper (Functional roles of enhancer RNAs for
oestrogen-dependent transcriptional activation), this paper identifies
putative enhancers in MCF-7 cells by looking for sites of overlap
between estrogen receptor binding (identified by ChIP) and primary
transcription (identified by GRO-seq). Similarly, they find that most of
the features of active enhancers associated with these sites (H3K4me1,
H3K27ac, bidirectional transcription and DNA loop formation) are
up-regulated by treatment with estradiol, which occurs in parallel to
the up-regulation of genes in the vicinity of these putative enhancers.

Where the paper gets interesting is the attempt to disentangle some of
the mechanistic details at work here. The obvious question is whether
the transcription of the enhancer RNA "causes" the increased deposition
of the active enhancer marks, or indeed the transcriptional
up-regulation of the neighbouring gene. Whilst the Li and Lam papers
tackle this for specific enhancers by targeting the associated eRNA with
siRNA/antisense oligonucleotides, in this paper the authors attempt a
global intervention by pre-incubating the cells in the general
transcriptional inhibitor flavopiridol before treating with E2. They
find that even when the cells are unable to respond to E2 by
up-regulating the transcription of the eRNA, the E2 treatment is still
able to induce higher occupancy of RNA Pol II, P300 and H3K27ac, as well
as an increase in enhancer/promoter looping. Although the flavopiridol
has a potentially global effect, they only identify its effects by
ChIP-qPCR or 3C assays over a small number of genes. Additionally, the
intervention is not quite as elegant as using siRNAs targeting the eRNA
specifically, because the flavopiridol also inhibits transcription of
the target gene, so they are unable to link eRNA production to the real
functional output of gene regulation.

Of course in both of these contrasting papers, the authors demonstrate
effects on a limited number of individual genes, so it is always
possible that the two sets of genes use different mechanisms. I do
wonder if there is a model which would explain both of these sets of
results, but at the moment they do seem to be mutually exclusive - one
claiming to show that removing the eRNA abolishes enhancer/promoter
looping, and the other that looping occurs even when transcription of
the eRNA is inhibited. Overall, very perplexing!

Let me know your thoughts in the comments...

Original paper: http://genome.cshlp.org/content/23/8/1210.long
