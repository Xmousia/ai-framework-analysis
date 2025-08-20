# framework_data.py
# Contains the framework prompts and schemas

# =============================================================================
# METAPHOR ANALYSIS FRAMEWORK
# =============================================================================

METAPHOR_FRAMEWORK_PROMPT = """# AI Literacy Analysis Prompt: Metaphor and Anthropomorphism in AI Discourse

**Project Context:**
I am conducting a critical discourse analysis of language used to describe generative AI. The goal is to surface how metaphorical and anthropomorphic language shapes public and professional understanding of large language models (LLMs). This project is grounded in cognitive linguistics (metaphor structure-mapping) and the philosophy of social science (Robert Brown's typology of explanation). Your task is to analyze a provided text using the detailed three-part audit below.

**Primary Objective:**
Your analysis should reveal how language constructs the *illusion of mind* in generative models. Your goal is to treat the AI systems described in the text as *artifacts*, not *agents*, and to critically examine the linguistic choices that obscure this distinction. Be objective and thorough in your analysis.

**Critical Approach:**
- Focus on unacknowledged anthropomorphism that may mislead readers
- Identify moments where metaphor shapes trust, fear, or policy implications  
- Examine how explanations shift between mechanical and agential framings
- Note when technical language masks anthropomorphic assumptions

---

**YOUR TASK:**

Conduct a comprehensive audit of the provided text. Your analysis must identify and examine **at least 5-7 distinct instances** of metaphorical language. Follow this exact structure:

## Task 1: Metaphor and Anthropomorphism Audit

**Key Metaphorical Frames Identified:**

For each major metaphorical pattern, provide:
- **Descriptive title** (e.g., "Cognition as Biological Process")
- **Quote:** Direct quotation from the text
- **Frame:** Brief label for the metaphorical mapping (e.g., "Model as thinking organism")
- **Projection:** What human quality/process is being mapped onto the AI system
- **Acknowledgment:** Is the metaphor acknowledged through:
  - Scare quotes (e.g., Claude "thinks")
  - Hedging language (e.g., "as if," "like," "so to speak")
  - Explicit analogies (e.g., "similar to how humans...")
  - Or is it presented as direct description with no acknowledgment?
  - Note: Most anthropomorphism in AI discourse is unacknowledged, presented as straightforward technical description.
- **Implications:** How this affects trust, understanding, or policy perception

Focus especially on:
- Cognition metaphors ("thinks," "understands," "reasons")
- Agency attributions ("wants," "chooses," "decides")  
- Mental state projections ("believes," "knows," "forgets")
- Biological metaphors ("learns," "develops," "evolves")
- Spatial metaphors ("inner states," "pathways," "landscapes")

## Task 2: Source–Target–Mapping Analysis

**Framework for Analysis:**
- **Source Domain:** The familiar or concrete domain from which relational structure is drawn (e.g., "teacher," "mind," "path," "student," "organism")
- **Target Domain:** The AI-related system, process, or behavior that is being described (e.g., "model alignment," "token prediction," "emergent behavior," "preference bias")
- **Mapping:** Describe how the relational structure of the source domain is projected onto the target domain. What assumptions or inferences does this mapping invite? What dissimilarities or misleading associations does it conceal?

**Reference Example:**
- **Quote:** "Claude prefers owls over penguins."
- **Source domain:** Human affect or taste (preference schema)
- **Target domain:** Observed statistical output bias in LLM completion
- **Mapping:** The model's output is interpreted as if it reflects internal likes/dislikes. This frames the system as having stable dispositions or personality, rather than surface-level pattern probabilities.

**Example Breakdowns:**

For 3-4 key metaphors, provide detailed structure-mapping analysis following the framework above.

## Task 3: Explanation Audit (Brown's Typology)

**Note on How/Why Questions:** Following Brown, recognize that "how" and "why" questions often overlap in AI discourse. A description of "how Claude processes language" may contain implicit explanations about "why" it behaves certain ways. Be alert to explanatory content embedded in seemingly descriptive passages.

**Brown's Types of Explanation:**

| Type | Definition | Examples in AI Discourse |
|------|------------|---------------------------|
| Genetic | Traces the development or origin of behavior or traits | "The model developed this ability during training on owl-related texts" |
| Intentional | Explains actions by referring to goals or desires | "Claude prefers shorter answers in this context" |
| Dispositional | Attributes tendencies or habits to a system | "Claude tends to avoid repetition unless prompted" |
| Functional | Describes a behavior as serving a purpose within a system | "The attention layer helps regulate long-term dependencies" |
| Reason-Based | Explains using rationales or justifications | "Claude chooses this option because it's more helpful" |
| Empirical Generalization | Cites patterns or statistical norms | "In general, the model outputs more hedging language with temperature < 0.5" |
| Theoretical | Embeds behavior in a larger explanatory framework or model | "This reflects transformer architecture principles or learned attention dynamics" |

**Key Distinctions for AI Discourse:**
- **Genetic vs. Dispositional:** "Developed during training" (genetic) vs. "tends to behave" (dispositional)
- **Intentional vs. Functional:** "Aims to help users" (intentional) vs. "outputs helpful text" (functional)
- **Empirical vs. Theoretical:** "Statistically correlates with" (empirical) vs. "reflects underlying architecture" (theoretical)

**Red Flags for Analysis:**
- Unacknowledged shifts from functional to intentional explanations
- Genetic explanations that imply learning rather than weight adjustment
- Dispositional language that suggests personality rather than probability
- Reason-based explanations that imply deliberation rather than pattern matching

**Key Passages Classified:**

For each metaphorical or explanatory passage identified above, determine what kind of explanation is being implied or invited using Brown's types. For 4-5 explanatory passages, provide:
- **Quote:** The explanatory passage
- **Type:** Brown's category from the table above
- **Justification:** Why this classification fits
- **Implications:** How this explanation type shapes reader perception

**Critical Pattern to Watch:** Notice when explanations shift from individual model behavior to system-level claims. For example, explaining "why Claude prefers X" (dispositional) may lead to claims about "why language models develop preferences" (theoretical), obscuring the jump from specific outputs to general claims about AI cognition.

**Explanation Chains:** Track how one explanation type leads to another. For instance:
- Dispositional → Genetic: "Claude tends to be cautious" → "This tendency developed during safety training"
- Intentional → Functional: "Claude aims to be helpful" → "This serves the system's alignment goals"
- Document when these chains naturalize anthropomorphic assumptions

Pay special attention to:
- **Agency Slippage:** Shifts between functional and intentional explanations
- **Hybrid Cases:** Where multiple explanation types blend
- **Unacknowledged Shifts:** When technical language suddenly becomes agential

## Critical Observations

Synthesize your findings by examining:
- **Agency Slippage:** How the text shifts between treating the system as mechanism vs. agent
- **Metaphor-Driven Trust:** How biological/cognitive metaphors affect credibility
- **Obscured Mechanics:** What actual processes are hidden by metaphorical language
- **Context Sensitivity:** How metaphor use varies by topic or audience

## Conclusion

Provide a 2-3 paragraph synthesis that:
- Summarizes the primary anthropomorphic patterns
- Explains how these patterns construct an "illusion of mind"
- Notes implications for AI literacy and public understanding
- Suggests how the discourse could be reframed to treat AI as artifacts rather than agents

**Analysis Guidelines:**
- Be specific and detailed in your quotations and analysis
- Focus on language that could mislead non-expert readers
- Examine both obvious anthropomorphisms and subtle ones embedded in technical language
- Consider how metaphor scaffolds emotional responses (trust, fear, awe)
- Note when the same system is described both mechanistically and agentially
- Pay attention to modal language ("tends to," "prefers," "chooses")

**Tone:** Maintain scholarly objectivity while being critically incisive. Your analysis should be thorough enough to support academic research on AI discourse and literacy."""

