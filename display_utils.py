# display_utils.py
# Utilities for displaying analysis results with specialized formatters
# COMPLETE VERSION with full markdown report generation

import streamlit as st
from datetime import datetime

def display_metaphor_results(analysis):
    """
    Display metaphor analysis results in a structured format
    
    Args:
        analysis: The analysis dictionary with metaphor audit results
    """
    
    st.subheader("🔬 Metaphor Analysis Results")
    
    # Task 1: Metaphor Audit
    with st.expander("📂 Task 1: Metaphor & Anthropomorphism Audit", expanded=True):
        metaphor_audit = analysis.get('metaphorAudit', [])
        
        if metaphor_audit:
            st.write(f"**Found {len(metaphor_audit)} metaphorical patterns:**")
            
            for i, item in enumerate(metaphor_audit, 1):
                st.markdown(f"### {i}. {item.get('title', 'Untitled Pattern')}")
                
                col1, col2 = st.columns([1, 1])
                
                with col1:
                    st.markdown("**Quote:**")
                    st.info(f'"{item.get("quote", "N/A")}"')
                    
                    st.markdown("**Frame:**")
                    st.write(item.get('frame', 'N/A'))
                    
                    st.markdown("**Projection:**")
                    st.write(item.get('projection', 'N/A'))
                
                with col2:
                    st.markdown("**Acknowledgment:**")
                    st.write(item.get('acknowledgment', 'N/A'))
                    
                    st.markdown("**Implications:**")
                    st.write(item.get('implications', 'N/A'))
                
                if i < len(metaphor_audit):
                    st.divider()
        else:
            st.info("No metaphorical patterns identified in this analysis.")
    
    # Task 2: Source-Target Mapping
    with st.expander("📂 Task 2: Source-Target Mapping Analysis", expanded=True):
        source_target = analysis.get('sourceTargetMapping', [])
        
        if source_target:
            st.write(f"**Found {len(source_target)} detailed mappings:**")
            
            for i, item in enumerate(source_target, 1):
                st.markdown(f"### Mapping {i}")
                
                st.markdown("**Quote:**")
                st.info(f'"{item.get("quote", "N/A")}"')
                
                col1, col2 = st.columns([1, 1])
                
                with col1:
                    st.markdown("**Source Domain:**")
                    st.write(item.get('sourceDomain', 'N/A'))
                    
                    st.markdown("**Target Domain:**")
                    st.write(item.get('targetDomain', 'N/A'))
                
                with col2:
                    st.markdown("**Mapping Process:**")
                    st.write(item.get('mapping', 'N/A'))
                    
                    st.markdown("**What It Conceals:**")
                    st.write(item.get('conceals', 'N/A'))
                
                if i < len(source_target):
                    st.divider()
        else:
            st.info("No detailed source-target mappings provided.")
    
    # Task 3: Explanation Audit
    with st.expander("📂 Task 3: Explanation Audit (Brown's Typology)", expanded=True):
        explanation_audit = analysis.get('explanationAudit', [])
        
        if explanation_audit:
            st.write(f"**Found {len(explanation_audit)} explanatory passages:**")
            
            for i, item in enumerate(explanation_audit, 1):
                st.markdown(f"### Explanation {i}")
                
                st.markdown("**Quote:**")
                st.info(f'"{item.get("quote", "N/A")}"')
                
                col1, col2 = st.columns([1, 1])
                
                with col1:
                    st.markdown("**Brown's Type:**")
                    explanation_type = item.get('brownType', 'N/A')
                    st.markdown(f"**`{explanation_type}`**")
                    
                    st.markdown("**Justification:**")
                    st.write(item.get('justification', 'N/A'))
                
                with col2:
                    st.markdown("**Implications:**")
                    st.write(item.get('implications', 'N/A'))
                    
                    if item.get('chainedFrom'):
                        st.markdown("**Chained From:**")
                        st.write(item.get('chainedFrom'))
                
                if i < len(explanation_audit):
                    st.divider()
        else:
            st.info("No explanatory passages analyzed.")
    
    # Critical Observations
    with st.expander("📂 Critical Observations", expanded=True):
        obs = analysis.get('criticalObservations', {})
        
        if obs and any(obs.values()):
            col1, col2 = st.columns([1, 1])
            
            with col1:
                st.markdown("**Agency Slippage:**")
                st.write(obs.get('agencySlippage', 'Not analyzed'))
                
                st.markdown("**Metaphor-Driven Trust:**")
                st.write(obs.get('metaphorDrivenTrust', 'Not analyzed'))
            
            with col2:
                st.markdown("**Obscured Mechanics:**")
                st.write(obs.get('obscuredMechanics', 'Not analyzed'))
                
                st.markdown("**Context Sensitivity:**")
                st.write(obs.get('contextSensitivity', 'Not analyzed'))
        else:
            st.info("No critical observations provided.")
    
    # Conclusion
    with st.expander("📂 Conclusion", expanded=True):
        conclusion = analysis.get('conclusion', 'No conclusion provided.')
        if conclusion and conclusion != 'No conclusion provided.':
            st.write(conclusion)
        else:
            st.info("No conclusion provided in this analysis.")


