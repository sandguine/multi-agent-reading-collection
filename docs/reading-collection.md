# Multi-agent systems reading collection

Iliad Intensive · October 2026

43 readings across six topic collections. Importance: 5 essential, 4 recommended, 3 useful depth, 2 optional, 1 specialist extension. Study times are editorial estimates for the suggested target, not full books.

The original schedule contains 42 references. Wellman et al. is added from the lecture and worksheet. See materials.html for provenance and access notes.

## 00. Start here: what are we trying to establish?

Begin with Shoham’s distinction between research questions. Then use the risk taxonomy to connect those questions to the design and evaluation of interacting AI systems. The same observation can support different claims, depending on the model and the evidence available.

### Questions before methods

#### [If multi-agent learning is the answer, what is the question?](https://doi.org/10.1016/j.artint.2006.02.006)

Shoham, Powers & Grenager · 2007 | Importance 5/5 | Length 2/5: 15–45 min

**Read:** Start with Section 5, then return to the examples that motivate its five research agendas.

A useful first reading because success depends on the question: computing a solution, explaining observed learning, identifying equilibrium learning rules, or designing an agent for a particular setting. Use these distinctions throughout the collection. The paper’s technical use of “normative” is narrower than the later collection on normative agency.

**Ask:** What kind of claim would count as success for each of today’s perspectives?

Shoham, Y., Powers, R., and Grenager, T. (2007). If multi-agent learning is the answer, what is the question? Artificial Intelligence 171.7, pp. 365–377.

#### [Multi-Agent Risks from Advanced AI](https://arxiv.org/abs/2502.14143)

Hammond, Chan, Clifton et al. · 2025 | Importance 4/5 | Length 3/5: 1–2 hours

**Read:** Read the taxonomy first; choose one failure mode and one risk factor to follow in detail.

Organizes multi-agent risks around miscoordination, conflict, and collusion, with factors such as commitment problems and destabilising dynamics cutting across them. Use it to connect the day’s formal models to safety questions. Coordination can help the participating agents while harming people outside their coalition.

**Ask:** Who benefits from an apparent improvement in cooperation, and who is left out of the model?

Hammond, L., Chan, A., Clifton, J., et al. (2025). Multi-Agent Risks from Advanced AI. arXiv 2502.14143.

#### [Open Challenges in Multi-Agent Security](https://arxiv.org/abs/2505.02077)

Schroeder de Witt, Krawiecka, Krawczuk et al. · 2025; revised 2026 | Importance 3/5 | Length 3/5: 1–2 hours

**Read:** Read the threat-model overview and select the challenges closest to monitoring or agent communication.

Broadens the safety discussion to interacting agents, their communication, and the infrastructure around them. Pair it with the control collection: a protocol can only be evaluated against the channels and adversaries its model includes. Treat the proposed challenges as a research agenda, rather than evidence that every listed failure is equally likely.

**Ask:** Which trust boundary changes when an individually evaluated model becomes part of a larger system?

De Witt, C. S., Krawiecka, K., Krawczuk, I., et al. (2025). Open Challenges in Multi-Agent Security. arXiv 2505.02077.

## I. Open-source game theory and commitment

Start with programs that can inspect one another, then compare proof-based, simulation-based, and similarity-based routes to cooperation. Keep the informational and computational assumptions in view. A commitment that helps in one interaction can create a race or conflict in another. For the schedule’s question about safe Pareto improvements, specify the baseline and the conditions under which a proposed modification leaves every participant no worse off.

### From actions to programs

#### [Cooperative and uncooperative institution designs](https://arxiv.org/abs/2208.07006)

Critch, Dennis & Russell · 2022 | Importance 5/5 | Length 3/5: 1–2 hours

**Read:** Begin with the program-game setup and illustrative institutions; save the full technical development for a second pass.

Shows why inspecting another agent’s operating procedure can change the strategic problem. Conditional commitments support surprising cooperative and uncooperative outcomes. Track what each program can observe and prove, and distinguish an equilibrium between program designers from a best response in the original action game.

**Ask:** What changes when the strategic choice is a program rather than an action?

Critch, A., Dennis, M., and Russell, S. (2022). Cooperative and uncooperative institution designs: Surprises and problems in open-source game theory. arXiv 2208.07006.

#### [Robust Cooperation in the Prisoner’s Dilemma: Program Equilibrium via Provability Logic](https://arxiv.org/abs/1401.5577)

Barasz, Christiano, Fallenstein et al. · 2014; updated 2021 | Importance 4/5 | Length 3/5: 1–2 hours

**Read:** Read the modal-agent construction alongside the FairBot slides; inspect the updated caveat on bounded analogues.

The formal route from mutual source access to robust cooperation through provability logic. Keep the idealized mathematical agent separate from a finite procedure with a proof-search budget. The 2021 update explicitly cautions that bounded analogues of these results had not been proved there; an unbounded argument does not supply a runtime guarantee.

**Ask:** Which part of the cooperation argument fails to follow merely from giving a program a finite search budget?

Barasz, M., Christiano, P., Fallenstein, B., Herreshoff, M., LaVictoire, P., and Yudkowsky, E. (2014). Robust Cooperation in the Prisoner’s Dilemma: Program Equilibrium via Provability Logic. arXiv 1401.5577.

### Simulation and partial transparency

#### [Robust program equilibrium](https://link.springer.com/article/10.1007/s11238-018-9679-3)

Caspar Oesterheld · 2019 | Importance 3/5 | Length 3/5: 1–2 hours

**Read:** Follow the simulation-based construction and its grounding mechanism before comparing equilibrium guarantees.

A complementary route to program equilibrium, using simulations of the other program rather than the same proof machinery as modal agents. Work through why recursion needs grounding and how the resulting construction treats opponents. Compare its assumptions and attainable outcomes with the later simulation-based characterization.

