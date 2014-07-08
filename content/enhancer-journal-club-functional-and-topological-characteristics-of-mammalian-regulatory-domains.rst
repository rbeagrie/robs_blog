Enhancer Journal Club: Functional and topological characteristics of mammalian regulatory domains
#################################################################################################
:date: 2014-05-07 20:30
:author: Rob Beagrie
:tags: Enhancers, Journal Club
:slug: enhancer-journal-club-functional-and-topological-characteristics-of-mammalian-regulatory-domains

This month, I'm going to do a short journal club on a paper called
"Functional and topological characteristics of mammalian regulatory
domains", which comes from François Spitz's group at the EMBL. The
original paper can be found at
http://genome.cshlp.org/content/early/2014/01/07/gr.163519.113, and the
abstract is as follows:

    Long-range regulatory interactions have an important role in shaping
    gene expression programs. However, the genomic features that
    organize these activities are still poorly characterized. We
    conducted a large operational analysis to chart the distribution of
    gene regulatory activities along the mouse genome, using hundreds of
    insertions of a regulatory sensor. We found that enhancers
    distribute their activities along broad regions and not in a
    gene-centric manner, defining large regulatory domains. Remarkably,
    these domains correlate strongly with the recently described TADs,
    which partition the genome into distinct self-interacting blocks.
    Different features, including specific repeats and CTCF-binding
    sites, correlate with the transition zones separating regulatory
    domains, and may help to further organize promiscuously distributed
    regulatory influences within large domains. These findings support a
    model of genomic organisation where TADs confine regulatory
    activities to specific but large regulatory domains, contributing to
    the establishment of specific gene expression profiles.

In essence, the authors use the Sleeping Beauty transposon to generate
mice with a single random insertion of a LacZ reporter gene. They then
allow these single transposons to excise and re-insert themselves,
generating a cohort of integrations which tend to fall into clustered
domains due to the preference of Sleeping Beauty to transpose locally.
This allows them to compare multiple identical insertions of the
reporter gene over genomic distances up to around 2Mb. The paper
reminded me of `Bas van Steensel's TRIP paper`_ from last year, but
there are a couple of key differences. Since the TRIP paper was done in
an ES cell line, their readout had to be gene expression level. In this
paper, the use of mice allows the authors to score their insertions
based on spatial distribution of expression. For me, this is a big plus.
Most of the obvious clinical application for basic research on enhancers
and other cis-regulatory elements is in developmental disease and this
is where the contribution of enhancers to spatial or temporal patterns
of gene expression is going to be most important.

They first look to see whether insertions showing expression in a given
tissue are located close to EP300 binding sites (as a proxy for
enhancers) in that tissue. They find a significant enrichment of limb
EP300 sites around insertions which show expression in limb tissues.
Furthermore, the closer an insertion was to an enhancer with a known
spatial activity pattern, the more likely the insertion was to show a
similar expression distribution. These effects were strongest within
50kb, but could be detected up to 200kb away, which is similar to the
effect distances seen in the TRIP paper measured earlier. It would have
been nice to see some analysis of TAD boundaries here. Are all of the
enhancer/insertion pairs studied within the same TAD? If not, is it
really that enhancers work better over 50kb range than 200kb or is it
simply that there is more likely to be a TAD boundary between the pair
the further apart they are? Similarly, since here they are only
considering a subset of enhancers with known spatial activity, it would
be a good idea to check the distribution of EP300 binding sites in the
vicinity. If an insertion is 200kb away from the nearest
well-characterised enhancer, perhaps there is more likely to be another,
closer enhancer which has not been characterised.

A very interesting finding here is that insertions are more likely to
show the expression pattern of a nearby enhancer if they occur between
the enhancer and it's endogenous target gene. Insertions in the opposite
direction from the enhancer than then endogenous gene show less
concordant expression, and insertions that occur beyond a target gene
are even less concordant. The most interesting interpretation of this
result is that the gene and the insertion are competing for the
enhancer, which makes sense given the evidence that this kind of
enhancer competition can occur between endogenous genes. Here again
though, it would have been useful to check that this is not influenced
by the greater chance of enhancer/insertion pairs being separated by a
TAD boundary if they are further apart. If it is the case that these
pairs are generally within the same TAD, I wonder if one could use
something like `structured interaction matrix analysis (SIMA)`_ to check
whether enhancers make more contacts in the direction of their target
gene in Hi-C interaction maps.

In the second half of the paper, they start to examine how Hi-C TADs
might be affecting expression patterns of their reporters. They group
local clusters of insertions together and classify those with similar
expression patterns as "Regulatory Domains" and those with a change in
expression pattern as "Transition Zones". They show that 80% of
regulatory domains fall within a single TAD, whilst only 45% of
transition zones do. They confirm the significance of this result by
random permutation of the various regions. One big caveat of this
analysis is that they use the TADs from the `Dixon Hi-C paper`_, which
are from mouse ES cells. The Dixon paper presents evidence that these
TADs are largely cell type invariant, but of course there are some
changes between the cell types examined. Changes in TAD boundary
position are likely to be much more pronounced across the multiple
tissues of a mouse embryo, and I think this makes the result they find
all the more striking. Certainly it's some of the most persuasive
evidence I've seen that topological domains might help to define
regulatory modules with real developmental relevance.

The large distance scales separating insertions with very similar
expression patterns suggests that enhancer activity (either alone or in
concert) acts over broad domains. The confinement of these insertions to
single topological domains suggests that either the local structure
defines the range of this activity, or that some third party defines
both the range of activity and the topological domain. Either way, the
paradigm here would be that these domains are regulatory modules with
all or most of the tissue specific genes in the same module being
co-regulated. On the other hand, there is lots of evidence (even some
from this paper) that genes have to compete with each other for
activation by enhancers. If enhancers are largely captured by the
closest gene, where is the evolutionary role for the domain? One might
begin to answer this question by looking at the positions of genes that
are expressed in a tissue specific manner. Can liver and brain specific
genes be found in the same TAD for example, or are all tissue specific
genes within a TAD generally specific for the same tissue? If anyone has
ever done some analysis like this please let me know in the comments!

.. _Bas van Steensel's TRIP paper: http://www.cell.com/cell/abstract/S0092-8674%2813%2900889-1
.. _structured interaction matrix analysis (SIMA): http://www.nature.com/ni/journal/v13/n12/full/ni.2432.html
.. _Dixon Hi-C paper: http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3356448/