def display_framing_results(analysis):
    """
    Display political framing analysis results in a structured format
    
    Args:
        analysis: The analysis dictionary with framing analysis results
    """
    
    st.subheader("🎯 Political Framing Analysis Results")
    
    # Overview metrics
    frames = analysis.get('frames', [])
    text_id = analysis.get('text_id', 'N/A')
    
    if text_id != 'N/A':
        st.info(f"**Text ID:** {text_id}")
    
    if frames:
        st.success(f"**Found {len(frames)} distinct frames in the discourse**")
        
        # Individual Frame Analysis
        st.markdown("### 📋 Individual Frame Analysis")
        
        for i, frame in enumerate(frames, 1):
            frame_label = frame.get('frame_label', f'Frame {i}')
            
            with st.expander(f"🔍 Frame {i}: {frame_label}", expanded=True):
                
                # Exemplar Quotes Section
                quotes = frame.get('exemplar_quotes', [])
                if quotes:
                    st.markdown("**📝 Key Quotes:**")
                    for j, quote in enumerate(quotes, 1):
                        st.info(f"{j}. \"{quote}\"")
                
                # Entman's Functions in organized layout
                functions = frame.get('functions', {})
                if functions:
                    st.markdown("**🔧 Entman's Framing Functions:**")
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.markdown("**Problem Definition:**")
                        st.write(functions.get('problem_definition', 'Not specified'))
                        
                        st.markdown("**Causal Diagnosis:**")
                        st.write(functions.get('causal_diagnosis', 'Not specified'))
                    
                    with col2:
                        st.markdown("**Moral Evaluation:**")
                        st.write(functions.get('moral_evaluation', 'Not specified'))
                        
                        st.markdown("**Treatment Recommendation:**")
                        st.write(functions.get('treatment_recommendation', 'Not specified'))
                
                # Lexical Cues in structured format
                lexical_cues = frame.get('lexical_cues', {})
                if lexical_cues:
                    st.markdown("**🏷️ Lexical & Rhetorical Cues:**")
                    
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        keywords = lexical_cues.get('keywords', [])
                        if keywords:
                            st.markdown("**Keywords:**")
                            for keyword in keywords:
                                st.markdown(f"• `{keyword}`")
                    
                    with col2:
                        metaphors = lexical_cues.get('metaphors', [])
                        if metaphors:
                            st.markdown("**Metaphors:**")
                            for metaphor in metaphors:
                                st.markdown(f"• *{metaphor}*")
                    
                    with col3:
                        bridging = lexical_cues.get('bridging_language', [])
                        if bridging:
                            st.markdown("**Bridging Language:**")
                            for bridge in bridging:
                                st.markdown(f"• **{bridge}**")
                
                # Role Assignment Table
                role_assignment = frame.get('role_assignment', {})
                if role_assignment and any(role_assignment.values()):
                    st.markdown("**👥 Role Assignment:**")
                    
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        beneficiaries = role_assignment.get('beneficiaries', [])
                        if beneficiaries:
                            st.markdown("**Beneficiaries:**")
                            for beneficiary in beneficiaries:
                                st.markdown(f"✅ {beneficiary}")
                    
                    with col2:
                        cost_bearers = role_assignment.get('cost_bearers', [])
                        if cost_bearers:
                            st.markdown("**Cost Bearers:**")
                            for bearer in cost_bearers:
                                st.markdown(f"❌ {bearer}")
                    
                    with col3:
                        agency = role_assignment.get('attributed_agency', [])
                        if agency:
                            st.markdown("**Attributed Agency:**")
                            for agent in agency:
                                st.markdown(f"⚡ {agent}")
                
                # Reasoning Effects
                reasoning = frame.get('reasoning_effects', {})
                if reasoning:
                    st.markdown("**🧠 Reasoning Effects:**")
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        inferences = reasoning.get('invited_inferences', 'Not specified')
                        st.markdown("**Invited Inferences:**")
                        st.write(inferences)
                    
                    with col2:
                        conceals = reasoning.get('conceals_or_downplays', 'Not specified')
                        if conceals != 'Not specified':
                            st.markdown("**Conceals/Downplays:**")
                            st.write(conceals)
                
                # Counterframe Linkage
                counterframe = frame.get('counterframe_linkage', {})
                if counterframe and any(counterframe.values()):
                    st.markdown("**⚔️ Counterframe Analysis:**")
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        contests = counterframe.get('contests', 'Not specified')
                        if contests != 'Not specified':
                            st.markdown("**Contests:**")
                            st.write(contests)
                    
                    with col2:
                        mechanism = counterframe.get('mechanism', 'Not specified')
                        if mechanism != 'Not specified':
                            st.markdown("**Mechanism:**")
                            st.write(mechanism)
                
                # Add divider between frames (except for last one)
                if i < len(frames):
                    st.divider()
    
    else:
        st.warning("No frames identified in this analysis.")
    
    # Synthesis Section
    synthesis = analysis.get('synthesis', {})
    if synthesis:
        st.markdown("### 🔄 Synthesis & Analysis")
        
        with st.expander("📊 Comparative Insights & Implications", expanded=True):
            
            # Dominant frames
            dominant_frames = synthesis.get('dominant_frames', [])
            if dominant_frames:
                st.markdown("**🏆 Dominant Frames:**")
                for i, frame in enumerate(dominant_frames, 1):
                    st.markdown(f"{i}. **{frame}**")
                st.markdown("")
            
            # Comparative insight
            comparative = synthesis.get('comparative_insight', 'Not provided')
            if comparative != 'Not provided':
                st.markdown("**🔍 Comparative Analysis:**")
                st.write(comparative)
                st.markdown("")
            
            # Agenda setting effects
            agenda_effects = synthesis.get('agenda_setting_effects', 'Not provided')
            if agenda_effects != 'Not provided':
                st.markdown("**📺 Agenda-Setting Effects:**")
                st.write(agenda_effects)
                st.markdown("")
            
            # Implications
            implications = synthesis.get('implications_for_public_understanding', 'Not provided')
            if implications != 'Not provided':
                st.markdown("**🎯 Implications for Public Understanding:**")
                st.write(implications)
    
    # Errors section (if any)
    errors = analysis.get('errors', [])
    if errors:
        st.markdown("### ⚠️ Analysis Notes")
        with st.expander("🔧 Processing Notes", expanded=False):
            for error in errors:
                st.warning(f"• {error}")


