# Assistant: Named Entity Expansion

## Purpose:
Extends partial entities (e.g., 'Apple' → 'Apple Inc., US tech firm').

## Strategy:
- Use AI (LLM or ML models) to classify or tag rows/columns with semantic labels
- Provide controls for model selection, taxonomy import, or confidence threshold
- Return enriched DataFrame with new columns or tags
- Preserve original data and append results in new fields
