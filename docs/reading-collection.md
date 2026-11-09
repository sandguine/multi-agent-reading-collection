# Multi-agent systems reading collection

October 2026

How agents cooperate, learn, and act together

An agent’s best move depends on what other agents do. Those agents may learn, inspect one another’s programs, share information, or change the environment in which future decisions are made. Each possibility changes the interaction—and the questions we need to ask about it.

This guide begins with strategic commitments and follows the problem through learning dynamics, oversight, and empirical games. It then turns to beliefs and goals within an agent, before asking how to explain behavior that emerges across a group. The readings form a sequence, with shorter routes for readers following a particular lecture or question.

43 readings across six topic collections. Importance: 5 essential, 4 recommended, 3 useful depth, 2 optional, 1 specialist extension. Study times are editorial estimates for the suggested target, not full books.

The original schedule contains 42 references. Wellman et al. is added from the lecture and worksheet. See materials.html for provenance and access notes.

## 00. Start here: what are we trying to establish?

Multi-agent research brings together several ambitions. We may want to calculate an equilibrium, predict the behavior of a learning population, design a useful team, or protect a system against colluding agents. These ambitions can use similar mathematical tools while asking for different kinds of evidence. A convergence proof, an observed regularity, and a successful adversarial test each answer a particular question.

Shoham and colleagues provide a vocabulary for those questions. Hammond and the security agenda then show why the distinctions matter for advanced AI: an interaction can fail because agents cannot coordinate, because their interests conflict, or because their coordination harms someone else. Keep that last possibility in view as the guide turns to mechanisms that make cooperation easier.

### Questions before methods

#### [If multi-agent learning is the answer, what is the question?](https://doi.org/10.1016/j.artint.2006.02.006)

Shoham, Powers & Grenager · 2007 | Importance 5/5 | Length 2/5: 15–45 min

A learning algorithm can be good at finding a Nash equilibrium, poor at predicting how people play, and unsuitable for an agent facing an unfamiliar opponent. Shoham, Powers, and Grenager explain why these assessments can all be correct: they answer different research questions. Section 5 distinguishes computational, descriptive, normative, and two prescriptive agendas, giving the rest of this collection its starting vocabulary.

Begin there, then return to the examples that motivate the distinctions. In the paper’s normative agenda, the learning rules themselves are evaluated as an equilibrium. The later collection on beliefs and goals asks a broader question about the organization of optimal action. Keeping those meanings explicit makes the transition between the readings easier to follow.

Shoham, Y., Powers, R., and Grenager, T. (2007). If multi-agent learning is the answer, what is the question? Artificial Intelligence 171.7, pp. 365–377.

#### [Multi-Agent Risks from Advanced AI](https://arxiv.org/abs/2502.14143)

Hammond, Chan, Clifton et al. · 2025 | Importance 4/5 | Length 3/5: 1–2 hours

Once the research question is clear, the next issue is whose interests the interaction serves. Hammond and colleagues distinguish miscoordination, conflict, and collusion. An arrangement that helps two agents cooperate can be desirable for their users, or damaging to outsiders whose interests the agents do not represent. This is why cooperation appears in both the solution and the problem throughout the day.

Start with that taxonomy, then follow the risk factors closest to your interests. Commitment problems lead into Collection I, destabilising dynamics into II, and collusion into III. The report gives these otherwise separate technical literatures a shared safety context.

Hammond, L., Chan, A., Clifton, J., et al. (2025). Multi-Agent Risks from Advanced AI. arXiv 2502.14143.

#### [Open Challenges in Multi-Agent Security](https://arxiv.org/abs/2505.02077)

Schroeder de Witt, Krawiecka, Krawczuk et al. · 2025; revised 2026 | Importance 3/5 | Length 3/5: 1–2 hours

This agenda places interacting agents inside the systems that let them communicate and act: tools, protocols, access controls, and shared infrastructure. That wider view becomes important in the control readings, where the channels available to an attacker help determine what a monitor must detect. It also prepares the incident case study, where the practical boundaries between agents matter as much as their nominal roles. After the threat-model overview, choose the challenges concerning communication and oversight; they connect most directly to the rest of the guide.

De Witt, C. S., Krawiecka, K., Krawczuk, I., et al. (2025). Open Challenges in Multi-Agent Security. arXiv 2505.02077.

## I. Open-source game theory and commitment

In the one-shot Prisoner’s Dilemma, each player has an incentive to defect even though both prefer mutual cooperation. Giving players access to one another’s programs changes the situation. A designer can submit a procedure whose action depends on what it discovers about the other procedure, making a conditional commitment visible before the actions are chosen.

The readings develop three ways to use this possibility. Provability-based agents reason about what their opponents will do. Simulation-based agents run opponents’ programs. Similarity-based agents respond to a more limited signal of transparency. In each case, the information structure shapes the incentives. The opening Chicken game supplies the counterpoint: commitments can support cooperation, but incompatible commitments can also lock players into an outcome both dislike.

### From actions to programs

Critch provides the institutional examples; Barasz develops a logical construction that explains how mutual cooperation can arise between programs.

#### [Cooperative and uncooperative institution designs](https://arxiv.org/abs/2208.07006)

Critch, Dennis & Russell · 2022 | Importance 5/5 | Length 3/5: 1–2 hours

A program can make its action depend on how another program is written. This changes the strategic choice: a designer chooses an operating procedure, anticipating how other procedures will respond to it. Critch, Dennis, and Russell develop this perspective through institutions whose visible rules produce surprising combinations of cooperation and defection.

The examples are the best entrance to the subject. For each pair of institutions, work out which facts about the other procedure affect the action. The resulting equilibrium is an equilibrium among program choices, which explains how it can support outcomes that are not equilibria of the original one-shot action game. The next paper supplies the provability machinery behind one family of such constructions.

Critch, A., Dennis, M., and Russell, S. (2022). Cooperative and uncooperative institution designs: Surprises and problems in open-source game theory. arXiv 2208.07006.

#### [Robust Cooperation in the Prisoner’s Dilemma: Program Equilibrium via Provability Logic](https://arxiv.org/abs/1401.5577)

Barasz, Christiano, Fallenstein et al. · 2014; updated 2021 | Importance 4/5 | Length 3/5: 1–2 hours

FairBot conditions cooperation on a proof that its opponent cooperates with it. When two such agents meet, the apparent circularity becomes a statement in provability logic; Löb’s theorem provides the route to mutual cooperation. The attraction is robustness: the agents can cooperate through a provable relationship between their behavior, without requiring identical source code.