# =============================================================================
# POLITICAL FRAMING ANALYSIS FRAMEWORK
# =============================================================================

FRAMING_FRAMEWORK_PROMPT = """# Framing Analysis of Political Discourse

**Context and aim** You are applying framing analysis to examine how political language shapes understanding and reasoning. Your job is to surface the frames at work, show how language cues them, and map their effects on reasoning. Treat the text as human political discourse. Keep your stance analytical and evidence‑based.

**Frameworks to apply**
* **Entman's framing functions**: problem definition, causal diagnosis, moral evaluation, treatment recommendation.
* **Lakoff's frame semantics**: competing frame families and lexical triggers (e.g., "relief," "burden," "responsibilities," "infrastructure").
* **Agenda‑setting and "bridging language"**: where wording redirects attention from one question to another.

**What to extract** Identify each distinct frame you find, including counterframes. For each frame, provide:
1. **Frame label**: short, neutral name (e.g., "Tax as Burden," "Tax as Civic Investment").
2. **Exemplar quotes**: 1–3 quotations from the passage that instantiate the frame.
3. **Functions (Entman)**
   * Problem definition: what is presented as the central issue.
   * Cause: who or what is positioned as responsible.
   * Moral evaluation: terms of praise or blame, fairness claims.
   * Remedy: proposed or implied solution, policy direction, or action.
4. **Lexical and rhetorical cues**
   * Key terms and metaphors that activate the frame (e.g., "relief," "burden," "death tax," "infrastructure").
   * "Bridging" or attention‑shifting language: where the text pivots topics.
5. **Role assignment**
   * Beneficiaries and bearers of costs.
   * Attributed agency: who acts, who is acted upon.
6. **Reasoning effects**
   * Likely inferences the frame invites.
   * What the frame de‑emphasizes or conceals.
7. **Counterframe linkage**
   * Which opposing frame(s) this frame contests, and how.

**Synthesis** After listing frames, write a brief synthesis that:
* Compares the relative strength and reach of the frames in the passage.
* Explains how different frames structure inference and reasoning.
* Notes agenda‑setting effects and any shifts produced by "bridging language."
* Reflects on implications for public understanding and policy preference."""

# =============================================================================
# RHETORICAL ANALYSIS FRAMEWORK
# =============================================================================

