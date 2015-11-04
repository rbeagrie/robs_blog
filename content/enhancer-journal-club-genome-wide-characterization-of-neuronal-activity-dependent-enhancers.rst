Enhancer Journal Club: Genome-wide identification and characterization of functional neuronal activity–dependent enhancers
##########################################################################################################################
:date: 2014-10-01 16:10
:author: Rob Beagrie
:tags: Enhancers, Journal Club, Neurons, FOS
:slug: enhancer-journal-club-genome-wide-characterization-of-neuronal-activity-dependent-enhancers

I noticed a nice paper this week in Nature Neuroscience from Michael
Greenberg's lab at Harvard Medical School. The paper discusses the
identification of enhancers in neurons which are activated (or deactivated)
when those neurons are stimulated by membrane de-polarization. The original
paper can be found at:
http://www.nature.com/neuro/journal/vaop/ncurrent/full/nn.3808.html

The abstract is as follows:

    Experience-dependent gene transcription is required for nervous system
    development and function. However, the DNA regulatory elements that control
    this program of gene expression are not well defined. Here we characterize the
    enhancers that function across the genome to mediate activity-dependent
    transcription in mouse cortical neurons. We find that the subset of enhancers
    enriched for monomethylation of histone H3 Lys4 (H3K4me1) and binding of the
    transcriptional coactivator CREBBP (also called CBP) that shows increased
    acetylation of histone H3 Lys27 (H3K27ac) after membrane depolarization of
    cortical neurons functions to regulate activity-dependent transcription. A
    subset of these enhancers appears to require binding of FOS, which was
    previously thought to bind primarily to promoters. These findings suggest that
    FOS functions at enhancers to control activity-dependent gene programs that are
    critical for nervous system function and provide a resource of functional
    cis-regulatory elements that may give insight into the genetic variants that
    contribute to brain development and disease.

It has been known for a while that neurons will respond to stimulation by
activating the transcription of certain genes - this is known as
"activity–dependent transcription". Whilst the signalling pathway leading from
changes in membrane potential to the transcription of early-response genes has
been the focus of a few studies, the way in which these few early-response
genes activate a broader transcriptional program is not well understood. The
authors postulated that the early-response might lead to activation of
enhancers, which lie upstream of the broader transcriptional changes in
stimulated cells.

They first set out to identify enhancers which are activated or deactivated
after membrane depolarization by KCl treatment of cortical neurons. They
perform ChIP-seq of H3K27Ac/me3, H3K4me1/3, CBP and RNA Pol II before and after
KCl addition, plus RNA-seq before and at 1/6 hours post depolarization. They
identify putative enhancers as CBP/H3K4me1-enriched sites >1 kb from an
annotated TSS, and found that 1468 of them (12%) showed at least a twofold
increase in H3K27Ac after depolarization, which they call "neuronal
activity–regulated enhancers".  In contrast, they only found 738 sites that
showed at least a twofold decrease. They nicely validated the neuronal
activity–regulated enhancers by showing that 14/14 tested regions showed
greater activity in a luciferase assay *after* depolarization. In contrast, no
putative enhancers with constant or decreased H3K27Ac after KCl treatment
showed higher activity in the luciferase assay following the same treatment.

So these putative enhancer regions can activate luciferase in response to
membrane depolarization, but the question remains whether they activate
endogenous genes *in vivo*. To answer this they asked whether the nearest genes
to neuronal activity–regulated enhancers also showed increases in transcription
on neuronal activation. Whilst they do show a significant increase in the
expression level of these genes, the increase is not that large. This could be
because many of the enhancer regions don't regulate the nearest gene (either
regulating a more distal gene or having no targets) or because the increase in
expression in each target gene is small. Presenting the data as a bean or box
plot of fold changes, rather than a bar chart of mean expression level could
have gone some way to answering this question.

The next obvious question is which factors might be responsible for activating
the neuronal activity–regulated enhancers. They perform a motif enrichment
analysis and find that AP-1 motif is the most highly enriched, which normally
binds FOS- and JUN-family proteins. This is nice as several of these
transcription factors are known early-response genes, but on the other hand the
AP-1 motif is normally thought of as a promoter motif and not as a component of
distal enhancers. ChIP seq for FOS protein confirmed that 96% of the identified
12,594 were at distal sites, not at promoters. Whilst this strongly implicates
FOS in the activation of these enhancers, only 42% of neuronal
activity–regulated enhancers were directly bound by FOS. That would seem to
indicate that FOS is neither necessary nor sufficient for enhancer activation
in a large number of cases. The paper does a good job of showing that FOS is
required for those enhancers where it binds, however. In a panel of eight such
enhancers tested in luciferase assays, all eight showed reduced activity if the
AP-1 binding site was mutated by a single base pair, or when cells were treated
with an shRNA against FOS.

They extend this approach genome wide by looking for genes which are
upregulated in response to membrane depolarization, but which show at least 33%
lower induction in the presence of FOS shRNA. Interestingly, only 53 of the 187
genes identified by this approach had a FOS-bound enhancer within 100kb. This
could indicate that many of the genes sensitive to FOS shRNA are indirect
targets. Alternatively, since only one shRNA is used, these genes could be
direct off-target effects or could lie downstream of off-target genes. One
interesting final possibility is that many of the activity regulated enhancers
act over distances of >100kb. Never the less, they test 14 of their 53 FOS
direct targets in the visual cortex of dark-housed mice exposed to light. 10/14
tested genes showed induction under these conditions, validating that these
genes can respond to neuronal stimulus in the intact brain.

Overall, I think it's very interesting that H3K27Ac can change quite
dramatically after only 2 hours of depolarization with KCl, and that many of
the new peaks which appear do seem to mark functional enhancers. One aspect
that could be interesting to explore is the peaks which are lost after
depolarization. The authors do perform motif analysis for these peaks, which
identified candidate TFs like Atoh1 and SRF, but a deeper investigation of how
enhancer repression might be involved in the response to neuronal stimulation
could be quite revealing.