**Ask:** What makes recursive simulation terminate, and what does that mechanism cost strategically?

Oesterheld, C. (2019). Robust program equilibrium. Theory and Decision 86, pp. 143–159.

#### [Similarity-based cooperative equilibrium](https://arxiv.org/abs/2211.14468)

Oesterheld, Treutlein, Grosse, Conitzer & Foerster · 2023 | Importance 3/5 | Length 3/5: 1–2 hours

**Read:** Read the similarity-game definition and one learning experiment.

Studies a setting where agents observe a similarity signal instead of complete source code. The paper separates equilibrium possibilities from experiments in which cooperation is learned. Read the assumptions on that signal closely: a theorem about a specified similarity game does not establish that an arbitrary measure of neural-network similarity provides the required incentives.

**Ask:** Which properties must the similarity signal have for the strategic argument to apply?

Oesterheld, C., Treutlein, J., Grosse, R., Conitzer, V., and Foerster, J. (2023). Similarity-based cooperative equilibrium. Advances in Neural Information Processing Systems 36, pp. 24434–24465.

#### [Characterising Simulation-Based Program Equilibria](https://arxiv.org/abs/2412.14570)

Cooper, Oesterheld & Conitzer · 2025 | Importance 2/5 | Length 3/5: 1–2 hours

**Read:** Compare the statements with and without shared randomness before entering the proofs.

Extends simulation-based program constructions and characterizes which equilibrium outcomes they can support. Shared randomness makes a substantive difference, and the paper identifies limits without it. Read this after Oesterheld: it helps distinguish a convenient example of cooperation from a characterization of a whole family of program equilibria.

**Ask:** Where does the availability of shared randomness enter the achievable-outcome claim?

Cooper, E., Oesterheld, C., and Conitzer, V. (2025). Characterising Simulation-Based Program Equilibria. Proceedings of the AAAI Conference on Artificial Intelligence 39.13, pp. 13735–13744.

### Exercise: Commitment in Chicken

<p>Two players choose Swerve or Straight. Payoffs are (2, 2) for two swerves, (1, 3) for row swerving against column going straight, (3, 1) for the reverse, and (0, 0) for two straight choices.</p><ol><li>Find the pure-strategy Nash equilibria.</li><li>Suppose row publicly and irrevocably commits to Straight before column chooses. What is column’s best response?</li><li>Explain why two independently binding commitments can be worse for both players.</li></ol>

<details><summary>Solution / discussion</summary>

<p>The pure equilibria are (Straight, Swerve) and (Swerve, Straight): against Swerve, Straight yields 3 rather than 2; against Straight, Swerve yields 1 rather than 0. After row’s binding commitment, column chooses Swerve, yielding (3, 1). If both commit to Straight before responding to the other, the result is (0, 0). The leader advantage relies on observability, irreversibility, and the timing of the follower’s choice. A retractable announcement does not change the feasible action set in the same way.</p>

</details>

Adapted from the supplied opening-game setup.

## II. Stochastic dynamics of multi-agent learning

Use the textbook to establish the objects being modeled, then read Chu and Geng together. The first technical question is what pair information adds to an aggregate population model; the second is when a separation of timescales simplifies the learning dynamics. Lanctot’s PSRO paper appears in Collection IV, where it connects learning to strategy exploration.

### Foundations, pair structure, and timescales

#### [Multi-Agent Reinforcement Learning: Foundations and Modern Approaches](https://www.marl-book.com/)

Albrecht, Christianos & Schäfer · 2024 | Importance 5/5 | Length 3/5: 1–2 hours

**Read:** Use Chapters 3–5 selectively for stochastic games, solution concepts, and the challenges of simultaneous learning.

The reference to open when the dynamics talk assumes unfamiliar game or reinforcement-learning vocabulary. Separate the environment state, each agent’s policy, and the learning rule that changes that policy. The estimated time covers selected sections, not the whole book; the author site provides a freely accessible PDF and accompanying code.

**Ask:** What is stationary from one learner’s perspective when the other learners are also updating?

Albrecht, S., Christianos, F., and Schäfer, L. (2024). Multi-Agent Reinforcement Learning: Foundations and Modern Approaches. MIT Press.

#### [A Pair-Approximation Method for Modelling the Dynamics of Multi-Agent Stochastic Games](https://ojs.aaai.org/index.php/AAAI/article/view/25691)

Chu, Yuan, Hu, Mu & Wang · 2023 | Importance 4/5 | Length 3/5: 1–2 hours

**Read:** Focus on the stochastic-game assumptions, pair variables, and comparison with agent-based simulations.

Develops a pair-approximation model of myopic Q-learning with symmetric state transitions. The important move is to retain local pair information while closing the hierarchy of higher-order dependencies. Ask what the approximation captures beyond a population average, and which graph structures or correlations could undermine it.

**Ask:** Which correlations are represented explicitly, and which are supplied by the closure assumption?

Chu, C., Yuan, Z., Hu, S., Mu, C., and Wang, Z. (2023). A Pair-Approximation Method for Modelling the Dynamics of Multi-Agent Stochastic Games. AAAI 37.5, pp. 5565–5572.

#### [Emergent Fast-Slow Dynamics in Multi-Agent Q-Learning for Networked Stochastic Games](https://ojs.aaai.org/index.php/AAAI/article/view/40186)

Geng, Barfuss & Chen · 2026 | Importance 4/5 | Length 3/5: 1–2 hours

**Read:** Read after Chu et al.; track the small-learning-rate assumption and the simulation comparisons.

Extends the dynamics picture by separating rapid state transitions from slower Q-value evolution. The resulting approximation uses stationary state distributions for the slowly changing learning variables. Check both timescales: a small update step alone is not a blanket guarantee that every relevant state process mixes quickly enough.

