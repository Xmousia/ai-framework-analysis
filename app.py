import streamlit as st
import google.generativeai as genai
import json
import re
from datetime import datetime

# Import custom modules
from framework_data import (
    FRAMEWORK_EXAMPLES,
    METAPHOR_EXAMPLE_TEXT,
    FRAMING_EXAMPLE_TEXT,
    RHETORICAL_EXAMPLE_TEXT
)
from display_utils import (
    display_metaphor_results, 
    display_framing_results,
    display_rhetorical_results,
    create_markdown_report
)

# =============================================================================
# PAGE SETUP
# =============================================================================

st.set_page_config(
    page_title="AI Framework Analysis Tool",
    page_icon="🔬",
    layout="wide"
)

# Complete CSS with workshop styles
st.markdown("""
<style>
.big-header {
    font-size: 2.5rem;
    font-weight: bold;
    color: #1f77b4;
    text-align: center;
    margin-bottom: 2rem;
}
.step-box {
    background: #f0f2f6;
    padding: 1.5rem;
    border-radius: 10px;
    border-left: 5px solid #1f77b4;
    margin: 1rem 0;
}
.completed-step {
    background: #d4edda;
    border-left: 5px solid #28a745;
}
.current-step {
    background: #fff3cd;
    border-left: 5px solid #ffc107;
}
.workshop-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 2rem;
    border-radius: 15px;
    text-align: center;
    margin-bottom: 2rem;
}
.workshop-title {
    font-size: 2.5rem;
    font-weight: bold;
    margin-bottom: 0.5rem;
}
.workshop-subtitle {
    font-size: 1.2rem;
    opacity: 0.9;
    font-style: italic;
}
.objective-box {
    background: #f8f9fa;
    border-left: 5px solid #28a745;
    padding: 1.5rem;
    margin: 1rem 0;
    border-radius: 8px;
}
.methodology-box {
    background: #e8f4fd;
    border: 2px solid #1f77b4;
    padding: 1.5rem;
    margin: 1.5rem 0;
    border-radius: 10px;
}
.insight-box {
    background: #fff3cd;
    border: 2px solid #ffc107;
    padding: 1.5rem;
    margin: 1.5rem 0;
    border-radius: 10px;
}
.pipeline-step {
    background: #f0f2f6;
    padding: 1rem;
    margin: 0.5rem 0;
    border-radius: 8px;
    border-left: 4px solid #6c757d;
}
.under-hood-section {
    background: #f8f9fa;
    border: 1px solid #dee2e6;
    padding: 1.5rem;
    border-radius: 10px;
    margin: 1.5rem 0;
}
</style>
""", unsafe_allow_html=True)

# =============================================================================
# SESSION STATE INITIALIZATION
# =============================================================================

def init_simple_state():
    """Initialize simple session state"""
    defaults = {
        'step': 1,
        'api_key': '',
        'api_configured': False,
        'selected_framework': None,
        'framework_prompt': '',
        'framework_schema': None,
        'text_to_analyze': '',
        'analysis_results': None,
        'model_name': 'gemini-2.5-flash',
        'show_workshop_page': False
    }
    
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

# =============================================================================
# WORKSHOP PAGE FUNCTIONS
# =============================================================================