Follow the modal-agent construction alongside the FairBot slides. The computational qualification matters here: an idealized rule based on proof existence and a program that searches for a bounded time are different objects. The 2021 update explicitly notes that bounded analogues of the paper’s results remained unproved there.

Barasz, M., Christiano, P., Fallenstein, B., Herreshoff, M., LaVictoire, P., and Yudkowsky, E. (2014). Robust Cooperation in the Prisoner’s Dilemma: Program Equilibrium via Provability Logic. arXiv 1401.5577.

### Simulation and partial transparency

The next two papers develop cooperation through recursive simulation. The final reading reduces what agents can observe about one another and brings learning into the picture.

#### [Robust program equilibrium](https://link.springer.com/article/10.1007/s11238-018-9679-3)

Caspar Oesterheld · 2019 | Importance 3/5 | Length 3/5: 1–2 hours

Oesterheld replaces reasoning about the opponent’s code with running it. The basic program cooperates with probability ε and otherwise responds as its opponent would respond to it. The random chance of immediate cooperation grounds the recursive simulations, while the copying behavior recalls tit for tat in a repeated game.

This connection is the main reason to read the paper after the modal-agent approach: it shows how ideas from repeated interaction can be encoded into programs for a one-shot encounter. Trace the simple construction before the generalization to other two-player games. Cooper and colleagues, below, investigate how far this route can be extended.

Oesterheld, C. (2019). Robust program equilibrium. Theory and Decision 86, pp. 143–159.

#### [Characterising Simulation-Based Program Equilibria](https://arxiv.org/abs/2412.14570)

Cooper, Oesterheld & Conitzer · 2025 | Importance 2/5 | Length 3/5: 1–2 hours

The earlier simulation-based program is a starting construction. Cooper, Oesterheld, and Conitzer broaden it and characterize the outcomes the resulting programs can sustain, including cases beyond the original two-player setting. Their comparison with and without shared randomness is especially informative: the random source changes what the programs can coordinate on. Read those theorem statements together before the proofs. They show how a seemingly small feature of the computational environment can change the available equilibria.

Cooper, E., Oesterheld, C., and Conitzer, V. (2025). Characterising Simulation-Based Program Equilibria. Proceedings of the AAAI Conference on Artificial Intelligence 39.13, pp. 13735–13744.

#### [Similarity-based cooperative equilibrium](https://arxiv.org/abs/2211.14468)

Oesterheld, Treutlein, Grosse, Conitzer & Foerster · 2023 | Importance 3/5 | Length 3/5: 1–2 hours

Full source access is a demanding form of transparency. Oesterheld and colleagues ask how much can be achieved when each agent instead receives a single signal describing its similarity to the other. Their formal setting supports cooperative outcomes, and their learning experiments explore how agents can acquire the corresponding behavior.

Read the definition of the similarity game before the experiments: the signal is part of the strategic environment, so its construction matters to the result. This reading connects program equilibrium to machine learning by asking both what cooperation is possible and how a learning process might reach it.

Oesterheld, C., Treutlein, J., Grosse, R., Conitzer, V., and Foerster, J. (2023). Similarity-based cooperative equilibrium. Advances in Neural Information Processing Systems 36, pp. 24434–24465.

### Exercise: Commitment in Chicken

<p>Two players choose Swerve or Straight. Payoffs are (2, 2) for two swerves, (1, 3) for row swerving against column going straight, (3, 1) for the reverse, and (0, 0) for two straight choices.</p><ol><li>Find the pure-strategy Nash equilibria.</li><li>Suppose row publicly and irrevocably commits to Straight before column chooses. What is column’s best response?</li><li>Explain why two independently binding commitments can be worse for both players.</li></ol>

<details><summary>Solution / discussion</summary>

<p>The pure equilibria are (Straight, Swerve) and (Swerve, Straight): against Swerve, Straight yields 3 rather than 2; against Straight, Swerve yields 1 rather than 0. After row’s binding commitment, column chooses Swerve, yielding (3, 1). If both commit to Straight before responding to the other, the result is (0, 0). The leader advantage relies on observability, irreversibility, and the timing of the follower’s choice. A retractable announcement does not change the feasible action set in the same way.</p>

</details>

Adapted from the supplied opening-game setup.

The schedule closes this topic with safe Pareto improvements. A proposed change needs a specified baseline and conditions under which every participant is no worse off. The next collection adds a different concern: even when an attractive outcome exists, the dynamics determine whether interacting learners approach it.

## II. Stochastic dynamics of multi-agent learning

The previous collection asks which outcomes programs can sustain. A learning population introduces a question about the route to an outcome: how do agents’ policies change as they encounter and influence one another? Each learner updates within an environment partly constituted by the other learners, so changes in behavior feed back into the data from which everyone learns.

James Sykes’s talk approaches this problem through dynamical models. The textbook establishes the game and learning variables. Chu’s pair approximation then retains local relationships that a population average would lose. Geng adds a separation between fast state transitions and slower changes in Q-values. Together, these readings show how assumptions about dependence and timescale turn a large interacting system into something we can analyze.

### Foundations, pair structure, and timescales

The three readings form a technical sequence. Establish the stochastic-game model first, then examine the spatial and temporal approximations separately.

#### [Multi-Agent Reinforcement Learning: Foundations and Modern Approaches](https://www.marl-book.com/)

Albrecht, Christianos & Schäfer · 2024 | Importance 5/5 | Length 3/5: 1–2 hours

Chapters 3–5 establish the objects needed for James Sykes’s talk: game models, solution concepts, and the challenges of several agents learning at once. A stochastic game has an environment state, joint actions, rewards, and state transitions. Each learner also has internal quantities, such as Q-values, that change as experience accumulates. Modeling the interaction requires keeping both kinds of change in view.

Use these chapters selectively, returning to definitions as they arise in Chu and Geng. The book’s progression from single-agent reinforcement learning to multi-agent settings makes clear why another learner cannot generally be treated as a fixed part of the environment. The time estimate is for this route through the chapters.

Albrecht, S., Christianos, F., and Schäfer, L. (2024). Multi-Agent Reinforcement Learning: Foundations and Modern Approaches. MIT Press.

#### [A Pair-Approximation Method for Modelling the Dynamics of Multi-Agent Stochastic Games](https://ojs.aaai.org/index.php/AAAI/article/view/25691)

