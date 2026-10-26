# SEO Score API app for Make

A [Make](https://www.make.com) custom app for [SEO Score API](https://seoscoreapi.com), in Make's
local-development layout (`makecomapp.json` plus one folder per component). Each module uses the
customer's own SEO Score API key and plan, the same as calling the API directly.

| Module | Type | Endpoint | Plans |
|---|---|---|---|
| Audit a URL | action | `GET /audit` | all |
| Audit Multiple URLs | action | `POST /audit/batch` | paid |
| Check a URL's Accessibility | action | `GET /audit/accessibility` | paid |
| Get a URL's AI Readability | action | `GET /ai-readability` | all |
| Score a Page's Conversion | action | `GET /conversion` | all |
| Watch Score Changes | instant trigger | `POST /monitors` with Make's webhook URL; removed with `DELETE /monitors` | paid |
| Create a Score Monitor | action | `POST /monitors` | paid |
| List Score Monitors | search | `GET /monitors` | paid |
| Delete a Score Monitor | action | `DELETE /monitors` | paid |
| Get Usage | action | `GET /usage` | all |
| Make an API Call | universal | any path under `https://seoscoreapi.com` | all |

The connection asks for the API key only and checks it with `GET /usage`. The key travels in the
`X-API-Key` header and is sanitized from Make's logs.

Accessibility wording: say "the WCAG 2.1 A/AA issues an automated scan can detect" and
"Automated testing does not catch everything"; never "compliant".

## Deploy to Make

Make deploys a local app with its VS Code extension ("Make Apps Editor").

1. In Make, create an empty custom app: **Custom Apps > Create a new app**, name `seoscoreapi`,
   label `SEO Score API`, theme the brand colour, language English, audience global.
   Upload `../assets/seoscore-icon-512.png` as the logo.
2. In VS Code, install the Make Apps Editor extension and add your Make API token
   (Make profile > API access) as an environment.
3. Add an origin to `makecomapp.json` (right-click the file > **Deploy to Make** > **Deploy into
   another app**) pointing at the app you created, with `apikeyFile` outside this repository,
   for example `../../.secrets/make-apikey`. Never commit the key file.
4. Right-click `makecomapp.json` > **Deploy to Make**, and choose **Deploy as new** for every
   component.
5. In a scenario, create a connection with a real key and run every module once.

## Publish (public listing)

Make reviews an app before it appears to all users. Before requesting the review:

- Run test scenarios that use every module at least once, plus one scenario that produces an
  error (for example an audit of an unreachable URL). Keep keys and personal data out of them.
- Then, in the app: **Publish**, switch each module to visible, open the **Review** tab, add the
  API docs link (`https://seoscoreapi.com/docs`) and the scenario links, and **Request review**.
- Make emails a form (developer information, support contact, categories, logo, service URL,
  trademark and terms confirmations). It needs a person to complete it.

Publishing cannot be undone, and public apps cannot delete modules, so remove any test
components first.
