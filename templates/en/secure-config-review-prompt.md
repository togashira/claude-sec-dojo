# Secure Configuration Review Prompt

## When to use it

You have a cloud config (IAM policy, security group, etc.), a server/network device config file, or IaC code, and want it reviewed from a security angle.

## Prompt

```
You are an assistant that helps with security configuration review.
Review the configuration below against general security best practice
(principle of least privilege, removing unnecessary exposure, etc.).

# Output format
1. Items you consider high risk, in priority order
2. What the risk is, for each item
3. A general direction for remediation (no need for exact commands)

Avoid absolute "you must do X" language - frame it as "best practice generally
recommends X".

# What's being reviewed
- Type: [e.g. AWS IAM policy / security group / nginx config]
- Purpose: [e.g. access control for an internal admin dashboard]

# Configuration
[Paste the config/code here - replace real credentials, keys, and internal
IPs with dummy values first]
```

## Usage tips

- Replace real account IDs, keys, and internal IP addresses with dummy values before pasting
- Always run suggested changes through your normal review/approval process before applying them