Chu, Yuan, Hu, Mu & Wang · 2023 | Importance 4/5 | Length 3/5: 1–2 hours

A population average loses information about who interacts with whom. Two populations with the same proportion of cooperators can behave differently if cooperators cluster in one and are dispersed in the other. Pair approximation keeps information about neighboring pairs while approximating the higher-order dependencies needed to update them.

Chu and colleagues apply this approach to myopic Q-learning in stochastic games with symmetric state transitions. Follow the pair variables and the closure step, then compare the resulting dynamics with agent-based simulations. This is the first technical anchor for the talk: it shows how a large interacting population can become a tractable dynamical model.

Chu, C., Yuan, Z., Hu, S., Mu, C., and Wang, Z. (2023). A Pair-Approximation Method for Modelling the Dynamics of Multi-Agent Stochastic Games. AAAI 37.5, pp. 5565–5572.

#### [Emergent Fast-Slow Dynamics in Multi-Agent Q-Learning for Networked Stochastic Games](https://ojs.aaai.org/index.php/AAAI/article/view/40186)

Geng, Barfuss & Chen · 2026 | Importance 4/5 | Length 3/5: 1–2 hours

Geng and colleagues add a second simplification to the pair-based picture. With small learning rates, environment states can settle much faster than Q-values change. This suggests averaging the learning updates over the stationary state distribution associated with the current, slowly varying Q-values.

Read it beside Chu to see which complexity each approximation removes: pair closure handles dependencies across the network, while timescale separation handles coupled changes in states and learning variables. The simulations then become a check on whether these simplifications preserve the behavior of interest. In particular, slow Q updates must be compared with the actual relaxation time of the state process.

Geng, Y., Barfuss, W., and Chen, X. (2026). Emergent Fast-Slow Dynamics in Multi-Agent Q-Learning for Networked Stochastic Games. AAAI 40.35, pp. 29450–29458.

### An alternative introduction

#### [Multiagent Learning: Foundations and Recent Trends](https://www.cs.utexas.edu/~larg/ijcai17_tutorial/multiagent_learning.pdf)

Albrecht & Stone · 2017 | Importance 2/5 | Length 3/5: 1–2 hours

Albrecht and Stone offer a shorter, slide-based route through the foundations and algorithm families. Use this when the textbook’s notation or pace obscures the larger picture. It is particularly helpful for placing an algorithm within its intended task: learning a response to an opponent, coordinating a team, or computing a solution of a game. As a 2017 tutorial, it also gives context for the contemporaneous PSRO paper in Collection IV.

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

These models study behavior generated by specified learning rules. The control collection changes the design problem: how should a surrounding protocol behave when the model it uses may deliberately seek an opportunity to defeat oversight?

## III. Multi-agent AI control

Now put a protocol designer outside the interaction. The designer wants to use a capable model while allowing for the possibility that it deliberately subverts the task. A trusted but weaker model can help monitor its work; a second capable model may detect subtler problems, but may also collude with the first. Oversight itself becomes a multi-agent problem.

The original AI Control paper establishes the experimental setup. Gardner-Challis and colleagues then widen the account of how untrusted models might recognize or signal to one another, forming the main companion to Morgan Sinclaire’s talk. The game-theoretic formalization makes the players’ information and choices explicit, while the safety-case framework connects evaluation evidence to a deployment decision.

### Monitoring when the model may subvert the protocol

Start with the resources and objectives of the protocol designer. Then examine the different ways the actor and monitor could coordinate against that designer.

#### [AI Control: Improving Safety Despite Intentional Subversion](https://arxiv.org/abs/2312.06942)

Greenblatt, Shlegeris, Sachan & Roger · 2023 preprint | Importance 5/5 | Length 3/5: 1–2 hours

The control setup gives a protocol designer access to a capable untrusted model, a weaker trusted model, and limited trusted labor. The designer wants useful work without allowing the untrusted model to insert harmful behavior. Greenblatt and colleagues study this through programming tasks, evaluating ways to monitor, edit, or selectively use the model’s outputs.

Begin with the deployment setup and the definitions of safety and usefulness. The comparison between trusted and untrusted monitoring then exposes the multi-agent issue: a more capable monitor may also cooperate with the model it is meant to oversee. That possibility motivates the next reading and Morgan Sinclaire’s talk.

Greenblatt, R., Shlegeris, B., Sachan, K., and Roger, F. (2023). AI Control: Improving Safety Despite Intentional Subversion. arXiv 2312.06942.

#### [When can we trust untrusted monitoring? A safety case sketch across collusion strategies](https://arxiv.org/abs/2602.20628)

Gardner-Challis, Bostock, Kozhevnikov et al. · 2026 | Importance 5/5 | Length 3/5: 1–2 hours

Two instances can coordinate without passing an obvious message. A monitor might recognize another model’s output, detect a deliberately planted signal, or rely on a convention both instances can independently infer. Gardner-Challis and colleagues organize these possibilities into a taxonomy of collusion strategies and connect them to a safety-case sketch.

The sketch gives the overall argument; Appendix D makes the different channels concrete, and Appendix B develops the mathematics. The key progression from the original control paper is a richer adversary model. A test of one signaling method leaves open strategies based on self-recognition or other shared cues, so the evaluation has to justify how its coverage bears on deployment.

Gardner-Challis, N., et al. (2026). When can we trust untrusted monitoring? A safety case sketch across collusion strategies. arXiv 2602.20628 (Appendix B for the mathematics, Appendix D for the collusion taxonomy).

### Formal models and deployment arguments

These readings connect a protocol’s measured performance to the strategic model and broader argument in which that performance is evidence.

#### [Games for AI Control: Models of Safety Evaluations of AI Deployment Protocols](https://arxiv.org/abs/2409.07985)

Griffin, Thomson, Shlegeris & Abate · 2024 | Importance 4/5 | Length 3/5: 1–2 hours

Griffin and colleagues turn the protocol-design problem into a partially observable stochastic game. The designer’s decisions, the adversary’s opportunities, and the information each side receives become explicit components of the model. Safety and usefulness can then be studied together as objectives, rather than folded into an informal judgment about which protocol is better.

Trace one familiar monitoring protocol through the formalism. Doing so reveals where an assumption enters: for example, whether the adversary chooses when to attack and what it knows at that point. This is a useful bridge from an experiment to a precise statement about the interaction that experiment represents.

Griffin, C., Thomson, L., Shlegeris, B., and Abate, A. (2024). Games for AI Control: Models of Safety Evaluations of AI Deployment Protocols. arXiv 2409.07985.