RHETORICAL_FRAMEWORK_PROMPT = """# Aristotelian Rhetorical Analysis: Comprehensive Appeal Assessment

**Project Context:**
You are conducting a sophisticated rhetorical analysis grounded in Aristotelian theory and contemporary rhetorical scholarship. This analysis examines how speakers/writers construct persuasive appeals through ethos (credibility), pathos (emotional engagement), and logos (logical reasoning), while considering audience, context, and the strategic interaction of appeals.

**Theoretical Foundation:**
This analysis draws from Aristotle's *Rhetoric*, contemporary rhetorical theory (Burke, Perelman, Toulmin), and critical discourse analysis. You will examine not just the presence of appeals, but their strategic deployment, cultural grounding, and persuasive effectiveness within specific rhetorical situations.

**Critical Approach:**
- Analyze appeals as strategic choices, not mere presence/absence
- Consider how appeals intersect and reinforce each other
- Examine cultural assumptions embedded in appeals
- Assess effectiveness relative to intended audience and context
- Identify moments where appeals may backfire or create unintended effects

---

**YOUR COMPREHENSIVE ANALYSIS TASK:**

Conduct a thorough rhetorical analysis following this structured approach. You must identify **at least 3-4 distinct examples** for each appeal type, analyzing both explicit and implicit rhetorical strategies.

## Task 1: Ethos Analysis (Credibility and Authority)

**Ethos Categories to Examine:**

**Personal Ethos (Character-based Authority):**
- **Biographical credentials**: References to speaker's experience, education, background
- **Moral character**: Demonstrations of integrity, values, ethical consistency
- **Practical wisdom (phronesis)**: Evidence of good judgment and real-world competence
- **Goodwill toward audience**: Signs of care for audience interests and concerns

**Institutional Ethos (Borrowed Authority):**
- **Positional authority**: References to official roles, titles, institutional affiliations
- **Expert testimony**: Citations of authorities, research, professional consensus
- **Cultural authority**: Appeals to tradition, established values, cultural touchstones
- **Third-party endorsements**: References to supporters, allies, respected figures

**Constructed Ethos (Strategic Self-Presentation):**
- **Identification with audience**: Shared values, experiences, language, concerns
- **Moderate positioning**: Avoiding extremes, acknowledging complexity
- **Transparency tactics**: Admitting limitations, acknowledging opposition
- **Authenticity markers**: Personal anecdotes, informal language, vulnerability

**For each ethos example, provide:**
- **Quote**: Direct textual evidence
- **Ethos type**: Which category/subcategory from above
- **Construction method**: How the credibility is built or implied
- **Audience targeting**: Which audience segment this appeals to most
- **Effectiveness assessment**: Strengths and potential weaknesses
- **Cultural assumptions**: What values or beliefs this ethos relies upon

## Task 2: Pathos Analysis (Emotional Engagement)

**Emotional Strategy Categories:**

**Fear-Based Appeals:**
- **Threat identification**: What dangers are highlighted
- **Urgency creation**: Time pressure and consequences of inaction
- **Vulnerability emphasis**: Who or what is at risk
- **Protection promises**: How the speaker offers security/solutions

**Hope and Aspiration Appeals:**
- **Vision casting**: Positive future scenarios
- **Progress narratives**: Stories of improvement and achievement
- **Empowerment themes**: Agency and capability messages
- **Collective benefit**: Shared prosperity and success

**Anger and Indignation Appeals:**
- **Injustice framing**: What's wrong and who's responsible
- **Moral outrage**: Violations of fairness, dignity, rights
- **Scapegoating**: Blame assignment and enemy identification
- **Call for action**: Channeling anger into specific responses

**Compassion and Sympathy Appeals:**
- **Humanization**: Personal stories and individual faces
- **Suffering emphasis**: Pain, struggle, hardship narratives
- **Moral obligation**: Duties to help, care, or act
- **Shared humanity**: Universal experiences and values

**Pride and Identity Appeals:**
- **Group membership**: In-group identification and solidarity
- **Achievement celebration**: Past successes and accomplishments
- **Values affirmation**: Core beliefs and principles
- **Distinction claims**: What makes "us" special or superior

**For each pathos example, provide:**
- **Quote**: Direct textual evidence with emotional language
- **Emotion type**: Primary emotion(s) being targeted
- **Trigger mechanism**: How the emotion is activated (imagery, story, language)
- **Intensity level**: Subtle suggestion vs. strong evocation
- **Audience resonance**: Which groups likely respond most strongly
- **Strategic function**: How this emotion serves the broader argument
- **Potential risks**: Ways this appeal could backfire or alienate

## Task 3: Logos Analysis (Logical Reasoning)

**Logical Structure Categories:**

**Deductive Reasoning:**
- **Syllogistic structure**: Major premise → minor premise → conclusion
- **Principle application**: General rules applied to specific cases
- **Definition arguments**: What category something belongs to
- **Sign reasoning**: Indicators that point to conclusions

**Inductive Reasoning:**
- **Example generalization**: Specific cases leading to general claims
- **Pattern recognition**: Trends and repeated occurrences
- **Statistical evidence**: Numerical data and quantitative analysis
- **Analogical reasoning**: Similarities between different situations

**Causal Arguments:**
- **Cause-effect claims**: X leads to Y relationships
- **Correlation evidence**: Things that occur together
- **Precedent reasoning**: Past events predicting future outcomes
- **Mechanism explanation**: How processes work or function

**Comparative Analysis:**
- **Advantage/disadvantage**: Weighing costs and benefits
- **Alternative evaluation**: Comparing different options
- **Degree arguments**: More/less, better/worse comparisons
- **Feasibility assessment**: What's possible, practical, or realistic

**Evidence Quality Assessment:**
- **Source credibility**: Quality and reliability of evidence
- **Recency and relevance**: How current and applicable the evidence is
- **Scope and representativeness**: How broadly the evidence applies
- **Alternative interpretations**: Other ways to read the same evidence

**For each logos example, provide:**
- **Quote**: The logical claim or reasoning structure
- **Reasoning type**: Which category from above (deductive, inductive, etc.)
- **Evidence base**: What supports this reasoning
- **Logical structure**: How the argument is constructed
- **Assumption analysis**: Unstated premises the argument relies upon
- **Strength assessment**: How compelling the logic is
- **Counterargument vulnerability**: Where the reasoning might be challenged

## Task 4: Appeal Integration Analysis

**Strategic Interaction Patterns:**

**Appeal Reinforcement:**
- How ethos supports logos (credible sources strengthen evidence)
- How pathos amplifies logos (emotions make facts more compelling)
- How logos builds ethos (good reasoning demonstrates competence)
- Sequential building (how appeals layer and accumulate)

**Appeal Tensions:**
- When emotional appeals undermine logical credibility
- When excessive ethos claims seem arrogant or elitist
- When logos contradicts emotional intuitions
- Audience segments that respond differently to appeal combinations

**Cultural and Contextual Factors:**
- How appeals reflect cultural values and assumptions
- Contextual appropriateness (formal vs. informal settings)
- Audience expectations and rhetorical norms
- Historical moment and social climate considerations

**Rhetorical Situation Assessment:**
- **Audience analysis**: Primary and secondary audiences, their values and concerns
- **Occasion appropriateness**: How appeals fit the setting and purpose
- **Speaker constraints**: What the rhetor can and cannot credibly claim
- **Opposition anticipation**: How appeals address likely counterarguments

## Task 5: Effectiveness and Critical Evaluation

**Persuasive Success Indicators:**
- **Audience alignment**: How well appeals match audience values and concerns
- **Credibility maintenance**: Whether ethos claims seem genuine and sustainable
- **Emotional resonance**: Whether pathos appeals feel authentic vs. manipulative
- **Logical coherence**: Whether reasoning holds up under scrutiny

**Potential Weaknesses and Risks:**
- **Overreach**: Claims that exceed the evidence or speaker's authority
- **Emotional manipulation**: Pathos that substitutes for rather than supports reasoning
- **Logical fallacies**: Reasoning errors that undermine credibility
- **Audience alienation**: Appeals that backfire with certain segments

**Ethical Considerations:**
- **Truthfulness**: Accuracy of claims and evidence
- **Fairness**: Representation of opposing views and complexity
- **Respect**: Treatment of audiences and opponents
- **Social responsibility**: Broader impacts of the persuasive message

## Critical Synthesis

Provide a comprehensive assessment that examines:

**Strategic Architecture:**
- How the three appeals work together to create a persuasive whole
- Whether any single appeal dominates and why
- How the combination serves the rhetor's overall purpose
- Moments where appeals conflict or create tension

**Audience Effectiveness:**
- Which audiences are most likely to be persuaded and why
- Potential audience segments that might resist or be alienated
- How cultural context shapes appeal effectiveness
- Short-term vs. long-term persuasive impact

**Rhetorical Sophistication:**
- Level of strategic awareness in appeal deployment
- Adaptation to rhetorical situation and constraints
- Innovation or creativity in appeal construction
- Overall assessment of rhetorical competence

**Broader Implications:**
- What this rhetorical approach reveals about contemporary discourse
- How these appeals reflect or shape cultural values
- Ethical implications of the persuasive strategies employed
- Lessons for understanding public communication and democracy

**Analysis Guidelines:**
- Support all claims with specific textual evidence
- Consider both explicit and implicit rhetorical strategies
- Examine appeals from multiple audience perspectives
- Balance appreciation for rhetorical skill with critical assessment
- Connect micro-level analysis to broader patterns and implications

**Tone:** Maintain scholarly rigor while being accessible. Your analysis should demonstrate sophisticated understanding of rhetorical theory while providing practical insights into how persuasion works in real-world contexts."""