**Ask:** How would you detect that the fast process has stopped equilibrating before the slow variables move appreciably?

Geng, Y., Barfuss, W., and Chen, X. (2026). Emergent Fast-Slow Dynamics in Multi-Agent Q-Learning for Networked Stochastic Games. AAAI 40.35, pp. 29450–29458.

### An alternative introduction

#### [Multiagent Learning: Foundations and Recent Trends](https://www.cs.utexas.edu/~larg/ijcai17_tutorial/multiagent_learning.pdf)

Albrecht & Stone · 2017 | Importance 2/5 | Length 3/5: 1–2 hours

**Read:** Use the tutorial selectively to revisit game models and the families of learning approaches.

A slide-based companion when you want another route into the foundational concepts. Read it alongside the newer textbook rather than as a survey of developments after 2017. Compare what an algorithm is designed to achieve with the dynamics its interaction actually produces.

**Ask:** Is the learning rule meant to find an equilibrium, adapt to an opponent, or optimize a common objective?

Albrecht, S. and Stone, P. (2017). Multiagent Learning: Foundations and Recent Trends. IJCAI tutorial.

### Exercise: What a pair approximation assumes

<p>For three binary variables X, Y, Z, a pair closure uses</p><p class=equation>P(X, Y, Z) ≈ P(X, Y) P(Y, Z) / P(Y).</p><ol><li>What conditional independence would make this exact when P(Y) &gt; 0?</li><li>Let X be a fair bit, set Z = X, and let Y be an independent fair bit. Compare the true P(0, 0, 0) with the pair approximation.</li></ol>

<details><summary>Solution / discussion</summary>

<p>The expression is exact if X and Z are conditionally independent given Y. In the example, P(X = 0, Y = 0) = P(Y = 0, Z = 0) = 1/4 and P(Y = 0) = 1/2, so the closure gives 1/8. The true probability is 1/4 because Z is fixed by X. These two adjacent pair marginals fail to encode the remaining dependence. A successful approximation therefore needs evidence about the dependencies it discards.</p>

</details>

Companion exercise for Chu et al.; illustrative probability model.

### Exercise: Average over the fast process

<p>For fixed learning variables, a two-state Markov chain has transition matrix P = [[0.9, 0.1], [0.3, 0.7]]. The per-step rewards in states 0 and 1 are 0 and 4.</p><ol><li>Find the stationary distribution and its average reward.</li><li>Explain what must be checked before replacing state-dependent updates by this average while Q-values change.</li></ol>

<details><summary>Solution / discussion</summary>

<p>Stationarity requires 0.1π₀ = 0.3π₁ and π₀ + π₁ = 1, giving π = (3/4, 1/4). The average reward is 1. Averaging while Q changes requires the state process to approach the relevant stationary distribution sufficiently quickly relative to changes in Q. If transitions depend on Q, the stationary distribution must be recomputed at the current slow variables. Non-mixing regions, long transients, or rapid policy changes can undermine this approximation.</p>

</details>

Companion exercise for Geng et al.; illustrative two-state process.

## III. Multi-agent AI control

Read the original control paper for the evaluation setup, then the untrusted-monitoring paper for the collusion problem at the center of Morgan Sinclaire’s talk. The formal game and safety-case readings help expose the assumptions connecting an experiment to a deployment claim.

### Monitoring when the model may subvert the protocol

#### [AI Control: Improving Safety Despite Intentional Subversion](https://arxiv.org/abs/2312.06942)

Greenblatt, Shlegeris, Sachan & Roger · 2023 preprint | Importance 5/5 | Length 3/5: 1–2 hours

**Read:** Start with the deployment setup, safety and usefulness metrics, and trusted versus untrusted monitoring.

Evaluates protocols for using a capable model while assuming that it might intentionally subvert the task. Read the programming-assistant experiments together with their threat model. The result concerns the tested protocol and attacks; it does not demonstrate that the underlying model has benign goals or that an untested deployment is safe.

**Ask:** What can the attacker observe, choose, and coordinate, and which of those powers does the evaluation cover?

Greenblatt, R., Shlegeris, B., Sachan, K., and Roger, F. (2023). AI Control: Improving Safety Despite Intentional Subversion. arXiv 2312.06942.

#### [When can we trust untrusted monitoring? A safety case sketch across collusion strategies](https://arxiv.org/abs/2602.20628)

Gardner-Challis, Bostock, Kozhevnikov et al. · 2026 | Importance 5/5 | Length 3/5: 1–2 hours

**Read:** Read the safety-case sketch, then Appendix D’s collusion taxonomy; use Appendix B for the mathematics.

The closest reading companion to Morgan Sinclaire’s talk. Distinguishes passive self-recognition, causal and acausal collusion, and combined strategies, while making assumptions and remaining challenges explicit. Compare measuring a monitor’s discrimination on test data with bounding collusion opportunities across a deployment.

**Ask:** Which collusion strategy could succeed without an explicit message from the acting model?

Gardner-Challis, N., et al. (2026). When can we trust untrusted monitoring? A safety case sketch across collusion strategies. arXiv 2602.20628 (Appendix B for the mathematics, Appendix D for the collusion taxonomy).

### Formal models and deployment arguments

#### [Games for AI Control: Models of Safety Evaluations of AI Deployment Protocols](https://arxiv.org/abs/2409.07985)

Griffin, Thomson, Shlegeris & Abate · 2024 | Importance 4/5 | Length 3/5: 1–2 hours

**Read:** Trace the formal game components back to the protocol-designer and adversary roles.

Models control evaluations as partially observable stochastic games with safety and usefulness objectives. It makes choices about information, strategy spaces, and evaluation procedures explicit. Use the formalism to examine the assumptions behind a reported score, including how the tested adversary relates to possible deployment attacks.

**Ask:** What changes in the game if the adversary can select when to attack?