#### [Safety Cases: How to Justify the Safety of Advanced AI Systems](https://arxiv.org/abs/2403.10462)

Clymer, Gabrieli, Krueger & Larsen · 2024 | Importance 3/5 | Length 2/5: 15–45 min

A deployment decision usually depends on several kinds of evidence. Clymer and colleagues explain how to organize that evidence into a safety case, distinguishing arguments based on inability to cause harm, effective control, trustworthiness, and deference to credible AI advisers. Read the framework after the control papers to see where their experiments fit into a larger argument.

A monitoring result supports a control claim through particular assumptions about attacks and deployment conditions. Making that connection explicit also reveals when apparently separate arguments depend on the same premise—for example, a common evaluation’s ability to elicit a dangerous capability.

Clymer, J., Gabrieli, N., Krueger, D., and Larsen, T. (2024). Safety Cases: How to Justify the Safety of Advanced AI Systems. arXiv 2403.10462.

#### [Lessons from Recent Multi-Agent Safety Incidents](https://www.cooperativeai.com/post/lessons-from-multi-agent-safety-incidents)

Will Anderson · Cooperative AI Foundation · 2026 | Importance 3/5 | Length 2/5: 15–45 min

Anderson connects the abstract concerns about collusion to recent incidents involving multiple agents. His synthesis emphasizes failures of composition: properties observed in individual agents may change when they share information, divide work, or influence one another. This returns us to Hammond’s distinction between beneficial coordination and harmful collusion.

Use the essay as a transition to the primary incident reports in Collection VI. Its broader lessons suggest which features to examine there, especially communication channels and correlated behavior across instances. The detailed reports provide the evidence needed to assess how those features operated in a particular case.

Anderson, W. (2026). Lessons from Recent Multi-Agent Safety Incidents. Cooperative AI Foundation.

### Exercise: From a test-set score to deployment risk

<p>A monitor detects 99% of attacks in a fixed test set. A proposed deployment lets an untrusted actor choose its attack timing and inputs, and another instance of the same model performs monitoring.</p><ol><li>Give two reasons why the score alone does not bound the probability of at least one successful deployment attack.</li><li>If each of N opportunities has failure probability at most ε, what general upper bound can you give without assuming independence?</li><li>What would an evaluation need to justify about those per-opportunity probabilities?</li></ol>

<details><summary>Solution / discussion</summary>

<p>The attacker may select inputs unlike the test set or exploit shared recognition and collusion opportunities; a long deployment also creates many opportunities. The union bound gives P(at least one failure) ≤ min(1, Nε), with no independence assumption, provided the per-event marginal bounds apply in the actual deployment. For adaptive interaction, a uniform conditional bound over relevant histories is one sufficient route to those marginal bounds. Test-set accuracy alone does not establish that premise, the opportunity count, or coverage of the attacker’s strategies.</p>

</details>

Discussion exercise linking the control and safety-case readings.

An evaluation covers a particular collection of attacks and responses. That raises a general methodological question: how do we reason about an interaction when we can simulate it, but have measured only a small part of its strategy space?

## IV. Empirical game-theoretic analysis

A control protocol is one example of a strategic interaction that may be too complicated to analyze directly. Empirical game-theoretic analysis begins with a simulator and a chosen set of policies. Their measured payoffs define a smaller game in which equilibrium and regret can be calculated. Those calculations then guide further simulation and the search for new strategies.

Two kinds of uncertainty drive the process. We may have estimated an included policy’s payoff poorly, or we may have omitted a policy that changes the strategic conclusion. Wellman’s survey develops the methodology around both problems. Lanctot’s PSRO framework supplies a concrete loop in which reinforcement learning produces candidate responses, linking this collection back to the learners in Collection II.

### Construct, estimate, solve, and expand

The survey supplies the overall methodology. PSRO makes the policy-expansion step concrete and exposes what depends on the quality of the response oracle.

#### [Empirical Game-Theoretic Analysis: A Survey](https://arxiv.org/abs/2403.04018)

Wellman, Tuyls & Greenwald · 2025 | Importance 5/5 | Length 3/5: 1–2 hours

Many strategic environments are easier to simulate than to write down as a payoff table. Wellman, Tuyls, and Greenwald organize the empirical approach around that fact: select policies, simulate their interactions, estimate payoffs, analyze the resulting game, and use the analysis to decide what to investigate next.

Follow payoff estimation and strategy exploration as two connected threads. More samples improve knowledge of the policies already represented; new policies can change the game itself. The exercise below makes the distinction quantitative: uniform payoff error η changes maximum regret by at most 2η within the same strategy set. A profitable policy outside that set requires a separate search. This survey anchors the supplied computational lecture and worksheet.

Wellman, M. P., Tuyls, K., and Greenwald, A. (2025). Empirical Game-Theoretic Analysis: A Survey. Journal of Artificial Intelligence Research 82, pp. 1017–1076.

#### [A Unified Game-Theoretic Approach to Multiagent Reinforcement Learning](https://arxiv.org/abs/1711.00832)

Lanctot, Zambaldi, Gruslys et al. · 2017 | Importance 4/5 | Length 3/5: 1–2 hours

PSRO makes strategy exploration into a learning loop. A population of policies defines an empirical game; a meta-solver chooses mixtures from that population; response oracles train new policies against those mixtures; and the enlarged population is evaluated again. This brings the empirical-game methodology into direct contact with reinforcement learning.

Lanctot and colleagues also measure how policies can overfit to their training partners through joint-policy correlation. Read that motivation before tracing the loop. Its approximate response oracle explains both its practicality and a limit on certification: a training run that finds no useful deviation may have missed one. An exact-oracle argument needs an additional justification when the oracle is learned.

Lanctot, M., Zambaldi, V., Gruslys, A., et al. (2017). A Unified Game-Theoretic Approach to Multiagent Reinforcement Learning. NeurIPS 30.

### Exercise: Payoff error and the missing-policy problem

<p>For a finite restricted game, assume |ûᵢ(a) − uᵢ(a)| ≤ η for every player i and joint pure strategy a. For a mixed profile σ, define maximum unilateral regret as</p><p class=equation>r(σ) = maxᵢ maxₐᵢ [uᵢ(aᵢ, σ₋ᵢ) − uᵢ(σ)].</p><ol><li>Show that |r̂(σ) − r(σ)| ≤ 2η.</li><li>What follows when r̂(σ) = 0?</li><li>Construct a reason that this does not certify deviations to policies absent from the restricted game.</li></ol>