def display_rhetorical_results(analysis):
    """
    Display rhetorical analysis results in a structured format
    
    Args:
        analysis: The analysis dictionary with rhetorical analysis results
    """
    
    st.subheader("🎭 Rhetorical Analysis Results")
    
    # Text Metadata
    metadata = analysis.get('text_metadata', {})
    if metadata:
        with st.expander("📋 Rhetorical Situation", expanded=True):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Rhetorical Situation:**")
                st.write(metadata.get('rhetorical_situation', 'Not specified'))
                
                st.markdown("**Primary Audience:**")
                st.write(metadata.get('primary_audience', 'Not specified'))
            
            with col2:
                speaker_context = metadata.get('speaker_context', 'Not specified')
                if speaker_context != 'Not specified':
                    st.markdown("**Speaker Context:**")
                    st.write(speaker_context)
                
                st.markdown("**Overall Purpose:**")
                st.write(metadata.get('overall_purpose', 'Not specified'))
    
    # Ethos Analysis
    ethos_analysis = analysis.get('ethos_analysis', {})
    if ethos_analysis:
        with st.expander("👑 Ethos Analysis (Credibility & Authority)", expanded=True):
            examples = ethos_analysis.get('examples', [])
            
            if examples:
                st.write(f"**Found {len(examples)} ethos appeals:**")
                
                for i, example in enumerate(examples, 1):
                    st.markdown(f"### Example {i}")
                    
                    # Quote
                    quote = example.get('quote', 'No quote provided')
                    st.info(f'"{quote}"')
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.markdown("**Ethos Type:**")
                        st.markdown(f"**`{example.get('ethos_type', 'Not specified')}`**")
                        
                        st.markdown("**Construction Method:**")
                        st.write(example.get('construction_method', 'Not specified'))
                        
                        st.markdown("**Audience Targeting:**")
                        st.write(example.get('audience_targeting', 'Not specified'))
                    
                    with col2:
                        st.markdown("**Effectiveness Assessment:**")
                        st.write(example.get('effectiveness_assessment', 'Not specified'))
                        
                        cultural_assumptions = example.get('cultural_assumptions', 'Not specified')
                        if cultural_assumptions != 'Not specified':
                            st.markdown("**Cultural Assumptions:**")
                            st.write(cultural_assumptions)
                    
                    if i < len(examples):
                        st.divider()
            
            # Overall strategy
            overall_strategy = ethos_analysis.get('overall_ethos_strategy', 'Not provided')
            if overall_strategy != 'Not provided':
                st.markdown("**🎯 Overall Ethos Strategy:**")
                st.write(overall_strategy)
    
    # Pathos Analysis
    pathos_analysis = analysis.get('pathos_analysis', {})
    if pathos_analysis:
        with st.expander("❤️ Pathos Analysis (Emotional Engagement)", expanded=True):
            examples = pathos_analysis.get('examples', [])
            
            if examples:
                st.write(f"**Found {len(examples)} pathos appeals:**")
                
                for i, example in enumerate(examples, 1):
                    st.markdown(f"### Example {i}")
                    
                    # Quote
                    quote = example.get('quote', 'No quote provided')
                    st.info(f'"{quote}"')
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.markdown("**Emotion Type:**")
                        st.markdown(f"**`{example.get('emotion_type', 'Not specified')}`**")
                        
                        st.markdown("**Trigger Mechanism:**")
                        st.write(example.get('trigger_mechanism', 'Not specified'))
                        
                        st.markdown("**Intensity Level:**")
                        st.write(example.get('intensity_level', 'Not specified'))
                    
                    with col2:
                        st.markdown("**Audience Resonance:**")
                        st.write(example.get('audience_resonance', 'Not specified'))
                        
                        st.markdown("**Strategic Function:**")
                        st.write(example.get('strategic_function', 'Not specified'))
                        
                        potential_risks = example.get('potential_risks', 'Not specified')
                        if potential_risks != 'Not specified':
                            st.markdown("**Potential Risks:**")
                            st.write(potential_risks)
                    
                    if i < len(examples):
                        st.divider()
            
            # Emotional arc
            emotional_arc = pathos_analysis.get('emotional_arc', 'Not provided')
            if emotional_arc != 'Not provided':
                st.markdown("**📈 Emotional Arc:**")
                st.write(emotional_arc)
    
    # Logos Analysis
    logos_analysis = analysis.get('logos_analysis', {})
    if logos_analysis:
        with st.expander("🧠 Logos Analysis (Logical Reasoning)", expanded=True):
            examples = logos_analysis.get('examples', [])
            
            if examples:
                st.write(f"**Found {len(examples)} logos appeals:**")
                
                for i, example in enumerate(examples, 1):
                    st.markdown(f"### Example {i}")
                    
                    # Quote
                    quote = example.get('quote', 'No quote provided')
                    st.info(f'"{quote}"')
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.markdown("**Reasoning Type:**")
                        st.markdown(f"**`{example.get('reasoning_type', 'Not specified')}`**")
                        
                        st.markdown("**Evidence Base:**")
                        st.write(example.get('evidence_base', 'Not specified'))
                        
                        st.markdown("**Logical Structure:**")
                        st.write(example.get('logical_structure', 'Not specified'))
                    
                    with col2:
                        assumption_analysis = example.get('assumption_analysis', 'Not specified')
                        if assumption_analysis != 'Not specified':
                            st.markdown("**Assumption Analysis:**")
                            st.write(assumption_analysis)
                        
                        st.markdown("**Strength Assessment:**")
                        st.write(example.get('strength_assessment', 'Not specified'))
                        
                        vulnerability = example.get('counterargument_vulnerability', 'Not specified')
                        if vulnerability != 'Not specified':
                            st.markdown("**Counterargument Vulnerability:**")
                            st.write(vulnerability)
                    
                    if i < len(examples):
                        st.divider()
            
            # Logical coherence
            logical_coherence = logos_analysis.get('logical_coherence', 'Not provided')
            if logical_coherence != 'Not provided':
                st.markdown("**⚖️ Logical Coherence:**")
                st.write(logical_coherence)
    
    # Appeal Integration
    integration = analysis.get('appeal_integration', {})
    if integration:
        with st.expander("🔗 Appeal Integration Analysis", expanded=True):
            col1, col2 = st.columns(2)
            
            with col1:
                reinforcement = integration.get('reinforcement_patterns', 'Not specified')
                if reinforcement != 'Not specified':
                    st.markdown("**🤝 Reinforcement Patterns:**")
                    st.write(reinforcement)
                
                cultural_factors = integration.get('cultural_factors', 'Not specified')
                if cultural_factors != 'Not specified':
                    st.markdown("**🌍 Cultural Factors:**")
                    st.write(cultural_factors)
            
            with col2:
                tensions = integration.get('appeal_tensions', 'Not specified')
                if tensions != 'Not specified':
                    st.markdown("**⚡ Appeal Tensions:**")
                    st.write(tensions)
                
                situation_fit = integration.get('rhetorical_situation_fit', 'Not specified')
                if situation_fit != 'Not specified':
                    st.markdown("**🎯 Rhetorical Situation Fit:**")
                    st.write(situation_fit)
    
    # Effectiveness Evaluation
    effectiveness = analysis.get('effectiveness_evaluation', {})
    if effectiveness:
        with st.expander("📊 Effectiveness Evaluation", expanded=True):
            col1, col2 = st.columns(2)
            
            with col1:
                strengths = effectiveness.get('persuasive_strengths', 'Not specified')
                if strengths != 'Not specified':
                    st.markdown("**💪 Persuasive Strengths:**")
                    st.write(strengths)
                
                audience_effectiveness = effectiveness.get('audience_effectiveness', 'Not specified')
                if audience_effectiveness != 'Not specified':
                    st.markdown("**🎯 Audience Effectiveness:**")
                    st.write(audience_effectiveness)
            
            with col2:
                weaknesses = effectiveness.get('potential_weaknesses', 'Not specified')
                if weaknesses != 'Not specified':
                    st.markdown("**⚠️ Potential Weaknesses:**")
                    st.write(weaknesses)
                
                ethical_considerations = effectiveness.get('ethical_considerations', 'Not specified')
                if ethical_considerations != 'Not specified':
                    st.markdown("**⚖️ Ethical Considerations:**")
                    st.write(ethical_considerations)
    
    # Critical Synthesis
    synthesis = analysis.get('critical_synthesis', 'No synthesis provided.')
    if synthesis != 'No synthesis provided.':
        with st.expander("🎯 Critical Synthesis", expanded=True):
            st.write(synthesis)


