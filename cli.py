import argparse
import sys


def run_cli():
    parser = argparse.ArgumentParser(
        prog="casino-recon",
        description="Casino Financial Reconciliation Tool"
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # import-xml command
    import_xml_parser = subparsers.add_parser(
        "import-xml",
        help="Import transactions from an XML file"
    )
    import_xml_parser.add_argument(
        "filepath",
        type=str,
        help="Path to XML file"
    )

    # reconcile command
    subparsers.add_parser(
        "reconcile",
        help="Run reconciliation checks"
    )

    # report command
    report_parser = subparsers.add_parser(
        "report",
        help="Generate reconciliation report"
    )
    report_parser.add_argument(
        "--output",
        type=str,
        help="Optional output file path"
    )

    args = parser.parse_args()

    dispatch_command(args)


def dispatch_command(args):
    if args.command == "import-xml":
        print(f"[INFO] Importing XML file: {args.filepath}")
        # TODO: Call xml import logic

    elif args.command == "reconcile":
        print("[INFO] Running reconciliation checks...")
        # TODO: Call reconciliation logic

    elif args.command == "report":
        print("[INFO] Generating report...")
        if args.output:
            print(f"[INFO] Output file: {args.output}")
        # TODO: Call reporting logic

    else:
        print("[ERROR] Unknown command.")
        sys.exit(1)