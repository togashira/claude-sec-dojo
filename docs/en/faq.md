# FAQ

**Q. Can I learn attack techniques (penetration testing, etc.) here?**
No. This repository deliberately scopes itself to defensive practice — detection, triage, and reporting. If you want to learn offensive techniques, look for properly authorized CTF platforms or dedicated courses elsewhere.

**Q. Can I paste real logs or config files into Claude?**
We don't recommend it. Real internal logs, credentials, and customer data can contain personal or sensitive information. The hands-on exercises here assume dummy data. If you need to work with real data, follow your company's security policy and data-handling rules, and anonymize or sample it first.

**Q. Should I just trust Claude's findings ("this looks suspicious", "this is risky")?**
Treat them as a starting point. Claude is good at surfacing possible anomalies and risks, but it also produces false positives. The final judgment and response should come from a human who knows the actual situation.

**Q. I can't program. Can I still use what's under `tools/`?**
`tools/` requires basic Python knowledge. Start with `modules/` and `templates/` in chat form at [claude.ai](https://claude.ai) first.

**Q. Is this useful even if my company has a dedicated security team?**
Yes. This isn't a replacement for a specialist team — it's meant to raise the quality of first-pass review and initial response from infrastructure/cloud engineers on the ground, which also makes escalation to the specialist team faster and more accurate.