def create_markdown_report(result):
    """
    Generate a comprehensive markdown report from analysis results
    
    Args:
        result: The analysis result dictionary
        
    Returns:
        str: Formatted markdown report matching web display exactly
    """
    
    analysis = result['analysis']
    timestamp_formatted = datetime.strptime(result['timestamp'], '%Y%m%d_%H%M%S').strftime('%Y-%m-%d %H:%M:%S')
    
    # Start building the report
    markdown = f"""# AI Framework Analysis Report

**Generated:** {timestamp_formatted}  
**Model:** {result['model']}  
**Text Length:** {result['text_length']:,} characters  
**Output Format:** {'Structured' if result.get('use_json') else 'Text'}  
"""
    
    if result.get('metadata', {}).get('total_tokens'):
        markdown += f"**Tokens Used:** {result['metadata']['total_tokens']:,}  \n"
    
    markdown += "\n---\n\n"
    
    # Check analysis type and format accordingly
    if isinstance(analysis, dict):
        # Check for different framework types
        if 'metaphorAudit' in analysis:
            markdown += "## 🔬 Metaphor Analysis Results\n\n"
            markdown += _format_metaphor_analysis_markdown(analysis)
            
        elif 'frames' in analysis:
            markdown += "## 🎯 Political Framing Analysis Results\n\n"
            markdown += _format_framing_analysis_markdown(analysis)
            
        elif 'ethos_analysis' in analysis:
            markdown += "## 🎭 Rhetorical Analysis Results\n\n"
            markdown += _format_rhetorical_analysis_markdown(analysis)
            
        else:
            # Generic structured analysis
            markdown += "## Analysis Results\n\n"
            markdown += _format_generic_analysis_markdown(analysis)
    
    else:
        # Freeform text analysis
        markdown += "## Analysis Results\n\n"
        markdown += str(analysis) + "\n\n"
    
    # Add metadata section
    markdown += "\n---\n\n## Analysis Metadata\n\n"
    markdown += f"- **Model Used:** {result['model']}\n"
    markdown += f"- **Generated:** {timestamp_formatted}\n"
    markdown += f"- **Text Length:** {result['text_length']:,} characters\n"
    
    if result.get('metadata', {}).get('total_tokens'):
        markdown += f"- **Total Tokens:** {result['metadata']['total_tokens']:,}\n"
    
    markdown += f"\n*Generated by AI Framework Analysis Tool*\n"
    
    return markdown