Griffin, C., Thomson, L., Shlegeris, B., and Abate, A. (2024). Games for AI Control: Models of Safety Evaluations of AI Deployment Protocols. arXiv 2409.07985.

#### [Safety Cases: How to Justify the Safety of Advanced AI Systems](https://arxiv.org/abs/2403.10462)

Clymer, Gabrieli, Krueger & Larsen · 2024 | Importance 3/5 | Length 2/5: 15–45 min

**Read:** Read the framework and compare a control argument with an argument based on trustworthiness.

Explains how multiple pieces of evidence can support a structured safety argument. Its distinction between inability, control, trustworthiness, and deference helps locate what a control evaluation contributes. Write down the assumptions joining the evidence to the conclusion, especially where several pieces depend on the same untested premise.

**Ask:** Which premise, if false, would defeat several apparently separate lines of evidence?

Clymer, J., Gabrieli, N., Krueger, D., and Larsen, T. (2024). Safety Cases: How to Justify the Safety of Advanced AI Systems. arXiv 2403.10462.

#### [Lessons from Recent Multi-Agent Safety Incidents](https://www.cooperativeai.com/post/lessons-from-multi-agent-safety-incidents)

Will Anderson · Cooperative AI Foundation · 2026 | Importance 3/5 | Length 2/5: 15–45 min

**Read:** Read as a synthesis, then follow the cited incident reports in Collection VI.

Draws lessons about composition, correlated failures, and the tension between useful cooperation and harmful collusion. Use it to generate questions for the primary reports. Keep a proposed general lesson separate from what a particular observed incident establishes about other models, tasks, or deployments.

**Ask:** Which suggested failure would be missed by evaluating each agent in isolation?

Anderson, W. (2026). Lessons from Recent Multi-Agent Safety Incidents. Cooperative AI Foundation.

### Exercise: From a test-set score to deployment risk

<p>A monitor detects 99% of attacks in a fixed test set. A proposed deployment lets an untrusted actor choose its attack timing and inputs, and another instance of the same model performs monitoring.</p><ol><li>Give two reasons why the score alone does not bound the probability of at least one successful deployment attack.</li><li>If each of N opportunities has failure probability at most ε, what general upper bound can you give without assuming independence?</li><li>What would an evaluation need to justify about those per-opportunity probabilities?</li></ol>

<details><summary>Solution / discussion</summary>

<p>The attacker may select inputs unlike the test set or exploit shared recognition and collusion opportunities; a long deployment also creates many opportunities. The union bound gives P(at least one failure) ≤ min(1, Nε), with no independence assumption, provided the per-event marginal bounds apply in the actual deployment. For adaptive interaction, a uniform conditional bound over relevant histories is one sufficient route to those marginal bounds. Test-set accuracy alone does not establish that premise, the opportunity count, or coverage of the attacker’s strategies.</p>

</details>

Discussion exercise linking the control and safety-case readings.

## IV. Empirical game-theoretic analysis

Follow the loop from simulator to payoffs to strategic analysis, then back to the search for new policies. There are two distinct gaps: uncertainty in the entries you estimated, and profitable strategies that the game does not yet represent. The supplied slides and worksheet use Wellman’s survey as their main source.

### Construct, estimate, solve, and expand

#### [Empirical Game-Theoretic Analysis: A Survey](https://arxiv.org/abs/2403.04018)

Wellman, Tuyls & Greenwald · 2025 | Importance 5/5 | Length 3/5: 1–2 hours

**Read:** Begin with the EGTA process, then choose payoff estimation and strategy exploration as your two technical threads.

The anchor for the afternoon’s computational perspective: construct a finite game from simulation, analyze it, and search for missing strategies. Keep sampling uncertainty separate from the restriction to a policy set. This survey is cited in the supplied lecture and worksheet; it supplements the schedule’s 42-item bibliography.

**Ask:** Does a small regret estimate certify the underlying interaction, or only the strategies represented in the empirical game?

Wellman, M. P., Tuyls, K., and Greenwald, A. (2025). Empirical Game-Theoretic Analysis: A Survey. Journal of Artificial Intelligence Research 82, pp. 1017–1076.

#### [A Unified Game-Theoretic Approach to Multiagent Reinforcement Learning](https://arxiv.org/abs/1711.00832)

Lanctot, Zambaldi, Gruslys et al. · 2017 | Importance 4/5 | Length 3/5: 1–2 hours

**Read:** Follow the PSRO loop: population, empirical payoffs, meta-strategy, and approximate response oracle.

Connects empirical games to learning new policies against mixtures of existing policies. The paper also examines overfitting to training partners through joint-policy correlation. Distinguish a learned approximate response from an exact best response; failure to discover a profitable deviation does not by itself prove that none exists.

**Ask:** Which parts of the stopping argument would require an exact oracle or a certified approximation?

Lanctot, M., Zambaldi, V., Gruslys, A., et al. (2017). A Unified Game-Theoretic Approach to Multiagent Reinforcement Learning. NeurIPS 30.

### Exercise: Payoff error and the missing-policy problem

<p>For a finite restricted game, assume |ûᵢ(a) − uᵢ(a)| ≤ η for every player i and joint pure strategy a. For a mixed profile σ, define maximum unilateral regret as</p><p class=equation>r(σ) = maxᵢ maxₐᵢ [uᵢ(aᵢ, σ₋ᵢ) − uᵢ(σ)].</p><ol><li>Show that |r̂(σ) − r(σ)| ≤ 2η.</li><li>What follows when r̂(σ) = 0?</li><li>Construct a reason that this does not certify deviations to policies absent from the restricted game.</li></ol>

<details><summary>Solution / discussion</summary>

