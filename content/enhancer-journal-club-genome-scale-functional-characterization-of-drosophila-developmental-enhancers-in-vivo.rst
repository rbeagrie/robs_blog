Enhancer Journal Club: Genome-scale functional characterization of Drosophila developmental enhancers in vivo
#############################################################################################################
:date: 2014-06-27 16:34
:author: Rob Beagrie
:tags: Enhancers, Journal Club
:slug: enhancer-journal-club-genome-scale-functional-characterization-of-drosophila-developmental-enhancers-in-vivo

Following on from last month's journal club, there was a new paper this
month from the Stark lab in Vienna also dealing with large-scale
characterisation of enhancer activity patterns. The original paper can
be found at www.nature.com/doifinder/10.1038/nature13395, and the
abstract is as follows:

    Transcriptional enhancers are crucial regulators of gene expression
    and animal development and the characterization of their genomic
    organization, spatiotemporal activities and sequence properties is a
    key goal in modern biology. Here we characterize the in vivo
    activity of 7,705 Drosophila melanogaster enhancer candidates
    covering 13.5% of the non-coding non-repetitive genome throughout
    embryogenesis. 3,557 (46%) candidates are active, suggesting a high
    density with 50,000 to 100,000 developmental enhancers genome-wide.
    The vast majority of enhancers display specific spatial patterns
    that are highly dynamic during development. Most appear to regulate
    their neighbouring genes, suggesting that the cis-regulatory genome
    is organized locally into domains, which are supported by
    chromosomal domains, insulator binding and genome evolution.
    However, 12 to 21 per cent of enhancers appear to skip non-expressed
    neighbours and regulate a more distal gene. Finally, we
    computationally identify cis-regulatory motifs that are predictive
    and required for enhancer activity, as we validate experimentally.
    This work provides global insights into the organization of an
    animal regulatory genome and the make-up of enhancer sequences and
    confirms and generalizes principles from previous studies. All
    enhancer patterns are annotated manually with a controlled
    vocabulary and all results are available through a web interface
    (http://enhancers.starklab.org), including the raw images of all
    microscopy slides for manual inspection at arbitrary zoom levels.

The idea here is to clone >7000 enhancer candidates upstream of a
reporter gene and assay each candidate's activity by imaging throughout
embryogenesis. The candidates are all cloned into the same genomic
location, which should help minimize context dependent effects. They
classified the candidates as being either constitutively active or
active in early, middle or late embryogenesis. They then show that the
candidates show DNase hypersensitivity, P300 binding and H3K27
acetylation at the relevant stage of embryogenesis (i.e.
mid-embryogenesis enhancers show higher active marks during
mid-embryogenesis than early or late). An interesting exception here is
constitutive enhancers, which only show P300 binding in early
embryogenesis - this perhaps indicates that P300 may be more important
for establishing enhancer activity than maintaining it.

They assign putative target genes to the 874 strongest enhancers by
matching the expression pattern of the enhancer with that of the closest
five genes up or downstream. Like in the Symmons et. al. paper I
discussed last month, they also find that Hi-C domain boundaries are
highly depleted between enhancers and their target genes. However, out
of 482 enhancer-gene assignments, only 28 enhancers appeared to regulate
more than one gene. I think this is an interesting point - if Hi-C
topological domains serve to constrain the genes affected by a certain
enhancer then they clearly aren't the only story. Most domains contain
multiple genes, yet it seems that enhancers may only affect a handful
(or even just one) of those potential targets - what is it that adds the
extra specificity? Of course the other explanation is that enhancer
presence may have very subtle or partially redundant expression effects
on multiple genes in the domain, of the type that are not easily
assigned by matching expression patterns. On this point, of the 28
enhancers regulating multiple targets 23 target two paralogues with
similar expression patterns, which might possibly indicate that this
method of assigning enhancers to genes could be biased towards the most
visually striking patterns.

Finally, they do some characterization of the identified enhancers.
Interestingly, 36% occur inside of genes and of those 79% appear to
regulate their "host" gene. I wonder whether those enhancers which do
not regulate their host gene are very far from the promoter? It would be
interesting to see whether being intragenic makes an enhancer more
likely to regulate its host gene above and beyond simply being closer to
the TSS. I also wonder if these enhancers are also acting as alternative
promoters, as identified in `Kowalczyk et al`_. They also identify
motifs which are most characteristics of enhancers in different tissue
types, which seem to be mostly transcription factor binding sites (e.g.
Zelda consensus binding sequences, which were enriched in early
embryonic enhancers.)  By mutating these transcription factor binding
sites in their identified enhancers they are able to abrogate activity
in 10 out of 11 cases, highlighting that these sequences are necessary
for enhancer function. I think the more interesting question though is
whether they are sufficient. It would have been interesting to take a
set of motifs that together are highly predictive for enhancer function
in a particular tissue and ask how many of the candidate sequences which
did not show any enhancer activity have similar enrichment for these
motifs.

All in all, a very thought provoking paper - also kudos to the authors
for making all of their images available at `enhancers.starklab.org`_, I
think that's a very nice touch.

.. _Kowalczyk et al: http://www.sciencedirect.com/science/article/pii/S109727651100997X
.. _enhancers.starklab.org: http://enhancers.starklab.org/