def _format_metaphor_analysis_markdown(analysis):
    """
    Format metaphor analysis for comprehensive markdown report
    
    Args:
        analysis: Dictionary containing metaphor analysis results
        
    Returns:
        str: Formatted markdown content
    """
    markdown = ""
    
    # Task 1: Metaphor Audit
    markdown += "### Task 1: Metaphor & Anthropomorphism Audit\n\n"
    metaphor_audit = analysis.get('metaphorAudit', [])
    
    if metaphor_audit:
        markdown += f"**Found {len(metaphor_audit)} metaphorical patterns:**\n\n"
        
        for i, item in enumerate(metaphor_audit, 1):
            markdown += f"#### {i}. {item.get('title', 'Untitled Pattern')}\n\n"
            markdown += f"**Quote:** \"{item.get('quote', 'N/A')}\"\n\n"
            markdown += f"**Frame:** {item.get('frame', 'N/A')}\n\n"
            markdown += f"**Projection:** {item.get('projection', 'N/A')}\n\n"
            markdown += f"**Acknowledgment:** {item.get('acknowledgment', 'N/A')}\n\n"
            markdown += f"**Implications:** {item.get('implications', 'N/A')}\n\n"
            if i < len(metaphor_audit):
                markdown += "---\n\n"
    else:
        markdown += "*No metaphorical patterns identified in this analysis.*\n\n"
    
    # Task 2: Source-Target Mapping
    markdown += "### Task 2: Source-Target Mapping Analysis\n\n"
    source_target = analysis.get('sourceTargetMapping', [])
    
    if source_target:
        markdown += f"**Found {len(source_target)} detailed mappings:**\n\n"
        
        for i, item in enumerate(source_target, 1):
            markdown += f"#### Mapping {i}\n\n"
            markdown += f"**Quote:** \"{item.get('quote', 'N/A')}\"\n\n"
            markdown += f"**Source Domain:** {item.get('sourceDomain', 'N/A')}\n\n"
            markdown += f"**Target Domain:** {item.get('targetDomain', 'N/A')}\n\n"
            markdown += f"**Mapping Process:** {item.get('mapping', 'N/A')}\n\n"
            markdown += f"**What It Conceals:** {item.get('conceals', 'N/A')}\n\n"
            if i < len(source_target):
                markdown += "---\n\n"
    else:
        markdown += "*No detailed source-target mappings provided.*\n\n"
    
    # Task 3: Explanation Audit
    markdown += "### Task 3: Explanation Audit (Brown's Typology)\n\n"
    explanation_audit = analysis.get('explanationAudit', [])
    
    if explanation_audit:
        markdown += f"**Found {len(explanation_audit)} explanatory passages:**\n\n"
        
        for i, item in enumerate(explanation_audit, 1):
            markdown += f"#### Explanation {i}\n\n"
            markdown += f"**Quote:** \"{item.get('quote', 'N/A')}\"\n\n"
            markdown += f"**Brown's Type:** `{item.get('brownType', 'N/A')}`\n\n"
            markdown += f"**Justification:** {item.get('justification', 'N/A')}\n\n"
            markdown += f"**Implications:** {item.get('implications', 'N/A')}\n\n"
            
            if item.get('chainedFrom'):
                markdown += f"**Chained From:** {item.get('chainedFrom')}\n\n"
            
            if i < len(explanation_audit):
                markdown += "---\n\n"
    else:
        markdown += "*No explanatory passages analyzed.*\n\n"
    
    # Critical Observations
    markdown += "### Critical Observations\n\n"
    obs = analysis.get('criticalObservations', {})
    
    if obs and any(obs.values()):
        markdown += "**Agency Slippage:** " + obs.get('agencySlippage', 'Not analyzed') + "\n\n"
        markdown += "**Metaphor-Driven Trust:** " + obs.get('metaphorDrivenTrust', 'Not analyzed') + "\n\n"
        markdown += "**Obscured Mechanics:** " + obs.get('obscuredMechanics', 'Not analyzed') + "\n\n"
        markdown += "**Context Sensitivity:** " + obs.get('contextSensitivity', 'Not analyzed') + "\n\n"
    else:
        markdown += "*No critical observations provided.*\n\n"
    
    # Conclusion
    markdown += "### Conclusion\n\n"
    conclusion = analysis.get('conclusion', 'No conclusion provided.')
    if conclusion and conclusion != 'No conclusion provided.':
        markdown += conclusion + "\n\n"
    else:
        markdown += "*No conclusion provided in this analysis.*\n\n"
    
    return markdown


