---
title: |
  Politics as a Flavoring Agent:\
  Moralized Demand and the Limits of Revealed Preference
author: PIATRA . INSTITUTE
date: June 2026
---

## Abstract

A consumer who will not switch phones over a country's politics will switch beer over an advertisement, and the asymmetry is usually explained by the phone costing more. This paper argues it is explained by the phones differing and the beers not. When functional quality across competing products has converged, political meaning can take over the work of differentiation, and it does so in two ways an outside observer cannot tell apart. Under sorting, politics changes which good a consumer chooses while leaving the good's experienced quality intact; under flavoring, politics changes the experience itself, so the same physical good is tasted as better when its label aligns and worse when it does not, the way a price tag moves reported pleasantness in the neural-imaging studies. The paper builds the smallest model that holds both channels and a mixture parameter, $\phi$, for how much of the political premium runs through flavoring rather than sorting. Solved over a population of 60,000 consumers in a polarized electorate, the model's first result is negative and exact: at the quality plateau the labeled market is invariant to $\phi$, so the choice data that revealed-preference analysis relies on are identical for every split between the two channels, and the political premium of $0.362$ in functional-quality units is consistent with $\phi$ anywhere in $[0, 1]$. Only a quantity the market never generates identifies the split, the within-good swing between a good's blind rating and its labeled rating, which the model fixes at $0.202$ per unit of $\phi$ and which is the design of the relabeling experiment. The second result makes the plateau quantitative. Sweeping functional dispersion locates a threshold near $\Delta F^* = 0.445$ below which politics decides the majority of contested choices, and placing ten categories on that axis reproduces the received susceptibility ordering, bottled water through cosmetics on the flavor-dominated side, phones through medical devices on the other, as an output rather than an assertion. The third result prices brand activism. Because moral contamination is negativity-dominant, with the misalignment penalty here $2.33$ times the alignment bonus, a neutral good that adopts a political position loses a centered mass-market base by $0.036$ of demand while a symmetric model gains it $0.008$, and the position pays only for a base already concentrated beyond $0.425$ toward the adopted pole, which is the large-share-brand penalty derived from the contagion asymmetry alone. The discipline running through all three results is a single refusal: to let the part of a moralized market that choice data settle, the premium, the threshold, and the activism penalty, pass for the part it cannot, the share of the premium that is taste rather than sorting, which waits on a measurement the market never makes.

## 1. The Two-Dollar Beer and the Thousand-Dollar Phone

The puzzle is ordinary and the standard explanation is wrong. A person who would never change a phone, a car, or a washing machine over the maker's politics will drop a beer, a coffee, or a razor over far less, and the difference is read off the price tag: the cheap thing is easy to abandon, the dear thing is not. The reading survives until you notice that the same person keeps the cheap things they like and abandons cheap things politics has touched, so cost is not doing the work. What separates the beer from the phone is that the phones in front of the buyer actually differ on dimensions the buyer can feel, and the beers, within a tier, do not. Where products have converged, the buyer has spare capacity to care about something other than the product, and politics is the most available something.

This is not a claim that political consumption is new or that consumers are dupes. It is a claim about where political meaning lands. A large literature already treats buying and boycotting as political participation (Stolle, Hooghe and Micheletti, 2005; Micheletti, 2003), measures how widespread it has become and who does it (Newman and Bartels, 2011; Endres and Panagopoulos, 2017), distinguishes the approach motive of the buycott from the avoidance motive of the boycott (Neilson, 2010; Kam and Deichert, 2020), and asks when a firm's public stance helps or hurts it (Vredenburg, Kapitan, Spry and Kemper, 2020; Bhagwat, Warren, Beck and Watson, 2020). The boycott in that literature is the consumer's exit, the cheapest channel of pressure when voice is costly and a substitute is at hand (Hirschman, 1970). All of it reads politics as a reason to act. The question here is narrower and, once asked, harder: when a consumer reports that the aligned beer is better, what is the word "better" measuring, and can any amount of market data tell us?

Two answers are available and they are usually fused. The first is that politics is a preference over an attribute, like sweetness or a logo, that the consumer happens to weigh; the aligned beer wins the choice but tastes the same as the other one, and the consumer would say so under questioning. Call this sorting, because it sorts buyers across goods without touching the goods. The second answer is that the politics has migrated into the taste, so the aligned beer is experienced as better, not merely chosen. Call this flavoring. The two are not rival theories of the same fact. They are two facts that produce the same market, and the paper's first business is to show they cannot be separated from the inside of one.

