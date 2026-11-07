# Initial Incident Report Prompt

## When to use it

A security incident (including a suspected one) has happened, and you need to quickly put together an initial report to share with stakeholders.

## Prompt

```
Below are raw notes taken during incident response. Organize them into an
initial report to share with stakeholders.

# Output format
1. Summary (3 lines or fewer)
2. Confirmed facts, in timeline order
3. Speculation / anything not yet confirmed (list under "open items")
4. Actions already taken
5. What decision or escalation is needed next

Clearly separate facts from speculation. Do not fill gaps with guesses.

# Incident info
- Detected at: [e.g. 2026-11-01 23:40]
- Detection source: [e.g. monitoring system alert]

# Raw notes
[Paste your response notes/logs here]
```

## Usage tips

- It's fine to paste in whatever you know so far, even mid-response - update it as things develop
- Treat the output as a draft - review it before sharing with stakeholders
