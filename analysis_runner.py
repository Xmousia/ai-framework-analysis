# analysis_runner.py
# Handles the AI analysis execution

import streamlit as st
import google.generativeai as genai
import json
from datetime import datetime

def run_ai_analysis(text, framework_prompt, analysis_schema=None, model_name="gemini-2.5-flash", generation_config=None):
    """
    Run AI analysis using the provided framework and schema
    
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
        # Show progress
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        status_text.text(f"🤖 Configuring {model_name}...")
        progress_bar.progress(10)
        
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
        
        progress_bar.progress(25)
        status_text.text("📤 Sending analysis request...")
        
        # Generate the content
        response = model.generate_content(text)
        
        progress_bar.progress(75)
        status_text.text("🔍 Processing response...")
        
        # Extract and process the response
        analysis_text = response.text
        
        if use_json:
            try:
                # Clean and parse JSON
                cleaned_text = analysis_text.strip()
                analysis_data = json.loads(cleaned_text)
                status_text.text("✅ JSON parsing successful!")
            except json.JSONDecodeError as e:
                st.warning(f"⚠️ JSON parsing failed: {e}")
                st.info("📄 Using text format instead")
                analysis_data = analysis_text
                use_json = False
        else:
            analysis_data = analysis_text
        
        progress_bar.progress(90)
        status_text.text("💾 Saving results...")
        
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
        
        progress_bar.progress(100)
        status_text.text("🎉 Analysis complete!")
        
        return result
        
    except Exception as e:
        st.error(f"❌ Analysis failed: {str(e)}")
        st.info("💡 Troubleshooting tips:")
        st.info("• Check your API key configuration")
        st.info(f"• Verify model '{model_name}' is available")
        st.info("• Try with shorter text (under 25,000 characters)")
        st.info("• Verify your framework prompt is properly formatted")
        return None