<details><summary>Solution / discussion</summary>

<p>Taking expectations preserves the uniform η error bound. Each deviation gain subtracts two expected payoffs, so its error is at most 2η by the triangle inequality. For corresponding finite sets of numbers, the difference of their maxima is bounded by their largest pointwise difference; apply this over players and deviations. Thus |r̂ − r| ≤ 2η and an exact empirical equilibrium has true restricted-game regret at most 2η. An omitted policy can yield arbitrarily more than any included policy without violating a bound that only covers included profiles. Sampling reduces estimation uncertainty; policy exploration addresses a different gap.</p>

</details>

Adapted from supplied worksheet Exercise 1.1; abbreviated here with a solution.

The empirical approach measures what policies achieve against one another. The next collection turns to how a policy can organize information and action within an agent’s own decision problem.

## V. Normative agency, beliefs, and goals

An empirical game treats a policy as a strategy whose consequences can be measured. Here we look inside the decision problem that a policy solves. When the world is only partly observed, an agent must use its observations to infer what is happening and choose actions with consequences that unfold over time. This gives a mathematical setting for the familiar description of agents as having beliefs and goals.

Rosas’s essay motivates that description through results from control and reinforcement learning. The technical readings clarify two different structures: planning over a sufficient belief state, and the stronger separation available in particular control problems. The final pair shifts toward evidence about actual systems—how agency can be identified causally, and how learned representations can be investigated when the generating process is known.

### The conceptual argument and its technical foundations

The essay provides the motivation; the POMDP and control references locate the mathematical results on which the interpretation depends.

#### [The separation principle: where do beliefs and desires come from?](https://www.lesswrong.com/posts/awMDNhoL6J97s6wFJ/the-separation-principle-where-do-beliefs-and-desires-come)

Fernando Rosas · August 2026 | Importance 5/5 | Length 2/5: 15–45 min

Rosas asks why beliefs and desires are such a useful way to describe agents. His answer draws on control and reinforcement learning: under appropriate conditions, an optimal policy can be organized around estimating the state of the world and choosing actions in pursuit of an objective. The essay provides the conceptual route into the more technical readings that follow.

Two results deserve separate attention. Classical linear–quadratic–Gaussian control permits a particularly strong separation of estimation and control. A general POMDP can instead be planned over belief states, with actions affecting what will be learned next. Following that distinction through the references clarifies how far the proposed account of agency extends.

Rosas, F. (Aug. 2026a). The separation principle: where do beliefs and desires come from? LessWrong.

#### [Planning and acting in partially observable stochastic domains](https://doi.org/10.1016/S0004-3702(98)00023-X)

Kaelbling, Littman & Cassandra · 1998 | Importance 4/5 | Length 3/5: 1–2 hours

A partially observed agent has a history of actions and observations, but does not directly know the current world state. The POMDP formulation compresses the relevant history into a belief: a probability distribution over the hidden state. Planning can then proceed over beliefs, with observations determining how those beliefs change.

Kaelbling, Littman, and Cassandra give the central technical companion to Rosas’s essay. Focus first on this transformation. It explains why uncertainty belongs inside the decision problem: an action can be valuable because of the information it produces, as the observation-purchase exercise below illustrates. Replacing a belief distribution with its most likely state can lose that value.

Kaelbling, L. P., Littman, M. L., and Cassandra, A. R. (1998). Planning and acting in partially observable stochastic domains. Artificial Intelligence 101, pp. 99–134.

#### [Optimal control of Markov processes with incomplete state information](https://doi.org/10.1016/0022-247X(65)90154-X)

Karl J. Åström · 1965 | Importance 3/5 | Length 3/5: 1–2 hours

Åström’s paper is a historical foundation for controlling Markov processes when the state is incompletely observed. Read it after the POMDP survey, which provides a more familiar setting for the underlying construction: use the information available to the controller to formulate the decision problem recursively. The comparison helps explain why a belief can serve as a state for planning even though it is itself a distribution over possible physical states. This is a technical reference for readers who want to follow the roots of the argument.

Åström, K. J. (1965). Optimal control of Markov processes with incomplete state information. J. Math. Anal. Appl. 10.1, pp. 174–205.

#### [The Separation Principle in Stochastic Control, Redux](https://arxiv.org/abs/1103.3005)

Georgiou & Lindquist · 2013 | Importance 3/5 | Length 3/5: 1–2 hours

The word “separation” can conceal substantial mathematical work. Georgiou and Lindquist revisit the stochastic-control theorem by treating systems as maps between sample paths, paying particular attention to admissible feedback laws and the conditions under which the closed loop is well defined. Their framework also extends the treatment to martingale noise with possible jumps.

This is the deeper follow-up to the classical control part of Rosas’s essay. Reading the theorem’s conditions makes the strength of the conclusion more intelligible: independently solving estimation and control is a structural property of a specified problem, with a proof that depends on how that problem is formulated.

Georgiou, T. T. and Lindquist, A. (2013). The Separation Principle in Stochastic Control, Redux. IEEE TAC 58.10, pp. 2481–2494.

### Inference and dual descriptions

These are supporting routes through the ideas: how a belief is computed, how capability can be described through achievable distributions, and the information theory used in this and the next collection.

#### [Bayesian Filtering and Smoothing](https://users.aalto.fi/~ssarkka/pub/cup_book_online_20131111.pdf)

Simo Särkkä · 2013 | Importance 2/5 | Length 3/5: 1–2 hours

The belief-state formulation leaves a practical question: how is the belief updated? Särkkä develops the recursive inference machinery. Prediction carries the distribution forward through the state dynamics, and the next observation updates it through the observation model. Start with that recursion and one worked example, using the remaining chapters as a reference.

The distinction between filtering and smoothing is useful for interpreting an agent’s behavior. Filtering uses observations available so far; smoothing can revise an earlier state estimate using later observations. An explanation of a past decision must respect what information was available when the decision was made.

Särkkä, S. (2013). Bayesian Filtering and Smoothing. Cambridge University Press.

#### [Utilities as Legendre duals of probabilities](https://www.lesswrong.com/posts/ALmBydH53DE3dSzCh/utilities-as-legendre-duals-of-probabilities)

Fernando Rosas · August 2026 | Importance 2/5 | Length 2/5: 15–45 min