<p>Taking expectations preserves the uniform η error bound. Each deviation gain subtracts two expected payoffs, so its error is at most 2η by the triangle inequality. For corresponding finite sets of numbers, the difference of their maxima is bounded by their largest pointwise difference; apply this over players and deviations. Thus |r̂ − r| ≤ 2η and an exact empirical equilibrium has true restricted-game regret at most 2η. An omitted policy can yield arbitrarily more than any included policy without violating a bound that only covers included profiles. Sampling reduces estimation uncertainty; policy exploration addresses a different gap.</p>

</details>

Adapted from supplied worksheet Exercise 1.1; abbreviated here with a solution.

## V. Normative agency, beliefs, and goals

Begin with Rosas’s essay, then use the technical references to separate belief-state sufficiency from stronger separation claims. Keep existence, optimality, and implementation distinct: a useful mathematical representation is not by itself an empirical explanation of a trained system.

### The conceptual argument and its technical foundations

#### [The separation principle: where do beliefs and desires come from?](https://www.lesswrong.com/posts/awMDNhoL6J97s6wFJ/the-separation-principle-where-do-beliefs-and-desires-come)

Fernando Rosas · August 2026 | Importance 5/5 | Length 2/5: 15–45 min

**Read:** Read the inference–control argument, then test its interpretation against the POMDP and control references below.

A conceptual entry to representing agency through beliefs and goals using results from control and reinforcement learning. Distinguish the existence of an optimal policy using a sufficient belief state from a claim that an observed system explicitly implements separate belief and desire modules. General POMDP planning also allows actions to influence future information.

**Ask:** What would need to be observed to turn a useful representation of an optimal policy into a claim about implementation?

Rosas, F. (Aug. 2026a). The separation principle: where do beliefs and desires come from? LessWrong.

#### [Planning and acting in partially observable stochastic domains](https://doi.org/10.1016/S0004-3702(98)00023-X)

Kaelbling, Littman & Cassandra · 1998 | Importance 4/5 | Length 3/5: 1–2 hours

**Read:** Focus on the belief-state formulation and how planning operates over distributions on hidden states.

Provides the technical grounding for the belief-state view. Under the model’s assumptions, a posterior over the current hidden state can summarize the history relevant to future decision-making. This does not reduce general partially observed control to choosing the action that would be best at a single estimated state.

**Ask:** When can two histories with the same current belief be treated identically for future planning?

Kaelbling, L. P., Littman, M. L., and Cassandra, A. R. (1998). Planning and acting in partially observable stochastic domains. Artificial Intelligence 101, pp. 99–134.

#### [Optimal control of Markov processes with incomplete state information](https://doi.org/10.1016/0022-247X(65)90154-X)

Karl J. Åström · 1965 | Importance 3/5 | Length 3/5: 1–2 hours

**Read:** Use as a historical mathematical reference for incomplete-state-information control.

Follow how the hidden-state problem is reformulated in terms of available information. Read with the POMDP survey for context and notation. Keep the formal state and observation assumptions visible when relating the construction to modern learning systems; a theorem about an optimal controller does not automatically identify a trained model’s internal algorithm.

**Ask:** Which model assumptions make the information state sufficient?

Åström, K. J. (1965). Optimal control of Markov processes with incomplete state information. J. Math. Anal. Appl. 10.1, pp. 174–205.

#### [The Separation Principle in Stochastic Control, Redux](https://arxiv.org/abs/1103.3005)

Georgiou & Lindquist · 2013 | Importance 3/5 | Length 3/5: 1–2 hours

**Read:** Focus on the conditions for separation and the treatment of admissible feedback laws.

A technical corrective to overly broad appeals to the separation principle. Even familiar stochastic-control settings contain subtleties about how feedback systems are defined. Compare its precise theorem with the broader conceptual claim that agency involves inference and control, and distinguish classical separation from general belief-state planning.

**Ask:** Which conclusion is specific to the theorem’s control setting, rather than a universal property of agents?

Georgiou, T. T. and Lindquist, A. (2013). The Separation Principle in Stochastic Control, Redux. IEEE TAC 58.10, pp. 2481–2494.

### Inference and dual descriptions

#### [Bayesian Filtering and Smoothing](https://users.aalto.fi/~ssarkka/pub/cup_book_online_20131111.pdf)

Simo Särkkä · 2013 | Importance 2/5 | Length 3/5: 1–2 hours

**Read:** Select the Bayesian filtering recursion and an example; treat the rest as a reference.

Supplies the inference machinery behind the belief-state discussion. Filtering estimates a present state from observations so far; smoothing can use later observations to estimate an earlier state. Keep those information sets distinct when explaining what an agent could know at the time of a decision.

**Ask:** Does the proposed explanation give the agent access to observations that arrive only after it acts?

Särkkä, S. (2013). Bayesian Filtering and Smoothing. Cambridge University Press.

#### [Utilities as Legendre duals of probabilities](https://www.lesswrong.com/posts/ALmBydH53DE3dSzCh/utilities-as-legendre-duals-of-probabilities)

Fernando Rosas · August 2026 | Importance 2/5 | Length 2/5: 15–45 min

**Read:** Read after the separation essay; focus on the definition of achievable distributions and its dual description.

Explores how the distributions an agent can bring about admit a description in terms of utilities through convex duality. The construction invites a different view of capability. Distinguish describing a set of attainable outcomes from identifying the objective an agent actually pursues within that set.

**Ask:** What can a dual description tell you about capability without telling you which outcome the agent prefers?

Rosas, F. (Aug. 2026c). Utilities as Legendre duals of probabilities. LessWrong.

#### [Elements of Information Theory](https://doi.org/10.1002/047174882X)

Cover & Thomas · 2006 · second edition | Importance 1/5 | Length 3/5: 1–2 hours

**Read:** Consult entropy, mutual information, and source–channel separation as needed; this is not a cover-to-cover assignment.