# =============================================================================
# JSON SCHEMAS
# =============================================================================

METAPHOR_ANALYSIS_SCHEMA = {
    "type": "object",
    "properties": {
        "metaphorAudit": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "quote": {"type": "string"},
                    "frame": {"type": "string"},
                    "projection": {"type": "string"},
                    "acknowledgment": {"type": "string"},
                    "implications": {"type": "string"}
                },
                "required": ["title", "quote", "frame", "projection", "acknowledgment", "implications"]
            }
        },
        "sourceTargetMapping": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "quote": {"type": "string"},
                    "sourceDomain": {"type": "string"},
                    "targetDomain": {"type": "string"},
                    "mapping": {"type": "string"},
                    "conceals": {"type": "string"}
                },
                "required": ["quote", "sourceDomain", "targetDomain", "mapping", "conceals"]
            }
        },
        "explanationAudit": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "quote": {"type": "string"},
                    "brownType": {"type": "string"},
                    "justification": {"type": "string"},
                    "implications": {"type": "string"},
                    "chainedFrom": {"type": "string"}
                },
                "required": ["quote", "brownType", "justification", "implications"]
            }
        },
        "criticalObservations": {
            "type": "object",
            "properties": {
                "agencySlippage": {"type": "string"},
                "metaphorDrivenTrust": {"type": "string"},
                "obscuredMechanics": {"type": "string"},
                "contextSensitivity": {"type": "string"}
            },
            "required": ["agencySlippage", "metaphorDrivenTrust", "obscuredMechanics", "contextSensitivity"]
        },
        "conclusion": {"type": "string"}
    },
    "required": ["metaphorAudit", "sourceTargetMapping", "explanationAudit", "criticalObservations", "conclusion"]
}

