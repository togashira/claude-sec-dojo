# Log Anomaly Analysis Prompt

## When to use it

You have logs from a network device or server and want to find behavior that might be abnormal.

## Prompt

```
You are an assistant that helps with security log analysis.
Analyze the log below and pick out up to 5 behaviors you consider abnormal.
For each one, include:
1. What might be happening (framed as a possibility, not a conclusion)
2. The specific log lines that support this
3. What to check next
Do not fill in information that isn't in the log by guessing.

# Context
- Device/system: [e.g. firewall fw01]
- Normal behavior (if known): [e.g. mostly successful auth from internal IPs, 9am-6pm weekdays]

# Log
[Paste the log here — strip any personal or sensitive data if this is real data]
```

## Usage tips

- For long logs, filtering by time window or IP range before pasting improves accuracy
- Treat the output as "possible" findings — the final judgment is yours