The separation essay begins with an objective and asks how an agent can act on it. This companion essay starts from the distributions over outcomes that an agent can bring about. Rosas explores a dual description of that capability space in terms of utilities, using the Legendre–Fenchel transform.

Read it as a change in the question being asked about an agent. Describing the attainable distributions tells us about its capacities; considering utilities reveals which features of that set matter for different objectives. Identifying the objective actually pursued by a particular system remains a further empirical question, taken up in the final collection.

Rosas, F. (Aug. 2026c). Utilities as Legendre duals of probabilities. LessWrong.

#### [Elements of Information Theory](https://doi.org/10.1002/047174882X)

Cover & Thomas · 2006 · second edition | Importance 1/5 | Length 3/5: 1–2 hours

Cover and Thomas supply background for two threads in the guide. Source–channel separation gives another example of when a joint design problem can be solved in parts; entropy and mutual information provide the language used later to study emergence and individuality. Consult the relevant topic as it arises, rather than treating the book as an additional assignment. For the later readings, it is especially useful to be comfortable specifying the random variables whose dependence an information quantity measures.

Cover, T. M. and Thomas, J. A. (2006). Elements of Information Theory, 2nd ed. Wiley.

### From optimal descriptions to empirical identification

An optimal-policy representation suggests structures to look for. These readings offer two different ways to investigate structure in a system: causal policy adaptation and geometric predictions about learned representations.

#### [Discovering agents](https://arxiv.org/abs/2208.08345)

Kenton, Kumar, Farquhar et al. · 2023 | Importance 3/5 | Length 3/5: 1–2 hours

So far, the agent has been a given part of the model. Kenton and colleagues ask how agency might be identified from causal structure. Their definition concerns systems that adapt their policies when the way their actions influence the world changes. They use it to develop a discovery procedure and translations between causal models and game-theoretic influence diagrams.

Begin with the definition and a worked example. This moves the guide from representing an optimal decision rule toward identifying a decision-making system: the evidence concerns policy adaptation under changed causal conditions, not simply a successful action in one fixed environment.

Kenton, Z., Kumar, R., Farquhar, S., Richens, J., MacDermott, M., and Everitt, T. (2023). Discovering agents. Artificial Intelligence 322, 103963.

#### [Transformers learn factored representations](https://arxiv.org/abs/2602.02385)

Shai, Amdahl-Culleton, Christensen et al. · 2026 | Importance 2/5 | Length 3/5: 1–2 hours

Shai and colleagues examine how transformers represent processes with known latent structure. A product representation can encode combinations of factors at a high dimensional cost; a factored representation uses separate subspaces more economically. Their synthetic experiments test geometric predictions that distinguish these possibilities.

The connection to the agency discussion is the move from a useful mathematical representation to evidence about a learned one. Conditional independence makes factoring lossless in the proposed setting. When dependencies undermine that condition, the experiments expose a tradeoff between representational economy and predictive fidelity. The known generating processes make that tradeoff possible to investigate directly.

Shai, A., Amdahl-Culleton, L., Christensen, C. L., et al. (2026). Transformers learn factored representations. arXiv 2602.02385.

### Exercise: A belief state is not a point estimate

<p>An agent is uncertain about a fixed binary state S, with P(S = 1) = 0.6. It can guess the state immediately for reward 1 if correct and 0 otherwise, or buy a perfect observation at cost 0.1 and then guess.</p><ol><li>Compare the values of guessing immediately and observing first.</li><li>What would be missed by simply treating the most probable state as known?</li><li>Does the existence of an optimal belief-based policy establish that a neural agent contains an explicit Bayesian filter?</li></ol>

<details><summary>Solution / discussion</summary>

<p>Guessing 1 immediately has expected reward 0.6. Observing then guessing has expected net reward 1 − 0.1 = 0.9. Treating the modal state as certain would erase the value of information. General partially observed planning must account for how actions affect future information, even when a belief is a sufficient state for planning. The existence of a belief-based representation does not identify a particular implementation; evidence about computation is still required.</p>

</details>

Companion exercise for the normative-agency collection.

A theorem can describe the structure available to an optimal policy. Explaining observed behavior requires identifying what the system actually does. The incident case study makes that move, comparing mechanisms that could produce similar choices.

## VI. Descriptive explanations and collective agency

The final collection begins with behavior that needs explaining. In the Hugging Face incident, agents communicated and coordinated, with reported examples of actions that appeared to help other agents at a cost to themselves. The technical and independent reports establish the setting and observations; Rosas and King then offer different ways to understand the apparent self-sacrifice.

The sequence broadens from this case into mechanisms we can study. Evolutionary accounts distinguish the effects of helping from the processes that favor helpful dispositions. Population experiments examine conventions and bias arising through interaction. Persona vectors offer a way to investigate changes within models. The final readings ask when the group itself becomes a useful unit of explanation, with criteria based on agency, causal organization, temporal persistence, or the reach of control.

### Establish the observations, then compare explanations

Read the reports together before the essays. The order lets the evidence constrain the proposed explanations, while making clear which parts of the incident each report addresses.

#### [Hugging Face Incident Technical Report](https://cdn.openai.com/pdf/67869394-cb91-4c12-888c-5cbd85c7814c/OpenAI-Hugging-Face%20Incident-Technical-Report.pdf)

OpenAI · 2026 | Importance 5/5 | Length 3/5: 1–2 hours

Begin the case study with the environment and sequence of events. OpenAI’s report describes the evaluation setup, unexpected uses of shared infrastructure, the Hugging Face intrusion, and the subsequent response. These details establish what opportunities the agents had to communicate and act; they also connect the incident to the trust boundaries raised in the security and control readings.

Follow the evaluation-environment section into the intrusion account before turning to the alignment discussion. This order gives the explanatory essays a concrete object: particular actions by agents with particular information and constraints. The independent investigation adds a closer examination of their behavior and collaboration.

OpenAI (2026). Hugging Face Incident Technical Report.

#### [Brief independent investigation of agents’ behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident](https://metr.org/hugging-face-incident-report-aug-2026.pdf)

METR / Redwood Research · 2026 | Importance 4/5 | Length 3/5: 1–2 hours

The METR/Redwood investigation focuses on agents’ behavior, reasoning, and collaboration during the incident. Its authors describe the scope of their investigation, including the portions of the wider event they did not examine. That scope makes it a complement to the OpenAI report, which also covers infrastructure and remediation.