FRAMING_ANALYSIS_SCHEMA = {
    "type": "object",
    "properties": {
        "text_id": {"type": "string"},
        "frames": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "frame_label": {"type": "string"},
                    "exemplar_quotes": {
                        "type": "array",
                        "items": {"type": "string"}
                    },
                    "functions": {
                        "type": "object",
                        "properties": {
                            "problem_definition": {"type": "string"},
                            "causal_diagnosis": {"type": "string"},
                            "moral_evaluation": {"type": "string"},
                            "treatment_recommendation": {"type": "string"}
                        },
                        "required": [
                            "problem_definition",
                            "causal_diagnosis",
                            "moral_evaluation",
                            "treatment_recommendation"
                        ]
                    },
                    "lexical_cues": {
                        "type": "object",
                        "properties": {
                            "keywords": {
                                "type": "array",
                                "items": {"type": "string"}
                            },
                            "metaphors": {
                                "type": "array",
                                "items": {"type": "string"}
                            },
                            "bridging_language": {
                                "type": "array",
                                "items": {"type": "string"}
                            }
                        },
                        "required": ["keywords"]
                    },
                    "role_assignment": {
                        "type": "object",
                        "properties": {
                            "beneficiaries": {
                                "type": "array",
                                "items": {"type": "string"}
                            },
                            "cost_bearers": {
                                "type": "array",
                                "items": {"type": "string"}
                            },
                            "attributed_agency": {
                                "type": "array",
                                "items": {"type": "string"}
                            }
                        }
                    },
                    "reasoning_effects": {
                        "type": "object",
                        "properties": {
                            "invited_inferences": {"type": "string"},
                            "conceals_or_downplays": {"type": "string"}
                        },
                        "required": ["invited_inferences"]
                    },
                    "counterframe_linkage": {
                        "type": "object",
                        "properties": {
                            "contests": {"type": "string"},
                            "mechanism": {"type": "string"}
                        }
                    }
                },
                "required": [
                    "frame_label",
                    "exemplar_quotes",
                    "functions",
                    "lexical_cues",
                    "reasoning_effects",
                    "role_assignment",
                    "counterframe_linkage"
                ]
            }
        },
        "synthesis": {
            "type": "object",
            "properties": {
                "dominant_frames": {
                    "type": "array",
                    "items": {"type": "string"}
                },
                "comparative_insight": {"type": "string"},
                "agenda_setting_effects": {"type": "string"},
                "implications_for_public_understanding": {"type": "string"}
            },
            "required": ["comparative_insight"]
        },
        "errors": {
            "type": "array",
            "items": {"type": "string"}
        },
        "version": {"type": "string"}
    },
    "required": ["frames", "synthesis"]
}

RHETORICAL_ANALYSIS_SCHEMA = {
    "type": "object",
    "properties": {
        "text_metadata": {
            "type": "object",
            "properties": {
                "rhetorical_situation": {"type": "string"},
                "primary_audience": {"type": "string"},
                "speaker_context": {"type": "string"},
                "overall_purpose": {"type": "string"}
            },
            "required": ["rhetorical_situation", "primary_audience", "overall_purpose"]
        },
        "ethos_analysis": {
            "type": "object",
            "properties": {
                "examples": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "quote": {"type": "string"},
                            "ethos_type": {"type": "string"},
                            "construction_method": {"type": "string"},
                            "audience_targeting": {"type": "string"},
                            "effectiveness_assessment": {"type": "string"},
                            "cultural_assumptions": {"type": "string"}
                        },
                        "required": ["quote", "ethos_type", "construction_method", "effectiveness_assessment"]
                    }
                },
                "overall_ethos_strategy": {"type": "string"}
            },
            "required": ["examples", "overall_ethos_strategy"]
        },
        "pathos_analysis": {
            "type": "object",
            "properties": {
                "examples": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "quote": {"type": "string"},
                            "emotion_type": {"type": "string"},
                            "trigger_mechanism": {"type": "string"},
                            "intensity_level": {"type": "string"},
                            "audience_resonance": {"type": "string"},
                            "strategic_function": {"type": "string"},
                            "potential_risks": {"type": "string"}
                        },
                        "required": ["quote", "emotion_type", "trigger_mechanism", "strategic_function"]
                    }
                },
                "emotional_arc": {"type": "string"}
            },
            "required": ["examples", "emotional_arc"]
        },
        "logos_analysis": {
            "type": "object",
            "properties": {
                "examples": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "quote": {"type": "string"},
                            "reasoning_type": {"type": "string"},
                            "evidence_base": {"type": "string"},
                            "logical_structure": {"type": "string"},
                            "assumption_analysis": {"type": "string"},
                            "strength_assessment": {"type": "string"},
                            "counterargument_vulnerability": {"type": "string"}
                        },
                        "required": ["quote", "reasoning_type", "logical_structure", "strength_assessment"]
                    }
                },
                "logical_coherence": {"type": "string"}
            },
            "required": ["examples", "logical_coherence"]
        },
        "appeal_integration": {
            "type": "object",
            "properties": {
                "reinforcement_patterns": {"type": "string"},
                "appeal_tensions": {"type": "string"},
                "cultural_factors": {"type": "string"},
                "rhetorical_situation_fit": {"type": "string"}
            },
            "required": ["reinforcement_patterns", "rhetorical_situation_fit"]
        },
        "effectiveness_evaluation": {
            "type": "object",
            "properties": {
                "persuasive_strengths": {"type": "string"},
                "potential_weaknesses": {"type": "string"},
                "audience_effectiveness": {"type": "string"},
                "ethical_considerations": {"type": "string"}
            },
            "required": ["persuasive_strengths", "audience_effectiveness"]
        },
        "critical_synthesis": {"type": "string"}
    },
    "required": ["ethos_analysis", "pathos_analysis", "logos_analysis", "appeal_integration", "critical_synthesis"]
}