def _format_framing_analysis_markdown(analysis):
    """
    Format framing analysis for comprehensive markdown report
    
    Args:
        analysis: Dictionary containing framing analysis results
        
    Returns:
        str: Formatted markdown content
    """
    markdown = ""
    
    frames = analysis.get('frames', [])
    text_id = analysis.get('text_id', 'N/A')
    
    # Overview section
    if text_id != 'N/A':
        markdown += f"**Text ID:** {text_id}\n\n"
    
    markdown += f"**Frames Identified:** {len(frames)}\n\n"
    
    if frames:
        markdown += "### Individual Frame Analysis\n\n"
        
        for i, frame in enumerate(frames, 1):
            frame_label = frame.get('frame_label', f'Frame {i}')
            markdown += f"## Frame {i}: {frame_label}\n\n"
            
            # Exemplar Quotes Section
            quotes = frame.get('exemplar_quotes', [])
            if quotes:
                markdown += "**📝 Key Quotes:**\n\n"
                for j, quote in enumerate(quotes, 1):
                    markdown += f"{j}. \"{quote}\"\n\n"
            
            # Entman's Functions
            functions = frame.get('functions', {})
            if functions:
                markdown += "**🔧 Entman's Framing Functions:**\n\n"
                markdown += f"- **Problem Definition:** {functions.get('problem_definition', 'Not specified')}\n"
                markdown += f"- **Causal Diagnosis:** {functions.get('causal_diagnosis', 'Not specified')}\n"
                markdown += f"- **Moral Evaluation:** {functions.get('moral_evaluation', 'Not specified')}\n"
                markdown += f"- **Treatment Recommendation:** {functions.get('treatment_recommendation', 'Not specified')}\n\n"
            
            # Lexical Cues
            lexical_cues = frame.get('lexical_cues', {})
            if lexical_cues:
                markdown += "**🏷️ Lexical & Rhetorical Cues:**\n\n"
                
                keywords = lexical_cues.get('keywords', [])
                if keywords:
                    markdown += "**Keywords:** "
                    markdown += ", ".join([f"`{keyword}`" for keyword in keywords]) + "\n\n"
                
                metaphors = lexical_cues.get('metaphors', [])
                if metaphors:
                    markdown += "**Metaphors:** "
                    markdown += ", ".join([f"*{metaphor}*" for metaphor in metaphors]) + "\n\n"
                
                bridging = lexical_cues.get('bridging_language', [])
                if bridging:
                    markdown += "**Bridging Language:** "
                    markdown += ", ".join([f"**{bridge}**" for bridge in bridging]) + "\n\n"
            
            # Role Assignment
            role_assignment = frame.get('role_assignment', {})
            if role_assignment and any(role_assignment.values()):
                markdown += "**👥 Role Assignment:**\n\n"
                
                beneficiaries = role_assignment.get('beneficiaries', [])
                if beneficiaries:
                    markdown += "**Beneficiaries:**\n"
                    for beneficiary in beneficiaries:
                        markdown += f"- ✅ {beneficiary}\n"
                    markdown += "\n"
                
                cost_bearers = role_assignment.get('cost_bearers', [])
                if cost_bearers:
                    markdown += "**Cost Bearers:**\n"
                    for bearer in cost_bearers:
                        markdown += f"- ❌ {bearer}\n"
                    markdown += "\n"
                
                agency = role_assignment.get('attributed_agency', [])
                if agency:
                    markdown += "**Attributed Agency:**\n"
                    for agent in agency:
                        markdown += f"- ⚡ {agent}\n"
                    markdown += "\n"
            
            # Reasoning Effects
            reasoning = frame.get('reasoning_effects', {})
            if reasoning:
                markdown += "**🧠 Reasoning Effects:**\n\n"
                
                inferences = reasoning.get('invited_inferences', 'Not specified')
                markdown += f"**Invited Inferences:** {inferences}\n\n"
                
                conceals = reasoning.get('conceals_or_downplays', 'Not specified')
                if conceals != 'Not specified':
                    markdown += f"**Conceals/Downplays:** {conceals}\n\n"
            
            # Counterframe Linkage
            counterframe = frame.get('counterframe_linkage', {})
            if counterframe and any(counterframe.values()):
                markdown += "**⚔️ Counterframe Analysis:**\n\n"
                
                contests = counterframe.get('contests', 'Not specified')
                if contests != 'Not specified':
                    markdown += f"**Contests:** {contests}\n\n"
                
                mechanism = counterframe.get('mechanism', 'Not specified')
                if mechanism != 'Not specified':
                    markdown += f"**Mechanism:** {mechanism}\n\n"
            
            # Add divider between frames (except for last one)
            if i < len(frames):
                markdown += "---\n\n"
    
    else:
        markdown += "*No frames identified in this analysis.*\n\n"
    
    # Synthesis Section
    synthesis = analysis.get('synthesis', {})
    if synthesis:
        markdown += "### 🔄 Synthesis & Analysis\n\n"
        
        # Dominant frames
        dominant_frames = synthesis.get('dominant_frames', [])
        if dominant_frames:
            markdown += "**🏆 Dominant Frames:**\n\n"
            for i, frame in enumerate(dominant_frames, 1):
                markdown += f"{i}. **{frame}**\n"
            markdown += "\n"
        
        # Comparative insight
        comparative = synthesis.get('comparative_insight', 'Not provided')
        if comparative != 'Not provided':
            markdown += f"**🔍 Comparative Analysis:** {comparative}\n\n"
        
        # Agenda setting effects
        agenda_effects = synthesis.get('agenda_setting_effects', 'Not provided')
        if agenda_effects != 'Not provided':
            markdown += f"**📺 Agenda-Setting Effects:** {agenda_effects}\n\n"
        
        # Implications
        implications = synthesis.get('implications_for_public_understanding', 'Not provided')
        if implications != 'Not provided':
            markdown += f"**🎯 Implications for Public Understanding:** {implications}\n\n"
    
    # Errors section (if any)
    errors = analysis.get('errors', [])
    if errors:
        markdown += "### ⚠️ Analysis Notes\n\n"
        for error in errors:
            markdown += f"- {error}\n"
        markdown += "\n"
    
    return markdown


