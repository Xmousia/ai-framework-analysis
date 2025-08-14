# display_utils.py
# Utilities for displaying analysis results

import streamlit as st
from datetime import datetime

def display_metaphor_results(analysis):
    """
    Display metaphor analysis results in a structured format
    
    Args:
        analysis: The analysis dictionary with metaphor audit results
    """
    
    st.subheader("📋 Metaphor Analysis Results")
    
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

def create_markdown_report(result):
    """
    Generate a markdown report from analysis results
    
    Args:
        result: The analysis result dictionary
        
    Returns:
        str: Formatted markdown report
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
    
    # Check if this is a metaphor analysis
    if isinstance(analysis, dict) and 'metaphorAudit' in analysis:
        markdown += "## Metaphor Analysis Results\n\n"
        
        # Task 1: Metaphor Audit
        markdown += "### Task 1: Metaphor & Anthropomorphism Audit\n\n"
        metaphor_audit = analysis.get('metaphorAudit', [])
        
        if metaphor_audit:
            for i, item in enumerate(metaphor_audit, 1):
                markdown += f"#### {i}. {item.get('title', 'Untitled')}\n\n"
                markdown += f"**Quote:** \"{item.get('quote', 'N/A')}\"\n\n"
                markdown += f"**Frame:** {item.get('frame', 'N/A')}\n\n"
                markdown += f"**Projection:** {item.get('projection', 'N/A')}\n\n"
                markdown += f"**Acknowledgment:** {item.get('acknowledgment', 'N/A')}\n\n"
                markdown += f"**Implications:** {item.get('implications', 'N/A')}\n\n"
                markdown += "---\n\n"
        else:
            markdown += "*No metaphorical patterns identified.*\n\n"
        
        # Task 2: Source-Target Mapping
        markdown += "### Task 2: Source-Target Mapping Analysis\n\n"
        source_target = analysis.get('sourceTargetMapping', [])
        
        if source_target:
            for i, item in enumerate(source_target, 1):
                markdown += f"#### Mapping {i}\n\n"
                markdown += f"**Quote:** \"{item.get('quote', 'N/A')}\"\n\n"
                markdown += f"**Source Domain:** {item.get('sourceDomain', 'N/A')}\n\n"
                markdown += f"**Target Domain:** {item.get('targetDomain', 'N/A')}\n\n"
                markdown += f"**Mapping:** {item.get('mapping', 'N/A')}\n\n"
                markdown += f"**Conceals:** {item.get('conceals', 'N/A')}\n\n"
                markdown += "---\n\n"
        else:
            markdown += "*No source-target mappings identified.*\n\n"
        
        # Task 3: Explanation Audit
        markdown += "### Task 3: Explanation Audit (Brown's Typology)\n\n"
        explanation_audit = analysis.get('explanationAudit', [])
        
        if explanation_audit:
            for i, item in enumerate(explanation_audit, 1):
                markdown += f"#### Explanation {i}\n\n"
                markdown += f"**Quote:** \"{item.get('quote', 'N/A')}\"\n\n"
                markdown += f"**Brown's Type:** {item.get('brownType', 'N/A')}\n\n"
                markdown += f"**Justification:** {item.get('justification', 'N/A')}\n\n"
                markdown += f"**Implications:** {item.get('implications', 'N/A')}\n\n"
                if item.get('chainedFrom'):
                    markdown += f"**Chained From:** {item.get('chainedFrom')}\n\n"
                markdown += "---\n\n"
        else:
            markdown += "*No explanatory passages analyzed.*\n\n"
        
        # Critical Observations
        markdown += "### Critical Observations\n\n"
        obs = analysis.get('criticalObservations', {})
        
        if obs and any(obs.values()):
            markdown += f"**Agency Slippage:** {obs.get('agencySlippage', 'Not analyzed')}\n\n"
            markdown += f"**Metaphor-Driven Trust:** {obs.get('metaphorDrivenTrust', 'Not analyzed')}\n\n"
            markdown += f"**Obscured Mechanics:** {obs.get('obscuredMechanics', 'Not analyzed')}\n\n"
            markdown += f"**Context Sensitivity:** {obs.get('contextSensitivity', 'Not analyzed')}\n\n"
        else:
            markdown += "*No critical observations provided.*\n\n"
        
        # Conclusion
        markdown += "### Conclusion\n\n"
        conclusion = analysis.get('conclusion', 'No conclusion provided.')
        markdown += f"{conclusion}\n\n"
        
    else:
        # Generic analysis display
        markdown += "## Analysis Results\n\n"
        if isinstance(analysis, dict):
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
                            else:
                                markdown += f"- {item}\n"
                        markdown += "\n"
                
                elif isinstance(section_content, dict):
                    for sub_name, sub_content in section_content.items():
                        sub_title = sub_name.replace('_', ' ').title()
                        markdown += f"**{sub_title}:** {sub_content}\n\n"
                
                else:
                    markdown += f"{section_content}\n\n"
        else:
            markdown += str(analysis) + "\n\n"
    
    # Add metadata section
    markdown += "---\n\n## Analysis Metadata\n\n"
    markdown += f"- **Model Used:** {result['model']}\n"
    markdown += f"- **Generated:** {timestamp_formatted}\n"
    markdown += f"- **Text Length:** {result['text_length']:,} characters\n"
    
    if result.get('metadata', {}).get('total_tokens'):
        markdown += f"- **Total Tokens:** {result['metadata']['total_tokens']:,}\n"
    
    return markdown