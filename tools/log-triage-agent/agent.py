#!/usr/bin/env python3
"""Flag possibly-anomalous behavior in a log file using Claude.

Usage:
    python agent.py sample-access.log
    python agent.py sample-access.log --lang en --output findings.md

IMPORTANT: Use this only with dummy/learning data. Never feed it real
production logs - they may contain personal or sensitive information.
"""

import argparse
import os
import sys
from pathlib import Path

import anthropic

PROMPTS = {
    "ja": {
        "system": "あなたはセキュリティログ分析を支援するアシスタントです。",
        "instruction": (
            "以下のログを分析し、通常と異なると考えられる挙動を最大5つまで"
            "ピックアップしてください。それぞれについて、\n"
            "1. 何が起きている可能性があるか(断定せず、可能性として)\n"
            "2. 判断の根拠になったログの該当部分\n"
            "3. 次に確認すべきこと\n"
            "を記載してください。ログにない情報を推測で補わないでください。\n\n"
            "# ログの背景情報\n{context}\n\n"
            "# ログ本体\n{log}"
        ),
        "default_context": "機器/システム: 不明(ファイルから判断してください)",
    },
    "en": {
        "system": "You are an assistant that helps with security log analysis.",
        "instruction": (
            "Analyze the log below and pick out up to 5 behaviors you consider "
            "abnormal. For each one, include:\n"
            "1. What might be happening (framed as a possibility, not a conclusion)\n"
            "2. The specific log lines that support this\n"
            "3. What to check next\n"
            "Do not fill in information that isn't in the log by guessing.\n\n"
            "# Context\n{context}\n\n"
            "# Log\n{log}"
        ),
        "default_context": "Device/system: unknown (infer from the file if possible)",
    },
}


def load_dotenv_if_present() -> None:
    """Minimal .env loader so the tool has no extra dependency."""
    env_path = Path(__file__).parent / ".env"
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip())


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("log_file", help="Path to a text file with log lines (dummy data only)")
    parser.add_argument("--lang", choices=["ja", "en"], default="ja", help="Output language (default: ja)")
    parser.add_argument("--context", default=None, help="Background info about the device/system")
    parser.add_argument("--output", default=None, help="Save the findings to this file instead of printing them")
    args = parser.parse_args()

    load_dotenv_if_present()

    log_path = Path(args.log_file)
    if not log_path.exists():
        print(f"Error: log file not found: {log_path}", file=sys.stderr)
        sys.exit(1)
    log_text = log_path.read_text(encoding="utf-8").strip()
    if not log_text:
        print(f"Error: log file is empty: {log_path}", file=sys.stderr)
        sys.exit(1)

    prompt_set = PROMPTS[args.lang]
    context = args.context or prompt_set["default_context"]
    model = os.environ.get("ANTHROPIC_MODEL", "claude-opus-5-5")

    client = anthropic.Anthropic()
    response = client.messages.create(
        model=model,
        max_tokens=4096,
        system=prompt_set["system"],
        messages=[
            {
                "role": "user",
                "content": prompt_set["instruction"].format(context=context, log=log_text),
            }
        ],
    )

    findings_text = "".join(block.text for block in response.content if block.type == "text")

    if args.output:
        Path(args.output).write_text(findings_text, encoding="utf-8")
        print(f"Findings saved to {args.output}")
    else:
        print(findings_text)


if __name__ == "__main__":
    main()
