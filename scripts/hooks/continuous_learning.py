#!/usr/bin/env python3
"""Nudge Codex to review long sessions for reusable, user-approved learnings."""

import hashlib
import json
import os
import sys
from pathlib import Path


MIN_PROMPTS = 10
MAX_HOOK_INPUT_BYTES = 2 * 1024 * 1024
REVIEW_PROMPT = (
    "Review this conversation for one durable, reusable learning only. "
    "If a proven correction, troubleshooting method, workaround, or project "
    "convention emerged, use the continuous-learning skill to draft one "
    "privacy-safe candidate and show it to the user for approval. If there is "
    "no clear reusable pattern, finish without suggesting a save. Do not read "
    "transcript files or unrelated conversations. Never write a learning "
    "without the user's approval."
)


def read_hook_input():
    raw = sys.stdin.buffer.read(MAX_HOOK_INPUT_BYTES + 1)
    if len(raw) > MAX_HOOK_INPUT_BYTES:
        return {}
    try:
        value = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, dict) else {}


def state_paths(payload):
    data_dir = os.environ.get("PLUGIN_DATA")
    session_id = payload.get("session_id")
    if not data_dir or not isinstance(session_id, str):
        return None
    if not session_id or len(session_id) > 2048:
        return None

    session_key = hashlib.sha256(session_id.encode("utf-8")).hexdigest()
    state_dir = Path(data_dir) / "continuous-learning"
    return (
        state_dir,
        state_dir / (session_key + ".count"),
        state_dir / (session_key + ".reviewed"),
    )


def count_prompt(count_path):
    descriptor = os.open(count_path, os.O_CREAT | os.O_APPEND | os.O_WRONLY, 0o600)
    try:
        if os.fstat(descriptor).st_size < MIN_PROMPTS:
            os.write(descriptor, b"x")
    finally:
        os.close(descriptor)


def request_review(count_path, reviewed_path, payload):
    if payload.get("stop_hook_active") is True:
        return
    try:
        if count_path.stat().st_size < MIN_PROMPTS:
            return
    except OSError:
        return

    try:
        descriptor = os.open(reviewed_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError:
        return
    os.close(descriptor)
    print(json.dumps({"decision": "block", "reason": REVIEW_PROMPT}))


def cleanup(state_dir, count_path, reviewed_path):
    for path in (count_path, reviewed_path):
        try:
            path.unlink()
        except OSError:
            pass
    try:
        state_dir.rmdir()
    except OSError:
        pass


def main():
    payload = read_hook_input()
    paths = state_paths(payload)
    if paths is None:
        return

    state_dir, count_path, reviewed_path = paths
    event = payload.get("hook_event_name")
    try:
        if event == "UserPromptSubmit":
            state_dir.mkdir(parents=True, exist_ok=True)
            count_prompt(count_path)
        elif event == "Stop":
            request_review(count_path, reviewed_path, payload)
        elif event == "SessionEnd":
            cleanup(state_dir, count_path, reviewed_path)
    except OSError:
        # Hook failures must not interrupt the user's work.
        return


if __name__ == "__main__":
    main()