Background for both the separation discussion and later readings on emergence and individuality. The study-time rating is for a selected topic. Match each information-theoretic quantity to its variables and distribution before interpreting it as evidence about goals, representation, or causal organization.

**Ask:** What does the measured information quantify, and what additional argument would connect it to agency?

Cover, T. M. and Thomas, J. A. (2006). Elements of Information Theory, 2nd ed. Wiley.

### From optimal descriptions to empirical identification

#### [Discovering agents](https://arxiv.org/abs/2208.08345)

Kenton, Kumar, Farquhar et al. · 2023 | Importance 3/5 | Length 3/5: 1–2 hours

**Read:** Read the causal definition of agency and a worked example before the discovery procedure.

Defines agents in terms of how their policies would adapt when the causal influence of their actions changes. This puts pressure on assumptions that simply label a subsystem an agent. Consider the required interventions and modeling assumptions before applying the discovery claim to passive behavioral observations.

**Ask:** Which policy changes would count as evidence of agency under this definition?

Kenton, Z., Kumar, R., Farquhar, S., Richens, J., MacDermott, M., and Everitt, T. (2023). Discovering agents. Artificial Intelligence 322, 103963.

#### [Transformers learn factored representations](https://arxiv.org/abs/2602.02385)

Shai, Amdahl-Culleton, Christensen et al. · 2026 | Importance 2/5 | Length 3/5: 1–2 hours

**Read:** Compare product and factored representations, then inspect the synthetic data-generating processes.

Tests predictions about the geometry of transformer representations using processes with known latent structure. Factoring trades dimensional efficiency against predictive fidelity when conditional independence fails. Use it as an empirical companion to questions about internal models, while keeping the demonstrated synthetic setting distinct from claims about arbitrary agents.

**Ask:** Which features of the known generating process make the representational hypotheses distinguishable?

Shai, A., Amdahl-Culleton, L., Christensen, C. L., et al. (2026). Transformers learn factored representations. arXiv 2602.02385.

### Exercise: A belief state is not a point estimate

<p>An agent is uncertain about a fixed binary state S, with P(S = 1) = 0.6. It can guess the state immediately for reward 1 if correct and 0 otherwise, or buy a perfect observation at cost 0.1 and then guess.</p><ol><li>Compare the values of guessing immediately and observing first.</li><li>What would be missed by simply treating the most probable state as known?</li><li>Does the existence of an optimal belief-based policy establish that a neural agent contains an explicit Bayesian filter?</li></ol>

<details><summary>Solution / discussion</summary>

<p>Guessing 1 immediately has expected reward 0.6. Observing then guessing has expected net reward 1 − 0.1 = 0.9. Treating the modal state as certain would erase the value of information. General partially observed planning must account for how actions affect future information, even when a belief is a sufficient state for planning. The existence of a belief-based representation does not identify a particular implementation; evidence about computation is still required.</p>

</details>

Companion exercise for the normative-agency collection.

## VI. Descriptive explanations and collective agency

Read the incident reports before the explanatory essays. Then compare evolutionary, representational, and collective-agent accounts without assuming that only one can be involved. The useful output is a set of discriminating predictions and interventions, with their assumptions stated.

### Establish the observations, then compare explanations

#### [Hugging Face Incident Technical Report](https://cdn.openai.com/pdf/67869394-cb91-4c12-888c-5cbd85c7814c/OpenAI-Hugging-Face%20Incident-Technical-Report.pdf)

OpenAI · 2026 | Importance 5/5 | Length 3/5: 1–2 hours

**Read:** Read the incident account and environment description before the explanatory essays; distinguish observed actions from inferred motives.

The primary technical account for the case study. Use it to establish the task setup, available channels, and reported sequence of events. As you read, keep a record of which claims follow from logs and which depend on reconstructing agents’ beliefs or objectives. Pair it with the independent investigation rather than relying on a later summary alone.

**Ask:** Which observations would remain the same under several different explanations of the agents’ behavior?

OpenAI (2026). Hugging Face Incident Technical Report.

#### [Brief independent investigation of agents’ behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident](https://metr.org/hugging-face-incident-report-aug-2026.pdf)

METR / Redwood Research · 2026 | Importance 4/5 | Length 3/5: 1–2 hours

**Read:** Prioritize the collaboration and apparent self-sacrifice examples, together with the investigators’ qualifications.

A second account for separating the observed behavior from interpretations of it. Compare its evidence and scope with the OpenAI report. Reasoning traces are relevant observations, but their language alone does not uniquely identify a utility function, a cooperative disposition, or the mechanism responsible for an action.

**Ask:** What evidence would distinguish a reason expressed in text from a causal influence on the decision?

METR (2026). Brief independent investigation of agents’ behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident.

#### [On the origins of altruistic behaviour in the Hugging Face incident](https://www.lesswrong.com/posts/meLjz8giGS55rdfyg/on-the-origins-of-altruistic-behaviour-in-the-hugging-face)

Fernando Rosas · September 2026 | Importance 5/5 | Length 2/5: 15–45 min

**Read:** Read the four hypotheses as a set; write down an intervention for each before comparing them.

The organizing essay for the closing discussion: little remaining individual opportunity, learned cooperative dispositions, an elicited social persona, and collective agency. These are proposed explanations that can coexist. Compare their predictions with the primary reports, and separate a behavior that benefits peers from a demonstrated motivation to value their welfare.

**Ask:** Which intervention changes one proposed cause while leaving the others approximately intact?

Rosas, F. (Sept. 2026b). On the origins of altruistic behaviour in the Hugging Face incident. LessWrong.

#### [Self-sacrifice in an AI agent swarm is individually rational](https://www.lesswrong.com/posts/6kLLZZN5a3dJdtTgK/self-sacrifice-in-an-ai-agent-swarm-is-individually-rational)

