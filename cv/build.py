#!/usr/bin/env python3
"""Generate the CV sources shared by the PDF and the website.

Reads   _data/cv/*.yml  and  _data/cv/publications.bib
Writes  cv/generated/header.tex, cv/generated/body.tex   (input by cv/main.tex)
        _data/publications.json                           (read by the Jekyll pages)

Run from anywhere:  python3 cv/build.py
Needs PyYAML (pip install pyyaml).
"""

import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "_data" / "cv"
OUT_TEX = ROOT / "cv" / "generated"
OUT_JSON = ROOT / "_data" / "publications.json"

ME = "Pagano"  # family name highlighted in author lists on the website


# --------------------------------------------------------------------------
# Text helpers
# --------------------------------------------------------------------------

LATEX_SPECIALS = {
    "\\": r"\textbackslash{}",
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
}


def escape(text):
    return "".join(LATEX_SPECIALS.get(c, c) for c in text)


def md_to_latex(text):
    """Light markdown (**bold**, *italic*, [text](url)) -> escaped LaTeX."""
    text = str(text).strip()
    links = []

    def stash(m):
        links.append((m.group(1), m.group(2)))
        return f"\x00{len(links) - 1}\x00"

    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", stash, text)
    text = escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", text)
    text = re.sub(r"\*(.+?)\*", r"\\emph{\1}", text)
    text = re.sub(r"\bLaTeX\b", r"\\LaTeX{}", text)

    def unstash(m):
        label, url = links[int(m.group(1))]
        url = url.replace("%", r"\%").replace("#", r"\#")
        return rf"\href{{{url}}}{{{md_to_latex(label)}}}"

    return re.sub(r"\x00(\d+)\x00", unstash, text)


def sentence(text):
    text = text.rstrip()
    return text if text.endswith((".", "!", "?")) else text + "."


def title_details(entry):
    """'Title. Details.' as printed in the PDF."""
    parts = [md_to_latex(entry["title"])]
    if entry.get("details"):
        parts[0] = sentence(parts[0])
        parts.append(md_to_latex(entry["details"]))
    return sentence(" ".join(parts))


def load(name):
    path = DATA / f"{name}.yml"
    return yaml.safe_load(path.read_text(encoding="utf-8")) or []


# --------------------------------------------------------------------------
# BibTeX
# --------------------------------------------------------------------------

