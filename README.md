# ai-framework-analysis
Streamlit application for applying theoretical frameworks to texts using AI, with built-in support for sophisticated discourse analysis and digital scholarship education.

# requirements.txt
streamlit>=1.28.0
google-generativeai>=0.7.0

# README.md
# AI Framework Analysis Tool

A Streamlit application for applying theoretical frameworks to texts using AI, with built-in support for sophisticated discourse analysis including metaphor analysis and political framing.

## Features

- **Example Framework Library**: Pre-built sophisticated frameworks (Metaphor Analysis, Political Framing) 
- **Three-Tiered Structure Options**: Freeform text, light structure, or strict JSON schemas
- **Interactive Schema Builder**: Design custom analysis structures with guided worksheets
- **Schema Import**: Paste existing JSON schemas built offline
- **AI-Powered Analysis**: Uses Google's latest Gemini models (2.5-pro, 2.5-flash, etc.)
- **Specialized Result Display**: Framework-aware formatting for complex analyses
- **Complete Workflow**: From framework design through critical reflection
- **Export Capabilities**: Download results as JSON and formatted markdown reports
- **Educational Focus**: "Prompt-as-Instrument" methodology for digital scholarship

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
   streamlit run app_v2_complete.py
   ```

4. **Try the examples:**
   - Start with "Metaphor & Anthropomorphism Analysis" 
   - Use the provided AI discourse text
   - Explore the structured JSON output

## File Structure

```
├── app_v2_complete.py    # Main Streamlit application (latest version)
├── framework_data.py     # Framework prompts and schemas
├── analysis_runner.py    # AI analysis execution
├── display_utils.py      # Result display utilities
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Usage Examples

### Example 1: Metaphor Analysis (Pre-built)
1. **Select framework**: "Browse Example Frameworks" → "Metaphor & Anthropomorphism Analysis"
2. **Auto-load schema**: Specialized JSON structure for discourse analysis
3. **Use example text**: AI discourse rich in metaphorical language
4. **Run analysis**: 3-part audit (metaphor identification, source-target mapping, explanation typology)
5. **Review results**: Structured findings with downloadable report

### Example 2: Political Framing (Pre-built)
1. **Select framework**: "Political Framing Analysis"
2. **Use tax discourse example**: Pre-loaded text about "tax relief"
3. **Analyze frames**: Entman's functions + Lakoff's frame semantics
4. **Export findings**: Professional report suitable for research

### Example 3: Custom Framework
1. **Create custom framework**: Use guided prompts and examples
2. **Choose structure level**: 
   - Freeform (exploration)
   - Light structure (assessment)
   - Strict schema (research tools)
3. **Build with worksheet**: Framework deconstruction guide
4. **Test and iterate**: Refine based on results

## Educational Applications

### Digital Scholarship Courses
- **"Prompt-as-Instrument" methodology**: Students create deployable analysis tools
- **Theory operationalization**: Bridge abstract concepts and computational implementation
- **Digital artifact creation**: Professional tools suitable for sharing and citation

### AI Literacy Education
- **AI as instrument and object**: Critical examination of both results and AI performance
- **Reflection integration**: Guided questions about AI capabilities and limitations
- **Methodological transparency**: All steps visible and documentable

### Research Applications
- **Reproducible analysis**: JSON schemas ensure consistent structure across runs
- **Comparative studies**: Standard formats enable cross-text analysis
- **Tool development**: Framework → schema → deployable instrument pipeline

## Framework Examples

### Metaphor & Anthropomorphism Analysis
- **Theoretical grounding**: Cognitive linguistics + philosophy of social science
- **Three-part audit**: Metaphor identification, source-target mapping, explanation typology
- **AI literacy focus**: Surfaces "illusion of mind" in AI discourse
- **Output**: Structured JSON with detailed findings and synthesis

### Political Framing Analysis  
- **Theoretical grounding**: Entman's framing functions + Lakoff's frame semantics
- **Components**: Frame identification, role assignment, reasoning effects, counterframe analysis
- **Policy focus**: How language shapes political understanding
- **Output**: Comprehensive frame mapping with synthesis

## Technical Specifications

### AI Models Supported
- **gemini-2.5-pro**: Most capable for complex analysis
- **gemini-2.5-flash**: Balanced performance and speed (default)
- **gemini-2.5-flash-lite**: Lightweight for quick iteration
- **learnlm-2.0-flash-experimental**: Educational optimization

### Configuration Options
- **Temperature control**: Creativity vs. consistency (0.0-1.0)
- **Token limits**: Configurable response length (1000-16000)
- **Advanced parameters**: Top-p, top-k for fine-tuning

### Data Management
- **Session persistence**: Work saves during browser session
- **Export formats**: JSON (structured data) + Markdown (readable reports)
- **Analysis history**: Track multiple runs for comparison
- **No data storage**: API keys and content never saved server-side

## Deployment

### Local Development
```bash
# Clone repository
git clone [your-repo-url]
cd ai-framework-analysis

# Install dependencies
pip install -r requirements.txt

# Run application
streamlit run app_v2_complete.py
```

### Streamlit Cloud (Recommended)
1. **Create GitHub repository** with your code
2. **Connect to Streamlit Cloud**: [share.streamlit.io](https://share.streamlit.io)
3. **Auto-deploy**: Updates when you push to GitHub
4. **Share URL**: Students use their own API keys

### Institutional Deployment
- **Heroku/Railway**: For custom domains and control
- **API management**: Consider rate limiting for public use
- **Student instructions**: Include API key setup in course materials

## Educational Integration

### Assignment Sequence
1. **Week 1-2**: Framework development in Colab (scaffolded)
2. **Week 3**: Convert to Streamlit tool (digital scholarship)
3. **Week 4**: Deploy and share publicly (portfolio building)
4. **Week 5**: Peer review of tools (assessment)

### Assessment Applications
- **Framework quality**: Theoretical sophistication and operationalization
- **Tool functionality**: Technical implementation and usability
- **Critical reflection**: AI literacy and methodological awareness
- **Digital artifact**: Professional presentation and documentation

### Pedagogical Benefits
- **Theory-practice bridge**: Abstract concepts become concrete tools
- **Computational thinking**: Logical decomposition without coding barriers
- **Public scholarship**: Tools become citable, shareable research instruments
- **AI literacy**: Critical engagement with AI capabilities and limitations

## API Usage and Costs

### Token Management
- **Typical analysis**: 5,000-15,000 tokens ($0.01-0.03)
- **Complex frameworks**: May use 20,000+ tokens ($0.04+)
- **Students pay**: Individual API keys, low-cost exploration
- **Free tier**: Google AI Studio provides generous free usage

### Best Practices
- **Start simple**: Use shorter texts for initial testing
- **Iterate efficiently**: Refine prompts before long analyses
- **Monitor usage**: Built-in token counters and cost estimates

## Contributing

### Framework Development
- **New examples**: Submit frameworks for different disciplines
- **Schema patterns**: Contribute reusable JSON structures
- **Display logic**: Enhance results formatting for specific frameworks

### Technical Improvements
- **UI/UX**: Better guidance and error handling
- **Assessment tools**: Rubric integration and grading features
- **Analytics**: Usage tracking and learning insights

### Educational Resources
- **Documentation**: Setup guides and troubleshooting
- **Video tutorials**: Framework design and tool usage
- **Assignment templates**: Ready-to-use course materials

## License

Open source - designed for educational and research use. Contributions welcome under educational fair use principles.