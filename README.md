# AI Framework Analysis Tool

A Streamlit application for applying theoretical frameworks to texts using AI, designed as the digital scholarship extension for the **"Prompt-as-Instrument Workshop: Using LLMs to Perform Theory-Driven Readings of Human Texts."**

*Developed as part of the AI literacy initiatives of W&M Libraries.*

## Educational Context

This tool serves as **Step 9** of the Prompt-as-Instrument Workshop, where students approach AI literacy as interpretive practice. Students use LLMs as both *instrument* (enacting theoretical methods) and *object* (producing outputs for critical analysis). The tool integrates with ACRL Framework standards including Research as Inquiry, Information Creation as Process, and Authority as Constructed.

### 8-Step Workshop Process
1. **Pick Your Text** *(Research as Inquiry)*
2. **Pick Your Lens** *(Strategic Exploration)*  
3. **Summarize Framework** *(Scholarship as Conversation)*
4. **Plan Your Analysis (Blueprint)** *(Information Creation)*
5. **Write Your Prompt** *(Authority as Constructed)*
6. **Test and Revise** *(Information Creation)*
7. **Annotate the Output** *(Authority as Constructed)*
8. **Write Your Reflection** *(Information Has Value)*
9. **Digital Scholarship Extension** *(This Tool)*

## Features

