Enhancer Journal Club: Activating RNAs associate with Mediator to enhance chromatin architecture and transcription
##################################################################################################################
:date: 2013-09-04 18:39
:author: Rob Beagrie
:category: Enhancers, Journal Club
:slug: enhancer-journal-club-activating-rnas-associate-with-mediator-to-enhance-chromatin-architecture-and-transcription

Another paper for the enhancers/eRNAs Journal Club series. This time
I've been reading Lai et al. which was published in February from Ramin
Shiekhattar's lab. Following on from the back to back Li and Lam papers
in June, I've decided to go back to this paper because it is (to my
knowledge) the first to show a link between expression of a non-coding
RNA and the formation of enhancer/promoter contacts.

I've posted a non-technical summary of this paper over at Science Gist:
http://sciencegist.com/doi/10.1038/nature11884

The abstract for the paper is as follows:

    Recent advances in genomic research have revealed the existence of a
    large number of transcripts devoid of protein-coding potential in
    multiple organisms. Although the functional role for long non-coding
    RNAs (lncRNAs) has been best defined in epigenetic phenomena such as
    X-chromosome inactivation and imprinting, different classes of
    lncRNAs may have varied biological functions. We and others have
    identified a class of lncRNAs, termed ncRNA-activating (ncRNA-a),
    that function to activate their neighbouring genes using a
    cis-mediated mechanism. To define the precise mode by which such
    enhancer-like RNAs function, we depleted factors with known roles in
    transcriptional activation and assessed their role in RNA-dependent
    activation. Here we report that depletion of the components of the
    co-activator complex, Mediator, specifically and potently diminished
    the ncRNA-induced activation of transcription in a heterologous
    reporter assay using human HEK293 cells. In vivo, Mediator is
    recruited to ncRNA-a target genes and regulates their expression. We
    show that ncRNA-a interact with Mediator to regulate its chromatin
    localization and kinase activity towards histone H3 serine 10. The
    Mediator complex harbouring disease displays diminished ability to
    associate with activating ncRNAs. Chromosome conformation capture
    confirmed the presence of DNA looping between the ncRNA-a loci and
    its targets. Importantly, depletion of Mediator subunits or ncRNA-a
    reduced the chromatin looping between the two loci. Our results
    identify the human Mediator complex as the transducer of activating
    ncRNAs and highlight the importance of Mediator and activating ncRNA
    association in human disease.

The paper starts with a small siRNA screen of possible factors that may
mediate activating non-coding RNA effects on neighbouring gene
transcription. The single hit shown is for Med12, a component of
mediator complex, but they go on to show that several other components
of the complex also have the same effect. Once they have confirmed that
knocking out a mediator component also affects the transcription of the
genes they propose are under the control of this ncRNA, they also show
that knocking down the ncRNA itself reduces the occupancy of mediator at
the promotors of this gene. This is a nice indication that the ncRNA
might be somehow delivering the mediator complex to the target genes. On
top of this, they use a kinase assay to show that two of their
non-coding RNAs actually appear to stimulate the kinase activity of
mediator towards H3S10, at least in vitro. Here it maybe would have been
nice to have a ChIP of H3S10p levels in vivo, just to show that this
mechanism may also be relevant in the biological system.

The really interesting part of the paper, at least for me, is figure 4.
Here they use siRNAs to knock down either mediator or the ncRNA and show
a loss of DNA looping between the ncRNA locus and the neighbouring gene.
Could this indicate that the ncRNA is somehow involved in forming these
chromatin loops? Unfortunately, it is a little difficult to tease apart
the causality in this particular experiment, as they have shown that
knocking down either mediator or the ncRNA causes a reduction in
transcription of the gene. The looping could therefore be a consequence
of this transcriptional activity and not be directly caused by the
ncRNA/mediator interaction. Alternatively, this could all be working
through a cohesin related pathway since cohesin seems to be involved in
stabilising these sorts of looping interactions and can also interact
with mediator. This would be interesting as the authors show in figure 1
that knocking down SMC1L or NIPBL doesn't seem to impair the ability of
the activating ncRNAs to activate luciferase transcription.

Taken together with the papers from the Rosenfeld and Glass labs, this
paper helps to demonstrate that there is some relationship between
non-coding/enhancer RNAs and enhancer/promoter looping that we really
don't understand yet.

Next in the Journal Club series: Hah et al. 2013 in *Genome Research*,
which very much contradicts the results of these three papers.