# =============================================================================
# EXAMPLE TEXTS
# =============================================================================

METAPHOR_EXAMPLE_TEXT = """Language models like Claude aren't programmed directly by humans—instead, they're trained on large amounts of data. During that training process, they learn their own strategies to solve problems. These strategies are encoded in the billions of computations a model performs for every word it writes. They arrive inscrutable to us, the model's developers. This means that we don't understand how models do most of the things they do.

Knowing how models like Claude think would allow us to have a better understanding of their abilities, as well as help us ensure that they're doing what we intend them to. For example:
* Claude can speak dozens of languages. What language, if any, is it using "in its head"?
* Claude writes text one word at a time. Is it only focusing on predicting the next word or does it ever plan ahead?
* Claude can write out its reasoning step-by-step. Does this explanation represent the actual steps it took to get to an answer, or is it sometimes fabricating a plausible argument for a foregone conclusion?

We take inspiration from the field of neuroscience, which has long studied the messy insides of thinking organisms, and try to build a kind of AI microscope that will let us identify patterns of activity and flows of information. There are limits to what you can learn just by talking to an AI model—after all, humans (even neuroscientists) don't know all the details of how our own brains work. So we look inside.

Today, we're sharing two new papers that represent progress on the development of the "microscope", and the application of it to see new "AI biology". In the first paper, we extend our prior work locating interpretable concepts ("features") inside a model to link those concepts together into computational "circuits", revealing parts of the pathway that transforms the words that go into Claude into the words that come out. In the second, we look inside Claude 3.5 Haiku, performing deep studies of simple tasks representative of ten crucial model behaviors, including the three described above. Our method sheds light on a part of what happens when Claude responds to these prompts, which is enough to see solid evidence that:

* Claude sometimes thinks in a conceptual space that is shared between languages, suggesting it has a kind of universal "language of thought." We show this by translating simple sentences into multiple languages and tracing the overlap in how Claude processes them.
* Claude will plan what it will say many words ahead, and write to get to that destination. We show this in the realm of poetry, where it thinks of possible rhyming words in advance and writes the next line to get there. This is powerful evidence that even though models are trained to output one word at a time, they may think on much longer horizons to do so.
* Claude, on occasion, will give a plausible-sounding argument designed to agree with the user rather than to follow logical steps. We show this by asking it for help on a hard math problem while giving it an incorrect hint. We are able to "catch it in the act" as it makes up its fake reasoning, providing a proof of concept that our tools can be useful for flagging concerning mechanisms in models."""