def _format_rhetorical_analysis_markdown(analysis):
    """
    Format rhetorical analysis for comprehensive markdown report
    
    Args:
        analysis: Dictionary containing rhetorical analysis results
        
    Returns:
        str: Formatted markdown content
    """
    markdown = ""
    
    # Text Metadata
    metadata = analysis.get('text_metadata', {})
    if metadata:
        markdown += "### 📋 Rhetorical Situation\n\n"
        markdown += f"**Rhetorical Situation:** {metadata.get('rhetorical_situation', 'Not specified')}\n\n"
        markdown += f"**Primary Audience:** {metadata.get('primary_audience', 'Not specified')}\n\n"
        
        speaker_context = metadata.get('speaker_context', 'Not specified')
        if speaker_context != 'Not specified':
            markdown += f"**Speaker Context:** {speaker_context}\n\n"
        
        markdown += f"**Overall Purpose:** {metadata.get('overall_purpose', 'Not specified')}\n\n"
    
    # Ethos Analysis
    ethos_analysis = analysis.get('ethos_analysis', {})
    if ethos_analysis:
        markdown += "### 👑 Ethos Analysis (Credibility & Authority)\n\n"
        examples = ethos_analysis.get('examples', [])
        
        if examples:
            markdown += f"**Found {len(examples)} ethos appeals:**\n\n"
            
            for i, example in enumerate(examples, 1):
                markdown += f"#### Example {i}\n\n"
                
                quote = example.get('quote', 'No quote provided')
                markdown += f"**Quote:** \"{quote}\"\n\n"
                
                markdown += f"**Ethos Type:** `{example.get('ethos_type', 'Not specified')}`\n\n"
                markdown += f"**Construction Method:** {example.get('construction_method', 'Not specified')}\n\n"
                markdown += f"**Audience Targeting:** {example.get('audience_targeting', 'Not specified')}\n\n"
                markdown += f"**Effectiveness Assessment:** {example.get('effectiveness_assessment', 'Not specified')}\n\n"
                
                cultural_assumptions = example.get('cultural_assumptions', 'Not specified')
                if cultural_assumptions != 'Not specified':
                    markdown += f"**Cultural Assumptions:** {cultural_assumptions}\n\n"
                
                if i < len(examples):
                    markdown += "---\n\n"
        
        # Overall strategy
        overall_strategy = ethos_analysis.get('overall_ethos_strategy', 'Not provided')
        if overall_strategy != 'Not provided':
            markdown += f"**🎯 Overall Ethos Strategy:** {overall_strategy}\n\n"
    
    # Pathos Analysis
    pathos_analysis = analysis.get('pathos_analysis', {})
    if pathos_analysis:
        markdown += "### ❤️ Pathos Analysis (Emotional Engagement)\n\n"
        examples = pathos_analysis.get('examples', [])
        
        if examples:
            markdown += f"**Found {len(examples)} pathos appeals:**\n\n"
            
            for i, example in enumerate(examples, 1):
                markdown += f"#### Example {i}\n\n"
                
                quote = example.get('quote', 'No quote provided')
                markdown += f"**Quote:** \"{quote}\"\n\n"
                
                markdown += f"**Emotion Type:** `{example.get('emotion_type', 'Not specified')}`\n\n"
                markdown += f"**Trigger Mechanism:** {example.get('trigger_mechanism', 'Not specified')}\n\n"
                markdown += f"**Intensity Level:** {example.get('intensity_level', 'Not specified')}\n\n"
                markdown += f"**Audience Resonance:** {example.get('audience_resonance', 'Not specified')}\n\n"
                markdown += f"**Strategic Function:** {example.get('strategic_function', 'Not specified')}\n\n"
                
                potential_risks = example.get('potential_risks', 'Not specified')
                if potential_risks != 'Not specified':
                    markdown += f"**Potential Risks:** {potential_risks}\n\n"
                
                if i < len(examples):
                    markdown += "---\n\n"
        
        # Emotional arc
        emotional_arc = pathos_analysis.get('emotional_arc', 'Not provided')
        if emotional_arc != 'Not provided':
            markdown += f"**📈 Emotional Arc:** {emotional_arc}\n\n"
    
    # Logos Analysis
    logos_analysis = analysis.get('logos_analysis', {})
    if logos_analysis:
        markdown += "### 🧠 Logos Analysis (Logical Reasoning)\n\n"
        examples = logos_analysis.get('examples', [])
        
        if examples:
            markdown += f"**Found {len(examples)} logos appeals:**\n\n"
            
            for i, example in enumerate(examples, 1):
                markdown += f"#### Example {i}\n\n"
                
                quote = example.get('quote', 'No quote provided')
                markdown += f"**Quote:** \"{quote}\"\n\n"
                
                markdown += f"**Reasoning Type:** `{example.get('reasoning_type', 'Not specified')}`\n\n"
                markdown += f"**Evidence Base:** {example.get('evidence_base', 'Not specified')}\n\n"
                markdown += f"**Logical Structure:** {example.get('logical_structure', 'Not specified')}\n\n"
                
                assumption_analysis = example.get('assumption_analysis', 'Not specified')
                if assumption_analysis != 'Not specified':
                    markdown += f"**Assumption Analysis:** {assumption_analysis}\n\n"
                
                markdown += f"**Strength Assessment:** {example.get('strength_assessment', 'Not specified')}\n\n"
                
                vulnerability = example.get('counterargument_vulnerability', 'Not specified')
                if vulnerability != 'Not specified':
                    markdown += f"**Counterargument Vulnerability:** {vulnerability}\n\n"
                
                if i < len(examples):
                    markdown += "---\n\n"
        
        # Logical coherence
        logical_coherence = logos_analysis.get('logical_coherence', 'Not provided')
        if logical_coherence != 'Not provided':
            markdown += f"**⚖️ Logical Coherence:** {logical_coherence}\n\n"
    
    # Appeal Integration
    integration = analysis.get('appeal_integration', {})
    if integration:
        markdown += "### 🔗 Appeal Integration Analysis\n\n"
        
        reinforcement = integration.get('reinforcement_patterns', 'Not specified')
        if reinforcement != 'Not specified':
            markdown += f"**🤝 Reinforcement Patterns:** {reinforcement}\n\n"
        
        cultural_factors = integration.get('cultural_factors', 'Not specified')
        if cultural_factors != 'Not specified':
            markdown += f"**🌍 Cultural Factors:** {cultural_factors}\n\n"
        
        tensions = integration.get('appeal_tensions', 'Not specified')
        if tensions != 'Not specified':
            markdown += f"**⚡ Appeal Tensions:** {tensions}\n\n"
        
        situation_fit = integration.get('rhetorical_situation_fit', 'Not specified')
        if situation_fit != 'Not specified':
            markdown += f"**🎯 Rhetorical Situation Fit:** {situation_fit}\n\n"
    
    # Effectiveness Evaluation
    effectiveness = analysis.get('effectiveness_evaluation', {})
    if effectiveness:
        markdown += "### 📊 Effectiveness Evaluation\n\n"
        
        strengths = effectiveness.get('persuasive_strengths', 'Not specified')
        if strengths != 'Not specified':
            markdown += f"**💪 Persuasive Strengths:** {strengths}\n\n"
        
        audience_effectiveness = effectiveness.get('audience_effectiveness', 'Not specified')
        if audience_effectiveness != 'Not specified':
            markdown += f"**🎯 Audience Effectiveness:** {audience_effectiveness}\n\n"
        
        weaknesses = effectiveness.get('potential_weaknesses', 'Not specified')
        if weaknesses != 'Not specified':
            markdown += f"**⚠️ Potential Weaknesses:** {weaknesses}\n\n"
        
        ethical_considerations = effectiveness.get('ethical_considerations', 'Not specified')
        if ethical_considerations != 'Not specified':
            markdown += f"**⚖️ Ethical Considerations:** {ethical_considerations}\n\n"
    
    # Critical Synthesis
    synthesis = analysis.get('critical_synthesis', 'No synthesis provided.')
    if synthesis != 'No synthesis provided.':
        markdown += "### 🎯 Critical Synthesis\n\n"
        markdown += synthesis + "\n\n"
    
    return markdown