## 2. Why Flavoring Is Physically Possible and Empirically Hidden

That goods carry meaning beyond their function is the oldest observation in the study of consumption, from conspicuous waste as a status display (Veblen, 1899) through taste as the marker of social position (Bourdieu, 1984) to the brand as a vessel of cultural myth (Holt, 2004). Politics is a recent entrant into that symbolic layer, not a break from it. What is new is the claim this paper tests, that the meaning does not stay in the layer of signification but reaches down into the layer of experience.

The flavoring channel is not a metaphor. Beliefs about a product change the experience of consuming it, measured at the level of report and of the brain. Told that a wine costs more, subjects rate it as more pleasant and show higher activity in the orbitofrontal regions that encode experienced pleasantness, with the wine held fixed (Plassmann, O'Doherty, Shiv and Rangel, 2008). Told that a beer contains a distinctive additive before tasting, subjects like it less; told after, they do not, so the expectation rather than the chemistry moves the verdict (Lee, Frederick and Ariely, 2006). The route that takes a price cue into a taste can take a political cue the same way, and the moral-psychology literature supplies the second half of the route: moral judgments recruit the machinery of physical disgust, so a moralized object can be experienced as contaminated rather than merely disapproved of (Chapman, Kim, Susskind and Anderson, 2009; Rozin, 1999). The contamination follows the laws of sympathetic magic, by which contact with a tainted source transfers the taint to an object that is physically unchanged (Rozin, Millman and Nemeroff, 1986). A beer can come to taste politically dirty in the same sense a glass can taste of the cockroach that briefly sat in it.

The contamination half of the route is stronger than the endorsement half, and the asymmetry has a name. Negativity dominance is the regularity that a negative element combined with a positive one yields an outcome more negative than the parts would predict, sharpest in the domain of contagion, where a drop of sewage spoils a barrel of wine but a drop of wine does nothing for a barrel of sewage (Rozin and Royzman, 2001; Baumeister, Bratslavsky, Finkenauer and Vohs, 2001). Carried into consumption it predicts that political misalignment should spoil a good more than alignment can sweeten it, and the marketing evidence agrees: disagreement with a brand's stand damages attitudes more than agreement repairs them (Mukherjee and Althuizen, 2020), and divisive stances are riskier for brands with more to lose (Hydock, Paharia and Blair, 2020). The model below builds the asymmetry in as a single ratio and lets it generate those findings rather than assuming them.

Politics enters here as a credence quality, a property the buyer cannot verify even after consuming the good, the class of attribute that the economics of information has studied since quality became uncertain and unobservable (Akerlof, 1970; Nelson, 1970). Ethical labels of this kind do move real purchases and not just stated attitudes, as a multistore field experiment on fair-trade coffee showed (Hainmueller, Hiscox and Sequeira, 2015). What this paper adds is upstream of the purchase: the credence claim does not only tip the choice, it can re-enter as the taste. The flavoring channel is therefore distinct from cause-related marketing, where a purchase funds a cause (Varadarajan and Menon, 1988), and from commodity activism, where resistance is routed through consumption (Banet-Weiser, 2012); both change what buying means, neither claims to change what the good is like in the mouth.

So flavoring is real and asymmetric. The difficulty is that none of it shows up where economists usually look. Revealed preference reads choices, and a choice records that the aligned beer won, not whether it won because it was preferred-as-an-attribute or because it was tasted-as-better. Stated satisfaction does not rescue the distinction, because a satisfied buyer can be reporting the pleasure of the taste or the pleasure of the alignment, and the word "satisfaction" does not separate them. The separation requires a measurement the market does not make: the same physical good, rated once with its label and once without. The expectation experiments make that measurement. The next sections show it is not one option among several but the only thing that identifies the mechanism at all.

## 3. The Model

A category holds substitutable goods. Consumer $i$ sits at a political position $x_i$ on a one-dimensional axis, drawn from a polarized electorate in which half the population clusters near $-\mu$ and half near $+\mu$, the affective sorting that the work on polarization documents (Iyengar, Lelkes, Levendusky, Malhotra and Westwood, 2019). Good $j$ has functional quality $F_j$ and, if it is politicized, a position $p_j$. Alignment between a consumer and a good is the Gaussian kernel

$$a_{ij} = \exp\!\left(-\frac{(x_i - p_j)^2}{2\tau^2}\right) \in (0, 1],$$

one when the consumer sits on the good's position and decaying to zero with distance. The political charge the good holds for the consumer is a bonus when aligned net of a penalty when not,

$$\pi_{ij} = \lambda_{+}\, a_{ij} - \lambda_{-}\,(1 - a_{ij}),$$

with $\lambda_{-} \ge \lambda_{+}$ the negativity-dominance asymmetry. A fully aligned consumer sees $\pi = \lambda_{+}$; a fully misaligned one sees $\pi = -\lambda_{-}$. The magnitudes are illustrative and anchored to the published effect sizes rather than estimated for any market: $\lambda_{+} = 0.15$ sits in the range of the price-on-pleasantness and label-on-taste shifts, and $\lambda_{-} = 0.35$ sets the contamination at $2.33$ times the bonus, in the band the negativity-dominance work reports.

The two channels differ in where $\pi$ goes. Under sorting it is expressive: it enters the utility that drives choice but not the hedonic quality the consumer would report for the good in hand. This is the orthodox reading and it is well founded, because identity is a standard argument of the utility function (Akerlof and Kranton, 2000), a good is a bundle of characteristics one of which can be its politics (Lancaster, 1966), and brands hold knowledge and relationships that drive differential response (Keller, 1993; Fournier, 1998), serving as material for the self and its reference groups (Escalas and Bettman, 2005; Bhattacharya and Sen, 2003; Tajfel and Turner, 1979). Under flavoring it is hedonic: it multiplies experienced quality, so the good is tasted as $F_j(1 + \pi_{ij})$. A mixture parameter $\phi \in [0, 1]$ is the share of the political charge that runs through flavoring. Labeled total utility, the quantity choice maximizes, is

$$U^{\text{lab}}_{ij} = F_j + \pi_{ij}\,\big(\phi F_j + (1 - \phi) F_0\big),$$

where $F_0$ is the reference quality of the category. The flavoring part scales with the good's own quality $F_j$; the sorting part is a fixed expressive weight scaled by the category reference $F_0$. One channel rides the quality; the other sits beside it. Stripped of its label, the good carries no expressive charge and only the hedonic channel survives, so its blind rating is

$$Q^{\text{blind}}_{ij} = F_j, \qquad Q^{\text{lab}}_{ij} = F_j\,(1 + \phi\,\pi_{ij}).$$

The whole argument lives in the gap between these last two lines, and in one feature of the utility: when the competing goods have converged to a common quality $F_j = F_0$, the bracket in $U^{\text{lab}}$ collapses to $F_0$ for every $\phi$, and total utility stops depending on $\phi$ at all.

## 4. The Market Cannot See the Mechanism

Set both goods at the plateau, $F_R = F_L = F_0$, on opposite political poles, and solve the labeled market over the 60,000 consumers. The result is exact and is the paper's center. Total labeled utility is

$$U^{\text{lab}}_{ij} = F_0\,(1 + \pi_{ij}),$$

with no $\phi$ in it. Every consumer's choice, and therefore every market share, every revealed-preference estimate, every diff-in-diff on the labeled data, is identical whether the political premium runs entirely through sorting ($\phi = 0$), entirely through flavoring ($\phi = 1$), or any mixture between. Sweeping $\phi$ across the grid, the market share of either good moves by $0$ to the precision of the arithmetic, and adding Gumbel choice noise leaves a residual dispersion of under $0.001$, confirming the invariance is a property of the model rather than of exact tie-breaking. The political premium itself, the labeled willingness-to-pay gap between a consumer's better- and worse-matched good, is pinned at $0.362$ in $F_0$ units, and it is pinned at that value for every $\phi$.

What identifies $\phi$ is the within-good swing the market never produces. The difference between a good's labeled and blind hedonic rating is $F_0\,\phi\,\pi_{ij}$, linear in $\phi$ through the origin, running from $0$ at $\phi = 0$ to $0.202$ at $\phi = 1$ for an aligned consumer. That swing is what a relabeling experiment measures when it serves one physical good twice, once with the aligning label and once blind, and reads the change in the rating. It is unavailable from any number a market generates, because a market never serves the same good under two labels to the same buyer and records the hedonic difference. The decomposition is therefore unidentified in the regime the phenomenon names: at the plateau the premium is real, its size is recoverable, and the fraction of it that is flavoring rather than sorting can be anything in $[0, 1]$ until someone runs the blind test.

![Left: market share of one good as the flavoring share $\phi$ sweeps from $0$ to $1$ at the quality plateau. The share does not move; the labeled market is exactly invariant to $\phi$, so revealed preference cannot recover the split between sorting and flavoring. Right: the within-good blind-versus-labeled hedonic swing for an aligned consumer, which is linear in $\phi$ and runs from $0$ to $0.202$. This is the only quantity that identifies $\phi$, and it is the measurement a market never makes and a relabeling experiment does.](../simulation/output/figures/identification.png){width=100%}

The reason the failure is total here and not elsewhere is the collapse of the bracket. Away from the plateau, when $F_R \ne F_L$, the $\phi$-weighted term no longer cancels and choice begins to respond to $\phi$, so the mixture becomes weakly identified from how buyers trade quality against politics. The identification problem and the plateau condition are the same fact seen twice: politics is most powerful, and least legible, where products have stopped differing.

## 5. The Good-Enough Plateau, as a Threshold

Let the two goods differ in quality. Good $R$ sits at the favorable pole with quality $F_0 + \Delta F / 2$, good $L$ at the opposite pole with $F_0 - \Delta F / 2$, so the functionally better good is always $R$ and politics is decisive for a consumer exactly when the political charge pulls them to the worse good $L$. Sweeping the functional dispersion $\Delta F$ from zero traces how far quality has to spread before function reclaims the choice. At $\Delta F = 0$ the politics-determined share is $0.501$, which is just the aligned-to-$L$ half of the electorate; it falls as the quality gap widens and the $L$-aligned consumers defect one by one to the better good. The share crosses below a quarter of the market, half of the politically susceptible subpopulation, at $\Delta F^{*} = 0.445$. Below that dispersion politics decides most contested choices; above it, function does.

Placing categories on the $\Delta F$ axis turns the threshold into the susceptibility typology the field has assembled by hand, now as model output. Using stipulated, ordinal estimates of how much competing products in a category actually differ on dimensions a buyer can feel, the ten categories partition five and five. Bottled water ($\Delta F = 0.03$, politics-determined share $0.497$), beer, coffee, fashion basics, and cosmetics ($0.20$, share $0.459$) fall on the flavor-dominated side; phones ($0.48$, share $0.110$), cars, televisions, industrial tools, and medical devices ($0.78$, share $0.000$) fall on the other. The ordering is not imposed on the model; it follows from where each category's quality dispersion sits relative to the single threshold the sweep locates, and it matches the received intuition that politics can own a beer and cannot own a pacemaker.

![Politics-determined choice share against functional dispersion $\Delta F$. The share falls from the polarized-electorate value near $0.50$ at the plateau to zero once quality differences are large enough to reclaim the choice, crossing the threshold $\Delta F^{*} = 0.445$ (dashed). Ten categories are placed on the axis at stipulated, ordinal dispersions; the five below the threshold are flavor-dominated (red), the five above it function-dominated (green), reproducing the received susceptibility typology as an output of the single threshold rather than as a hand-built table.](../simulation/output/figures/plateau.png){width=100%}

The threshold gives a mechanism to a condition the marketing literature names but leaves qualitative. Commoditization is described as the drift toward homogeneity, price sensitivity, and low switching cost (Reimann, Schilke and Thomas, 2010), and the good-enough plateau is the point at which improving products overshoot what buyers can use (Christensen, 1997); the model turns that point into the dispersion $\Delta F^{*}$ at which politics changes from a tiebreaker into the decider. Visibility belongs on the same axis, since identity-relevant goods are the ones consumed in public where a label can be read by others (Berger and Heath, 2007), and a fuller model would let visibility shift the threshold rather than fixing it.

The threshold also disciplines the theory's reach. Politics seasons a good; it does not cook one. A category with real, felt performance gaps does not become politically flavorable by being shouted at, because the buyer who can feel the difference spends it on the difference. The plateau is a precondition, and the model makes the precondition a number rather than a mood.

## 6. The Activism Trap

The first two results take the goods' politics as given. The third asks what happens when a neutral good acquires one. A brand at no political position serves a base distributed around some mean alignment; it adopts a position, here the $+1$ pole, and each customer's demand moves by the political charge $\pi$ now attached to the good. Because the charge is negativity-dominant, the alienated tail of the base loses more than the aligned tail gains, and whether the move pays depends entirely on where the base already sits.

For a mass-market brand, whose base is centered on the electorate because being mass-market means drawing from all of it, adoption is a loss. Demand falls by $0.036$ when the brand politicizes, and the loss is a creature of the asymmetry alone: rerun the same adoption with a symmetric charge, $\lambda_{-} = \lambda_{+}$, and the centered brand instead gains $0.008$. The penalty is not that half the country disagrees, which a symmetric model would wash out, but that the half that disagrees withdraws harder than the half that approves leans in. Adoption pays only for a base already concentrated toward the adopted pole: the demand change crosses zero at a base mean of $0.425$, so a brand whose customers sit beyond that point gains and every broader brand loses. A challenger whose base is the pole itself gains $0.021$; a brand that picks the pole opposite its base loses $0.138$. This is the large-share-brand result, that visible incumbents are punished for stances that reward niche entrants, derived from the contagion asymmetry rather than stipulated.

![Change in a brand's demand when a neutral good adopts the $+1$ political position, against the brand's existing base mean. The curve is negative for a centered mass-market base (red point, $-0.036$), crosses zero at a base mean of $0.425$ (dashed), and is positive only for a base already concentrated near the adopted pole. Under a symmetric charge the centered brand would instead gain; the penalty is a property of negativity dominance, not of disagreement as such.](../simulation/output/figures/asymmetry.png){width=100%}

The size of the trap tracks the one parameter that sets it. As the negativity-dominance ratio climbs from $1.0$ to $4.0$, the centered brand's demand change falls from $+0.008$ to $-0.101$ and the break-even base mean rises from $-0.15$ to past the edge of the electorate, so that at strong contamination no broad brand can adopt a position and come out ahead. The model thus reads the Bud Light episode and its kind not as a marketing error to be corrected by better execution but as the expected value of putting a pole's politics on a good whose base spans the center, in a category, beer, that the plateau result already marks as maximally flavorable. The execution was incidental. The geometry was adverse before the campaign ran.

## 7. The Cases, Read Through the Model

The model does its work here by sorting the public cases along its two axes, the sorting-versus-flavoring split and the discipline-versus-ritual split, and the cases resist the lazy reading in both directions. Bud Light is the clean instance of the activism trap: a commodity at the plateau, a centered mass base, a pole-ward stance, and a collapse that substitution made costless to the boycotters, the apparatus then stable because the alienated half had a dozen interchangeable lagers to defect to. Nike and Kaepernick is the mirror case. The base was not centered, an apparel brand already concentrated among younger urban consumers, so the same maneuver that broke a centered beer brand consolidated a polarized shoe brand, as the break-even result predicts for a base past the threshold.

The discipline-versus-ritual axis separates the boycotts the model treats as flavoring rituals from those with a material object, a distinction the boycott literature has drawn from several directions: by participant motivation (Klein, Smith and John, 2004), by the social dilemma of withholding consumption (Sen, Gürhan-Canli and Morwitz, 2001), by media leverage rather than lost revenue (Friedman, 1999), and by the conditions under which a firm actually responds (King, 2008). The Israel-related consumer boycotts of fast food and coffee run largely through symbolic association and local franchise actions rather than supply-chain complicity, in categories the plateau marks as flavorable, and their effect concentrates where ideological alignment is densest, which is the signature of an identity ritual that stabilizes a group, a brand community defined as much by what it refuses as by what it buys (Muniz and O'Guinn, 2001), rather than a sanction that moves a firm. The corporate exits from Russia sit at the other end: the object was real, the cost to the firm was a balance-sheet write-down rather than a consumer's free substitution, and the pressure operated on the producer's books rather than the consumer's palate, so the flavoring model does not apply and should not be stretched to. Ben and Jerry's occupies the contested middle, where an actual distribution policy in occupied territory, a material object, was carried by a brand whose politics was already a core ingredient rather than a campaign, which is why the dispute reached corporate governance rather than the checkout line. The model's contribution to these cases is not a verdict on any of them but a grammar that keeps the symbolic and the material from being argued as if they were the same move.

## 8. The Cover That Vagueness Gave

The first result is the one to state most carefully, because it cuts against the instrument it uses. It does not show that political premiums are illusions, or that flavoring is the truth behind a sorting facade. It shows that the two are observationally equivalent on market data at the plateau, so that any claim of the form "consumers in this category genuinely taste their politics" is, on revealed-preference evidence alone, unfalsifiable, and the honest move is to run the relabeling experiment rather than to read the market harder. The decomposition is identifiable, but only by a measurement outside the market, and naming that measurement is the positive content of a negative result.

The numbers carry that content and none beyond it. The model is illustrative and not estimated: the $0.362$ premium, the $0.445$ threshold, the $0.036$ penalty are properties of a stipulated parameterization chosen to sit in the band of the cited effect sizes, and none is a measurement of beer, of cosmetics, or of any firm. The category dispersions that produce the typology are ordinal stipulations, so the partition demonstrates that a single threshold can generate the received ordering, not that bottled water's dispersion is truly $0.03$. And flavoring is not a synonym for fraud or for false consciousness. A consumer who tastes the politics is having a real experience, the orbitofrontal cortex does not distinguish the pleasure a price cue buys from the pleasure the wine buys, and a boycott that targets a genuine supply-chain harm is doing political economy whatever it also does to the palate. Whether a given act of moralized consumption is taste, tribute, or justice is a question the model sharpens and does not close.

What the model removes is the cover that vagueness gave. The claim that politics has become part of what consumers buy is true and, stated that way, empty, because it is satisfied by sorting and by flavoring alike and asks for no evidence either could fail. Made precise, it splits into a part the market settles, the premium and the threshold and the activism penalty, and a part the market cannot reach, the share of the premium that is flavoring, which waits on an experiment. The two-dollar beer and the thousand-dollar phone differ in their politics because they differ in everything else first.

## References

Akerlof, G. A. (1970). The market for lemons: Quality uncertainty and the market mechanism. *Quarterly Journal of Economics*, 84(3), 488–500.

Akerlof, G. A., and Kranton, R. E. (2000). Economics and identity. *Quarterly Journal of Economics*, 115(3), 715–753.

Banet-Weiser, S. (2012). *Authentic™: The Politics of Ambivalence in a Brand Culture*. New York University Press.

Baumeister, R. F., Bratslavsky, E., Finkenauer, C., and Vohs, K. D. (2001). Bad is stronger than good. *Review of General Psychology*, 5(4), 323–370.

Berger, J., and Heath, C. (2007). Where consumers diverge from others: Identity signaling and product domains. *Journal of Consumer Research*, 34(2), 121–134.

Bhagwat, Y., Warren, N. L., Beck, J. T., and Watson, G. F. (2020). Corporate sociopolitical activism and firm value. *Journal of Marketing*, 84(5), 1–21.

Bhattacharya, C. B., and Sen, S. (2003). Consumer-company identification: A framework for understanding consumers' relationships with companies. *Journal of Marketing*, 67(2), 76–88.

Bourdieu, P. (1984). *Distinction: A Social Critique of the Judgement of Taste* (R. Nice, Trans.). Harvard University Press.

Chapman, H. A., Kim, D. A., Susskind, J. M., and Anderson, A. K. (2009). In bad taste: Evidence for the oral origins of moral disgust. *Science*, 323(5918), 1222–1226.

Christensen, C. M. (1997). *The Innovator's Dilemma: When New Technologies Cause Great Firms to Fail*. Harvard Business School Press.

Endres, K., and Panagopoulos, C. (2017). Boycotts, buycotts, and political consumerism in America. *Research & Politics*, 4(4), 1–9.

Escalas, J. E., and Bettman, J. R. (2005). Self-construal, reference groups, and brand meaning. *Journal of Consumer Research*, 32(3), 378–389.

Fournier, S. (1998). Consumers and their brands: Developing relationship theory in consumer research. *Journal of Consumer Research*, 24(4), 343–373.

Friedman, M. (1999). *Consumer Boycotts: Effecting Change Through the Marketplace and the Media*. Routledge.

Hainmueller, J., Hiscox, M. J., and Sequeira, S. (2015). Consumer demand for fair trade: Evidence from a multistore field experiment. *Review of Economics and Statistics*, 97(2), 242–256.

Hirschman, A. O. (1970). *Exit, Voice, and Loyalty: Responses to Decline in Firms, Organizations, and States*. Harvard University Press.

Holt, D. B. (2004). *How Brands Become Icons: The Principles of Cultural Branding*. Harvard Business School Press.

Hydock, C., Paharia, N., and Blair, S. (2020). Should your brand pick a side? How market share determines the impact of corporate political advocacy. *Journal of Marketing Research*, 57(6), 1135–1151.

Iyengar, S., Lelkes, Y., Levendusky, M., Malhotra, N., and Westwood, S. J. (2019). The origins and consequences of affective polarization in the United States. *Annual Review of Political Science*, 22, 129–146.

Kam, C. D., and Deichert, M. (2020). Boycotting, buycotting, and the psychology of political consumerism. *Journal of Politics*, 82(1), 72–88.

Keller, K. L. (1993). Conceptualizing, measuring, and managing customer-based brand equity. *Journal of Marketing*, 57(1), 1–22.

King, B. G. (2008). A political mediation model of corporate response to social movement activism. *Administrative Science Quarterly*, 53(3), 395–421.

Klein, J. G., Smith, N. C., and John, A. (2004). Why we boycott: Consumer motivations for boycott participation. *Journal of Marketing*, 68(3), 92–109.

Lancaster, K. J. (1966). A new approach to consumer theory. *Journal of Political Economy*, 74(2), 132–157.

Lee, L., Frederick, S., and Ariely, D. (2006). Try it, you'll like it: The influence of expectation, consumption, and revelation on preferences for beer. *Psychological Science*, 17(12), 1054–1058.

Micheletti, M. (2003). *Political Virtue and Shopping: Individuals, Consumerism, and Collective Action*. Palgrave Macmillan.

Mukherjee, S., and Althuizen, N. (2020). Brand activism: Does courting controversy help or hurt a brand? *International Journal of Research in Marketing*, 37(4), 772–788.

Muniz, A. M., and O'Guinn, T. C. (2001). Brand community. *Journal of Consumer Research*, 27(4), 412–432.

Neilson, L. A. (2010). Boycott or buycott? Understanding political consumerism. *Journal of Consumer Behaviour*, 9(3), 214–227.

Nelson, P. (1970). Information and consumer behavior. *Journal of Political Economy*, 78(2), 311–329.

Newman, B. J., and Bartels, B. L. (2011). Politics at the checkout line: Explaining political consumerism in the United States. *Political Research Quarterly*, 64(4), 803–817.

Plassmann, H., O'Doherty, J., Shiv, B., and Rangel, A. (2008). Marketing actions can modulate neural representations of experienced pleasantness. *Proceedings of the National Academy of Sciences*, 105(3), 1050–1054.

Reimann, M., Schilke, O., and Thomas, J. S. (2010). Toward an understanding of industry commoditization: Its nature and role in evolving marketing competition. *International Journal of Research in Marketing*, 27(2), 188–197.

Rozin, P. (1999). The process of moralization. *Psychological Science*, 10(3), 218–221.

Rozin, P., and Royzman, E. B. (2001). Negativity bias, negativity dominance, and contagion. *Personality and Social Psychology Review*, 5(4), 296–320.

Rozin, P., Millman, L., and Nemeroff, C. (1986). Operation of the laws of sympathetic magic in disgust and other domains. *Journal of Personality and Social Psychology*, 50(4), 703–712.

Sen, S., Gürhan-Canli, Z., and Morwitz, V. (2001). Withholding consumption: A social dilemma perspective on consumer boycotts. *Journal of Consumer Research*, 28(3), 399–417.

Stolle, D., Hooghe, M., and Micheletti, M. (2005). Politics in the supermarket: Political consumerism as a form of political participation. *International Political Science Review*, 26(3), 245–269.

Tajfel, H., and Turner, J. C. (1979). An integrative theory of intergroup conflict. In W. G. Austin and S. Worchel (Eds.), *The Social Psychology of Intergroup Relations* (pp. 33–47). Brooks/Cole.

Varadarajan, P. R., and Menon, A. (1988). Cause-related marketing: A coalignment of marketing strategy and corporate philanthropy. *Journal of Marketing*, 52(3), 58–74.

Veblen, T. (1899). *The Theory of the Leisure Class: An Economic Study of Institutions*. Macmillan.

Vredenburg, J., Kapitan, S., Spry, A., and Kemper, J. A. (2020). Brands taking a stand: Authentic brand activism or woke washing? *Journal of Public Policy & Marketing*, 39(4), 444–460.
