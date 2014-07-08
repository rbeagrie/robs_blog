Enhancer Journal Club: eRNAs are required for p53-dependent enhancer activity and gene transcription.
#####################################################################################################
:date: 2013-11-25 10:03
:author: Rob Beagrie
:tags: Enhancers, Journal Club, cis regulation, DNA damage, enhancers, gene expression, P53
:slug: enhancer-journal-club-ernas-are-required-for-p53-dependent-enhancer-activity-and-gene-transcription

Back to eRNAs, and this time we're going to look at possible roles in
DNA damage control. This paper by Melo et al. is from Reuven Agami's lab
at the Netherlands Cancer Institute. The abstract is as follows:

    Binding within or nearby target genes involved in cell proliferation
    and survival enables the p53 tumor suppressor gene to regulate their
    transcription and cell-cycle progression. Using genome-wide
    chromatin-binding profiles, we describe binding of p53 also to
    regions located distantly from any known p53 target gene.
    Interestingly, many of these regions possess conserved p53-binding
    sites and all known hallmarks of enhancer regions. We demonstrate
    that these p53-bound enhancer regions (p53BERs) indeed contain
    enhancer activity and interact intrachromosomally with multiple
    neighboring genes to convey long-distance p53-dependent
    transcription regulation. Furthermore, p53BERs produce, in a
    p53-dependent manner, enhancer RNAs (eRNAs) that are required for
    efficient transcriptional enhancement of interacting target genes
    and induction of a p53-dependent cell-cycle arrest. Thus, our
    results ascribe transcription enhancement activity to p53 with the
    capacity to regulate multiple genes from a single genomic binding
    site. Moreover, eRNA production from p53BERs is required for
    efficient p53 transcription enhancement.

As always, I've posted a non-technical summary over at ScienceGist:
http://sciencegist.com/gists/209

This is a nice paper that fits with most of the other eRNA papers
published in similar areas this year. Like others, they start by
investigating the binding of a particular transcription factor (in this
case P53) outside of genes, and find that this extra-genic binding
correlates with known markers of enhancers (in this case H3K4me1,
K3K27Ac and P300). They test these regions in a luciferase assay and
find that they do indeed show enhancer activity, and crucially they show
that this enhancer activity is at least partially P53 dependent by
simultaneously knocking down P53.

They want to identify possible target genes, and they decide to do this
by identifying enhancer/promoter loops using a 4C screen. Using a
chemical called nutlin which increases stability (therefore steady state
concentration) of P53, they show that increased P53 levels increase
expression of some identified target genes. Again, as a nice control
they also do a simultaneous knock down of P53 to show that the effect of
the nutlin treatment is really P53 dependent. Not only is the
transcription of nearby genes activated by the presence of P53, but also
the production of enhancer RNAs from the enhancer loci themselves. This
leads to the most interesting experiment, where they try to investigate
whether it is the eRNA or the enhancer DNA which is responsible for
activation. They do this by creating a chimeric transcript where the
eRNA is fused to 24 copies of MS2 RNA. They can then tether this RNA to
a luciferase reporter using an MS2-CP:GAL4 fusion protein. This
tethering does indeed seem to increase the transcription of the
luciferase, and activation is not seen when a mutated transcript is
used. This is a really nice result, but much of the activation effect is
observable even when no MS2-CP:GAL4 fusion protein is added. This
appears to indicate that the presence of the eRNA in the nucleus
activates the expression of the luciferase even when it is not
physically present at the luciferase promoter, which I personally can't
make sense of. The authors merely say that *"The remaining
MS2-CP-independent transcriptional activation can be attributed to the
overexpression of the eRNA-MS2 in the nucleus."* - so perhaps I am
missing something very obvious here...

Finally, they tie the eRNA producing regions back to a functional
effect. One of the primary functions of P53 is to arrest the cell cycle
following DNA damage, so they expose the cell to ionizing radiation
whilst simultaneously knocking down the eRNA. This experiment shows that
knock down of the P53 induced eRNA allows a partial bypass of the normal
cell cycle arrest, although of course the effect is not as dramatic as
knocking down P53 itself.

All in all, this is a very interesting paper that provided one of the
first insights into a functional role for eRNAs. My feeling at the
moment is that the slew of papers about eRNAs this year have
demonstrated an important function for eRNAs but even taken together,
the evidence for a cis-acting mechanism as opposed to eRNAs being
another class of trans-acting ncRNAs is not yet air-tight.
