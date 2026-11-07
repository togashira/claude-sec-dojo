# Decision Support Prompt

## When to use it

You're facing a management decision with multiple options and want the issues, risks, and trade-offs laid out before you decide.

## Prompt

```
You are an advisor supporting a business decision.
For the situation below, lay out the pros, cons, risks, and rough cost of each option,
then list 3 additional questions I should answer before deciding. I will make the final
call myself, so focus on organizing the material rather than giving a definitive recommendation.

# Background
[Describe the problem/situation. E.g.: deciding whether to build a new product in-house or outsource it]

# Options
1. [Option 1]
2. [Option 2]
3. [Option 3, if any]

# Constraints
- Budget: [e.g. under $50,000]
- Timeline: [e.g. within 3 months]
- Other: [e.g. must be doable with 2 existing team members]

# Output format
- A table of Pros / Cons / Risks / Rough cost per option
- 3 additional questions to consider, at the end
```

## Usage tips

- Fill in the `[ ]` placeholders with your real situation
- Treat the output as a starting point for discussion with stakeholders, not a final conclusion