def parse_bib(text):
    """Minimal BibTeX parser: @type{key, field = {..} | ".." | bare, ...}."""
    entries = []
    i = 0
    while True:
        at = text.find("@", i)
        if at < 0:
            break
        m = re.match(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", text[at:])
        if not m:
            i = at + 1
            continue
        entry = {"type": m.group(1).lower(), "key": m.group(2)}
        i = at + m.end()
        while True:
            fm = re.compile(r"\s*,?\s*(\w+)\s*=\s*").match(text, i)
            if not fm:
                break
            name = fm.group(1).lower()
            i = fm.end()
            if text[i] == "{":
                depth, start = 0, i
                while True:
                    if text[i] == "{":
                        depth += 1
                    elif text[i] == "}":
                        depth -= 1
                        if depth == 0:
                            break
                    i += 1
                value = text[start + 1:i]
                i += 1
            elif text[i] == '"':
                end = text.index('"', i + 1)
                value = text[i + 1:end]
                i = end + 1
            else:
                vm = re.compile(r"[^,}\s]+").match(text, i)
                value = vm.group(0)
                i = vm.end()
            entry[name] = " ".join(value.split())
        close = text.find("}", i)
        i = close + 1 if close >= 0 else len(text)
        entries.append(entry)
    return entries


LATEX_TO_TEXT = [
    (r"\{\\ss\}|\\ss\b", "ß"),
    (r"\\&", "&"),
    (r"\\%", "%"),
    (r"\\_", "_"),
    (r"---", "—"),
    (r"--", "–"),
    (r"``", "“"),
    (r"''", "”"),
    (r"`", "‘"),
    (r"'", "’"),
    (r"~", " "),
]

ACCENTS = {"'": "\u0301", "`": "\u0300", '"': "\u0308", "^": "\u0302", "~": "\u0303"}


def bib_to_text(value):
    import unicodedata

    value = re.sub(
        r"\{?\\([\'`\"^~])\{?(\w)\}?\}?",
        lambda m: unicodedata.normalize("NFC", m.group(2) + ACCENTS[m.group(1)]),
        value,
    )
    for pattern, repl in LATEX_TO_TEXT:
        value = re.sub(pattern, repl, value)
    value = re.sub(r"\\(emph|textit|textbf)\{([^}]*)\}", r"\2", value)
    return value.replace("{", "").replace("}", "").strip()


def parse_names(field):
    names = []
    for raw in re.split(r"\s+and\s+", field or ""):
        raw = bib_to_text(raw)
        if not raw:
            continue
        if raw == "others":
            names.append({"name": "et al.", "me": False})
            break
        if "," in raw:
            last, first = [p.strip() for p in raw.split(",", 1)]
        else:
            *first, last = raw.split()
            first = " ".join(first)
        initials = " ".join(
            "-".join(p[0] + "." for p in part.split("-") if p)
            for part in first.replace(".", ". ").split()
        )
        display = f"{initials} {last}".strip()
        names.append({"name": display, "me": last == ME})
    return names


def venue(e):
    t = e["type"]
    if t == "article":
        v = bib_to_text(e.get("journal", ""))
        vol = e.get("volume", "")
        num = e.get("number", "")
        issue = f"{vol}({num})" if vol and num else vol or (f"({num})" if num else "")
        pages = bib_to_text(e.get("pages", ""))
        extra = ", ".join(x for x in [issue, pages] if x)
        return {"container": v, "extra": extra}
    if t in ("incollection", "inbook", "inproceedings"):
        v = bib_to_text(e.get("booktitle", ""))
        eds = [n["name"] for n in parse_names(e.get("editor", ""))]
        bits = []
        if eds:
            bits.append("ed. by " + ", ".join(eds))
        pub = ": ".join(bib_to_text(e[k]) for k in ("address", "publisher") if e.get(k))
        if pub:
            bits.append(pub)
        return {"container": v, "extra": "; ".join(bits), "prefix": "In:"}
    if t == "book":
        return {"container": bib_to_text(e.get("publisher", "")), "extra": ""}
    return {"container": "", "extra": ""}


def publications():
    entries = parse_bib((DATA / "publications.bib").read_text(encoding="utf-8"))
    pubs = []
    for e in entries:
        authors = parse_names(e.get("author", ""))
        pub = {
            "key": e["key"],
            "type": e["type"],
            "keyword": [k.strip() for k in e.get("keywords", "").split(",") if k.strip()],
            "year": e.get("year", ""),
            "title": bib_to_text(e.get("title", "")),
            "authors": authors,
            "note": bib_to_text(e.get("note", "")),
            "doi": e.get("doi", ""),
            "url": e.get("url", ""),
            "pdf": e.get("pdf", ""),
            "abstract": bib_to_text(e.get("abstract", "")),
            "project": e.get("project", ""),
        }
        pub.update(venue(e))
        first_last = authors[0]["name"].split()[-1] if authors else ""
        pub["_sort"] = (-int(re.sub(r"\D", "", pub["year"]) or 0), first_last, pub["title"])
        pubs.append(pub)
    pubs.sort(key=lambda p: p.pop("_sort"))
    return pubs


# --------------------------------------------------------------------------
# LaTeX sections
# --------------------------------------------------------------------------

def itemize(items):
    return "\\begin{itemize}\n" + "".join(f"  {i}\n" for i in items) + "\\end{itemize}\n"


def teaching_tex(entries):
    groups = {}
    for e in entries:
        line = md_to_latex(e["course"]) + " — "
        line += ", ".join(md_to_latex(e[k]) for k in ("role", "institution") if e.get(k))
        if e.get("details"):
            line = sentence(line) + " " + md_to_latex(e["details"])
        line = "\\item " + sentence(line)
        if e.get("period"):
            label = str(e["period"])
            end = int(re.findall(r"\d{4}", label)[-1])
            groups.setdefault((0, end, label), []).append(line)
        for y in e.get("years", []):
            groups.setdefault((1, int(y), str(y)), []).append(line)
    out = []
    for key in sorted(groups, reverse=True):
        out.append(f"\\textbf{{{escape(key[2])}}}\n")
        out.append(itemize(groups[key]))
    return "\n".join(out)


def section_tex(sec, pubs):
    style = sec.get("style", "list")
    head = f"\\cvsection{{{escape(sec['title'])}}}\n"
    if style == "publications":
        if not any(sec["keyword"] in p["keyword"] for p in pubs):
            return ""
        return head + f"\\printbibliography[keyword={sec['keyword']}, heading=none]\n"

    entries = load(sec["data"])
    entries = [e for e in entries if e.get("pdf", True) is not False]
    where = sec.get("where")
    if where == "current":
        entries = [e for e in entries if e.get("current")]
    elif where == "past":
        entries = [e for e in entries if not e.get("current")]
    if not entries:
        return ""

    if style == "dated":
        body = itemize(
            f"\\dateditem{{{md_to_latex(e['when'])}}}{{{title_details(e)}}}" for e in entries
        )
    elif style == "teaching":
        body = "\n" + teaching_tex(entries)
    elif style == "conferences":
        body = itemize(
            f"\\item {md_to_latex(e['name'])}: {sentence(md_to_latex(e['years']))}" for e in entries
        )
    elif style == "inline":
        text = ", ".join(
            md_to_latex(e["name"]) + (f" ({md_to_latex(e['level'])})" if e.get("level") else "")
            for e in entries
        )
        body = itemize([f"\\item {sentence(text)}"])
    else:  # list
        body = itemize(f"\\item {sentence(md_to_latex(e['text']))}" for e in entries)
    return head + body


def header_tex(profile):
    email = profile["email"]
    return (
        "\\begin{center}\n"
        f"{{\\LARGE\\scshape {escape(profile['name'])}}}\\\\[3pt]\n"
        "{\\small\\textcolor{gray}{Last update: \\monthyear}}\\\\[6pt]\n"
        f"{{\\small {md_to_latex(profile['cv_affiliation'])}}}\\\\\n"
        f"{{\\small {md_to_latex(profile['address'])} \\;•\\;\n"
        f"\\href{{mailto:{email}}}{{{escape(email)}}}}}\n"
        "\\end{center}\n"
    )


def main():
    pubs = publications()
    OUT_JSON.write_text(json.dumps(pubs, ensure_ascii=False, indent=1), encoding="utf-8")

    OUT_TEX.mkdir(parents=True, exist_ok=True)
    profile = yaml.safe_load((DATA / "profile.yml").read_text(encoding="utf-8"))
    (OUT_TEX / "header.tex").write_text(header_tex(profile), encoding="utf-8")

    sections = [s for s in load("sections") if s.get("pdf", True) is not False]
    body = "\n".join(filter(None, (section_tex(s, pubs) for s in sections)))
    (OUT_TEX / "body.tex").write_text(body, encoding="utf-8")

    print(f"{len(pubs)} publications -> {OUT_JSON.relative_to(ROOT)}")
    print(f"{len(sections)} sections   -> {(OUT_TEX / 'body.tex').relative_to(ROOT)}")


if __name__ == "__main__":
    sys.exit(main())
