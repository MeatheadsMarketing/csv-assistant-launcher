# Assistant: Column Value Filter Generator

## Purpose:
Builds drop-down or checkbox filters for selected column values.

## Strategy:
- Use pandas filtering, regex, and date parsing to build logic
- Use Streamlit widgets (checkboxes, sliders, dropdowns) for inputs
- Return only the filtered/selected portion of the data
- Tag or export the subset as needed for downstream use
