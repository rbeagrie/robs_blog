Enhancer Journal Club: Rev-Erbs repress macrophage gene expression by inhibiting enhancer-directed transcription
################################################################################################################
:date: 2013-07-11 09:07
:author: rbeagrie
:category: Enhancers, Journal Club
:slug: enhancer-journal-club-rev-erbs-repress-macrophage-gene-expression-by-inhibiting-enhancer-directed-transcription

**Update 08/08/2013:** I've added a plain english summary of this paper
at ScienceGist. Find it here: http://www.sciencegist.com/p/179

Two super interesting papers about enhancers came out in Nature last
week from the Glass and Rosenfeld labs at UCSD. I'm not sure what to
make of them, so I thought I would start a blog, and ask the internet
what it thinks!

So the first of the two papers is by Lam et. al. and comes from the
Glass lab. They were looking at two transcriptional repressors
(Rev-Erb-α and Rev-Erb-β) and found some surprising effects on
enhancers.

Here's the abstract:

    Rev-Erb-α and Rev-Erb-β are nuclear receptors that regulate the
    expression of genes involved in the control of circadian rhythm,
    metabolism and inflammatory responses. Rev-Erbs function as
    transcriptional repressors by recruiting nuclear receptor
    co-repressor (NCoR)-HDAC3 complexes to Rev-Erb response elements in
    enhancers and promoters of target genes, but the molecular basis for
    cell-specific programs of repression is not known. Here we present
    evidence that in mouse macrophages Rev-Erbs regulate target gene
    expression by inhibiting the functions of distal enhancers that are
    selected by macrophage-lineage-determining factors, thereby
    establishing a macrophage-specific program of repression.
    Remarkably, the repressive functions of Rev-Erbs are associated with
    their ability to inhibit the transcription of enhancer-derived RNAs
    (eRNAs). Furthermore, targeted degradation of eRNAs at two enhancers
    subject to negative regulation by Rev-Erbs resulted in reduced
    expression of nearby messenger RNAs, suggesting a direct role of
    these eRNAs in enhancer function. By precisely defining eRNA start
    sites using a modified form of global run-on sequencing that
    quantifies nascent 5' ends, we show that transfer of full enhancer
    activity to a target promoter requires both the sequences mediating
    transcription-factor binding and the specific sequences encoding the
    eRNA transcript. These studies provide evidence for a direct role of
    eRNAs in contributing to enhancer functions and suggest that
    Rev-Erbs act to suppress gene expression at a distance by repressing
    eRNA transcription.

Essentially they first map the genomic locations of these two repressors
and find that they colocalise primarily with monomethylated histone H3
lysine 4 (H3K4me1 - a known marker of enhancers). When they knock out
the proteins in blood cells, they see around 140 genes increasing
expression and 70 decreasing (and since these are known repressors, it
makes sense that removing them primarily leads to upregulation of
genes.) What is perhaps more surprising is that only three of the 141
genes which increase their expression level show Rev-Erbs binding at the
promotor, indicating that their binding to enhancers may be regulating
other genes. They test a few of these regions in luciferase assays (a
standard assay for enhancer activity), to verify that they are bona fide
enhancers, and they use GRO-seq (a method for mapping nascent
transcription) to show that the regions outside of known genes which are
marked by both Rev-Erbs binding and H3K4me1 are transcribed in both
directions.

So far so good, there are a few examples of activators/repressors
binding to enhancers instead of promotors, and the idea of enhancers
being transcribed to produce eRNAs (enhancer RNAs) also been floating
around for a few years. What's really interesting is that when they
knock out Rev-Erbs they see increased transcription of eRNAs from sites
that were previously bound by the repressors. So now they have seen that
transcription increases at both the enhancers where the protein was
bound and the nearby genes, the obvious question is whether and how
transcription at the two sites are linked. One can imagine a few
scenarios:

#. **No causation:** The increased transcription of both genes and eRNAs
   are both caused by some other effect
#. **The act of transcription of the gene induces transcription of the
   enhancer:** If the enhancer moves to contact the gene when the
   Rev-Erbs is knocked out, the increased proximity to active RNA
   polymerase could induce the increased transcription of the enhancer
#. **The act of transcription of the enhancer induces transcription of
   the gene:** Equally, the removal of the repressor could increase the
   transcription of the enhancer, so when it is brought close to the
   promoter of the nearby gene, transcription of that gene is also
   activated
