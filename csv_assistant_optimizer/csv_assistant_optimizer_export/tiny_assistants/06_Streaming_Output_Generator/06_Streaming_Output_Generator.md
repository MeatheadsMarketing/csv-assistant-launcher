# Assistant: Streaming Output Generator

## Purpose:
Sends data in chunks (e.g., for Kafka, webhooks, batch APIs).

## Strategy:
- Convert the DataFrame into a structured output format
- Allow user to configure export options (filename, schema, destination)
- Trigger downloads, webhooks, or file saves
- Return confirmation or preview of exported format
