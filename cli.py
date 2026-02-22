import argparse
import sys
import logging
from db import initialize_database
# from xml_parser import import_machine_report
# from reconciler import run_reconciliation
# from reports import generate_report

def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )

def run_cli():
    configure_logging()

    parser = argparse.ArgumentParser(
        prog="casino-recon",
        description="Casino Financial Reconciliation Tool"
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # init-db
    subparsers.add_parser(
        "init-db",
        help="Initialize the database schema"
    )

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
    try:
        if args.command == "init-db":
            logging.info("Initializing database schema...")
            initialize_database()
            logging.info("Database initialized successfully.")

        elif args.command == "import-xml":
            logging.info(f"Importing XML file: {args.filepath}")
            # import_machine_report(args.filepath)
            logging.info("XML import completed.")

        elif args.command == "reconcile":
            logging.info("Running reconciliation checks...")
            # run_reconciliation()
            logging.info("Reconciliation completed.")

        elif args.command == "report":
            logging.info("Generating reconciliation report...")
            # generate_report(args.output)
            logging.info("Report generation completed.")

        else:
            logging.error("Unknown command.")
            sys.exit(1)

    except Exception as e:
        logging.exception("An unexpected error occurred.")
        sys.exit(1)