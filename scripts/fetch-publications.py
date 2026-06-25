# We can fetch from ORCID's public api as follows:
# https://pub.orcid.org/v3.0/{orcid-id}/works

import datetime as dt
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List

import requests

MY_NAME = "Daragh M. Hollman"
OUTPUT_FILE = Path(__file__).parents[1] / "content/publications.md"

ORCID_ID = "0009-0004-8128-2384"
BASE_URL = f"https://pub.orcid.org/v3.0/{ORCID_ID}"

# Setting the header lets us return json instead of XML
HEADERS = {"Accept": "application/json"}

PAGE_HEADER = (
    f"""+++
date = '{dt.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")}'
draft = false
title = 'My Publications'
+++
"""
    + """
<style>
.w {
    max-width: 100pc
}
</style>

"""
)


def main():

    entries = get_profile_entries()

    content = PAGE_HEADER

    for e in entries:

        content += format_entry(e)
        content += "\n\n"

    with open(OUTPUT_FILE, "w") as f:
        f.write(content)

    print(f"Saved entries to: {OUTPUT_FILE}")


@dataclass
class Author:
    given_names: str
    family_name: str

    # ORCIDs for other authors are not required, and so may be missing.
    orcid: str | None = None

    @property
    def cited_name(self) -> str:
        return f"{self.given_names} {self.family_name}"


@dataclass
class ORCIDEntry:
    index: int
    putcode: str
    doi: str
    title: str
    authors: List[Author]
    year: str
    publication_type: str


def get_profile_entries() -> List[ORCIDEntry]:
    """
    Fetch publications from an author's ORCID.
    """

    # Get all publications
    response = requests.get(f"{BASE_URL}/works", headers=HEADERS)
    response.raise_for_status()

    profile_data: List[Dict[Any]] = response.json()["group"]

    profile_entries: List[ORCIDEntry] = []
    for i, entry_info in enumerate(profile_data):

        putcode = entry_info["work-summary"][0]["put-code"]
        title = entry_info["work-summary"][0]["title"]["title"]["value"]

        # Get further information about this work
        response = requests.get(f"{BASE_URL}/work/{putcode}", headers=HEADERS)
        response.raise_for_status()

        entry_data: List[Dict[Any]] = response.json()

        external_ids = entry_data["external-ids"]
        doi = None
        if external_ids:
            for item in external_ids.get("external-id", []):
                if item.get("external-id-type") == "doi":
                    url = item.get("external-id-url")
                    doi = url["value"] if url else None
                    break

        publication_type = entry_data["type"]
        year = entry_data["publication-date"]["year"]["value"]

        authors: List[Author] = []
        author_info: Dict
        for author_info in entry_data["contributors"]["contributor"]:
            full_name = author_info["credit-name"]["value"]
            name_tuple = _split_name(full_name)

            orcid = (author_info.get("contributor-orcid") or {}).get("path", None)

            this_author = Author(*name_tuple, orcid=orcid)

            authors.append(this_author)

        this_entry = ORCIDEntry(
            len(profile_data) - i, putcode, doi, title, authors, year, publication_type
        )
        profile_entries.append(this_entry)

    print(f"Found {len(profile_entries)} entries:")
    for i, e in enumerate(profile_entries):

        # 80 is a standard limit for terminals, -3 for the dots we will add.
        char_lim = 80 - 3
        shorten_title = len(e.title) > char_lim

        if shorten_title:
            title = e.title[:char_lim] + "..."

        else:
            title = e.title

        print(f"{len(profile_entries) - i:03} | {e.putcode} | {title}")

    return profile_entries


def _split_name(full_name: str) -> tuple[str, str]:
    parts = full_name.strip().split()

    if len(parts) < 2:
        raise ValueError("Name must contain at least 2 words")

    *first_and_middle, surname = parts

    initials = " ".join(f"{name[0].upper()}." for name in first_and_middle)

    return (initials, surname)


def _names_match(author_name: str, my_name: str) -> bool:
    """
    A helper to check if names match. Compare names by matching initials +
    surname, tolerating formatting differences.
    """
    try:
        my_initials, my_surname = _split_name(my_name)
        author_initials, author_surname = _split_name(author_name)

    except ValueError:
        return False

    if my_surname.lower() != author_surname.lower():
        return False

    # Compare only the initials that both sides share — the shorter one wins.
    # e.g. "D." matches "D. M." since the record may have omitted middle names.
    my_parts = my_initials.split()
    author_parts = author_initials.split()
    min_len = min(len(my_parts), len(author_parts))

    return my_parts[:min_len] == author_parts[:min_len]


def format_entry(entry: ORCIDEntry) -> str:

    lines: List[str] = []

    lines.append(f"{entry.index:03} | _{entry.title}_")

    author_names: List[str] = []
    for author in entry.authors:
        cited = author.cited_name
        if _names_match(cited, MY_NAME):
            cited = f"**{cited}**"
        author_names.append(cited)

    lines.append(", ".join(author_names))

    lines.append(f"({entry.year}), [{entry.doi}]()")

    return "  \n".join(lines)


if __name__ == "__main__":
    main()
