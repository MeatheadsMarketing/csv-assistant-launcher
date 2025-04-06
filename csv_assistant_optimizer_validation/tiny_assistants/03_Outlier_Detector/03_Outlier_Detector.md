# Assistant: Outlier Detector

## Purpose:
Flags statistical outliers in numeric fields.

## Strategy:
- Apply validation rules and output flagged results
- Where applicable, allow user-defined thresholds via UI
- Return a DataFrame with validation results or a separate report
- Ensure compatibility with downstream validation summary generator