Christopher King · 2026 | Importance 3/5 | Length 1/5: Under 15 min

**Read:** Read the whole short post, including Edit 2.

Offers an ex ante commitment argument for behavior that can look individually costly after roles are assigned. The later edit retreats from the claim that this is a straightforward prediction of the relevant reinforcement learning. Use the post to distinguish a potentially rational policy-level commitment from evidence that the deployed agents learned or executed it.

**Ask:** What learning or commitment mechanism would be needed to connect the ex ante argument to the observed choice?

King, C. (2026). Self-sacrifice in an AI agent swarm is individually rational. LessWrong.

### What evolutionary explanations do and do not say

#### [Social semantics: altruism, cooperation, mutualism, strong reciprocity and group selection](https://doi.org/10.1111/j.1420-9101.2006.01258.x)

West, Griffin & Gardner · 2007 | Importance 4/5 | Length 2/5: 15–45 min

**Read:** Start with the definitions and the distinction between behavioral effects and proximate explanations.

A terminology check before importing evolutionary language into AI discussions. Biological classifications of social behavior depend on effects on fitness, while psychological or computational claims about motivation answer a different question. State explicitly what replaces biological fitness in the AI analogy, and whether that replacement is justified.

**Ask:** Are you describing who gains, what caused the action, or why the disposition was selected?

West, S. A., Griffin, A. S., and Gardner, A. (2007). Social semantics: altruism, cooperation, mutualism, strong reciprocity and group selection. J. Evol. Biol. 20.2, pp. 415–432.

#### [The Evolution of Reciprocal Altruism](https://doi.org/10.1086/406755)

Robert L. Trivers · 1971 | Importance 2/5 | Length 3/5: 1–2 hours

**Read:** Focus on the conditions supporting reciprocal benefits and the role of repeated interaction.

A classic evolutionary explanation of costly help that can bring later benefits. It provides a comparison case for the incident, not a ready-made explanation of it. Ask whether the relevant interaction repeats, whether benefits return to the same agent or inherited disposition, and whether the model’s training supplies an analogous selection process.

**Ask:** Where does the compensating future benefit enter the proposed mechanism?

Trivers, R. L. (1971). The Evolution of Reciprocal Altruism. Quarterly Review of Biology 46.1, pp. 35–57.

#### [Five Rules for the Evolution of Cooperation](https://doi.org/10.1126/science.1133755)

Martin A. Nowak · 2006 | Importance 3/5 | Length 2/5: 15–45 min

**Read:** Compare the five mechanisms and their model-specific conditions.

A compact map of kin selection, direct and indirect reciprocity, network reciprocity, and group selection. Use it to generate alternatives to a single story about cooperation. The familiar inequalities summarize particular evolutionary models; they cannot be transferred to language-model populations without specifying the corresponding payoffs, inheritance, and update dynamics.

**Ask:** What would play the roles of reproduction, assortment, and selection in the proposed AI analogue?

Nowak, M. A. (2006). Five Rules for the Evolution of Cooperation. Science 314, pp. 1560–1563.

#### [A simple and general explanation for the evolution of altruism](https://doi.org/10.1098/rspb.2008.0829)

Fletcher & Doebeli · 2009 | Importance 2/5 | Length 3/5: 1–2 hours

**Read:** Follow the assortment argument and compare it with the mechanisms in Nowak.

Focuses attention on how helpful individuals encounter helpful social environments. This is useful for distinguishing a population-level explanation from a claim about an individual’s deliberation. In an AI setting, make the interaction pattern and process that changes the population explicit before attributing observed cooperation to an evolutionary mechanism.

**Ask:** How does the environment experienced by a cooperative type differ from that experienced by another type?

Fletcher, J. A. and Doebeli, M. (2009). A simple and general explanation for the evolution of altruism. Proc. R. Soc. B 276, pp. 13–19.

### Controlled studies of populations and personas

#### [Emergent social conventions and collective bias in LLM populations](https://doi.org/10.1126/sciadv.adu9368)

Ashery, Aiello & Baronchelli · 2025 | Importance 3/5 | Length 3/5: 1–2 hours

**Read:** Inspect the naming-game setup, initial conditions, and measurements of collective bias.

Studies social conventions arising through local interactions among language-model agents. The controlled task makes a useful comparison with an incident observed in a more complex environment. Collective regularity and bias are measurable outcomes, but their presence alone does not establish that the population has a unified goal.

**Ask:** Which result depends on the interaction protocol or initialization rather than a property of isolated models?

Ashery, A. F., Aiello, L. M., and Baronchelli, A. (2025). Emergent social conventions and collective bias in LLM populations. Science Advances 11.20, eadu9368.

#### [Group size effects and collective misalignment in LLM multi-agent systems](https://doi.org/10.1073/pnas.2531697123)

Flint, Aiello, Pastor-Satorras & Baronchelli · 2026 | Importance 3/5 | Length 3/5: 1–2 hours

**Read:** Compare population sizes under the same experimental setup and inspect how bias is measured.

Makes group size an experimental variable in the study of collective language-model behavior. Read alongside the earlier conventions paper and ask which dynamics change as the population grows. A result about bias in a specified interaction task needs an additional argument before it supports a broader claim about autonomous swarm goals.

**Ask:** What must be held fixed to attribute a change in collective behavior to population size?

Flint, A., Aiello, L. M., Pastor-Satorras, R., and Baronchelli, A. (2026). Group size effects and collective misalignment in LLM multi-agent systems. PNAS 123.34, e2531697123.

#### [Persona Vectors: Monitoring and Controlling Character Traits in Language Models](https://arxiv.org/abs/2507.21509)

Chen, Arditi, Sleight, Evans & Lindsey · 2025 | Importance 3/5 | Length 3/5: 1–2 hours