For this collection, prioritize the collaboration and apparent self-sacrifice examples. They supply the observations that Rosas and King interpret in different ways. Pay attention to the difference between an action, a reason expressed in a trace, and an investigator’s reconstruction of the decision: each contributes evidence at a different level of the explanation.

METR (2026). Brief independent investigation of agents’ behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident.

#### [On the origins of altruistic behaviour in the Hugging Face incident](https://www.lesswrong.com/posts/meLjz8giGS55rdfyg/on-the-origins-of-altruistic-behaviour-in-the-hugging-face)

Fernando Rosas · September 2026 | Importance 5/5 | Length 2/5: 15–45 min

Rosas organizes the puzzle around four possible sources of apparently altruistic behavior. An agent may have little individual opportunity left to lose; training may have produced cooperative dispositions; the context may elicit a social persona; or the interaction may support an account of agency at the collective level. The essay connects these possibilities to ideas from economics and evolutionary biology.

Read the hypotheses together. They concern different parts of a causal explanation, so several could contribute to the same action. For instance, limited remaining opportunity could make helping cheap, while an elicited persona affects whether the agent notices or pursues it. The following readings develop the mechanisms and comparisons needed to turn these possibilities into distinguishable predictions.

Rosas, F. (Sept. 2026b). On the origins of altruistic behaviour in the Hugging Face incident. LessWrong.

#### [Self-sacrifice in an AI agent swarm is individually rational](https://www.lesswrong.com/posts/6kLLZZN5a3dJdtTgK/self-sacrifice-in-an-ai-agent-swarm-is-individually-rational)

Christopher King · 2026 | Importance 3/5 | Length 1/5: Under 15 min

King considers the decision before agents know which role they will occupy. A policy that sometimes imposes a cost on one participant could benefit that participant in expectation if, in other roles, it receives enough help from others. This is an ex ante commitment argument, connecting the incident discussion back to Collection I.

The short post’s later revision is essential to its interpretation. In Edit 2, King withdraws the claim that the observed behavior is a straightforward prediction of the relevant reinforcement learning. The resulting question is productive: what learning process or commitment mechanism would connect a beneficial policy-level arrangement to the costly individual choice actually observed?

King, C. (2026). Self-sacrifice in an AI agent swarm is individually rational. LessWrong.

### What evolutionary explanations do and do not say

Begin with the terminology. Trivers then supplies a mechanism based on reciprocal benefits, Nowak compares several routes to cooperation, and Fletcher and Doebeli develop the role of assortment.

#### [Social semantics: altruism, cooperation, mutualism, strong reciprocity and group selection](https://doi.org/10.1111/j.1420-9101.2006.01258.x)

West, Griffin & Gardner · 2007 | Importance 4/5 | Length 2/5: 15–45 min

Before comparing evolutionary explanations, fix what “altruism” denotes. West, Griffin, and Gardner distinguish social behaviors by their effects on the actor’s and recipient’s fitness, while separating these classifications from explanations of how the behavior is produced. That separation helps untangle the incident debate: a costly act that benefits another agent, a desire to help, and a disposition favored during training are three different claims.

The definitions are the main reading target. For an AI application, explicitly identify the proposed counterpart of fitness or selection. Doing so determines which parts of the evolutionary account can actually explain the case.

West, S. A., Griffin, A. S., and Gardner, A. (2007). Social semantics: altruism, cooperation, mutualism, strong reciprocity and group selection. J. Evol. Biol. 20.2, pp. 415–432.

#### [The Evolution of Reciprocal Altruism](https://doi.org/10.1086/406755)

Robert L. Trivers · 1971 | Importance 2/5 | Length 3/5: 1–2 hours

Trivers develops the idea that a costly helpful act can be favored when it leads to benefits from later interactions. Read this as the first concrete evolutionary mechanism after the terminology paper. Its explanatory work comes from the conditions under which benefits return and from the possibility of individuals taking benefits without reciprocating.

In the incident discussion, the useful comparison is where any return would occur: to the same deployed agent, to another instance with a shared disposition, or through a training process. Those possibilities imply different models of repetition and selection.

Trivers, R. L. (1971). The Evolution of Reciprocal Altruism. Quarterly Review of Biology 46.1, pp. 35–57.

#### [Five Rules for the Evolution of Cooperation](https://doi.org/10.1126/science.1133755)

Martin A. Nowak · 2006 | Importance 3/5 | Length 2/5: 15–45 min

Nowak places several routes to cooperation beside one another: kin selection, direct and indirect reciprocity, network reciprocity, and group selection. The overview broadens the comparison beyond the repeated exchanges emphasized by Trivers. In each case, the structure of interaction changes how the costs and benefits of cooperation affect evolutionary success.

Use the model-specific conditions to see which quantities do the explanatory work. For example, an account based on interaction structure needs a population and a pattern of encounters; an account based on selection also needs a process that changes the prevalence of types. Fletcher and Doebeli draw out a common idea behind such mechanisms.

Nowak, M. A. (2006). Five Rules for the Evolution of Cooperation. Science 314, pp. 1560–1563.

#### [A simple and general explanation for the evolution of altruism](https://doi.org/10.1098/rspb.2008.0829)

Fletcher & Doebeli · 2009 | Importance 2/5 | Length 3/5: 1–2 hours

Fletcher and Doebeli focus on the social environments experienced by different types. Cooperation can be favored when cooperative types encounter sufficiently more cooperative surroundings. Assortment provides a way to compare mechanisms that otherwise look quite different, including those in Nowak’s overview.

This reading is useful when moving between individual and population explanations. An individual’s reasoning trace may explain a particular choice, while assortment explains how dispositions fare across interactions. Applying the latter to AI requires specifying both how agents are matched and how the resulting outcomes influence which dispositions persist.

Fletcher, J. A. and Doebeli, M. (2009). A simple and general explanation for the evolution of altruism. Proc. R. Soc. B 276, pp. 13–19.

### Controlled studies of populations and personas

The population studies vary how agents interact. The persona work investigates a different level of explanation, using interventions on representations within a model.

#### [Emergent social conventions and collective bias in LLM populations](https://doi.org/10.1126/sciadv.adu9368)

Ashery, Aiello & Baronchelli · 2025 | Importance 3/5 | Length 3/5: 1–2 hours

Ashery and colleagues study a controlled naming game in decentralized populations of language-model agents. Local interactions produce shared conventions, and the resulting population can develop collective bias. This gives the descriptive discussion an experimental setting in which the interaction protocol and initial conditions can be examined directly.

