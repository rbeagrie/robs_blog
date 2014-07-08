Enhancer (sort of) Journal Club: Detection and replication of epistasis influencing transcription in humans
###########################################################################################################
:date: 2014-04-03 08:44
:author: Rob Beagrie
:category: Enhancers, Journal Club
:slug: enhancer-sort-of-journal-club-detection-and-replication-of-epistasis-influencing-transcription-in-humans

I thought I would write a short journal club on a paper that I really
enjoyed reading recently. It isn't as directly related to enhancers as
previous papers I've covered, but I think it has some interesting
implications for the field. The paper is called "Detection and
replication of epistasis influencing transcription in humans" and comes
from Peter Visscher's lab at the University of Queensland. The original
paper can be found at:
http://www.nature.com/nature/journal/vaop/ncurrent/full/nature13005.html
and the abstract is as follows:

    Epistasis is the phenomenon whereby one polymorphism's effect on a
    trait depends on other polymorphisms present in the genome. The
    extent to which epistasis influences complex traits and contributes
    to their variation is a fundamental question in evolution and human
    genetics. Although often demonstrated in artificial gene
    manipulation studies in model organisms, and some examples have been
    reported in other species, few examples exist for epistasis among
    natural polymorphisms in human traits. Its absence from empirical
    findings may simply be due to low incidence in the genetic control
    of complex traits, but an alternative view is that it has previously
    been too technically challenging to detect owing to statistical and
    computational issues. Here we show, using advanced computation and a
    gene expression study design, that many instances of epistasis are
    found between common single nucleotide polymorphisms (SNPs). In a
    cohort of 846 individuals with 7,339 gene expression levels measured
    in peripheral blood, we found 501 significant pairwise interactions
    between common SNPs influencing the expression of 238 genes (P <
    2.91 × 10(-16)). Replication of these interactions in two
    independent data sets showed both concordance of direction of
    epistatic effects (P = 5.56 × 10(-31)) and enrichment of interaction
    P values, with 30 being significant at a conservative threshold of P
    < 9.98 × 10(-5). Forty-four of the genetic interactions are located
    within 5 megabases of regions of known physical chromosome
    interactions (P = 1.8 × 10(-10)). Epistatic networks of three SNPs
    or more influence the expression levels of 129 genes, whereby one
    cis-acting SNP is modulated by several trans-acting SNPs. For
    example, MBNL1 is influenced by an additive effect at rs13069559,
    which itself is masked by trans-SNPs on 14 different chromosomes,
    with nearly identical genotype-phenotype maps for each cis-trans
    interaction. This study presents the first evidence, to our
    knowledge, for many instances of segregating common polymorphisms
    interacting to influence human traits.

The study is a sort of spiritual cousin of the recent explosion of
Genome Wide Association Studies (GWAS). In a normal GWAS study, one
measures variations in DNA sequence (generally single nucleotide
changes, or SNPs) and looks for correlations to an aspect of phenotype,
for example susceptibility to a disease, or expression of a certain
gene. Generally, these studies only have the statistical power to ask
whether a certain sequence variant has an independent effect on the
outcome - i.e. does having an A instead of a T at position x lead to an
increased chance of heart disease? Recently, it has become clear that
many of the sequence variants identified in these studies may actually
be changes in the sequence of cis-regulatory regions such as enhancers
(for a nice review on this, see Sakabe, Savic and Nobrega 2012 -
http://genomebiology.com/2012/13/1/238). In this paper, the authors are
looking for pairwise SNP interactions associated with heritable gene
expression. In other words, "having an A instead of a T at position x
increases expression of this gene, but only if you also have a C instead
of a G at position y".

What they find in the course of their study is (for me) super
interesting. They find 501 of these pairwise interactions, where 26 are
cases in which both SNPs lie within 1Mb of the promoter (the authors
call these cis-cis acting), 13 are cases in which both SNPs are farther
than 1Mb from the promoter (trans-trans) and 462 are cases in which one
of the SNPs is within 1Mb and the other is not (cis-trans). Of course,
the caveat with this and all studies using SNP arrays is that the SNP
you observe may not have a functional effect, and may only be
genetically linked to a functional sequence variant by virtue of being
close by it in the genome.

I find it very striking that they find so many interactions over 1Mb
away. One clear interpretation of the data is that the trans acting SNPs
are actually some form of distal enhancer or repressor. Indeed, the
authors present evidence that these SNPs are significantly enriched
within 5mb of long-range interactions detected by Hi-C. If this is true,
it would involve a huge expansion of the set of currently known
ultra-long range regulatory elements, as in the current state of
knowledge only a handful of enhancers that act over distances greater
than 1Mb have been characterized. One other clear interpretation is that
these SNPs actually control the expression of other genes, and it is the
gene product that regulates the activity of the cis-SNP. It would be
interesting to test whether SNPs which did not show an independent
effect on the expression of the gene to which they are epistatic had
independent effects on the expression of any other gene. My reading of
the paper is that they did not do this (although I could be missing
something), but in either case they only analyzed probes that mapped to
RefSeq genes and would therefore be missing any regulation that might be
mediated through non coding RNA expression.

In any case, it is interesting that at least some of the cis-trans
interactions they detect may be enhancer/promoter pairs. In this case,
the implication would be that the effect of a particular enhancer
sequence can actually be dependent on the sequence of the promoter that
it controls. Currently, many enhancers are identified or verified
through luciferase assays, where we test the ability of a DNA sequence
to affect the transcription of the luciferase gene. I think this finding
certainly highlights that these assays may be more sensitive to the
choice of promoter than perhaps was previously thought. Conversely, they
identify a large number of cases where the trans-SNP has a masking
effect on the cis-SNP. In other words there is a cis-SNP which is
associated with decreased expression of the gene, but the effect is not
observed in the presence of the trans-SNP. This possibly points to some
redundancy in the system, by which these regulatory elements serve to
maintain the correct expression level of the gene in the presence of
deleterious promoter mutations. This would mean that one could not
observe the effect of these regulatory elements by deleting them.

All in all, I think this is a really nice paper and certainly highlights
a lot of issues that deserve some more thought and research.
