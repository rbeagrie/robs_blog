Enhancer Journal Club: Functional roles of enhancer RNAs for oestrogen-dependent transcriptional activation
###########################################################################################################
:date: 2013-08-02 12:33
:author: Rob Beagrie
:tags: Enhancers, Journal Club
:slug: enhancer-journal-club-functional-roles-of-enhancer-rnas-for-oestrogen-dependent-transcriptional-activation

**Update 12/08/2013:** I've added a plain english summary of this paper
at ScienceGist. Find it here: http://sciencegist.com/p/189

So, now for the second of the two papers about enhancer RNAs from the
27th June edition of Nature. This one is by Li et al. and comes from the
Rosenfeld lab, who are also at UCSD. Like `the Lam et al. paper`_, they
examine the effect of a particular transcription factor (in this case
ER-α) on human breast cancer cells. Their findings are also similar to
the Lam et al. paper, but the two articles diverge when they start to
explore the mechanism through which their eRNAs appear to be acting.

Here's the abstract:

    The functional importance of gene enhancers in regulated gene
    expression is well established. In addition to widespread
    transcription of long non-coding RNAs (lncRNAs) in mammalian cells,
    bidirectional ncRNAs are transcribed on enhancers, and are thus
    referred to as enhancer RNAs (eRNAs). However, it has remained
    unclear whether these eRNAs are functional or merely a reflection of
    enhancer activation. Here we report that in human breast cancer
    cells 17β-oestradiol (E2)-bound oestrogen receptor α (ER-α) causes a
    global increase in eRNA transcription on enhancers adjacent to
    E2-upregulated coding genes. These induced eRNAs, as functional
    transcripts, seem to exert important roles for the observed
    ligand-dependent induction of target coding genes, increasing the
    strength of specific enhancer–promoter looping initiated by ER-α
    binding. Cohesin, present on many ER-α-regulated enhancers even
    before ligand treatment, apparently contributes to E2-dependent gene
    activation, at least in part by stabilizing E2/ER-α/eRNA-induced
    enhancer–promoter looping. Our data indicate that eRNAs are likely
    to have important functions in many regulated programs of gene
    transcription.

So they start by treating MCF-7 breast cancer cells with E2, which binds
to their transcription factor of interest (ER-α) and allows it to bind
to DNA. When they map the binding sites of activated ER-α by ChIP-seq,
they find 31052. Of all of these sites, only around 900 are direct
binding to promoters, whilst 7174 of the sites co-localise with H3K4me1
and H3K27Ac - histone marks known to be associated with active
enhancers. They then map transcription of RNA by GRO-seq and identify
1309 genes which have up-regulated transcription on treatment with E2,
finding that almost all of these genes (1145) have an ER-α bound site
within 200Kb of their promoters. Again, the majority of these sites,
even near to activated genes, are not themselves promoters (and so are
likely to be enhancers). Finally, when they look at the GRO-seq data for
these ER-α sites near activated genes, they find a large upregulation of
eRNAs transcribed bidirectionally from the putative enhancer.

The next question is whether these putative enhancer regions are
involved in actively regulating the expression of nearby genes. Since
both the eRNA and the nearby gene are activated when they treat the
cells with E2, they can address this question by E2 treatment whilst
simultaneously reducing the level of the nearby eRNA. If the eRNA is not
involved in activating the nearby gene, this treatment should have no
effect on the activity of the gene itself. They choose three genes
(FOXC1, TFF1 and CA12) and use two independent methods of knocking down
the eRNA (siRNAs and LNAs), showing that when the level of RNA from the
nearby enhancer is reduced, the genes are no longer activated in the
presence of E2. One could argue that this is an effect of transcription,
i.e. that the treatment with siRNAs or LNAs is, for example, reducing
the occupancy of RNA Polymerase over the enhancer and therefore reducing
delivery of RNA Polymerase to the promoter of the nearby gene. To answer
these sorts of questions, they use GRO-seq to show that treatment with
the LNA does not reduce the transcription of the enhancer RNA (only the
level of the mature eRNA). I really like the fact that they also check
that the LNA treatment does not affect methylation of the enhancer, nor
does it increase the levels of H3K9me3 or H3K27me3 silencing marks. All
this supports their contention that it is the RNA product which is
important here, and not just the level of transcription of the enhancer.