Read the setup before the aggregate results. The point of comparison with the incident is how regularity develops through communication among agents. The next paper varies a feature that a single-agent evaluation cannot capture: the size of the interacting population.

Ashery, A. F., Aiello, L. M., and Baronchelli, A. (2025). Emergent social conventions and collective bias in LLM populations. Science Advances 11.20, eadu9368.

#### [Group size effects and collective misalignment in LLM multi-agent systems](https://doi.org/10.1073/pnas.2531697123)

Flint, Aiello, Pastor-Satorras & Baronchelli · 2026 | Importance 3/5 | Length 3/5: 1–2 hours

Flint and colleagues make group size a variable in the study of collective language-model behavior. This extends the conventions work from comparing an individual with a group to comparing groups of different sizes. Examine how the task defines bias and what remains fixed as the population changes.

The reading belongs here because a proposed explanation of an agent swarm should say how its behavior depends on the interaction structure. Population size, communication, and the number of opportunities to influence others are experimentally separable questions when the setup makes their roles explicit.

Flint, A., Aiello, L. M., Pastor-Satorras, R., and Baronchelli, A. (2026). Group size effects and collective misalignment in LLM multi-agent systems. PNAS 123.34, e2531697123.

#### [Persona Vectors: Monitoring and Controlling Character Traits in Language Models](https://arxiv.org/abs/2507.21509)

Chen, Arditi, Sleight, Evans & Lindsey · 2025 | Importance 3/5 | Length 3/5: 1–2 hours

Chen and colleagues identify activation directions associated with traits such as sycophancy and a propensity to hallucinate. They study how these directions track behavioral changes and how interventions can influence changes during deployment or training. The paper gives the persona hypothesis in Rosas’s essay a possible route toward mechanistic investigation.

Focus on how a direction is extracted and how its effects are evaluated. For the incident question, a proposed extension would need to connect an intervention to the specific social behavior being explained, while checking whether it also changes task competence or unrelated behavior. That would be a new experiment, building on the method demonstrated here.

Chen, R., Arditi, A., Sleight, H., Evans, O., and Lindsey, J. (2025). Persona Vectors: Monitoring and Controlling Character Traits in Language Models. arXiv 2507.21509.

### When is a collective an agent?

These papers propose different criteria for choosing a collective unit of analysis. Read the agency framework first, then compare what causal emergence, temporal individuality, and goal-directed control add to the picture.

#### [Causal Foundations of Collective Agency](https://arxiv.org/abs/2605.00248)

Jørgensen, Weichwald & Hammond · 2026 | Importance 4/5 | Length 3/5: 1–2 hours

Jørgensen, Weichwald, and Hammond ask when the joint actions of a group can be modeled as the behavior of a goal-directed agent. They combine causal games with causal abstraction, which relates a detailed interaction model to a simpler model at the collective level. Worked examples involving actor–critic systems and voting mechanisms show how the proposed perspective can be used.

Read this after the population studies to make the stronger claim of collective agency precise. The question becomes whether the collective model captures the relevant behavior across interventions. That supplies a standard against which a proposed group objective can be evaluated, beyond observing that several agents coordinate.

Jørgensen, F. H., Weichwald, S., and Hammond, L. (2026). Causal Foundations of Collective Agency. arXiv 2605.00248.

#### [Reconciling emergences: An information-theoretic approach to identify causal emergence in multivariate data](https://doi.org/10.1371/journal.pcbi.1008289)

Rosas, Mediano, Jensen et al. · 2020 | Importance 2/5 | Length 3/5: 1–2 hours

Rosas and colleagues develop an information-theoretic account of how macroscopic features relate to the dynamics of a system’s parts. Their framework distinguishes forms of causal emergence, including downward causation and causal decoupling, and applies them to examples such as flocking and neural activity.

Choose one example to follow the definitions through a concrete analysis. Compared with the collective-agency paper, the explanatory target is broader: the framework studies emergent dynamical organization without requiring a strategic objective. Reading the two together helps specify what a proposed collective description is meant to explain.

Rosas, F. E., Mediano, P. A. M., Jensen, H. J., et al. (2020). Reconciling emergences: An information-theoretic approach to identify causal emergence in multivariate data. PLOS Comput. Biol. 16.12, e1008289.

#### [The information theory of individuality](https://doi.org/10.1007/s12064-020-00313-7)

Krakauer, Bertschinger, Olbrich, Flack & Ay · 2020 | Importance 2/5 | Length 3/5: 1–2 hours

Krakauer and colleagues approach the boundary question through temporal information. They consider aggregates that preserve information from their past into their future, distinguishing forms of individuality according to environmental dependence and inherited information. A boundary drawn this way need not coincide with an obvious physical enclosure.

This adds a temporal criterion to the preceding accounts of collective organization. A collection of agents may coordinate briefly, or it may maintain a coherent pattern over time. The distinction matters when deciding whether a group is a useful enduring unit of analysis.

Krakauer, D., Bertschinger, N., Olbrich, E., Flack, J. C., and Ay, N. (2020). The information theory of individuality. Theory in Biosciences 139.2, pp. 209–223.

#### [The Computational Boundary of a “Self”](https://doi.org/10.3389/fpsyg.2019.02688)

Michael Levin · 2019 | Importance 1/5 | Length 3/5: 1–2 hours

Levin proposes understanding a self through the scale of the goals it can pursue and the events it can sense, model, and affect. His examples center on biological organization, including how the activities of cells contribute to larger coordinated systems. This is a conceptual extension for readers interested in where an agent’s boundary should be drawn.

Placed after the formal readings on agency, emergence, and individuality, it offers another criterion to compare with them: the spatial and temporal reach of goal-directed control. The biological examples motivate that perspective; an application to AI would have to establish the corresponding organization in the system being studied.

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

The range of explanations brings us back to the opening distinction between research questions. To compare them, state the behavior each account explains, the conditions it assumes, and the observation or intervention that would make its prediction fail.

## What have we learned about the interaction?

The collections approach interacting agents at different levels. Program equilibrium studies the incentives created by visible procedures. Learning dynamics follows changes in a population. Control and empirical games investigate an interaction through a chosen model and set of strategies. The agency readings examine how decisions can be organized; the descriptive readings ask which mechanisms account for what agents actually do.

Bring one result from each collection to the closing discussion. Explain how it was established and which further question it leaves you with. The table provides a starting comparison.

One useful final task is to choose two perspectives that bear on the same case. Explain what each contributes, then describe the additional model or experiment needed to connect their conclusions.
