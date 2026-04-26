from __future__ import annotations

import argparse
import json
from dataclasses import asdict

from .config import load_config


def cmd_info(_: argparse.Namespace) -> int:
    print("hydro-insar-swin-inversion")
    print("Container-oriented software scaffold for hydrologic inversion from InSAR and multisensor constraints.")
    return 0


def cmd_check_config(args: argparse.Namespace) -> int:
    cfg = load_config(args.config)
    print(f"Config OK: {cfg.project_name}")
    print(f"Study area: {cfg.study_area.name} ({cfg.study_area.region})")
    return 0


def cmd_show_paths(args: argparse.Namespace) -> int:
    cfg = load_config(args.config)
    print(json.dumps(asdict(cfg), indent=2, default=str))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="hisi")
    sub = parser.add_subparsers(dest="command", required=True)

    p_info = sub.add_parser("info", help="Show package information.")
    p_info.set_defaults(func=cmd_info)

    p_check = sub.add_parser("check-config", help="Validate an example config file.")
    p_check.add_argument("config", help="Path to YAML config.")
    p_check.set_defaults(func=cmd_check_config)

    p_paths = sub.add_parser("show-paths", help="Print the parsed config content.")
    p_paths.add_argument("config", help="Path to YAML config.")
    p_paths.set_defaults(func=cmd_show_paths)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())

