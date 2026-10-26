# OpenAPI description

`seoscoreapi.openapi.json` (and the same document as `seoscoreapi.openapi.yaml`) describes the
public SEO Score API in OpenAPI 3.0.3: servers, the `X-API-Key` security scheme, tags, and real
example responses for `GET /audit` and `GET /ai-readability`.

Raw URLs for importers and directories:

- JSON: `https://raw.githubusercontent.com/SeoScoreAPI/examples/master/openapi/seoscoreapi.openapi.json`
- YAML: `https://raw.githubusercontent.com/SeoScoreAPI/examples/master/openapi/seoscoreapi.openapi.yaml`

The server also publishes its own generated schema at https://seoscoreapi.com/openapi.json
(OpenAPI 3.1, every endpoint). This file is built from it:

    pip install pyyaml
    python3 openapi/build_openapi.py

The script keeps the developer endpoints, leaves out account and billing actions and the HTML
tool pages, and stops with an error when the live schema has an endpoint it does not know yet,
so new endpoints get a tag and a name before they are published. `examples/` holds the full
responses the two example responses are cut from.

Check the result with any OpenAPI linter, for example:

    npx @redocly/cli@1 lint openapi/seoscoreapi.openapi.json