Now for the really interesting parts. They start off with a standard
luciferase assay, in which they show that the enhancer region they
identified upstream of FOXC1 can activate luciferase driven from the
FOXC1 promoter. The question is still whether it is the DNA sequence of
the enhancer or the RNA it produces which has this effect. They delete
the part of the enhancer that codes for the RNA and replace it with five
UAS sites, and unsurprisingly the luciferase is no longer activated. Now
they can cleverly use the UAS sites to artificially recruit a modified
version of the enhancer RNA back to the enhancer - and the activity is
restored. This is a clear demonstration that for this particular
enhancer, the eRNA required for activation of the FOXC1 promoter. An
interesting point that is not well highlighted in the paper is that when
they tether the eRNA to a random piece of DNA (i.e. not the enhancer
sequence) they do not get activation. This indicates that the eRNA alone
is not sufficient to activate the gene, there is still a requirement for
some part of the enhancer's DNA sequence. One experiment which would
have been nice would be to express the eRNA from a separate plasmid
without tethering it to the enhancer sequence. This would answer the
question of whether the eRNA is a real enhancer (in the sense of needing
to be close to the promoter it activates) or whether it is really a new
class of non-coding RNA - essentially a separate gene which controls
FOXC1 activation whether it is close to it or not.

The current thinking in the field is that many (if not most) enhancers
physically contact the genes which they activate by forming large DNA
loops. They tested two of their enhancer regions and found that when
they treat with E2 (the small molecule that activates these genes) they
see an increase in looping between the enhancer and the gene (as
measured by 3D-DSL, one of the many chromosome conformation capture
techniques). At a different pair of enhancers, they show that in the
presence of E2 (where the genes and enhancers are active) removing the
RNA product of the enhancer by treating with LNAs actually reduces not
only the activity of the gene, but also the looping between enhancer and
promoter. This suggests that the eRNAs produced by these enhancers are
somehow actually involved in mediating the contacts between the enhancer
and the gene, which if true would be a very interesting finding.

Finally they try to address how these eRNA might be causing looping
between the enhancer and the gene. One protein thought to be involved in
stabilising these loops is cohesin, which they show to increase its
binding to the enhancers when the cells are treated with E2. They also
show that some specific eRNAs can interact directly with cohesin and
that knocking down the eRNAs decreased the amount of cohesin bound to
enhancers after treating with E2. Last of all, they show that when the
levels of some cohesin subunits are reduced, around two thirds of
previously identified E2 target genes are no longer activated by E2.
This leads them to their conclusion:

    On the basis of these results, we speculate that many regulatory
    genomic regions, such as enhancers, harbour the cohesin complex,
    which ‘poises’ the enhancer for the stable eRNA-induced looping
    necessary for gene activation events. However, we cannot exclude the
    possibility that the role of cohesin could also reflect
    non-enhancer-based regulation.

All in all, a very interesting and powerful paper. My main criticism is
that neither this paper or `the Lam et al. paper`_ adequately rules out
the possibility of these eRNAs acting in trans - that is to say, does
the RNA really need to be transcribed close to the promoter to have an
activating effect? This paper lists the following as evidence that eRNAs
work in this way:

#. Most eRNAs they studied were present at roughly 5-15 copies per cell
#. ChIRP mapping of the FOXC1 eRNA showed it was bound most strongly at
   its site of transcription (i.e. at the enhancer). It was only found
   at 15 other regions, and none of these regions were adjacent to a
   gene activated in the presence of E2
#. Gro-seq analysis showed that 95% of the E2 responsive genes were
   unaffected by knocking down FOXC1 eRNA

For the first point, I'm really not sure how this demonstrates that the
eRNAs are working at close range. Lots of other non-coding RNAs have
been discovered which have similar copy numbers but have clear location
independent effects.

For the second two, I'm happy to take these as evidence that the FOXC1
eRNA acts primarily on the FOXC1 gene and does not have any major
trans-effects. What they do not do is show a requirement for the eRNA to
work in this way. In other words: if the eRNA was artificially added to
a cell in which it was not transcribed from the endogenous enhancer,
could it still cause activation of FOXC1 and/or looping between the
enhancer and the gene? In my eyes, this possibility is not ruled out by
the experiments in the paper.

What does the internet think? Does the eRNA cause the looping, the
activation or both? What ought to be the next experiments to dissect
these complicated causal relationships? Let me know in the comments!

Paper reference:
http://www.nature.com/nature/journal/v498/n7455/full/nature12210.html

.. _the Lam et al. paper: http://blog.rob.beagrie.com/2013/07/11/enhancer-journal-club-rev-erbs-repress-macrophage-gene-expression-by-inhibiting-enhancer-directed-transcription/
