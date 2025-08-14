import streamlit as st
import google.generativeai as genai
import json
import os
from datetime import datetime
import textwrap

# Import custom modules
from framework_data import METAPHOR_FRAMEWORK_PROMPT, METAPHOR_ANALYSIS_SCHEMA, FRAMEWORK_EXAMPLES
from display_utils import display_metaphor_results, create_markdown_report
from analysis_runner import run_ai_analysis

# Configure page
st.set_page_config(
    page_title="AI Framework Analysis Tool v2",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
.main-header {
    font-size: 2.5rem;
    font-weight: bold;
    color: #1f77b4;
    text-align: center;
    margin-bottom: 2rem;
}
.step-header {
    font-size: 1.5rem;
    font-weight: bold;
    color: #2e7d32;
    margin-top: 2rem;
    margin-bottom: 1rem;
}
.info-box {
    background-color: rgba(227, 242, 253, 0.1);
    border: 1px solid rgba(25, 118, 210, 0.3);
    padding: 1rem;
    border-radius: 0.5rem;
    border-left: 4px solid #1976d2;
    margin: 1rem 0;
    color: inherit;
}
.success-box {
    background-color: rgba(232, 245, 232, 0.1);
    border: 1px solid rgba(76, 175, 80, 0.3);
    padding: 1rem;
    border-radius: 0.5rem;
    border-left: 4px solid #4caf50;
    margin: 1rem 0;
    color: inherit;
}
.warning-box {
    background-color: rgba(255, 243, 224, 0.1);
    border: 1px solid rgba(245, 124, 0, 0.3);
    padding: 1rem;
    border-radius: 0.5rem;
    border-left: 4px solid #f57c00;
    margin: 1rem 0;
    color: inherit;
}
</style>
""", unsafe_allow_html=True)

# Initialize session state
def init_session_state():
    """Initialize all session state variables"""
    defaults = {
        'api_configured': False,
        'framework_prompt': '',
        'analysis_schema': None,
        'model_configured': False,
        'text_to_analyze': '',
        'analysis_results': None,
        'analysis_history': [],
        'reflection_text': '',
        'current_step': 1,
        'model_name': 'gemini-2.5-flash',
        'generation_config': {
            'temperature': 0.8,
            'top_p': 0.8,
            'top_k': 10,
            'max_output_tokens': 8192
        }
    }
    
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

def display_progress():
    """Display progress indicator"""
    steps = [
        "🔑 Setup", 
        "📚 Framework", 
        "🏗️ Schema", 
        "📖 Text Input", 
        "🎯 Analysis", 
        "🤔 Reflection"
    ]
    
    cols = st.columns(len(steps))
    for i, (col, step) in enumerate(zip(cols, steps)):
        with col:
            if i + 1 < st.session_state.current_step:
                st.success(f"✅ {step}")
            elif i + 1 == st.session_state.current_step:
                st.info(f"🔄 {step}")
            else:
                st.write(f"⏳ {step}")

def setup_api():
    """Step 1: API Configuration"""
    st.markdown('<div class="step-header">🔑 Step 1: API Configuration</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <b>Steps to get a free Gemini API key:</b><br>
    1. <b>Go to Google AI Studio:</b> Log in using a Google account<br>
    2. <b>Accept Terms & Conditions:</b> If it's the first visit, agree to the terms<br>
    3. <b>Click "Get API Key":</b> Usually found in the top-left or prominent location<br>
    4. <b>Create API Key:</b> Click "Create API Key" and select an existing Google Cloud Project, or create a new one<br>
    5. <b>Copy the API Key:</b> Once generated, copy and securely store the key<br><br>
    🔗 <a href="https://makersuite.google.com/app/apikey" target="_blank">Get your API key here</a>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        api_key = st.text_input(
            "Google AI API Key",
            type="password",
            placeholder="Paste your API key here and press Enter...",
            help="Get your free API key from Google AI Studio",
            key="api_key_input"
        )
        
        # Add a button as alternative to pressing Enter
        if st.button("🔗 Connect to Google AI", disabled=not api_key, key="connect_api"):
            st.session_state.api_key_submitted = True
    
    with col2:
        st.markdown("**Model Configuration**")
        
        # Model selection
        model_name = st.selectbox(
            "Gemini Model",
            [
                "gemini-2.5-pro",
                "gemini-2.5-flash",
                "gemini-2.5-flash-lite",
                "learnlm-2.0-flash-experimental"
            ],
            index=1,  # Default to gemini-2.5-flash
            help="Choose the Gemini model for analysis"
        )
        
        # Store model choice
        st.session_state.model_name = model_name
    
    # Advanced model configuration
    with st.expander("🔧 Advanced Model Settings", expanded=False):
        st.markdown("**Generation Parameters:**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            temperature = st.slider(
                "Temperature",
                min_value=0.0,
                max_value=1.0,
                value=0.8,
                step=0.1,
                help="Controls creativity (0.0 = deterministic, 1.0 = very creative)"
            )
            
            top_p = st.slider(
                "Top P",
                min_value=0.0,
                max_value=1.0,
                value=0.8,
                step=0.1,
                help="Controls diversity of word choices"
            )
        
        with col2:
            top_k = st.slider(
                "Top K",
                min_value=1,
                max_value=40,
                value=10,
                step=1,
                help="Limits vocabulary choices to top K words"
            )
            
            max_tokens = st.slider(
                "Max Output Tokens",
                min_value=1000,
                max_value=16000,
                value=8192,
                step=500,
                help="Maximum length of AI response"
            )
        
        # Store generation config
        st.session_state.generation_config = {
            "temperature": temperature,
            "top_p": top_p,
            "top_k": top_k,
            "max_output_tokens": max_tokens
        }
        
        # Show current config
        st.json(st.session_state.generation_config)
    
    # Check if API key was entered (either by pressing Enter or clicking button)
    if api_key and (st.session_state.get('api_key_submitted') or api_key != st.session_state.get('previous_api_key', '')):
        st.session_state.previous_api_key = api_key
        try:
            genai.configure(api_key=api_key)
            # Test the connection with selected model
            test_model = genai.GenerativeModel(st.session_state.model_name)
            st.session_state.api_configured = True
            st.session_state.current_step = max(st.session_state.current_step, 2)
            
            st.markdown(f"""
            <div class="success-box">
            ✅ <b>API Key Configured Successfully!</b><br>
            Using model: <code>{st.session_state.model_name}</code>
            </div>
            """, unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"❌ API Configuration Error: {str(e)}")
    
    return api_key

def framework_input():
    """Step 2: Theoretical Framework Input"""
    if not st.session_state.api_configured:
        st.warning("⚠️ Please configure your API key first")
        return
    
    st.markdown('<div class="step-header">📚 Step 2: Your Theoretical Framework</div>', unsafe_allow_html=True)
    
    # Framework selection
    framework_choice = st.radio(
        "Choose your framework approach:",
        [
            "Browse Example Frameworks",
            "Create Custom Framework"
        ],
        help="Start with examples to see sophisticated framework design",
        key="framework_choice_radio"
    )
    
    if framework_choice == "Browse Example Frameworks":
        st.markdown("""
        <div class="info-box">
        <b>Example Frameworks:</b> These demonstrate how to operationalize complex theoretical approaches
        and create sophisticated analysis tools.
        </div>
        """, unsafe_allow_html=True)
        
        # Display available examples
        example_choice = st.selectbox(
            "Select an example framework:",
            list(FRAMEWORK_EXAMPLES.keys()),
            help="Each example shows prompt design and JSON schema creation"
        )
        
        if example_choice:
            example = FRAMEWORK_EXAMPLES[example_choice]
            
            # Show example details
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"**{example_choice}**")
                st.write(f"📖 {example['description']}")
                st.write(f"🎓 **Discipline:** {example['discipline']}")
                
                with st.expander("📋 View Complete Framework Prompt", expanded=False):
                    st.text_area(
                        "Framework Prompt", 
                        value=example['prompt'], 
                        height=400, 
                        disabled=True,
                        key=f"prompt_display_{example_choice}"
                    )
            
            with col2:
                st.markdown("**Framework Features:**")
                
                if example_choice == "Metaphor & Anthropomorphism Analysis":
                    st.markdown("""
                    • 3-part audit structure
                    • Cognitive linguistics grounding
                    • Brown's explanation typology
                    • AI literacy focus
                    • Structured JSON output
                    """)
                
                elif example_choice == "Political Framing Analysis":
                    st.markdown("""
                    • Entman's framing functions
                    • Lakoff's frame semantics
                    • Agenda-setting analysis
                    • Role assignment mapping
                    • Counterframe detection
                    """)
                
                with st.expander("🔍 View JSON Schema"):
                    st.json(example['schema'])
            
            # Option to use this example
            if st.button(f"✅ Use {example_choice}", key=f"use_example_{example_choice}"):
                st.session_state.framework_prompt = example['prompt']
                st.session_state.analysis_schema = example['schema']
                st.session_state.current_step = max(st.session_state.current_step, 4)  # Skip schema builder
                st.session_state.model_configured = True
                st.success(f"✅ {example_choice} framework loaded and configured!")
                st.rerun()
        
    else:  # Create Custom Framework
        st.markdown("""
        <div class="info-box">
        <b>Custom Framework Guidelines:</b><br>
        • Clear explanation of your theoretical framework<br>
        • Specific instructions for applying it to texts<br>
        • Examples of good analysis<br>
        • Output format requirements<br><br>
        💡 <b>Tip:</b> Study the example frameworks above to see sophisticated prompt design!
        </div>
        """, unsafe_allow_html=True)
        
        # Show examples for inspiration
        with st.expander("💡 Need Inspiration? View Example Framework Structures"):
            st.markdown("""
            **Example Framework Patterns:**
            
            **📖 Literary Analysis Framework:**
            ```
            # Character Development Analysis
            
            **Theoretical Background:** 
            Apply theories of character development (dynamic vs. static, round vs. flat)
            
            **Analysis Instructions:**
            1. Identify main characters and categorize development type
            2. Track character changes through specific scenes
            3. Analyze techniques used to reveal character
            4. Evaluate effectiveness of character arcs
            
            **Output Requirements:**
            - Character profiles with evidence
            - Development timeline
            - Literary technique analysis
            - Overall assessment
            ```
            
            **🎭 Rhetorical Analysis Framework:**
            ```
            # Aristotelian Rhetorical Analysis
            
            **Theoretical Background:**
            Apply Aristotle's rhetorical triangle (ethos, pathos, logos)
            
            **Analysis Instructions:**
            1. Identify appeals to ethos (credibility/authority)
            2. Locate pathos appeals (emotional engagement)  
            3. Find logos elements (logical reasoning)
            4. Assess effectiveness and interaction of appeals
            
            **Output Requirements:**
            - Categorized examples with quotes
            - Effectiveness ratings
            - Audience analysis
            - Strategic assessment
            ```
            """)
        
        framework_prompt = st.text_area(
            "Your Custom Framework Prompt",
            value=st.session_state.framework_prompt,
            height=400,
            placeholder="""Example structure:
            
# Your Framework Name

**Theoretical Background:**
[Explain your theoretical approach and key concepts]

**Analysis Instructions:**
[Step-by-step instructions for applying your framework]
[What should the AI look for? How should it analyze?]

**Output Requirements:**
[How you want results organized and formatted]

**Examples:**
[Sample analysis to guide the AI's work]

**Tone and Approach:**
[Analytical stance, academic level, citation style]""",
            help="This becomes the 'system instruction' that guides the AI's analysis",
            key="custom_framework_textarea"
        )
        
        if framework_prompt and len(framework_prompt) > 100:
            st.session_state.framework_prompt = framework_prompt
            
            # Show framework stats
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Framework Length", f"{len(framework_prompt):,} chars")
            with col2:
                if len(framework_prompt) < 500:
                    st.metric("Quality", "Too Short", delta="⚠️")
                elif len(framework_prompt) > 15000:
                    st.metric("Quality", "Very Long", delta="⚠️")
                else:
                    st.metric("Quality", "Good", delta="✅")
            with col3:
                word_count = len(framework_prompt.split())
                st.metric("Word Count", f"{word_count:,}")
            
            # Framework analysis
            if st.checkbox("📊 Analyze Framework Quality"):
                st.markdown("**Framework Analysis:**")
                
                has_background = "background" in framework_prompt.lower() or "theory" in framework_prompt.lower()
                has_instructions = "instruction" in framework_prompt.lower() or "analyze" in framework_prompt.lower()
                has_examples = "example" in framework_prompt.lower() or "sample" in framework_prompt.lower()
                has_output = "output" in framework_prompt.lower() or "format" in framework_prompt.lower()
                
                components = [
                    ("Theoretical Background", has_background),
                    ("Analysis Instructions", has_instructions), 
                    ("Examples/Samples", has_examples),
                    ("Output Format", has_output)
                ]
                
                for component, present in components:
                    status = "✅" if present else "⚠️"
                    st.write(f"{status} {component}")
                
                completeness = sum(c[1] for c in components) / len(components)
                if completeness >= 0.75:
                    st.success("🎉 Well-structured framework!")
                else:
                    st.warning("💡 Consider adding missing components for better AI performance")
            
            # Only advance when user explicitly confirms
            if st.button("✅ Continue with this Framework", key="confirm_custom_framework"):
                st.session_state.current_step = max(st.session_state.current_step, 3)
                st.rerun()

def schema_builder():
    """Step 3: Interactive JSON Schema Builder"""
    if not st.session_state.framework_prompt:
        st.warning("⚠️ Please complete your framework prompt first")
        return
    
    st.markdown('<div class="step-header">🏗️ Step 3: Analysis Structure Designer</div>', unsafe_allow_html=True)
    
    # Educational framing
    st.markdown("""
    <div class="info-box">
    <b>Understanding Prompt vs. Schema:</b><br>
    🔧 <b>Your Prompt = Method</b> - The interpretive instrument (your theoretical lens)<br>
    📦 <b>Schema = Container</b> - The shape of acceptable answers for reuse and comparison
    </div>
    """, unsafe_allow_html=True)
    
    # Check if we're using the metaphor framework
    is_metaphor_framework = "Metaphor and Anthropomorphism" in st.session_state.framework_prompt
    is_framing_framework = "Framing Analysis" in st.session_state.framework_prompt
    
    if is_metaphor_framework or is_framing_framework:
        framework_type = "Metaphor Analysis" if is_metaphor_framework else "Framing Analysis"
        st.markdown(f"""
        <div class="success-box">
        <b>{framework_type}:</b> Using the specialized schema designed for this framework.
        </div>
        """, unsafe_allow_html=True)
        
        schema_to_use = METAPHOR_ANALYSIS_SCHEMA if is_metaphor_framework else FRAMEWORK_EXAMPLES["Political Framing Analysis"]["schema"]
        st.session_state.analysis_schema = schema_to_use
        st.session_state.model_configured = True
        st.session_state.current_step = max(st.session_state.current_step, 4)
        
        with st.expander(f"🔍 View {framework_type} Schema", expanded=False):
            st.json(schema_to_use)
        
        st.success(f"✅ {framework_type} schema configured automatically!")
        
    else:
        # Three-tiered approach
        st.markdown("### Choose Your Analysis Structure")
        
        structure_choice = st.radio(
            "Select the level of structure that fits your needs:",
            [
                "1. 🆓 Freeform Text (Exploration & Quick Reads)",
                "2. 📋 Light Structure (Assessment & Peer Review)", 
                "3. 🔧 Strict Schema (Reuse & Tool Building)",
                "4. 📄 Paste Existing Schema (I have one ready)"
            ],
            help="Each tier serves different pedagogical and research purposes",
            key="structure_tier_choice"
        )
        
        if "1. 🆓 Freeform" in structure_choice:
            st.markdown("""
            <div class="info-box">
            <b>Freeform Text Analysis</b><br>
            ✅ Best for: Early exploration, quick reads, creative interpretation<br>
            ✅ Easiest for students<br>
            ⚠️ Harder to compare across runs
            </div>
            """, unsafe_allow_html=True)
            
            st.session_state.analysis_schema = None
            st.session_state.model_configured = True
            st.session_state.current_step = max(st.session_state.current_step, 4)
            
            st.info("📝 The AI will provide structured paragraphs with clear headings.")
            
            if st.button("✅ Use Freeform Text", key="confirm_freeform"):
                st.success("Ready for analysis! Your framework will generate readable text output.")
                st.rerun()
        
        elif "2. 📋 Light Structure" in structure_choice:
            st.markdown("""
            <div class="info-box">
            <b>Light Structure Analysis</b><br>
            ✅ Best for: Classroom assessment, peer review, side-by-side comparison<br>
            ✅ Human-first but aligned outputs<br>
            ✅ Good balance of flexibility and consistency
            </div>
            """, unsafe_allow_html=True)
            
            # Simple structured format
            st.subheader("🔍 Framework Deconstruction")
            st.markdown("*Identify your main analysis categories:*")
            
            categories_input = st.text_area(
                "If you were teaching someone your framework, what are the 3-5 main things they should look for?",
                placeholder="Example for Literary Analysis:\n1. Character development patterns\n2. Symbolic language use\n3. Narrative structure choices\n4. Thematic connections",
                height=150,
                key="framework_categories"
            )
            
            # Create simple structure
            lightweight_schema = {
                "type": "object",
                "properties": {
                    "analysis_overview": {"type": "string"},
                    "main_findings": {
                        "type": "array",
                        "items": {
                            "type": "object", 
                            "properties": {
                                "category": {"type": "string"},
                                "evidence": {"type": "string"},
                                "interpretation": {"type": "string"}
                            },
                            "required": ["category", "evidence", "interpretation"]
                        }
                    },
                    "synthesis": {"type": "string"}
                },
                "required": ["analysis_overview", "main_findings", "synthesis"]
            }
            
            st.session_state.analysis_schema = lightweight_schema
            st.session_state.model_configured = True
            st.session_state.current_step = max(st.session_state.current_step, 4)
            
            if st.button("✅ Use Light Structure", key="confirm_light"):
                st.success("Ready for analysis! Your output will have consistent sections for easy comparison.")
                st.rerun()
        
        elif "3. 🔧 Strict Schema" in structure_choice:
            st.markdown("""
            <div class="info-box">
            <b>Strict Schema (JSON)</b><br>
            ✅ Best for: Reuse, tool building, batch processing, rigorous comparison<br>
            ✅ Enables rubric-aligned checks and data analysis<br>
            ⚠️ Requires more upfront design work
            </div>
            """, unsafe_allow_html=True)
            
            st.subheader("🏗️ Custom Schema Builder")
            
            # Framework deconstruction worksheet
            with st.expander("📋 Framework Deconstruction Worksheet", expanded=True):
                st.markdown("**Step 1: Identify Your Analysis Categories**")
                categories_text = st.text_area(
                    "What are the 3-5 main things your framework looks for?",
                    placeholder="List your main analytical categories...",
                    height=100,
                    key="schema_categories"
                )
                
                st.markdown("**Step 2: Define Information Needed**")
                details_text = st.text_area(
                    "For each category, what specific information do you need?",
                    placeholder="What questions does your framework ask? What would good evidence look like?",
                    height=100,
                    key="schema_details"
                )
            
            # Interactive schema builder
            if categories_text and details_text:
                st.markdown("**Step 3: Build Your Schema**")
                
                # Parse categories
                categories = [cat.strip() for cat in categories_text.split('\n') if cat.strip()]
                
                if len(categories) > 0:
                    schema = {"type": "object", "properties": {}, "required": []}
                    
                    for i, category in enumerate(categories):
                        st.markdown(f"**Category: {category}**")
                        
                        col1, col2 = st.columns(2)
                        with col1:
                            is_list = st.checkbox(
                                f"Multiple items for '{category}'?",
                                key=f"is_list_{i}",
                                help="Check if this category will have multiple examples/items"
                            )
                        
                        with col2:
                            if is_list:
                                fields_input = st.text_input(
                                    "Fields for each item (comma-separated)",
                                    placeholder="quote, analysis, significance",
                                    key=f"fields_{i}"
                                )
                        
                        # Build schema part
                        clean_category = category.lower().replace(' ', '_').replace('-', '_')
                        
                        if is_list and fields_input:
                            fields = [f.strip() for f in fields_input.split(',') if f.strip()]
                            if fields:
                                schema["properties"][clean_category] = {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {field: {"type": "string"} for field in fields},
                                        "required": fields
                                    }
                                }
                                schema["required"].append(clean_category)
                        else:
                            schema["properties"][clean_category] = {"type": "string"}
                            schema["required"].append(clean_category)
                    
                    # Add conclusion
                    schema["properties"]["conclusion"] = {"type": "string"}
                    schema["required"].append("conclusion")
                    
                    st.session_state.analysis_schema = schema
                    
                    with st.expander("🔍 Generated Schema Preview"):
                        st.json(schema)
                    
                    if st.button("✅ Use This Schema", key="confirm_custom_schema"):
                        st.session_state.model_configured = True
                        st.session_state.current_step = max(st.session_state.current_step, 4)
                        st.success("Custom schema configured! Ready for structured analysis.")
                        st.rerun()
            
            else:
                st.info("💡 Complete the framework deconstruction above to build your schema.")
        
        else:  # Paste Existing Schema
            st.markdown("""
            <div class="info-box">
            <b>Paste Existing Schema</b><br>
            ✅ Perfect for: Students who built schemas offline or want to reuse previous work<br>
            ✅ Supports any valid JSON Schema format<br>
            💡 Tip: Make sure your schema uses lowercase types ("object", "array", "string")
            </div>
            """, unsafe_allow_html=True)
            
            # Schema input area
            schema_text = st.text_area(
                "Paste your JSON Schema here:",
                height=300,
                placeholder="""{
  "type": "object",
  "properties": {
    "analysis_overview": {"type": "string"},
    "main_findings": {
      "type": "array", 
      "items": {
        "type": "object",
        "properties": {
          "category": {"type": "string"},
          "evidence": {"type": "string"},
          "analysis": {"type": "string"}
        },
        "required": ["category", "evidence", "analysis"]
      }
    },
    "conclusion": {"type": "string"}
  },
  "required": ["analysis_overview", "main_findings", "conclusion"]
}""",
                help="Paste a valid JSON Schema that defines your analysis structure",
                key="paste_schema_input"
            )
            
            if schema_text:
                try:
                    # Validate JSON
                    parsed_schema = json.loads(schema_text)
                    
                    # Basic validation
                    if not isinstance(parsed_schema, dict):
                        st.error("❌ Schema must be a JSON object")
                    elif "type" not in parsed_schema:
                        st.warning("⚠️ Schema should have a 'type' field")
                    elif "properties" not in parsed_schema:
                        st.warning("⚠️ Schema should have 'properties' field")
                    else:
                        # Schema looks valid
                        st.success("✅ Valid JSON Schema detected!")
                        
                        # Show preview
                        with st.expander("🔍 Schema Preview", expanded=True):
                            st.json(parsed_schema)
                        
                        # Schema analysis
                        col1, col2, col3 = st.columns(3)
                        
                        with col1:
                            num_properties = len(parsed_schema.get("properties", {}))
                            st.metric("Properties", num_properties)
                        
                        with col2:
                            required_fields = len(parsed_schema.get("required", []))
                            st.metric("Required Fields", required_fields)
                        
                        with col3:
                            has_arrays = any(
                                prop.get("type") == "array" 
                                for prop in parsed_schema.get("properties", {}).values()
                            )
                            complexity = "Complex" if has_arrays else "Simple"
                            st.metric("Complexity", complexity)
                        
                        # Use this schema
                        if st.button("✅ Use This Schema", key="confirm_pasted_schema"):
                            st.session_state.analysis_schema = parsed_schema
                            st.session_state.model_configured = True
                            st.session_state.current_step = max(st.session_state.current_step, 4)
                            st.success("Schema configured! Ready for structured analysis.")
                            st.rerun()
                            
                except json.JSONDecodeError as e:
                    st.error(f"❌ Invalid JSON: {str(e)}")
                    st.info("💡 Check for missing commas, quotes, or brackets")
                    
                except Exception as e:
                    st.error(f"❌ Schema error: {str(e)}")
            
            # Help section for schema creation
            with st.expander("❓ Need Help with JSON Schema Format?"):
                st.markdown("""
                **Basic JSON Schema Structure:**
                ```json
                {
                  "type": "object",
                  "properties": {
                    "section_name": {"type": "string"},
                    "list_section": {
                      "type": "array",
                      "items": {
                        "type": "object", 
                        "properties": {
                          "field1": {"type": "string"},
                          "field2": {"type": "string"}
                        },
                        "required": ["field1", "field2"]
                      }
                    }
                  },
                  "required": ["section_name", "list_section"]
                }
                ```
                
                **Key Points:**
                - Use lowercase types: "object", "array", "string"
                - "properties" defines the structure
                - "required" lists mandatory fields
                - "items" defines array element structure
                
                **Tools for Building Schemas:**
                - [JSON Schema Validator](https://www.jsonschemavalidator.net/)
                - [JSON Editor Online](https://jsoneditoronline.org/)
                """)
        
        # Add note about schema-framework relationship
        if st.session_state.get('analysis_schema'):
            st.markdown("""
            <div class="success-box">
            ✅ <b>Schema Ready!</b> Your framework prompt will provide the analytical method, 
            while your schema ensures consistent, structured output format.
            </div>
            """, unsafe_allow_html=True)

def text_input():
    """Step 4: Text Input for Analysis"""
    if not st.session_state.model_configured:
        st.warning("⚠️ Please complete the schema design first")
        return
    
    st.markdown('<div class="step-header">📖 Step 4: Text Input</div>', unsafe_allow_html=True)
    
    # Check if we're using specialized frameworks
    is_metaphor_framework = st.session_state.analysis_schema == METAPHOR_ANALYSIS_SCHEMA
    is_framing_framework = st.session_state.analysis_schema == FRAMEWORK_EXAMPLES.get("Political Framing Analysis", {}).get("schema")
    
    if is_metaphor_framework:
        st.markdown("""
        <div class="info-box">
        <b>Good Sources for Metaphor Analysis:</b><br>
        🤖 AI company blogs • 📰 Tech journalism • 📄 Research papers<br>
        🎤 Tech interviews • 📋 Policy documents • 💼 Product descriptions
        </div>
        """, unsafe_allow_html=True)
        
        text_options = [
            "Use example text (AI discourse)",
            "Paste your own text",
            "Upload text file"
        ]
    elif is_framing_framework:
        st.markdown("""
        <div class="info-box">
        <b>Good Sources for Framing Analysis:</b><br>
        🗳️ Political speeches • 📰 News articles • 📺 Campaign materials<br>
        📋 Policy documents • 💬 Social media posts • 🎤 Debate transcripts
        </div>
        """, unsafe_allow_html=True)
        
        text_options = [
            "Use example text (tax relief discourse)",
            "Paste your own text",
            "Upload text file"
        ]
    else:
        st.markdown("""
        <div class="info-box">
        <b>Good Text Sources:</b><br>
        📰 Articles • 📄 Academic papers • 🎤 Speeches • 📋 Documents<br>
        💼 Reports • 📚 Literary texts • 🗞️ News stories
        </div>
        """, unsafe_allow_html=True)
        
        text_options = [
            "Paste your text",
            "Upload text file"
        ]
    
    text_method = st.radio("How do you want to input text?", text_options)
    
    if text_method == "Use example text (AI discourse)" and is_metaphor_framework:
        # Load example text for metaphor analysis
        example_text = """Language models like Claude aren't programmed directly by humans—instead, they're trained on large amounts of data. During that training process, they learn their own strategies to solve problems. These strategies are encoded in the billions of computations a model performs for every word it writes. They arrive inscrutable to us, the model's developers. This means that we don't understand how models do most of the things they do.

Knowing how models like Claude think would allow us to have a better understanding of their abilities, as well as help us ensure that they're doing what we intend them to. For example:
* Claude can speak dozens of languages. What language, if any, is it using "in its head"?
* Claude writes text one word at a time. Is it only focusing on predicting the next word or does it ever plan ahead?
* Claude can write out its reasoning step-by-step. Does this explanation represent the actual steps it took to get to an answer, or is it sometimes fabricating a plausible argument for a foregone conclusion?

We take inspiration from the field of neuroscience, which has long studied the messy insides of thinking organisms, and try to build a kind of AI microscope that will let us identify patterns of activity and flows of information. There are limits to what you can learn just by talking to an AI model—after all, humans (even neuroscientists) don't know all the details of how our own brains work. So we look inside.

Today, we're sharing two new papers that represent progress on the development of the "microscope", and the application of it to see new "AI biology". In the first paper, we extend our prior work locating interpretable concepts ("features") inside a model to link those concepts together into computational "circuits", revealing parts of the pathway that transforms the words that go into Claude into the words that come out. In the second, we look inside Claude 3.5 Haiku, performing deep studies of simple tasks representative of ten crucial model behaviors, including the three described above. Our method sheds light on a part of what happens when Claude responds to these prompts, which is enough to see solid evidence that:

* Claude sometimes thinks in a conceptual space that is shared between languages, suggesting it has a kind of universal "language of thought." We show this by translating simple sentences into multiple languages and tracing the overlap in how Claude processes them.
* Claude will plan what it will say many words ahead, and write to get to that destination. We show this in the realm of poetry, where it thinks of possible rhyming words in advance and writes the next line to get there. This is powerful evidence that even though models are trained to output one word at a time, they may think on much longer horizons to do so.
* Claude, on occasion, will give a plausible-sounding argument designed to agree with the user rather than to follow logical steps. We show this by asking it for help on a hard math problem while giving it an incorrect hint. We are able to "catch it in the act" as it makes up its fake reasoning, providing a proof of concept that our tools can be useful for flagging concerning mechanisms in models."""
        
        st.session_state.text_to_analyze = example_text
        st.success("✅ Example text loaded - rich in AI metaphors!")
        
        with st.expander("📖 View Example Text", expanded=False):
            st.text_area("Example text:", value=example_text, height=200, disabled=True)
    
    elif text_method == "Use example text (tax relief discourse)" and is_framing_framework:
        # Load example text for framing analysis
        example_text = """The Finance Committee tax overhaul delivers benefits directly to the working and middle class through doubling the standard deduction and the child tax credit, as well as lowering rates across the board... Last night, the Senate Finance Committee passed comprehensive legislation to overhaul the nation’s broken tax code and create a fairer system that will move America forward, boost job growth, and increase hard-working Americans’ take-home pay. The Finance Committee’s tax reform plan includes the repeal of the regressive and punitive individual mandate tax, providing relief for working-class families who may not be able to afford or may not want to purchase health insurance. The proposal has received high-praise from thought-leaders.... The Senate Finance Committee kicked-off its markup of a once-in-a-generation opportunity to overhaul our nation’s tax code. In their opening statements, Republicans up and down the dais highlighted a key feature of the Tax Cuts and Jobs Act – tax relief and increased take-home pay for the middle class."""
        
        st.session_state.text_to_analyze = example_text
        st.success("✅ Example text loaded - rich in framing language!")
        
        with st.expander("📖 View Example Text", expanded=False):
            st.text_area("Example text:", value=example_text, height=200, disabled=True)
    
    elif "Paste" in text_method:
        text_to_analyze = st.text_area(
            "Text to Analyze",
            value=st.session_state.get('text_to_analyze', ''),
            height=300,
            placeholder="Paste your text here...",
            help="The AI will apply your framework to analyze this text"
        )
        if text_to_analyze:
            st.session_state.text_to_analyze = text_to_analyze
    
    else:  # Upload file
        uploaded_file = st.file_uploader("Upload text file", type=['txt', 'md'])
        if uploaded_file:
            text_to_analyze = uploaded_file.read().decode('utf-8')
            st.session_state.text_to_analyze = text_to_analyze
            st.success(f"✅ File uploaded: {len(text_to_analyze):,} characters")
    
    # Show text stats if we have text
    if st.session_state.get('text_to_analyze'):
        st.session_state.current_step = max(st.session_state.current_step, 5)
        
        text_length = len(st.session_state.text_to_analyze)
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Text Length", f"{text_length:,} chars")
        with col2:
            est_time = "1-2 min" if text_length < 10000 else "3-5 min"
            st.metric("Est. Time", est_time)
        with col3:
            status = "Good" if 1000 < text_length < 25000 else "Check length"
            st.metric("Status", status)

def run_analysis():
    """Step 5: Run the AI Analysis"""
    if not st.session_state.get('text_to_analyze'):
        st.warning("⚠️ Please input text to analyze first")
        return
    
    st.markdown('<div class="step-header">🎯 Step 5: AI Analysis</div>', unsafe_allow_html=True)
    
    # Show analysis parameters
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"**Framework:** {len(st.session_state.framework_prompt):,} characters")
        st.info(f"**Text Length:** {len(st.session_state.text_to_analyze):,} characters")
    
    with col2:
        format_type = "Structured" if st.session_state.analysis_schema else "Text"
        st.info(f"**Output Format:** {format_type}")
        st.info(f"**Model:** {st.session_state.model_name}")
    
    # Show current model configuration
    with st.expander("🔧 Current Model Configuration", expanded=False):
        config_display = {
            "Model": st.session_state.model_name,
            **st.session_state.generation_config
        }
        st.json(config_display)
    
    if st.button("🚀 Run Analysis", type="primary", use_container_width=True):
        # Use the external analysis runner with current config
        result = run_ai_analysis(
            st.session_state.text_to_analyze,
            st.session_state.framework_prompt,
            st.session_state.analysis_schema,
            st.session_state.model_name,
            st.session_state.generation_config
        )
        
        if result:
            st.session_state.analysis_results = result
            st.session_state.analysis_history.append(result)
            st.session_state.current_step = max(st.session_state.current_step, 6)
            st.success("🎉 Analysis completed successfully!")
            st.rerun()
        else:
            st.error("❌ Analysis failed. Please check your inputs and try again.")

def display_results():
    """Display analysis results"""
    if not st.session_state.analysis_results:
        st.warning("⚠️ No analysis results yet. Run an analysis first.")
        return
    
    st.markdown('<div class="step-header">📊 Analysis Results</div>', unsafe_allow_html=True)
    
    result = st.session_state.analysis_results
    
    # Results header
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info(f"**Generated:** {result['timestamp']}")
    with col2:
        st.info(f"**Format:** {'Structured' if result.get('use_json') else 'Text'}")
    with col3:
        if result.get('metadata', {}).get('total_tokens'):
            st.info(f"**Tokens:** {result['metadata']['total_tokens']:,}")
    
    # Use specialized display for different analysis types
    if isinstance(result['analysis'], dict) and 'metaphorAudit' in result['analysis']:
        display_metaphor_results(result['analysis'])
    else:
        # Generic display
        st.subheader("📄 Analysis Results")
        if isinstance(result['analysis'], dict):
            # Pretty display for structured results
            for section_name, section_content in result['analysis'].items():
                with st.expander(f"📂 {section_name.replace('_', ' ').title()}", expanded=True):
                    if isinstance(section_content, list):
                        if not section_content:
                            st.write("*No items found*")
                        else:
                            for i, item in enumerate(section_content, 1):
                                if isinstance(item, dict):
                                    st.markdown(f"**Item {i}:**")
                                    for field_name, field_value in item.items():
                                        st.write(f"• **{field_name.replace('_', ' ').title()}:** {field_value}")
                                else:
                                    st.write(f"{i}. {item}")
                                if i < len(section_content):
                                    st.divider()
                    
                    elif isinstance(section_content, dict):
                        for sub_name, sub_content in section_content.items():
                            st.write(f"**{sub_name.replace('_', ' ').title()}:** {sub_content}")
                    
                    else:
                        st.write(section_content)
        else:
            st.write(result['analysis'])
    
    # Download options
    st.subheader("💾 Download Results")
    col1, col2 = st.columns(2)
    
    with col1:
        json_str = json.dumps(result, indent=2, ensure_ascii=False)
        st.download_button(
            label="📄 Download JSON",
            data=json_str,
            file_name=f"analysis_{result['timestamp']}.json",
            mime="application/json"
        )
    
    with col2:
        markdown_report = create_markdown_report(result)
        st.download_button(
            label="📝 Download Report",
            data=markdown_report,
            file_name=f"analysis_report_{result['timestamp']}.md",
            mime="text/markdown"
        )

def reflection_section():
    """Step 6: Critical Reflection"""
    if not st.session_state.analysis_results:
        st.warning("⚠️ Complete an analysis first before reflecting")
        return
    
    st.markdown('<div class="step-header">🤔 Step 6: Critical Reflection</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <b>Reflect on AI as both INSTRUMENT and OBJECT:</b><br>
    🔧 <b>AI as Instrument:</b> How well did it apply your framework?<br>
    🔍 <b>AI as Object:</b> What does its performance reveal about AI capabilities?
    </div>
    """, unsafe_allow_html=True)
    
    # Guided questions
    with st.expander("📋 Reflection Guide Questions", expanded=True):
        st.markdown("""
        **🔧 AI as Analytical Instrument:**
        - How accurately did the AI apply your theoretical framework?
        - What aspects did it handle well vs. poorly?
        - Were the examples and quotes appropriate and insightful?
        - How does the analysis compare to what a human expert might produce?
        
        **🔍 AI as Object of Study:**
        - What patterns did you notice in how the AI interprets theory?
        - What does the AI's performance reveal about its strengths/limitations?
        - How does AI analytical thinking differ from human thinking?
        - What biases or blind spots did you observe?
        
        **💭 Synthesis and Implications:**
        - How has this changed your understanding of AI capabilities?
        - What are the ethical implications of using AI for analysis?
        - How might AI tools change academic research and writing?
        """
        )
    
    reflection_text = st.text_area(
        "Your Reflection",
        value=st.session_state.reflection_text,
        height=400,
        placeholder="Write your critical reflection here...\n\nConsider specific examples from your analysis results, comparisons to manual analysis, insights about AI capabilities and limitations, and implications for academic integrity and scholarship.",
        help="This reflection is a key deliverable for understanding AI literacy"
    )
    
    if reflection_text:
        st.session_state.reflection_text = reflection_text
        
        # Reflection analysis
        reflection_length = len(reflection_text)
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Reflection Length", f"{reflection_length:,} chars")
        
        with col2:
            if reflection_length < 500:
                st.metric("Status", "Too Short", delta="⚠️")
            else:
                st.metric("Status", "Good", delta="✅")
        
        if reflection_length >= 500:
            st.success("✅ Substantial reflection provided!")
        
        # Download reflection
        if st.button("💾 Download Reflection"):
            reflection_content = f"""# AI Framework Analysis Reflection
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Analysis Summary
- **Framework Used:** {st.session_state.framework_prompt[:100]}...
- **Model Used:** {st.session_state.analysis_results.get('model', 'Unknown')}
- **Text Analyzed:** {st.session_state.analysis_results['text_length']:,} characters
- **Analysis Format:** {'Structured' if st.session_state.analysis_results.get('use_json') else 'Text'}
- **Generated:** {st.session_state.analysis_results['timestamp']}

## Critical Reflection

{reflection_text}
"""
            
            st.download_button(
                label="📄 Download Reflection",
                data=reflection_content,
                file_name=f"reflection_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
                mime="text/markdown"
            )

def main():
    """Main application"""
    init_session_state()
    
    # Header
    st.markdown('<div class="main-header">🔬 AI Framework Analysis Tool v2</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <b>Welcome!</b> Apply theoretical frameworks to texts using AI, then critically examine both the results and the AI's performance.<br>
    <b>Note:</b> This is v2 with enhanced schema building capabilities and example frameworks.
    </div>
    """, unsafe_allow_html=True)
    
    # Progress indicator
    display_progress()
    
    # Sidebar navigation
    st.sidebar.title("📋 Navigation")
    
    sections = {
        "🔑 API Setup": setup_api,
        "📚 Framework": framework_input,
        "🏗️ Schema Builder": schema_builder,
        "📖 Text Input": text_input,
        "🎯 Run Analysis": run_analysis,
        "📊 View Results": display_results,
        "🤔 Reflection": reflection_section
    }
    
    selected_section = st.sidebar.radio(
        "Choose a section:",
        list(sections.keys()),
        index=0,  # Always start at first section
        key="main_navigation"
    )
    
    # Show selected section
    sections[selected_section]()
    
    # Sidebar status
    st.sidebar.markdown("---")
    st.sidebar.subheader("📈 Status")
    
    status_items = [
        ("API Configured", st.session_state.api_configured),
        ("Framework Set", bool(st.session_state.framework_prompt)),
        ("Schema Ready", st.session_state.model_configured),
        ("Text Input", bool(st.session_state.get('text_to_analyze'))),
        ("Analysis Complete", bool(st.session_state.analysis_results)),
        ("Reflection Written", bool(st.session_state.reflection_text))
    ]
    
    for item, status in status_items:
        emoji = "✅" if status else "⏳"
        st.sidebar.write(f"{emoji} {item}")
    
    # Analysis history in sidebar
    if st.session_state.analysis_history:
        st.sidebar.markdown("---")
        st.sidebar.subheader(f"📚 Analysis History ({len(st.session_state.analysis_history)})")
        for i, run in enumerate(st.session_state.analysis_history[-3:], 1):  # Show last 3
            st.sidebar.write(f"📄 Run {i}: {run['timestamp']}")

if __name__ == "__main__":
    main()