#. **The product of transcription of the enhancer induces transcription
   of the gene:** The RNA produced from the enhancer could somehow be
   activating the gene.

Of these scenarios, number three is how a lot of people have
conceptualised transcription at enhancers for a while. The more
interesting option is number four, where it is actually the RNA product
of the enhancer which has an active role, not just the fact that the
enhancer is transcribed.

To establish that enhancer activity really causes the change in activity
at the nearby gene, they use two independent approaches (siRNAs and
antisense oligonucleotides) to reduce the eRNAs, and observe that when
the eRNA product is not present the activation of the nearby gene is
decreased. This nicely establishes that there is a causal relationship
at work, and rules out scenario number one. It also makes it unlikely
that transcription at the gene inducing transcription of the enhancer is
having a major effect (since if this was the case, activity of the gene
would not be affected by removing the eRNA product). It would have been
nice to rule this out more formally by using siRNAs against the gene and
demonstrating that the level of transcription of the enhancer is not
affected, but I don't think it's a crucial experiment. What it does not
rule out is that transcription of the enhancer may be the important
factor, since siRNAs in particular are known to repress the promoters of
their targets as well as simply reducing the level of mature RNA
product.

Finally, the most interesting experiment of the paper. The authors
return to dissecting one particular putative enhancer region in a
luciferase assay, where they add different fragments of the Mmp9
enhancer region into a plasmid expressing luciferase at a low level from
a minimal promoter. The enhancer region is made up of a central core
containing binding sites for a number of different transcription
factors, a region which codes for the antisense eRNA and a region which
codes for the sense eRNA. The entire region does activate the expression
of the luciferase, as expected. Normally, people think of enhancers as
functioning by recruiting transcription factors, so one would expect
that the core region on it's own (which contains the transcription
factor binding sites) would be sufficient to activate the luciferase.
However, the authors find that the core region on it's own does not have
enhancer activity in their assay. In fact the activity is restored only
by the addition of the core region plus the sense eRNA (but not the
antisense eRNA). One could argue here that the region which codes for
the eRNA actually contains some transcription factor binding sites that
we simply aren't able to detect with conventional methods, so finally
the authors also show that if you insert the core region plus the
reversed sequence of the sense eRNA, you still get no activation. This
is important because any transcription factors would bind equally well
to the normal or the reversed sequence, but the eRNA which is produced
would be completely different. They also use RT-PCR to demonstrate that
in the context of the luciferase assay the enhancer region is producing
the eRNAs they expect it to be producing.

Taken together, this is a really interesting demonstration that in the
case of the two specific enhancers they investigate, the enhancer
activity really depends on the actual product of transcription (the
eRNA) and not just generally on transcription of the enhancer region in
a non sequence specific manner. Of course, as ever, there are some
points that this paper does not address. Is this eRNA dependent
mechanism really the one which is operating *in vivo*? The siRNA and
antisense oligo experiment makes this very likely, but really the killer
experiment only demonstrates the effect in the context of an artificial
luciferase assay, so there is at least a possibility that it is the act
of transcription and not the eRNA product which is important at the
endogenous locus. If it is the real *in vivo* mechanism, is it a general
one or is it more widespread? The effect is only explored in detail at 2
of around 1000 identified enhancer regions, so something completely
different could be going on at the other 998.

Most importantly though, in my opinion the paper does not address
whether these regions are really enhancers, and not simply new
non-coding RNA genes. The activity of an enhancer should require close
proximity to its target genes, but this is not demonstrated for any of
the enhancers studied in the paper. If it really is the specific eRNA
which is activating the luciferase promoter, could you get this effect
by expressing the eRNA from a different plasmid, or do they really need
to be in conctact? For me, this is the most interesting question, but
fortunately this aspect is explored in more detail in the second of
these two papers - which I'll be discussing next time!

Paper reference:
http://www.nature.com/nature/journal/v498/n7455/full/nature12209.html

**Update:** `Journal club on the second paper is now up!`_

.. _Journal club on the second paper is now up!: http://blog.rob.beagrie.com/2013/08/02/enhancer-journal-club-functional-roles-of-enhancer-rnas-for-oestrogen-dependent-transcriptional-activation/
