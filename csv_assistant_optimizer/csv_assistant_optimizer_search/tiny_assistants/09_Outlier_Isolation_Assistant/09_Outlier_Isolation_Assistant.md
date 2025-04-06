# Assistant: Outlier Isolation Assistant

## Purpose:
Tags rows that are statistical outliers for any given metric.

## Strategy:
- Use pandas filtering, regex, and date parsing to build logic
- Use Streamlit widgets (checkboxes, sliders, dropdowns) for inputs
- Return only the filtered/selected portion of the data
- Tag or export the subset as needed for downstream use