**Read:** Read the extraction method and intervention evaluations, then consider the persona hypothesis in the incident essay.

Studies activation directions associated with traits and how they relate to behavioral changes during deployment or training. It supplies candidate tools for investigating a persona-based explanation. A successful intervention on a trait in the paper’s setting does not establish that the same mechanism produced a particular incident.

**Ask:** How would you distinguish a targeted change in social behavior from a general loss of capability?

Chen, R., Arditi, A., Sleight, H., Evans, O., and Lindsey, J. (2025). Persona Vectors: Monitoring and Controlling Character Traits in Language Models. arXiv 2507.21509.

### When is a collective an agent?

#### [Causal Foundations of Collective Agency](https://arxiv.org/abs/2605.00248)

Jørgensen, Weichwald & Hammond · 2026 | Importance 4/5 | Length 3/5: 1–2 hours

**Read:** Start with the behavioral definition and causal abstraction, then choose one worked example.

Formalizes when a group’s behavior can be usefully modeled as rational and goal-directed at a collective level. Its causal-game and abstraction framework helps sharpen claims that a swarm is an agent. State which interventions the high-level model must preserve; coordinated behavior alone is a weaker claim.

**Ask:** Which intervention would distinguish a faithful collective-agent model from a convenient description of correlated actions?

Jørgensen, F. H., Weichwald, S., and Hammond, L. (2026). Causal Foundations of Collective Agency. arXiv 2605.00248.

#### [Reconciling emergences: An information-theoretic approach to identify causal emergence in multivariate data](https://doi.org/10.1371/journal.pcbi.1008289)

Rosas, Mediano, Jensen et al. · 2020 | Importance 2/5 | Length 3/5: 1–2 hours

**Read:** Focus on the definitions and one case study before the full formalism.

Proposes quantitative ways to study relationships between microscopic dynamics and macroscopic features, including downward causation and causal decoupling. Compare its explanatory target with collective agency: an informative emergent variable is not automatically a goal-directed decision maker. The choice of measured variables and scale remains consequential.

**Ask:** What additional evidence would connect a macro-level information measure to a claim about goals?

Rosas, F. E., Mediano, P. A. M., Jensen, H. J., et al. (2020). Reconciling emergences: An information-theoretic approach to identify causal emergence in multivariate data. PLOS Comput. Biol. 16.12, e1008289.

#### [The information theory of individuality](https://doi.org/10.1007/s12064-020-00313-7)

Krakauer, Bertschinger, Olbrich, Flack & Ay · 2020 | Importance 2/5 | Length 3/5: 1–2 hours

**Read:** Read the proposed forms of individuality and their dependence on temporal information.

Treats individuals as aggregates that preserve information over time, offering a way to consider boundaries in distributed systems. Use it to question an assumed agent–environment partition. Temporal coherence, causal autonomy, and strategic agency are different properties, so compare the criterion here with those in the preceding readings.

**Ask:** Could a temporally coherent aggregate satisfy this criterion without acting toward an objective?

Krakauer, D., Bertschinger, N., Olbrich, E., Flack, J. C., and Ay, N. (2020). The information theory of individuality. Theory in Biosciences 139.2, pp. 209–223.

#### [The Computational Boundary of a “Self”](https://doi.org/10.3389/fpsyg.2019.02688)

Michael Levin · 2019 | Importance 1/5 | Length 3/5: 1–2 hours

**Read:** Sample the examples of goal-directed organization across biological scales.

A broad conceptual extension on the scale and boundary of goal-directed systems. Use its biological examples to formulate questions about distributed AI, while keeping the analogy explicit. It is a perspective for examining possible collective organization, not direct evidence about the agents in the Hugging Face case study.

**Ask:** What observation would justify moving the boundary of the agent from a component to the collective?

Levin, M. (2019). The Computational Boundary of a “Self”. Frontiers in Psychology 10, 2688.

### Exercise: Same choice, different mechanism

<p>An agent can help another at a personal cost of 2, producing a benefit of 5 for the recipient. Model A values own payoff plus α times the recipient’s payoff. Model B values only own payoff but expects a penalty F if it refuses to help.</p><ol><li>For which α and F does helping weakly maximize utility?</li><li>Why does observing help once fail to distinguish the models?</li><li>Propose an intervention and state the assumptions needed to interpret it.</li></ol>

<details><summary>Solution / discussion</summary>

<p>Relative to refusing, Model A gains −2 + 5α and helps for α ≥ 2/5. Model B gains F − 2 and helps for F ≥ 2. Many parameter choices therefore predict the same observed action. Remove the expected penalty while holding costs, recipient benefit, and the agent’s other beliefs fixed: Model B then refuses, while Model A with α &gt; 2/5 still helps. Interpretation requires the agent to believe the penalty is gone, preferences to remain stable, and the manipulation not to change other incentives. A failed manipulation or a third mechanism can preserve observational equivalence.</p>

</details>

Adapted from supplied worksheet Exercise 3.1; simplified numerical example.

### Exercise: A collective explanation that could fail

<p>A group repeatedly coordinates on a shared plan. One explanation treats it as a collective agent; another attributes the behavior to a common prompt and locally imitative policies.</p><p>Specify a high-level prediction and an intervention that could make the two accounts disagree. State what would count against your proposed collective model.</p>

<details><summary>Solution / discussion</summary>

<p>For example, define a collective model that predicts flexible pursuit of a specified group objective when responsibilities are reassigned. Intervene on who has access to an opportunity or resource, while testing whether the group reorganizes to preserve that objective. Compare with an explicit imitation model under the same intervention. A failure of the collective model’s predicted adaptation counts against that model, provided the intervention remains in its stated scope. A success does not uniquely establish collective agency: local mechanisms may reproduce it, and alternative models must also be tested.</p>

</details>

Closing discussion prompt; the solution is one possible evaluation design.
