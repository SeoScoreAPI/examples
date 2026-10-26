"""Build the Postman collection and environment from openapi/seoscoreapi.openapi.json.

    python3 openapi/build_openapi.py      # first, if the API changed
    python3 postman/build_postman.py

Needs Node.js: the conversion itself is Postman's own converter (openapi-to-postmanv2, run
with npx). This script then tidies the result: one collection-level API key, optional query
parameters switched off, and only the real example responses kept.
"""
import json
import pathlib
import subprocess
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
SPEC = ROOT / "openapi/seoscoreapi.openapi.json"
OUT = ROOT / "postman"
CONVERTER = "openapi-to-postmanv2@4"
PUBLIC = {"Service health", "Request a free API key (emails a code)", "Verify the emailed code and receive the key"}
KEEP_RESPONSES = {"SEO audit of one URL", "AI readability score of one URL"}

DESCRIPTION = """\
SEO Score API audits a web page and returns JSON: a 0 to 100 score, a grade, category scores, \
AI readability scores and a prioritized fix list.

**Setup:** get a free key (20 audits a month, no credit card) at https://seoscoreapi.com/#signup, \
or run *Account > Request a free API key* and then *Verify the emailed code*. Put the key in \
the `apiKey` variable (collection Variables tab, or the "SEO Score API" environment). Every \
request sends it as the `X-API-Key` header.

**Start with** *Audit > SEO audit of one URL*. Optional query parameters are switched off; \
tick them to try them.

Some endpoints need a paid plan; the request description says which. Plans: \
https://seoscoreapi.com/#pricing. Docs: https://seoscoreapi.com/docs.
"""


def convert():
    with tempfile.TemporaryDirectory() as tmp:
        raw = pathlib.Path(tmp) / "raw.json"
        subprocess.run(
            ["npx", "-y", CONVERTER, "-s", str(SPEC), "-o", str(raw),
             "-O", "folderStrategy=Tags,"
                   "parametersResolution=Example,includeAuthInfoInExample=false"],
            check=True, stdout=subprocess.DEVNULL)
        return json.loads(raw.read_text())


def tidy(col):
    col["info"]["name"] = "SEO Score API"
    col["info"]["description"] = {"content": DESCRIPTION, "type": "text/markdown"}
    col["auth"] = {"type": "apikey", "apikey": [
        {"key": "key", "value": "X-API-Key", "type": "string"},
        {"key": "value", "value": "{{apiKey}}", "type": "string"},
        {"key": "in", "value": "header", "type": "string"}]}
    col["variable"] = [
        {"key": "baseUrl", "value": "https://seoscoreapi.com", "type": "string"},
        {"key": "apiKey", "value": "", "type": "string", "description": "Your SEO Score API key"},
    ]
    for folder in col["item"]:
        for req in folder["item"]:
            r = req["request"]
            # Requests inherit the collection auth unless the operation is public (noauth).
            if req["name"] in PUBLIC:
                r["auth"] = {"type": "noauth"}
            else:
                r.pop("auth", None)
            for q in r["url"].get("query", []):
                desc = q.get("description", {})
                text = desc.get("content", "") if isinstance(desc, dict) else str(desc)
                if "(Required)" not in text:
                    q["disabled"] = True
            if req["name"] in KEEP_RESPONSES:
                req["response"] = [x for x in req.get("response", []) if x.get("code") == 200]
            else:
                req["response"] = []
    return col


def environment():
    return {
        "name": "SEO Score API",
        "values": [
            {"key": "baseUrl", "value": "https://seoscoreapi.com", "type": "default", "enabled": True},
            {"key": "apiKey", "value": "", "type": "secret", "enabled": True},
        ],
        "_postman_variable_scope": "environment",
    }


def main():
    col = tidy(convert())
    col["info"].pop("_postman_id", None)
    (OUT / "SEO-Score-API.postman_collection.json").write_text(json.dumps(col, indent=2, ensure_ascii=False) + "\n")
    (OUT / "SEO-Score-API.postman_environment.json").write_text(json.dumps(environment(), indent=2) + "\n")
    n = sum(len(f["item"]) for f in col["item"])
    print(f"{n} requests in {len(col['item'])} folders")


if __name__ == "__main__":
    main()
