# Learning Path

We recommend working through the four modules in this order. It follows a path a working infrastructure/cloud engineer is likely to actually experience: network operations → cloud → log analysis/incident response → configuration review.

| # | Module | What you'll learn |
|---|---|---|
| 1 | [Network Log Analysis Basics](../../modules/01-network-log-analysis/README.md) | How to spot anomalies in network device logs |
| 2 | [Cloud Security Basics (AWS/Azure)](../../modules/02-cloud-security-basics/README.md) | Common cloud misconfigurations and how to find them |
| 3 | [Incident Response Basics](../../modules/03-incident-response-basics/README.md) | How to organize initial response and reporting when something happens |
| 4 | [Secure Configuration Review](../../modules/04-secure-config-review/README.md) | How to review config files and IaC from a security angle |

## How to pace yourself

- Each module follows the same shape: concept explanation → hands-on (dummy data) → example prompts for Claude
- After finishing a module, try the matching prompt in [templates/en/](../../templates/en/) against your own situation (never real production secrets)
- Once you've finished all four, try [tools/log-triage-agent/](../../tools/log-triage-agent/) as your first taste of automation

## Prerequisites

- Basic hands-on experience with networking, servers, or cloud operations (you don't need to be an expert)
- No prior security expertise assumed — each module explains the concepts it needs
