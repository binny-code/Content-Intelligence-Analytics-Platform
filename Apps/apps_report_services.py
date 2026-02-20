from apps.analytics.services import regression_analysis
from apps.llm_engine.llm_service import analyze_content

def generate_business_report():
    stats = regression_analysis()

    explanation_prompt = f"""
    Explain this statistical result in business terms:
    {stats}
    """

    explanation = analyze_content(explanation_prompt)

    return {
        "statistics": stats,
        "business_explanation": explanation
    }
