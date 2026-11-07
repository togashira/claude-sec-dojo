#!/usr/bin/env python3
"""Turn bullet-point activity notes into a weekly report using Claude.

Usage:
    python agent.py notes.txt
    python agent.py notes.txt --lang en --output report.md
"""

import argparse
import os
import sys
from pathlib import Path

import anthropic

PROMPTS = {
    "ja": {
        "system": "あなたは経営報告の整理を支援するアシスタントです。",
        "instruction": (
            "以下は今週の活動を箇条書きでまとめたメモです。これを元に、"
            "社内共有用の週次報告書を作成してください。\n\n"
            "# 出力形式\n"
            "1. 今週のまとめ(3行以内)\n"
            "2. 実施したこと(箇条書き、成果がわかるように)\n"
            "3. 進行中の課題・ブロッカー\n"
            "4. 来週の予定\n\n"
            "# トーン\n{tone}\n\n"
            "# 今週の活動メモ\n{notes}"
        ),
        "default_tone": "です・ます調で、簡潔に。上司への報告を想定。",
    },
    "en": {
        "system": "You are an assistant that helps organize management reports.",
        "instruction": (
            "Below are bullet-point notes on this week's activities. Turn them "
            "into a weekly status report for internal sharing.\n\n"
            "# Output format\n"
            "1. This week's summary (3 lines or fewer)\n"
            "2. What was done (bullet list, with outcomes where possible)\n"
            "3. Ongoing issues / blockers\n"
            "4. Plan for next week\n\n"
            "# Tone\n{tone}\n\n"
            "# This week's notes\n{notes}"
        ),
        "default_tone": "Concise and professional, written for a manager.",
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
    parser.add_argument("notes_file", help="Path to a text file with bullet-point notes")
    parser.add_argument("--lang", choices=["ja", "en"], default="ja", help="Report language (default: ja)")
    parser.add_argument("--tone", default=None, help="Tone instruction for the report")
    parser.add_argument("--output", default=None, help="Save the report to this file instead of printing it")
    args = parser.parse_args()

    load_dotenv_if_present()

    notes_path = Path(args.notes_file)
    if not notes_path.exists():
        print(f"Error: notes file not found: {notes_path}", file=sys.stderr)
        sys.exit(1)
    notes = notes_path.read_text(encoding="utf-8").strip()
    if not notes:
        print(f"Error: notes file is empty: {notes_path}", file=sys.stderr)
        sys.exit(1)

    prompt_set = PROMPTS[args.lang]
    tone = args.tone or prompt_set["default_tone"]
    model = os.environ.get("ANTHROPIC_MODEL", "claude-opus-5-5")

    client = anthropic.Anthropic()
    response = client.messages.create(
        model=model,
        max_tokens=4096,
        system=prompt_set["system"],
        messages=[
            {
                "role": "user",
                "content": prompt_set["instruction"].format(tone=tone, notes=notes),
            }
        ],
    )

    report_text = "".join(block.text for block in response.content if block.type == "text")

    if args.output:
        Path(args.output).write_text(report_text, encoding="utf-8")
        print(f"Report saved to {args.output}")
    else:
        print(report_text)


if __name__ == "__main__":
    main()
