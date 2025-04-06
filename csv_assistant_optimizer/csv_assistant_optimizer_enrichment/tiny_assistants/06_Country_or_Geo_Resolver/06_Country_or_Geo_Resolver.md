# Assistant: Country/Geo Resolver

## Purpose:
Enriches locations with geo data (country code, continent, etc.).

## Strategy:
- Apply AI, statistical, or rule-based inference depending on the feature
- Provide optional tuning controls via kwargs or UI sliders
- Ensure non-destructive enrichment (add columns instead of overwriting)
- Log confidence levels where applicable