def show_workshop_page():
    """Enhanced workshop page that properly integrates with the actual pedagogical framework"""
    
    # Workshop Header - Updated to match actual workshop
    st.markdown("""
    <div class="workshop-header">
        <div class="workshop-title">🔬 Prompt-as-Instrument Workshop</div>
        <div class="workshop-subtitle">Using LLMs to Perform Theory-Driven Readings of Human Texts</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Introduction with proper context
    st.markdown("## 🎓 Digital Scholarship Extension")
    
    st.markdown("""
    This tool serves as the **digital scholarship extension** for the Prompt-as-Instrument Workshop. 
    While the main workshop has students manually work through framework selection, prompt writing, and 
    iterative testing, this tool provides a **technological scaffold** for exploring these concepts.
    
    **Workshop Context:** Students approach AI literacy as an interpretive practice, treating LLMs as both 
    *instrument* (enacting their method) and *object* (producing outputs for critique).
    """)
    
    # The 8-Step Workshop Process
    st.markdown('<div class="methodology-box">', unsafe_allow_html=True)
    st.markdown("## 📚 **The 8-Step Workshop Process**")
    st.markdown("*This tool supports Steps 5-8 and serves as the optional Step 9 extension*")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Steps 1-4: Foundation Building**
        1. 📖 **Pick Your Text** *(Research as Inquiry)*
        2. 🔍 **Pick Your Lens** *(Strategic Exploration)*
        3. 📝 **Summarize Framework** *(Scholarship as Conversation)*
        4. 🎯 **Plan Your Analysis (Blueprint)** *(Information Creation)*
        """)
    
    with col2:
        st.markdown("""
        **Steps 5-8: Implementation & Critique** *(Tool-Supported)*
        5. ✍️ **Write Your Prompt** *(Authority as Constructed)*
        6. 🔄 **Test and Revise** *(Information Creation)*
        7. 📋 **Annotate the Output** *(Authority as Constructed)*
        8. 💭 **Write Your Reflection** *(Information Has Value)*
        """)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Tool as Digital Scholarship Extension
    st.markdown('<div class="insight-box">', unsafe_allow_html=True)
    st.markdown("### 💡 **This Tool as Step 9: Digital Scholarship Extension**")
    st.markdown("""
    **Instead of manually testing prompts**, this tool demonstrates how theoretical frameworks can become 
    **computationally actionable** while maintaining scholarly rigor. Students can:
    
    - **See expert-level framework implementations** (Steps 3-4: Summary & Blueprint)
    - **Experience prompt-as-instrument design** (Step 5: Professional prompt architecture)
    - **Practice critical evaluation** (Steps 7-8: Annotating and reflecting on AI outputs)
    - **Build reusable scholarly tools** (Step 9: Packaging frameworks for others)
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # ACRL Framework Integration
    st.markdown("## 🏛️ **ACRL Information Literacy Framework Connections**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🔍 Research as Inquiry**  
        *Framework selection and refinement*
        
        **📊 Information Creation as a Process**  
        *Iterative prompt development and testing*
        
        **👑 Authority Is Constructed and Contextual**  
        *How frameworks confer interpretive authority*
        """)
    
    with col2:
        st.markdown("""
        **🔍 Searching as Strategic Exploration**  
        *Locating and synthesizing scholarly frameworks*
        
        **💬 Scholarship as Conversation**  
        *Operationalizing scholarly concepts computationally*
        
        **💎 Information Has Value**  
        *Ethical use of AI and proper citation practices*
        """)
    
    # LLM as Instrument & Object
    st.markdown("## 🔬 **LLM as Both Instrument & Object**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### **🛠️ LLM as Instrument**
        *The AI enacts your theoretical method*
        
        - Applies framework consistently
        - Processes large texts systematically  
        - Generates structured outputs
        - Enables scalable analysis
        """)
    
    with col2:
        st.markdown("""
        ### **🔍 LLM as Object** 
        *The AI's output becomes data for critique*
        
        - Where does it succeed/fail?
        - What does it miss or overemphasize?
        - How do its biases shape interpretation?
        - What are the framework's limitations?
        """)
    
    # Assessment Integration
    st.markdown('<div class="objective-box">', unsafe_allow_html=True)
    st.markdown("## 🎯 **Assessment Rubric Elements**")
    st.markdown("""
    **This tool helps students demonstrate:**
    
    - **Framework Clarity & Accuracy:** See expert implementations
    - **Blueprint Specificity:** Experience well-structured prompts  
    - **Iteration Rationale:** Understand prompt refinement process
    - **Analytical Annotations:** Practice critical evaluation of AI outputs
    - **Synthesis & Reflection:** Connect theory, tool, and critique
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Getting Started - Updated for workshop context
    st.markdown("## 🎯 **Ready to Explore?**")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📚 Start Analysis Tool", use_container_width=True, type="primary"):
            st.session_state.show_workshop_page = False
            st.session_state.step = 1
            st.rerun()
    
    with col2:
        if st.button("🔍 Explore Frameworks", use_container_width=True):
            st.session_state.show_workshop_page = False
            st.session_state.step = 2
            st.rerun()
    
    with col3:
        # Workshop resource package
        workshop_resources = create_workshop_resource_package()
        st.download_button(
            label="📦 Download Full Workshop Guide",
            data=workshop_resources,
            file_name="prompt_as_instrument_workshop_complete.md",
            mime="text/markdown",
            use_container_width=True
        )
    
    # Footer with pedagogical context
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #6c757d; margin-top: 2rem;">
        <em>This digital scholarship extension bridges traditional humanities pedagogy with computational methods, 
        demonstrating how theoretical frameworks can become actionable tools while maintaining critical rigor.</em>
    </div>
    """, unsafe_allow_html=True)

def create_workshop_resource_package():
    """Create enhanced workshop resources that integrate with the actual pedagogy"""
    
    resources = f"""# Prompt-as-Instrument Workshop: Complete Guide
## Using LLMs to Perform Theory-Driven Readings of Human Texts

### Abstract
This activity approaches AI literacy as an interpretive practice that can also inform tool-use skills. Students select a theoretical lens for reading human texts, translate that lens into a carefully structured prompt, and iteratively test the prompt with a large language model.

The model functions both as:
* **Instrument** — enacting the student's method on a target text  
* **Object** — producing outputs that can themselves be annotated and critiqued

### Learning Outcomes (ACRL Framework)
* **Research as Inquiry** — Formulate and refine research questions; select appropriate theoretical lenses
* **Information Creation as a Process** — Translate theory into a procedural prompt; iterate with documented versions  
* **Authority Is Constructed and Contextual** — Evaluate how interpretive frames confer or withhold authority
* **Searching as Strategic Exploration** — Locate, compare, and synthesize scholarly sources to build actionable frameworks
* **Scholarship as Conversation** — Cite, operationalize, and critique scholarly concepts in applied settings
* **Information Has Value** — Address citation ethics and reflect on responsible use of generative systems

## The 8-Step Workshop Process

### Steps 1-4: Foundation Building
1. **Pick Your Text** *(Research as Inquiry)*
   - Choose a human-authored text to analyze (news article, speech, press release, etc.)
   
2. **Pick Your Lens** *(Searching as Strategic Exploration)*  
   - Select a theoretical framework from class readings or your own research
   
3. **Summarize Your Framework** *(Scholarship as Conversation)*
   - Explain the framework's key terms and how it works
   - Cite at least two scholarly sources
   
4. **Plan Your Analysis (Blueprint)** *(Information Creation as a Process)*
   - Describe what a good application of your framework would look like
   - Be concrete and specific about expected outcomes

### Steps 5-8: Implementation & Critique  
5. **Write Your Prompt** *(Authority Is Constructed and Contextual)*
   - Turn your blueprint into clear instructions for the LLM
   - Include definitions, examples, and desired formatting
   
6. **Test and Revise** *(Information Creation as a Process)*
   - Run your prompt and record outputs
   - Create at least two versions with documented rationale for changes
   
7. **Annotate the Output** *(Authority Is Constructed and Contextual)*  
   - Mark up one final output highlighting where the model succeeds/fails
   - Identify framework insights and AI limitations
   
8. **Write Your Reflection** *(Information Has Value)*
   - 2-3 paragraphs analyzing the model's performance as both instrument and object
   - Address ethical considerations and framework effectiveness

### Step 9: Digital Scholarship Extension (Optional)
Use the AI Framework Analysis Tool or build your own simple implementation:
* Google Colab notebook for uploaded texts
* Streamlit app with web interface  
* Lightweight deployment for sharing
* Batch processing for multiple texts

## This Tool as Digital Scholarship Extension

### How It Supports Workshop Goals:
- **Expert Framework Implementations** (Steps 3-4: See professional framework summaries and blueprints)
- **Prompt Architecture Examples** (Step 5: Experience well-structured prompts)  
- **Parameter Exploration** (Step 6: Understand iteration and refinement)
- **Structured Outputs for Analysis** (Step 7: Download results for annotation)
- **Critical Evaluation Practice** (Step 8: Reflect on AI as instrument vs object)

### LLM as Instrument & Object
**Instrument:** The AI applies theoretical frameworks systematically and consistently
**Object:** The AI's outputs reveal both framework insights and AI limitations, becoming data for critical analysis

## Sample Frameworks Available:
1. **Metaphor & Anthropomorphism Analysis** — AI discourse analysis using cognitive linguistics
2. **Political Framing Analysis** — Discourse analysis using Entman's framing functions  
3. **Aristotelian Rhetorical Analysis** — Comprehensive ethos, pathos, logos analysis

## Assessment Elements This Tool Supports:
* **Framework Clarity & Accuracy** — See expert implementations
* **Blueprint Specificity** — Experience well-structured analysis plans  
* **Iteration Rationale** — Understand prompt refinement process
* **Analytical Annotations** — Practice critical evaluation of AI outputs
* **Synthesis & Reflection** — Connect theory, tool use, and critique

---
*This workshop bridges traditional humanities pedagogy with digital methods, preparing students for scholarly work in an AI-integrated academic landscape.*

Generated by AI Framework Analysis Tool - Workshop Edition
"""
    
    return resources

# =============================================================================
# MAIN APP LOGIC
# =============================================================================

def main():
    """Main application with workshop page integration"""
    init_simple_state()
    
    # Check if workshop page should be shown
    if st.session_state.get('show_workshop_page', False):
        show_workshop_page()
        
        # Add back button
        st.markdown("---")
        if st.button("← Back to Analysis Tool", type="secondary"):
            st.session_state.show_workshop_page = False
            st.rerun()
        return
    
    # Header with workshop info
    st.markdown('<div class="big-header">🔬 AI Framework Analysis Tool</div>', unsafe_allow_html=True)
    
    # Workshop info banner
    st.info("🎓 **Workshop Tool:** This demonstrates the Framework-to-Prompt-to-Analysis pipeline for digital scholarship. Click 'About Workshop' below to learn more!")
    
    # Clear step indicator
    show_step_progress()
    
    # Main content based on current step
    if st.session_state.step == 1:
        step_1_api_setup()
    elif st.session_state.step == 2:
        step_2_choose_framework()
    elif st.session_state.step == 3:
        step_3_add_text()
    elif st.session_state.step == 4:
        step_4_run_analysis()
    elif st.session_state.step == 5:
        step_5_view_results()
    
    # Navigation buttons at bottom
    show_navigation_buttons()
    
    # Enhanced sidebar with workshop info
    with st.sidebar:
        st.markdown("### 🎓 Workshop Navigation")
        if st.button("📚 About This Workshop", use_container_width=True, type="primary"):
            st.session_state.show_workshop_page = True
            st.rerun()
        
        # Download workshop resources
        workshop_resources = create_workshop_resource_package()
        st.download_button(
            label="📦 Download Workshop Resources",
            data=workshop_resources,
            file_name="prompt_as_instrument_workshop_complete.md",
            mime="text/markdown",
            use_container_width=True
        )
        
        st.markdown("### 🔄 Reset")
        if st.button("Start Over", type="secondary", use_container_width=True):
            # Clear everything except workshop page preference
            keys_to_keep = ['show_workshop_page']
            for key in list(st.session_state.keys()):
                if key not in keys_to_keep:
                    del st.session_state[key]
            st.rerun()

def show_step_progress():
    """Show clear step progress"""
    steps = [
        "🔑 API Setup",
        "📚 Choose Framework", 
        "📖 Add Text",
        "🎯 Run Analysis",
        "📊 View Results"
    ]
    
    st.markdown("### Progress:")
    
    cols = st.columns(5)
    for i, (col, step_name) in enumerate(zip(cols, steps), 1):
        with col:
            if i < st.session_state.step:
                st.markdown(f"✅ **{step_name}**")
            elif i == st.session_state.step:
                st.markdown(f"🔄 **{step_name}**")
            else:
                st.markdown(f"⏳ {step_name}")
    
    st.markdown("---")

def show_navigation_buttons():
    """Show navigation buttons"""
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        if st.session_state.step > 1:
            if st.button("⬅️ Back", use_container_width=True):
                st.session_state.step -= 1
                st.rerun()
    
    with col2:
        st.markdown(f"**Step {st.session_state.step} of 5**")
    
    with col3:
        # Next button conditions
        can_proceed = False
        if st.session_state.step == 1 and st.session_state.api_configured:
            can_proceed = True
        elif st.session_state.step == 2 and st.session_state.selected_framework:
            can_proceed = True
        elif st.session_state.step == 3 and st.session_state.text_to_analyze:
            can_proceed = True
        elif st.session_state.step == 4 and st.session_state.analysis_results:
            can_proceed = True
        
        if can_proceed and st.session_state.step < 5:
            if st.button("Next ➡️", use_container_width=True, type="primary"):
                st.session_state.step += 1
                st.rerun()

# =============================================================================
# STEP 1: API SETUP
# =============================================================================

def step_1_api_setup():
    """Step 1: Simple API setup"""
    st.markdown('<div class="step-box current-step">', unsafe_allow_html=True)
    st.markdown("## 🔑 Step 1: API Setup")
    st.markdown("Get your free Google AI API key to power the analysis.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Instructions
    st.markdown("""
    **Quick Setup:**
    1. 🌐 Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
    2. 🔑 Sign in with Google account
    3. 🎯 Click "Create API Key"
    4. 📋 Copy the key and paste below, then press ENTER
    """)
    
    # API key input
    api_key = st.text_input(
        "Paste your API key here:",
        type="password",
        value=st.session_state.api_key,
        placeholder="AIzaSyC... (starts with AIzaSy)",
        help="Your API key should start with 'AIzaSy' and be about 39 characters long"
    )
    
    if api_key:
        st.session_state.api_key = api_key.strip()  # Remove any whitespace
        
        # Basic format check
        if not api_key.startswith('AIzaSy'):
            st.warning("⚠️ API key should start with 'AIzaSy'. Double-check your key.")
        elif len(api_key) < 30:
            st.warning("⚠️ API key seems too short. Make sure you copied the complete key.")
        else:
            # Test the API key
            if st.button("🔗 Test Connection", type="primary"):
                with st.spinner("Testing API key..."):
                    try:
                        genai.configure(api_key=api_key)
                        test_model = genai.GenerativeModel("gemini-2.5-flash")
                        
                        # Try a simple test query
                        test_response = test_model.generate_content("Say 'API test successful'")
                        
                        st.session_state.api_configured = True
                        st.success("✅ API key works perfectly! Ready for next step.")
                        
                    except Exception as e:
                        st.error(f"❌ API key test failed: {str(e)}")
                        st.session_state.api_configured = False
                        
                        # Help with common issues
                        st.markdown("""
                        **Common fixes:**
                        - Make sure you copied the complete API key
                        - Check that your Google Cloud project has AI services enabled
                        - Try generating a new API key
                        """)
    
    else:
        st.info("👆 Paste your API key above to get started")
    
    # Model selection (only show if API is working)
    if st.session_state.api_configured:
        st.markdown("### 🤖 Choose Model")
        model_choice = st.selectbox(
            "Which model to use?",
            [
                "gemini-2.5-flash (Recommended - Fast & Smart)",
                "gemini-2.5-pro (Slower but Most Capable)",
                "gemini-2.5-flash-lite (Fastest)"
            ]
        )
        st.session_state.model_name = model_choice.split(" ")[0]
        
        # Show current status
        st.success(f"✅ Ready with {st.session_state.model_name}")
    
    # Debug info if there are issues
    if api_key and not st.session_state.api_configured:
        with st.expander("🔍 Debug Info"):
            st.write(f"Key length: {len(api_key)} characters")
            st.write(f"Starts correctly: {api_key.startswith('AIzaSy')}")
            st.write(f"Key preview: {api_key[:10]}...")
            st.write("If this looks wrong, try copying the key again from Google AI Studio.")

# =============================================================================
# STEP 2: CHOOSE FRAMEWORK (WITH COMPLETE DISPLAY FIX)
# =============================================================================

def step_2_choose_framework():
    """Step 2: Choose analysis framework"""
    st.markdown('<div class="step-box current-step">', unsafe_allow_html=True)
    st.markdown("## 📚 Step 2: Choose Your Analysis Framework")
    st.markdown("Pick an example framework or create your own.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Framework choice
    framework_type = st.radio(
        "What would you like to do?",
        [
            "📋 Use an Example Framework (Recommended)",
            "✏️ Write My Own Framework"
        ]
    )
    
    if "Example" in framework_type:
        show_example_frameworks()
    else:
        show_custom_framework()

def show_example_frameworks():
    """Show example framework options with COMPLETE framework display"""
    st.markdown("### 🎓 Example Frameworks")
    
    # Simple framework selection
    framework_names = list(FRAMEWORK_EXAMPLES.keys())
    selected_name = st.selectbox(
        "Choose a framework:",
        framework_names,
        format_func=lambda x: f"📋 {x}"
    )
    
    if selected_name:
        framework = FRAMEWORK_EXAMPLES[selected_name]
        
        # Show framework info
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown(f"**{selected_name}**")
            st.write(framework['description'])
            st.write(f"**Field:** {framework['discipline']}")
            
            # FIXED: Show COMPLETE framework instead of truncated version
            with st.expander("🔍 See Complete Framework Details"):
                st.text_area(
                    "Complete Framework Instructions:",
                    value=framework['prompt'],  # REMOVED the [:500] + "..." truncation
                    height=400,  # Increased height to accommodate full text
                    disabled=True
                )
                
                # Add download button for the framework
                st.download_button(
                    label="💾 Download Framework Text",
                    data=framework['prompt'],
                    file_name=f"{selected_name.lower().replace(' ', '_')}_framework.txt",
                    mime="text/plain",
                    use_container_width=True
                )
        
        with col2:
            st.markdown("**What you'll get:**")
            if "Metaphor" in selected_name:
                st.markdown("""
                • Metaphor identification
                • Source-target mapping  
                • Explanation analysis
                • AI literacy insights
                """)
            elif "Framing" in selected_name:
                st.markdown("""
                • Frame identification
                • Role assignments
                • Reasoning effects
                • Political implications
                """)
            elif "Rhetorical" in selected_name:
                st.markdown("""
                • Ethos, pathos, logos
                • Appeal effectiveness
                • Audience analysis
                • Strategic assessment
                """)
        
        # Use this framework
        if st.button(f"✅ Use {selected_name}", type="primary", use_container_width=True):
            st.session_state.selected_framework = selected_name
            st.session_state.framework_prompt = framework['prompt']
            st.session_state.framework_schema = framework['schema']
            st.success(f"Great! Using {selected_name}")
            st.balloons()

def show_custom_framework():
    """Show custom framework creation"""
    st.markdown("### ✏️ Create Your Own Framework")
    
    st.info("""
    **Tips for good frameworks:**
    • Explain your theoretical approach
    • Give clear analysis instructions  
    • Include examples of what you want
    • Specify output format
    """)
    
    custom_prompt = st.text_area(
        "Write your framework instructions:",
        height=300,
        placeholder="""Example:

# Literary Character Analysis

Analyze how the author develops characters in this text.

**Instructions:**
1. Identify main characters
2. Find evidence of character development
3. Analyze literary techniques used
4. Assess effectiveness

**Output:**
Provide structured analysis with quotes and explanations.""",
        value=st.session_state.framework_prompt
    )
    
    if custom_prompt and len(custom_prompt) > 100:
        st.session_state.framework_prompt = custom_prompt
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Length", f"{len(custom_prompt)} characters")
        with col2:
            quality = "Good" if len(custom_prompt) > 300 else "Too short"
            st.metric("Quality", quality)
        
        if st.button("✅ Use My Framework", type="primary"):
            st.session_state.selected_framework = "Custom Framework"
            st.session_state.framework_schema = None  # Freeform output
            st.success("Custom framework ready!")

# =============================================================================
# STEP 3: ADD TEXT
# =============================================================================

def step_3_add_text():
    """Step 3: Add text to analyze"""
    st.markdown('<div class="step-box current-step">', unsafe_allow_html=True)
    st.markdown("## 📖 Step 3: Add Text to Analyze")
    st.markdown("Provide the text you want to analyze with your framework.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Show what framework we're using
    st.info(f"**Using:** {st.session_state.selected_framework}")
    
    # Text input options
    text_method = st.radio(
        "How do you want to add text?",
        get_text_options()
    )
    
    if "example" in text_method.lower():
        handle_example_text(text_method)
    elif "paste" in text_method.lower():
        handle_paste_text()
    else:
        handle_upload_text()
    
    # Show text stats if we have text
    if st.session_state.text_to_analyze:
        show_simple_text_stats()

def get_text_options():
    """Get text input options based on framework"""
    options = ["✏️ Paste my own text", "📄 Upload a file"]
    
    # Add example text options based on framework
    if st.session_state.selected_framework:
        if "Metaphor" in st.session_state.selected_framework:
            options.insert(0, "📋 Use example (AI technology text)")
        elif "Framing" in st.session_state.selected_framework:
            options.insert(0, "📋 Use example (political speech)")
        elif "Rhetorical" in st.session_state.selected_framework:
            options.insert(0, "📋 Use example (MLK's Letter)")
    
    return options

def handle_example_text(method):
    """Handle example text selection"""
    if "AI technology" in method:
        st.session_state.text_to_analyze = METAPHOR_EXAMPLE_TEXT
        st.success("✅ Loaded AI technology example text")
        
    elif "political speech" in method:
        st.session_state.text_to_analyze = FRAMING_EXAMPLE_TEXT  
        st.success("✅ Loaded political speech example text")
        
    elif "MLK" in method:
        st.session_state.text_to_analyze = RHETORICAL_EXAMPLE_TEXT
        st.success("✅ Loaded MLK Letter example text")
    
    # Show preview
    if st.session_state.text_to_analyze:
        with st.expander("👀 Preview text"):
            st.text_area(
                "Text preview:",
                value=st.session_state.text_to_analyze[:500] + "...",
                height=150,
                disabled=True
            )

def handle_paste_text():
    """Handle text pasting"""
    text = st.text_area(
        "Paste your text here:",
        value=st.session_state.text_to_analyze,
        height=300,
        placeholder="Paste the text you want to analyze..."
    )
    
    if text:
        st.session_state.text_to_analyze = text

def handle_upload_text():
    """Handle file upload"""
    uploaded_file = st.file_uploader(
        "Choose a text file:",
        type=['txt', 'md']
    )
    
    if uploaded_file:
        try:
            text = uploaded_file.read().decode('utf-8')
            st.session_state.text_to_analyze = text
            st.success(f"✅ Loaded {uploaded_file.name}")
        except Exception as e:
            st.error(f"Error reading file: {e}")

def show_simple_text_stats():
    """Show simple text statistics"""
    text_length = len(st.session_state.text_to_analyze)
    word_count = len(st.session_state.text_to_analyze.split())
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Characters", f"{text_length:,}")
    with col2:
        st.metric("Words", f"{word_count:,}")
    with col3:
        if text_length < 1000:
            status = "Short"
        elif text_length > 25000:
            status = "Long"
        else:
            status = "Good"
        st.metric("Length", status)

# =============================================================================
# STEP 4: RUN ANALYSIS (WITH ENHANCED JSON ERROR HANDLING)
# =============================================================================

def step_4_run_analysis():
    """Step 4: Run the analysis with enhanced JSON error handling"""
    st.markdown('<div class="step-box current-step">', unsafe_allow_html=True)
    st.markdown("## 🎯 Step 4: Run Analysis")
    st.markdown("Ready to analyze your text with AI!")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Show what we're about to analyze
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**📋 Analysis Setup:**")
        st.write(f"• **Framework:** {st.session_state.selected_framework}")
        st.write(f"• **Text length:** {len(st.session_state.text_to_analyze):,} characters")
        st.write(f"• **Model:** {st.session_state.model_name}")
    
    with col2:
        st.markdown("**⏱️ Expected time:**")
        text_length = len(st.session_state.text_to_analyze)
        if text_length < 5000:
            est_time = "30-60 seconds"
        elif text_length < 15000:
            est_time = "1-2 minutes"
        else:
            est_time = "2-3 minutes"
        st.write(f"• **Estimated:** {est_time}")
    
    # Run analysis button
    if st.button("🚀 Start Analysis", type="primary", use_container_width=True):
        run_the_analysis()

def run_the_analysis():
    """Run analysis with enhanced JSON error handling"""
    try:
        # Double-check API key exists
        if not st.session_state.api_key:
            st.error("❌ No API key found. Please go back to Step 1.")
            return
        
        # Configure API
        genai.configure(api_key=st.session_state.api_key)
        
        # Show progress
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        status_text.text("🤖 Configuring API...")
        progress_bar.progress(10)
        
        # Test API key again before analysis
        try:
            test_model = genai.GenerativeModel(st.session_state.model_name)
            status_text.text("🔑 API key verified...")
            progress_bar.progress(25)
        except Exception as api_error:
            st.error(f"❌ API key validation failed: {str(api_error)}")
            st.error("Please go back to Step 1 and check your API key.")
            return
        
        status_text.text("🤖 Starting analysis...")
        progress_bar.progress(50)
        
        # Run analysis using ENHANCED function with better error handling
        result = run_ai_analysis_enhanced(
            text=st.session_state.text_to_analyze,
            framework_prompt=st.session_state.framework_prompt,
            analysis_schema=st.session_state.framework_schema,
            model_name=st.session_state.model_name,
            generation_config={
                'temperature': 0.8,
                'top_p': 0.8,
                'top_k': 10,
                'max_output_tokens': 8192
            }
        )
        
        progress_bar.progress(100)
        status_text.text("✅ Analysis complete!")
        
        if result:
            st.session_state.analysis_results = result
            st.success("🎉 Analysis finished! Ready to view results.")
            st.balloons()
        else:
            st.error("❌ Analysis failed. Please try again.")
            
    except Exception as e:
        st.error(f"❌ Error during analysis: {str(e)}")
        st.info("💡 Try going back to Step 1 to re-enter your API key.")
        
        # Show debug info
        with st.expander("🔍 Debug Info"):
            st.write(f"API Key exists: {bool(st.session_state.api_key)}")
            st.write(f"API Key length: {len(st.session_state.api_key) if st.session_state.api_key else 0}")
            st.write(f"Model: {st.session_state.model_name}")
            if st.session_state.api_key:
                st.write(f"Key starts with: {st.session_state.api_key[:10]}...")

def run_ai_analysis_enhanced(text, framework_prompt, analysis_schema=None, model_name="gemini-2.5-flash", generation_config=None):
    """
    Enhanced AI analysis with robust JSON error handling
    
    Args:
        text: Text to analyze
        framework_prompt: The theoretical framework prompt
        analysis_schema: Optional JSON schema for structured output
        model_name: Gemini model to use
        generation_config: Model generation parameters
        
    Returns:
        dict: Analysis results with metadata
    """
    
    # Default generation config if none provided
    if generation_config is None:
        generation_config = {
            "temperature": 0.8,
            "top_p": 0.8,
            "top_k": 10,
            "max_output_tokens": 8192
        }
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    try:
        # Configure the model based on whether we have a schema
        if analysis_schema:
            model = genai.GenerativeModel(
                model_name=model_name,
                generation_config={
                    **generation_config,
                    "response_mime_type": "application/json",
                    "response_schema": analysis_schema
                },
                system_instruction=framework_prompt
            )
            use_json = True
        else:
            model = genai.GenerativeModel(
                model_name=model_name,
                generation_config=generation_config,
                system_instruction=framework_prompt
            )
            use_json = False
        
        # Generate the content
        response = model.generate_content(text)
        
        # Extract and process the response
        analysis_text = response.text
        
        if use_json:
            try:
                # Clean and parse JSON with enhanced error handling
                cleaned_text = analysis_text.strip()
                analysis_data = json.loads(cleaned_text)
                st.success("✅ JSON parsing successful!")
            except json.JSONDecodeError as e:
                st.warning(f"⚠️ JSON parsing failed: {e}")
                st.info("🔧 Attempting to fix JSON formatting...")
                
                # Try to fix common JSON issues
                try:
                    fixed_text = fix_json_string(cleaned_text)
                    analysis_data = json.loads(fixed_text)
                    st.success("✅ JSON automatically repaired!")
                except:
                    st.warning("🔄 Using text format instead of structured output")
                    analysis_data = analysis_text
                    use_json = False
        else:
            analysis_data = analysis_text
        
        # Create the result object
        result = {
            "timestamp": timestamp,
            "model": model_name,
            "generation_config": generation_config,
            "framework_preview": framework_prompt[:200] + "..." if len(framework_prompt) > 200 else framework_prompt,
            "text_preview": text[:200] + "..." if len(text) > 200 else text,
            "text_length": len(text),
            "use_json": use_json,
            "analysis": analysis_data,
            "raw_response": analysis_text,
            "metadata": {}
        }
        
        # Safely extract usage metadata
        try:
            if hasattr(response, 'usage_metadata'):
                usage = response.usage_metadata
                result["metadata"] = {
                    "prompt_tokens": getattr(usage, 'prompt_token_count', None),
                    "response_tokens": getattr(usage, 'candidates_token_count', None),
                    "total_tokens": getattr(usage, 'total_token_count', None)
                }
            else:
                result["metadata"] = {
                    "prompt_tokens": None,
                    "response_tokens": None,
                    "total_tokens": None
                }
        except Exception as metadata_error:
            st.warning(f"⚠️ Could not extract usage metadata: {metadata_error}")
            result["metadata"] = {
                "prompt_tokens": None,
                "response_tokens": None,
                "total_tokens": None
            }
        
        return result
        
    except Exception as e:
        st.error(f"❌ Analysis failed: {str(e)}")
        st.info("💡 Troubleshooting tips:")
        st.info("• Check your API key configuration")
        st.info(f"• Verify model '{model_name}' is available")
        st.info("• Try with shorter text (under 25,000 characters)")
        st.info("• Verify your framework prompt is properly formatted")
        return None

def fix_json_string(json_str):
    """
    Attempt to fix common JSON formatting issues
    
    Args:
        json_str: The malformed JSON string
        
    Returns:
        str: Potentially fixed JSON string
    """
    
    # Remove any non-printable characters
    json_str = ''.join(char for char in json_str if ord(char) >= 32 or char in '\n\r\t')
    
    # Fix common quote issues
    # Replace smart quotes with regular quotes
    json_str = json_str.replace('"', '"').replace('"', '"')
    json_str = json_str.replace(''', "'").replace(''', "'")
    
    # Fix newlines within strings
    json_str = re.sub(r'(?<!\\)\n(?![}\]])', '\\n', json_str)
    
    # Fix unescaped quotes within strings
    # This is a simple approach - more sophisticated fixing could be added
    json_str = re.sub(r'(?<!\\)"(?=.*[^"]*"[^"]*$)', '\\"', json_str)
    
    # Remove trailing commas
    json_str = re.sub(r',\s*}', '}', json_str)
    json_str = re.sub(r',\s*]', ']', json_str)
    
    # Try to find and complete incomplete JSON
    # Count braces and brackets
    open_braces = json_str.count('{') - json_str.count('}')
    open_brackets = json_str.count('[') - json_str.count(']')
    
    # Add missing closing braces/brackets
    json_str += '}' * open_braces
    json_str += ']' * open_brackets
    
    return json_str

# =============================================================================
# STEP 5: VIEW RESULTS
# =============================================================================

def step_5_view_results():
    """Step 5: View and download results"""
    st.markdown('<div class="step-box current-step">', unsafe_allow_html=True)
    st.markdown("## 📊 Step 5: Your Analysis Results")
    st.markdown("Here's what the AI found using your framework!")
    st.markdown('</div>', unsafe_allow_html=True)
    
    if not st.session_state.analysis_results:
        st.error("No results found. Please run analysis first.")
        return
    
    result = st.session_state.analysis_results
    
    # Quick stats
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Framework", st.session_state.selected_framework)
    with col2:
        st.metric("Analysis Type", "Structured" if result.get('use_json') else "Freeform")
    with col3:
        timestamp = datetime.strptime(result['timestamp'], '%Y%m%d_%H%M%S').strftime('%H:%M')
        st.metric("Completed", timestamp)
    
    st.markdown("---")
    
    # Display results using specialized functions
    analysis = result['analysis']
    
    if isinstance(analysis, dict):
        if 'metaphorAudit' in analysis:
            display_metaphor_results(analysis)
        elif 'frames' in analysis:
            display_framing_results(analysis)
        elif 'ethos_analysis' in analysis:
            display_rhetorical_results(analysis)
        else:
            # Generic structured display
            display_generic_results(analysis)
    else:
        # Freeform text display
        st.markdown("### 📝 Analysis Results")
        st.write(analysis)
    
    # Download options
    st.markdown("---")
    st.markdown("### 💾 Download Your Results")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # JSON download
        json_str = json.dumps(result, indent=2, ensure_ascii=False)
        st.download_button(
            label="📄 Download JSON Data",
            data=json_str,
            file_name=f"analysis_{result['timestamp']}.json",
            mime="application/json",
            use_container_width=True
        )
    
    with col2:
        # Report download
        markdown_report = create_markdown_report(result)
        st.download_button(
            label="📋 Download Report",
            data=markdown_report,
            file_name=f"report_{result['timestamp']}.md",
            mime="text/markdown",
            use_container_width=True
        )
    
    # Start over option
    st.markdown("---")
    if st.button("🔄 Analyze Different Text", use_container_width=True):
        st.session_state.step = 3  # Go back to text input
        st.session_state.text_to_analyze = ""
        st.rerun()

def display_generic_results(analysis):
    """Display generic structured results"""
    st.markdown("### 📄 Structured Results")
    
    for section_name, content in analysis.items():
        section_title = section_name.replace('_', ' ').title()
        
        with st.expander(f"📂 {section_title}", expanded=True):
            if isinstance(content, list):
                for i, item in enumerate(content, 1):
                    if isinstance(item, dict):
                        st.markdown(f"**Item {i}:**")
                        for key, value in item.items():
                            st.write(f"• **{key.replace('_', ' ').title()}:** {value}")
                    else:
                        st.write(f"{i}. {item}")
                    
                    if i < len(content):
                        st.markdown("---")
            
            elif isinstance(content, dict):
                for key, value in content.items():
                    st.write(f"**{key.replace('_', ' ').title()}:** {value}")
            
            else:
                st.write(content)

# =============================================================================
# RUN THE APP
# =============================================================================

if __name__ == "__main__":
    main()