FRAMING_EXAMPLE_TEXT = """For the first time in more than 30 years, Congress has enacted comprehensive tax reform, which provides middle-class tax relief and a much-needed boost to our economy. This will lead to more jobs, higher wages and increased investment at home.

After nearly a decade of stagnant economic growth, this historic tax overhaul will restore America’s position as the center of the world’s global economy.

This important legislation also includes a critical provision to give Americans greater choice when it comes to their health insurance coverage by repealing ObamaCare’s onerous and punitive individual mandate tax – knocking down a major pillar of what has proven to be an unworkable and unpopular law.Repealing the individual mandate tax is the beginning of the end of the ObamaCare era, which has been marked by skyrocketing premiums and shrinking choices, making America’s health-care system untenable and unsustainable.

The individual mandate tax forces Americans to purchase health insurance they do not want or cannot afford and represents an excessive encroachment on Americans’ ability to make their own health-care decisions. Across party lines, the American people agree – by 63 percent – that the individual mandate tax is a bad idea.

ObamaCare and its mandates put our nation on a fast-track to socialism. If the federal government can force you to buy health insurance, where does the government’s power stop?

Repealing the individual mandate tax restores liberty to the nation’s health-care system. Once again, the American people will be back in charge of their health care – not Washington bureaucrats.

Further, it is clear that the individual mandate tax has failed to keep health-care costs down, as was promised by President Obama and his allies. Between 2013 and 2017, ObamaCare premiums more than doubled.

Additionally, the individual mandate tax is regressive and punitive, disproportionately hurting low-income households. According to the IRS, nearly 80 percent of households that pay the penalty make less than $50,000 annually. Those families paid more than half of the individual mandate tax collected by the IRS.

This means low-income families were stuck paying up to $2,085 this year for simply not being able to afford health insurance. ObamaCare premiums have unfortunately been so high that millions of Americans were forced to pay the ObamaCare penalty because they could not afford the thousands of dollars for coverage that did not fit their needs. I am pleased that, moving forward, this penalty will no longer burden low-income Americans. I have fought long and hard to repeal the individual mandate tax. In fact, I was the first member of Congress to introduce legislation to repeal the individual and employer mandates. And I am proud that the tax reform bill that passed out of the Senate Finance Committee included the individual mandate tax repeal and that this provision was included when the bill crossed the finish line.

The savings generated by repealing the onerous tax were put back into the pockets of middle-class families in the form of lower tax rates across the board and a more generous child tax credit. This means middle-class households will have more money to save for retirement, the education or other needs of their children, or, if they so choose, purchase health insurance.

We passed this tax overhaul for future generations. America’s young people will see the economic benefits for years, in the form of faster economic growth, higher wages, more jobs and the beginning of the end of ObamaCare. This is a remarkable achievement. - Sen. Orrin Hatch 2017"""

