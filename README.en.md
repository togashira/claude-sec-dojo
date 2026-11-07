# ClaudeSecDojo

**A beginner-friendly open-source project for IT engineers to build real-world security skills with Claude.**
Starting from day-to-day practice — network operations, cloud infrastructure, log analysis — this repo collects guides, prompt templates, and working tools that use Claude as a partner for learning security thinking and workflows.

[日本語版はこちら](README.md)

## What this is

Security isn't just a specialist team's job — it's something every infrastructure, cloud, and development engineer runs into regularly. Yet many working engineers never get a systematic chance to learn practical skills like:

- How to spot anomalies in logs
- How to check cloud configurations for misconfigurations
- What to do, and how to report, when an incident happens

This repository focuses on building **defensive practice — detection, triage, and reporting skills — not offensive technique**, and provides:

- **Learning modules** that teach security thinking ([modules/](modules/))
- **Prompt templates** you can copy and use as-is ([templates/](templates/en/))
- **Simple working tools** such as a log-anomaly-triage draft generator ([tools/](tools/))

**Scope of this repository:** defensive practice only — log analysis, configuration review, incident reporting. It does not cover attack techniques or penetration-testing methodology against real systems.

## Quick start

1. Read [docs/en/getting-started.md](docs/en/getting-started.md)
2. Check the suggested order in [docs/en/learning-path.md](docs/en/learning-path.md)
3. Work through the modules under [modules/](modules/) one at a time
4. Copy a prompt from [templates/en/](templates/en/) for situations you hit in your own work
5. When you're ready to automate further, try [tools/log-triage-agent/](tools/log-triage-agent/)

## Repository layout

```
docs/        Guides and learning path (ja/ and en/)
modules/     Security learning modules (each one bilingual JA/EN in a single file)
templates/   Copy-paste prompt templates (ja/ and en/)
tools/       Small working tools / agent examples
```

## Who this is for

- IT engineers working in networking, infrastructure, or cloud operations
- Security beginners who already touch logs and config files in their day-to-day work
- People who want to spread security basics internally — trainers, lead engineers, etc.

## Ground rules

- This content is for learning and defensive purposes. Do not use it to access or attack systems you don't own or lack authorization for
- Hands-on exercises assume dummy data and a local/isolated environment
- Never paste real production secrets — actual logs, credentials, customer data — into Claude as-is

## Contributing

Improvements, new modules, and new use cases are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT License](LICENSE)
