# framework_data.py
# Contains the framework prompts and schemas

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

# framework_data.py
# Contains the framework prompts and schemas

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

# framework_data.py
# Contains the framework prompts and schemas

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

# New framing analysis example
FRAMING_FRAMEWORK_PROMPT = """# Framing Analysis of "Tax Relief" Discourse

**Context and aim** You are applying framing analysis to a short passage about tax policy that contrasts "tax relief" with alternative ways of describing taxation. Your job is to surface the frames at work, show how language cues them, and map their effects on reasoning. Treat the text as human political discourse. Keep your stance analytical and evidence‑based.

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
* Explains how "tax relief" structures inference compared to "tax as infrastructure/civic investment."
* Notes agenda‑setting effects and any shifts produced by "bridging language."
* Reflects on implications for public understanding and policy preference."""

# JSON Schemas
METAPHOR_ANALYSIS_SCHEMA = {
    "type": "object",  # Changed from "OBJECT"
    "properties": {
        "metaphorAudit": {
            "type": "array",  # Changed from "ARRAY"
            "items": {
                "type": "object",  # Changed from "OBJECT"
                "properties": {
                    "title": {"type": "string"},  # Changed from "STRING"
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
# Framework examples for the UI
FRAMEWORK_EXAMPLES = {
    "Metaphor & Anthropomorphism Analysis": {
        "prompt": METAPHOR_FRAMEWORK_PROMPT,
        "schema": METAPHOR_ANALYSIS_SCHEMA,
        "description": "Analyzes metaphorical language in AI discourse using cognitive linguistics",
        "discipline": "Digital Humanities / AI Literacy"
    },
    "Political Framing Analysis": {
        "prompt": FRAMING_FRAMEWORK_PROMPT,
        "schema": FRAMING_ANALYSIS_SCHEMA,
        "description": "Examines political discourse using Entman's framing functions and Lakoff's frame semantics",
        "discipline": "Political Science / Communication Studies"
    }
}