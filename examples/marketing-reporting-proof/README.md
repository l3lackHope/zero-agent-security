# Marketing Reporting Automation Proof

Self-directed portfolio proof. **Not client production history.**

This small runnable example mirrors a paid n8n reporting brief:

- ingest representative Meta Ads + GA4-style metrics
- normalize them into one weekly reporting schema
- calculate week-on-week changes
- produce a short summary payload suitable for AI-assisted polishing
- prepare a delivery object for Monday email
- keep the design simple enough to swap the sample inputs for real APIs later

## Run

```bash
python test_reporting.py
```

The sample code uses only the Python standard library.

## Why this exists

The production version would replace sample inputs with the buyer's Meta Marketing API, Google Ads API and GA4 properties, then write to Google Sheets or BigQuery, feed Looker Studio, generate a concise summary, email it on schedule and alert on failures.

This proof deliberately does **not** claim a live paid-client Meta/Google Ads deployment.
