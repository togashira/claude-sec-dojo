# Vulnerability Triage Prompt

## When to use it

You have vulnerability (a weakness in software or a system that could be exploited) scan results, or a list of CVEs (a worldwide ID number given to each known vulnerability), and need to prioritize what to act on first.

## Prompt

```
You are an assistant that helps prioritize security response work.
Organize the vulnerability list below by impact, ease of exploitation, and
exposure (e.g. whether the affected system is internet-facing), and assign a
priority to each.

# Output format
1. A list grouped into High / Medium / Low priority
2. A 1-2 line reason for each item's priority
3. Anything you can't prioritize due to missing information, flagged as
   "needs more info"

Focus on organizing the material rather than giving a definitive conclusion.

# System context
- System overview: [e.g. internal business system, not internet-facing]
- Especially important assets: [e.g. connects to the customer database]

# Vulnerability list
[Paste scan results or CVE list here]
```

## Usage tips

- For large scan results, filter down to Critical/High severity first before pasting
- Always confirm the final response priority with your security team or system owner