- **Three Sophisticated Frameworks**: Pre-built analyses for Metaphor/Anthropomorphism, Political Framing, and Aristotelian Rhetorical Analysis
- **Complete Framework Transparency**: Full theoretical prompts visible (no truncation) for educational transparency
- **Robust Error Handling**: Enhanced JSON parsing with automatic repair and graceful fallbacks
- **5-Step Analysis Pipeline**: Clear workflow from API setup through results review
- **Workshop Integration**: Downloadable resources package with complete pedagogical framework
- **Professional Results Display**: Framework-specific formatting with download capabilities
- **Educational Focus**: Supports critical AI literacy through theory-driven practice

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Get a Google AI API key:**
   - Visit [Google AI Studio](https://aistudio.google.com/apikey)
   - Sign in with your Google account
   - Accept terms and create an API key
   - Keep this key secure (never share publicly)

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```

4. **Try the workshop approach:**
   - Start with the Workshop page to understand pedagogical context
   - Move through the 5-step analysis pipeline
   - Use provided example texts for initial exploration
   - Download results for critical annotation (Workshop Step 7)

## File Structure

```
├── app.py                # Main Streamlit application (production ready)
├── framework_data.py     # Framework prompts, schemas, and example texts
├── display_utils.py      # Specialized result display utilities
├── analysis_runner.py    # AI analysis execution (optional - enhanced version in app.py)
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Available Frameworks

### 1. Metaphor & Anthropomorphism Analysis
- **Purpose**: AI discourse analysis using cognitive linguistics
- **Method**: Brown's explanation typology + structure-mapping theory
- **Output**: Metaphor audit, source-target mapping, explanation analysis
- **Use Case**: Critical AI literacy, examining "illusion of mind" in AI discourse

### 2. Political Framing Analysis  
- **Purpose**: Political discourse analysis using Entman's framing functions
- **Method**: Frame identification, role assignment, reasoning effects
- **Output**: Structured frame analysis with lexical cues and counterframe linkage
- **Use Case**: Political communication, media analysis, policy discourse

### 3. Aristotelian Rhetorical Analysis
- **Purpose**: Comprehensive rhetorical analysis of persuasive discourse  
- **Method**: Ethos, pathos, logos identification and effectiveness assessment
- **Output**: Detailed appeal analysis with strategic integration assessment
- **Use Case**: Speech analysis, persuasive writing, communication studies

## 5-Step Analysis Pipeline

### Step 1: API Setup
- Configure Google AI API key with connection testing
- Select from available Gemini models (2.0-flash, 2.0-pro, etc.)
- Adjust parameters (temperature, token limits) for educational needs

### Step 2: Framework Selection  
- Browse three sophisticated frameworks with complete theoretical context
- View full prompts and schemas (educational transparency)
- Download framework documentation and workshop resources

### Step 3: Text Input
- Use provided examples optimized for each framework
- Paste custom text or upload documents
- Preview text with character/word counts

### Step 4: Run Analysis
- Execute framework with robust error handling
- Automatic JSON repair for parsing issues
- Clear progress indicators and error feedback

### Step 5: View Results
- Framework-specific result displays
- Download as JSON (structured data) or formatted reports
- Support for Workshop Step 7 (critical annotation)

## Educational Applications

### Workshop Deployment
- **Instructor demonstration**: Show framework-to-prompt process
- **Student extension**: Digital scholarship after manual workshop completion  
- **Assessment support**: Results align with workshop rubric elements
- **Critical engagement**: Tool as both instrument and object of analysis

### AI Literacy Outcomes
- **Theoretical operationalization**: Bridge abstract frameworks and computational implementation
- **Critical AI evaluation**: Examine AI performance and limitations systematically
- **Digital scholarship skills**: Create professional, citable analytical tools
- **Methodological transparency**: Full visibility into AI configuration and prompts

### Course Integration
- **Upper-level undergraduates**: Advanced writing and analysis courses
- **Graduate students**: Digital humanities and research methods
- **Writing instructors**: Integrate theory-driven AI literacy into composition pedagogy
- **Cross-disciplinary**: Adaptable frameworks for various fields

## Technical Specifications

### AI Models Supported
- **gemini-2.0-flash**: Balanced performance (default, recommended)
- **gemini-2.0-pro**: Enhanced reasoning for complex frameworks
- **gemini-1.5-flash**: Alternative option
- **learnlm-1.5-pro-experimental**: Educational optimization

### Enhanced Error Handling
- **Smart JSON Repair**: Automatic fixing of common formatting issues
- **Graceful Fallbacks**: Text format when JSON repair fails
- **User Feedback**: Clear error messages and troubleshooting guidance
- **Retry Mechanism**: Users can easily re-run failed analyses

### Configuration Options
- **Temperature control**: Balance creativity vs. consistency (0.0-1.0)
- **Token limits**: Configurable response length (1000-8000 tokens)
- **Educational parameters**: Optimized defaults for pedagogical use

## Deployment

### Streamlit Cloud (Recommended for Education)
1. **Push to GitHub**: Commit all files to your repository
2. **Connect Streamlit Cloud**: Visit [share.streamlit.io](https://share.streamlit.io)
3. **Deploy automatically**: Updates when you push changes
4. **Student access**: Students use their own API keys (low cost)
5. **Workshop integration**: Direct link from course materials

### Local Development
```bash
# Clone repository
git clone [your-repo-url]
cd ai-framework-analysis

# Install dependencies
pip install -r requirements.txt

# Run application  
streamlit run app.py
```

### Institutional Deployment
- **Custom domains**: Deploy on Heroku/Railway for institutional branding
- **API management**: Consider rate limiting for public access
- **Course integration**: Include setup instructions in syllabus

## Workshop Assessment Integration

### Supports All Workshop Deliverables
- **Framework Blueprints**: Tool demonstrates professional implementation
- **Prompt Refinement**: Students can compare their prompts to professional versions
- **Critical Annotation**: Download results for Workshop Step 7
- **Reflection Essays**: Tool performance supports Workshop Step 8 analysis

### Assessment Rubric Elements
- **Theoretical Sophistication**: Tool shows advanced framework implementation
- **Technical Competence**: Professional-grade error handling and UX
- **Critical Awareness**: Transparency enables evaluation of AI as instrument/object
- **Digital Scholarship**: Demonstrates theory-to-computation pipeline

## API Usage and Costs

### Token Management
- **Typical analysis**: 3,000-8,000 tokens ($0.01-0.02 per run)
- **Student-friendly**: Low cost for educational exploration
- **Free tier**: Google AI provides generous free monthly allocation
- **Built-in estimates**: Token counting and cost prediction

### Best Practices for Education
- **Start with examples**: Use provided texts for reliable results
- **Iterate efficiently**: Test with shorter texts before longer analyses
- **Monitor usage**: Teach students to track API consumption

## Future Enhancements (High Priority)

### Pedagogically Valuable Additions
1. **Framework Comparison Mode**: Run same text through multiple frameworks
2. **Iteration Dashboard**: Track prompt refinement process over time
3. **Built-in Annotation Interface**: Support Workshop Step 7 directly in tool
4. **Reflection Prompts**: Guided questions for Workshop Step 8

### Extended Features
- **Collaborative Workspace**: Share and comment on analyses
- **Assessment Integration**: Direct connection to LMS platforms
- **Framework Builder Wizard**: Guided creation of new frameworks
- **Performance Analytics**: Track learning and tool usage patterns

## Contributing

### Framework Development
- **New theoretical frameworks**: Submit implementations for different disciplines
- **Pedagogical improvements**: Enhance workshop integration and assessment support
- **Display enhancements**: Better formatting for complex analytical outputs

### Technical Contributions
- **Error handling**: Further improve JSON parsing reliability
- **User experience**: Enhanced guidance and educational scaffolding
- **Performance**: Optimization for educational use patterns

## License

Open source - designed for educational and research use. Contributions welcome under educational fair use principles. Tool developed to support responsible AI literacy education in humanities contexts.

## Citation

When using this tool in academic work or sharing with students, please cite as:
```
AI Framework Analysis Tool: Digital Extension for Prompt-as-Instrument Workshop.
[W&M Libraries], 2025. https://[libraries.wm.edu]
```