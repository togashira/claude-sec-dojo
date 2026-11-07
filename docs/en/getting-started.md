# Getting Started

## What you'll learn here

This isn't about attack technique. It's about **understanding and responding to situations from a security angle, in the networking/cloud/server work you already do.** Specifically:

- Spotting suspicious behavior in logs and triaging by priority
- Reviewing cloud (AWS/Azure) configurations from a security angle
- Organizing the facts and writing a clear report when something happens

These are things any networking or cloud engineer runs into day to day, security specialist or not.

## How to use Claude here

Think of Claude as a partner with security knowledge on tap:

- Have it read a long log and summarize what matters
- Have it review a config file (IaC or otherwise) and point out risks
- Use it to organize what to check first during initial incident response

**Important assumption:** Claude's findings are a starting point — the final call and the actual response are still yours. Any action that touches production must be reviewed and approved by a human. Also be careful not to paste real production secrets (actual logs, credentials, customer data) in as-is.

## Two ways to use it

### 1. Chat (no programming needed)

Create an account at [claude.ai](https://claude.ai) and start asking Claude for help right away. Copy a prompt from [templates/en/](../../templates/en/) and paste it in.

**Start here.**

### 2. Tools / automation (some technical knowledge needed)

If you want to automate recurring log review, use the Claude API. See [tools/](../../tools/) for an example.

## Your first step

1. Read [learning-path.md](learning-path.md) to see the suggested order
2. Start with [modules/01-network-log-analysis/README.md](../../modules/01-network-log-analysis/README.md)
3. Once comfortable, try the prompts in [templates/en/](../../templates/en/) against your own (anonymized) logs or configs
