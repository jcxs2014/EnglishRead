import re, html, urllib.request, json, os
from datetime import date

SRC = "granta"
FEED = "https://granta.com/feed/"
MAX_ITEMS = 10
BASE = f"/Users/jcxs2014/Documents/Works/EnglishRead/notes/{SRC}"
SOURCE_NAME = "Granta"

def get_body(xml, tag):
    m = re.search(rf'<{tag}>\s*<!\[CDATA\[(.*?)\]\]>\s*</{tag}>', xml, re.S)
    if not m:
        m = re.search(rf'<{tag}>(.*?)</{tag}>', xml, re.S)
    return html.unescape(m.group(1)).strip() if m else ""

def strip_html(s):
    s = re.sub(r'<br\s*/?>', '\n', s, flags=re.I)
    s = re.sub(r'</?p[^>]*>', '\n', s, flags=re.I)
    return html.unescape(re.sub(r'<[^>]+>', '', s)).strip()

def fetch():
    out_dir = f"{BASE}/{date.today():%Y-%m-%d_%A}"
    os.makedirs(out_dir, exist_ok=True)
    idx_path = f"{out_dir}/index.json"

    req = urllib.request.Request(FEED, headers={"User-Agent": "Mozilla/5.0"})
    data = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "ignore")
    items = re.findall(r'<item>(.*?)</item>', data, re.S)
    print(f"[feed] {len(items)} items total  |  out: {out_dir}\n")

    seen = set()
    if os.path.exists(idx_path):
        with open(idx_path, encoding="utf-8") as f:
            seen = {a["url"] for a in json.load(f) if a.get("url")}

    saved = []
    idx_num = 0
    for it in items:
        if idx_num >= MAX_ITEMS:
            break
        tm = re.search(r'<title>\s*<!\[CDATA\[([^\]]+)\]\]>\s*</title>', it)
        if not tm:
            tm = re.search(r'<title>(.*?)</title>', it, re.S)
        title = html.unescape(tm.group(1)).strip() if tm else f"item_{idx_num+1}"
        lm = re.search(r'<link>\s*<!\[CDATA\[([^\]]+)\]\]>\s*</link>', it)
        if not lm:
            lm = re.search(r'<link>(.*?)</link>', it, re.S)
        link = html.unescape(lm.group(1)).strip() if lm else ""
        pub_m = re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
        pub = pub_m.group(1).strip() if pub_m else ""
        if link and link in seen:
            continue

        ce = strip_html(get_body(it, "content:encoded"))
        desc = strip_html(get_body(it, "description"))
        body = ce if len(ce) > len(desc) else desc
        if len(body) < 500:
            continue

        idx_num += 1
        safe = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')[:40]
        fname = f"{idx_num:02d}_{safe}.md"
        full_text = (f"---\ntitle: {title}\nsource: {SOURCE_NAME}\nurl: {link}"
                     f"\npublished: {pub}\nchars: {len(body)}\n---\n\n"
                     f"# {title}\n\nSource: {SOURCE_NAME}\nURL: {link}\nPublished: {pub}\n\n---\n\n{body}\n")
        with open(f"{out_dir}/{fname}", "w", encoding="utf-8") as f:
            f.write(full_text)
        seen.add(link)
        saved.append({"idx": idx_num, "title": title, "url": link, "pub": pub,
                      "chars": len(body), "file": fname,
                      "preview": body[:180].replace("\n", " ")})
        print(f"[{idx_num:02d}] {title[:70]}")
        print(f"     pub: {pub}  |  body: {len(body)} chars  |  {fname}\n")

    with open(idx_path, "w", encoding="utf-8") as f:
        json.dump(saved, f, ensure_ascii=False, indent=2)
    print(f"=== Saved {len(saved)} articles to {out_dir} ===")

if __name__ == "__main__":
    fetch()