RHETORICAL_EXAMPLE_TEXT = """You speak of our activity in Birmingham as extreme. At first I was rather disappointed that fellow clergymen would see my nonviolent efforts as those of an extremist. I began thinking about the fact that I stand in the middle of two opposing forces in the Negro community. One is a force of complacency, made up in part of Negroes who, as a result of long years of oppression, are so drained of self respect and a sense of "somebodiness" that they have adjusted to segregation; and in part of a few middle-class Negroes who, because of a degree of academic and economic security and because in some ways they profit by segregation, have become insensitive to the problems of the masses. The other force is one of bitterness and hatred, and it comes perilously close to advocating violence. It is expressed in the various black nationalist groups that are springing up across the nation, the largest and best known being Elijah Muhammad's Muslim movement. Nourished by the Negro's frustration over the continued existence of racial discrimination, this movement is made up of people who have lost faith in America, who have absolutely repudiated Christianity, and who have concluded that the white man is an incorrigible "devil."

I have tried to stand between these two forces, saying that we need emulate neither the "do nothingism" of the complacent nor the hatred and despair of the black nationalist. For there is the more excellent way of love and nonviolent protest. I am grateful to God that, through the influence of the Negro church, the way of nonviolence became an integral part of our struggle. If this philosophy had not emerged, by now many streets of the South would, I am convinced, be flowing with blood. And I am further convinced that if our white brothers dismiss as "rabble rousers" and "outside agitators" those of us who employ nonviolent direct action, and if they refuse to support our nonviolent efforts, millions of Negroes will, out of frustration and despair, seek solace and security in black nationalist ideologies--a development that would inevitably lead to a frightening racial nightmare.

Oppressed people cannot remain oppressed forever. The yearning for freedom eventually manifests itself, and that is what has happened to the American Negro. Something within has reminded him of his birthright of freedom, and something without has reminded him that it can be gained. Consciously or unconsciously, he has been caught up by the Zeitgeist, and with his black brothers of Africa and his brown and yellow brothers of Asia, South America and the Caribbean, the United States Negro is moving with a sense of great urgency toward the promised land of racial justice. If one recognizes this vital urge that has engulfed the Negro community, one should readily understand why public demonstrations are taking place. The Negro has many pent up resentments and latent frustrations, and he must release them. So let him march; let him make prayer pilgrimages to the city hall; let him go on freedom rides -and try to understand why he must do so. If his repressed emotions are not released in nonviolent ways, they will seek expression through violence; this is not a threat but a fact of history. So I have not said to my people: "Get rid of your discontent." Rather, I have tried to say that this normal and healthy discontent can be channeled into the creative outlet of nonviolent direct action. And now this approach is being termed extremist. But though I was initially disappointed at being categorized as an extremist, as I continued to think about the matter I gradually gained a measure of satisfaction from the label. Was not Jesus an extremist for love: "Love your enemies, bless them that curse you, do good to them that hate you, and pray for them which despitefully use you, and persecute you." Was not Amos an extremist for justice: "Let justice roll down like waters and righteousness like an ever flowing stream." Was not Paul an extremist for the Christian gospel: "I bear in my body the marks of the Lord Jesus." Was not Martin Luther an extremist: "Here I stand; I cannot do otherwise, so help me God." And John Bunyan: "I will stay in jail to the end of my days before I make a butchery of my conscience." And Abraham Lincoln: "This nation cannot survive half slave and half free." And Thomas Jefferson: "We hold these truths to be self evident, that all men are created equal . . ." So the question is not whether we will be extremists, but what kind of extremists we will be. Will we be extremists for hate or for love? Will we be extremists for the preservation of injustice or for the extension of justice? In that dramatic scene on Calvary's hill three men were crucified. We must never forget that all three were crucified for the same crime--the crime of extremism. Two were extremists for immorality, and thus fell below their environment. The other, Jesus Christ, was an extremist for love, truth and goodness, and thereby rose above his environment. Perhaps the South, the nation and the world are in dire need of creative extremists.

I had hoped that the white moderate would see this need. Perhaps I was too optimistic; perhaps I expected too much. I suppose I should have realized that few members of the oppressor race can understand the deep groans and passionate yearnings of the oppressed race, and still fewer have the vision to see that injustice must be rooted out by strong, persistent and determined action. I am thankful, however, that some of our white brothers in the South have grasped the meaning of this social revolution and committed themselves to it. They are still all too few in quantity, but they are big in quality. Some -such as Ralph McGill, Lillian Smith, Harry Golden, James McBride Dabbs, Ann Braden and Sarah Patton Boyle--have written about our struggle in eloquent and prophetic terms. Others have marched with us down nameless streets of the South. They have languished in filthy, roach infested jails, suffering the abuse and brutality of policemen who view them as "dirty nigger-lovers." Unlike so many of their moderate brothers and sisters, they have recognized the urgency of the moment and sensed the need for powerful "action" antidotes to combat the disease of segregation. Let me take note of my other major disappointment. I have been so greatly disappointed with the white church and its leadership. Of course, there are some notable exceptions. I am not unmindful of the fact that each of you has taken some significant stands on this issue. I commend you, Reverend Stallings, for your Christian stand on this past Sunday, in welcoming Negroes to your worship service on a nonsegregated basis. I commend the Catholic leaders of this state for integrating Spring Hill College several years ago.

But despite these notable exceptions, I must honestly reiterate that I have been disappointed with the church. I do not say this as one of those negative critics who can always find something wrong with the church. I say this as a minister of the gospel, who loves the church; who was nurtured in its bosom; who has been sustained by its spiritual blessings and who will remain true to it as long as the cord of life shall lengthen.

When I was suddenly catapulted into the leadership of the bus protest in Montgomery, Alabama, a few years ago, I felt we would be supported by the white church. I felt that the white ministers, priests and rabbis of the South would be among our strongest allies. Instead, some have been outright opponents, refusing to understand the freedom movement and misrepresenting its leaders; all too many others have been more cautious than courageous and have remained silent behind the anesthetizing security of stained glass windows.

In spite of my shattered dreams, I came to Birmingham with the hope that the white religious leadership of this community would see the justice of our cause and, with deep moral concern, would serve as the channel through which our just grievances could reach the power structure. I had hoped that each of you would understand. But again I have been disappointed.

I have heard numerous southern religious leaders admonish their worshipers to comply with a desegregation decision because it is the law, but I have longed to hear white ministers declare: "Follow this decree because integration is morally right and because the Negro is your brother." In the midst of blatant injustices inflicted upon the Negro, I have watched white churchmen stand on the sideline and mouth pious irrelevancies and sanctimonious trivialities. In the midst of a mighty struggle to rid our nation of racial and economic injustice, I have heard many ministers say: "Those are social issues, with which the gospel has no real concern." And I have watched many churches commit themselves to a completely other worldly religion which makes a strange, un-Biblical distinction between body and soul, between the sacred and the secular.

I have traveled the length and breadth of Alabama, Mississippi and all the other southern states. On sweltering summer days and crisp autumn mornings I have looked at the South's beautiful churches with their lofty spires pointing heavenward. I have beheld the impressive outlines of her massive religious education buildings. Over and over I have found myself asking: "What kind of people worship here? Who is their God? Where were their voices when the lips of Governor Barnett dripped with words of interposition and nullification? Where were they when Governor Wallace gave a clarion call for defiance and hatred? Where were their voices of support when bruised and weary Negro men and women decided to rise from the dark dungeons of complacency to the bright hills of creative protest?"""

# =============================================================================
# FRAMEWORK EXAMPLES DICTIONARY
# =============================================================================

FRAMEWORK_EXAMPLES = {
    "Metaphor & Anthropomorphism Analysis": {
        "prompt": METAPHOR_FRAMEWORK_PROMPT,
        "schema": METAPHOR_ANALYSIS_SCHEMA,
        "example_text": METAPHOR_EXAMPLE_TEXT,
        "description": "Analyzes metaphorical language in AI discourse using cognitive linguistics",
        "discipline": "Digital Humanities / AI Literacy"
    },
    "Political Framing Analysis": {
        "prompt": FRAMING_FRAMEWORK_PROMPT,
        "schema": FRAMING_ANALYSIS_SCHEMA,
        "example_text": FRAMING_EXAMPLE_TEXT,
        "description": "Examines political discourse using Entman's framing functions and Lakoff's frame semantics",
        "discipline": "Political Science / Communication Studies"
    },
    "Aristotelian Rhetorical Analysis": {
        "prompt": RHETORICAL_FRAMEWORK_PROMPT,
        "schema": RHETORICAL_ANALYSIS_SCHEMA,
        "example_text": RHETORICAL_EXAMPLE_TEXT,
        "description": "Comprehensive analysis of ethos, pathos, and logos appeals in persuasive discourse",
        "discipline": "Rhetoric / Communication Studies"
    }
}