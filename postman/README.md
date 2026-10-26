# Postman collection

`SEO-Score-API.postman_collection.json` has every public endpoint, grouped by tag, with working
example values. `SEO-Score-API.postman_environment.json` holds the two variables it uses.

1. Postman > **Import** > choose both files (or paste the raw GitHub URLs).
2. Put your key in `apiKey` (collection Variables tab or the "SEO Score API" environment).
   A free key: https://seoscoreapi.com/#signup, or run *Account > Request a free API key* and
   *Verify the emailed code*.
3. Send *Audit > SEO audit of one URL*.

Optional query parameters are switched off; tick them to try them. Requests marked paid in their
description need a paid plan (https://seoscoreapi.com/#pricing).

Rebuild after the API changes (needs Node.js for Postman's converter):

    python3 openapi/build_openapi.py
    python3 postman/build_postman.py
