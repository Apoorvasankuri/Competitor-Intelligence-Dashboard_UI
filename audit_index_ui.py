from pathlib import Path
import sys

FILE = Path("index.html")

CHECKS = {
    "Source Metadata Mapping": [
        "sourceDomain",
        "sourceType",
        "sourceCategory",
        "sourcePriority",
        "sourceAuthorityScore",
        "preferredForExecutiveSummary",
        "sourceNotes",
        "sourceMatchMethod",
    ],

    "Source Badge UI": [
        "getSourceBadge",
        "Official / Primary",
        "Specialist Source",
        "Business Media",
        "Aggregator",
        "Low Authority",
    ],

    "Search Lens Mapping": [
        "searchQuery",
        "searchQueryType",
        "detectedClientAuthority",
        "detectedStrategicTheme",
        "acceptedByGate",
    ],

    "Search Lens Badge UI": [
        "getSearchLensBadge",
        "Competitor Lens",
        "SBU Lens",
        "Client / Authority Lens",
        "Theme Lens",
        "Competitor + SBU",
        "Competitor + Client",
        "SBU + Client",
    ],

    "Core UI Still Present": [
        "loadDataFromAPI",
        "renderArticleCard",
        "renderExecutiveSummary",
    ],
}


def read():
    if not FILE.exists():
        print(f"❌ Missing file: {FILE}")
        sys.exit(1)
    return FILE.read_text(encoding="utf-8", errors="ignore")


def main():
    text = read()
    total_failures = 0

    print("\n=== Audit: index.html ===")

    for section, checks in CHECKS.items():
        print(f"\n{section}")
        print("-" * len(section))

        failures = 0
        for item in checks:
            if item in text:
                print(f"✅ {item}")
            else:
                print(f"❌ {item}")
                failures += 1

        total_failures += failures

    print("\nSummary:")
    print(f"Total failures: {total_failures}")

    if total_failures:
        sys.exit(1)


if __name__ == "__main__":
    main()