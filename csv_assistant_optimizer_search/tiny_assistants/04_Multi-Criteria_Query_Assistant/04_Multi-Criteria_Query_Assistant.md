# Assistant: Multi-Criteria Query Assistant

## Purpose:
Lets users combine multiple filters (e.g., price < 50 and category = A).

## Strategy:
- Use pandas filtering, regex, and date parsing to build logic
- Use Streamlit widgets (checkboxes, sliders, dropdowns) for inputs
- Return only the filtered/selected portion of the data
- Tag or export the subset as needed for downstream use