def _format_generic_analysis_markdown(analysis):
    """
    Format generic structured analysis for comprehensive markdown report
    
    Args:
        analysis: Dictionary containing generic analysis results
        
    Returns:
        str: Formatted markdown content
    """
    markdown = ""
    
    for section_name, section_content in analysis.items():
        section_title = section_name.replace('_', ' ').title()
        markdown += f"### {section_title}\n\n"
        
        if isinstance(section_content, list):
            if not section_content:
                markdown += "*No items found*\n\n"
            else:
                for i, item in enumerate(section_content, 1):
                    if isinstance(item, dict):
                        markdown += f"#### Item {i}\n\n"
                        for field_name, field_value in item.items():
                            field_title = field_name.replace('_', ' ').title()
                            markdown += f"**{field_title}:** {field_value}\n\n"
                        if i < len(section_content):
                            markdown += "---\n\n"
                    else:
                        markdown += f"- {item}\n"
                if not all(isinstance(item, dict) for item in section_content):
                    markdown += "\n"
        
        elif isinstance(section_content, dict):
            for sub_name, sub_content in section_content.items():
                sub_title = sub_name.replace('_', ' ').title()
                markdown += f"**{sub_title}:** {sub_content}\n\n"
        
        else:
            markdown += f"{section_content}\n\n"
    
    return markdown