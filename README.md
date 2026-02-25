# SEO Score API — Examples

Code examples for integrating [SEO Score API](https://seoscoreapi.com) into your projects.

## Quick Start

Get a free API key (5 audits/day):
```bash
curl -X POST https://seoscoreapi.com/signup \
  -H "Content-Type: application/json" \
  -d '{"email": "you@example.com"}'
```

## Examples

### cURL
```bash
curl -H "X-API-Key: YOUR_KEY" \
  "https://seoscoreapi.com/audit?url=https://example.com"
```

### Python
```python
import requests

resp = requests.get(
    "https://seoscoreapi.com/audit",
    params={"url": "https://example.com"},
    headers={"X-API-Key": "YOUR_KEY"}
)
data = resp.json()
print(f"Score: {data['score']}/100 ({data['grade']})")
for p in data["priorities"]:
    print(f"  [{p['severity']}] {p['issue']}")
```

### JavaScript / Node.js
```javascript
const resp = await fetch(
  "https://seoscoreapi.com/audit?url=https://example.com",
  { headers: { "X-API-Key": "YOUR_KEY" } }
);
const data = await resp.json();
console.log(`Score: ${data.score}/100 (${data.grade})`);
data.priorities.forEach(p =>
  console.log(`  [${p.severity}] ${p.issue}`)
);
```

### PHP
```php
$ch = curl_init();
curl_setopt_array($ch, [
    CURLOPT_URL => "https://seoscoreapi.com/audit?url=https://example.com",
    CURLOPT_HTTPHEADER => ["X-API-Key: YOUR_KEY"],
    CURLOPT_RETURNTRANSFER => true,
]);
$data = json_decode(curl_exec($ch), true);
echo "Score: {$data['score']}/100 ({$data['grade']})\n";
```

### Ruby
```ruby
require 'net/http'
require 'json'

uri = URI("https://seoscoreapi.com/audit?url=https://example.com")
req = Net::HTTP::Get.new(uri)
req["X-API-Key"] = "YOUR_KEY"
resp = Net::HTTP.start(uri.hostname, uri.port, use_ssl: true) { |http| http.request(req) }
data = JSON.parse(resp.body)
puts "Score: #{data['score']}/100 (#{data['grade']})"
```

### Go
```go
req, _ := http.NewRequest("GET", "https://seoscoreapi.com/audit?url=https://example.com", nil)
req.Header.Set("X-API-Key", "YOUR_KEY")
resp, _ := http.DefaultClient.Do(req)
// parse resp.Body as JSON
```

## Batch Audits (Paid Plans)

```python
resp = requests.post(
    "https://seoscoreapi.com/audit/batch",
    json={"urls": ["https://site1.com", "https://site2.com", "https://site3.com"]},
    headers={"X-API-Key": "YOUR_KEY"}
)
for result in resp.json()["results"]:
    print(f"{result['url']}: {result['score']}/100")
```

## Score Monitoring (Paid Plans)

```python
# Set up daily monitoring
requests.post(
    "https://seoscoreapi.com/monitors",
    json={"url": "https://your-site.com", "frequency": "daily"},
    headers={"X-API-Key": "YOUR_KEY"}
)

# List monitors
resp = requests.get(
    "https://seoscoreapi.com/monitors",
    headers={"X-API-Key": "YOUR_KEY"}
)
print(resp.json())
```

## CI/CD Integration

Use our [GitHub Action](https://github.com/SeoScoreAPI/seo-audit-action):

```yaml
- uses: SeoScoreAPI/seo-audit-action@v1
  with:
    url: "https://your-site.com"
    api-key: ${{ secrets.SEO_SCORE_API_KEY }}
    threshold: 85
```

## Links

- **Website:** https://seoscoreapi.com
- **API Docs:** https://seoscoreapi.com/docs
- **GitHub Action:** https://github.com/SeoScoreAPI/seo-audit-action
- **Blog:** https://seoscoreapi.com/blog

## Pricing

| Plan | Price | Audits | Features |
|------|-------|--------|----------|
| Free | $0 | 5/day | All 28 checks |
| Starter | $5/mo | 200/mo | + Monitoring, Batch |
| Basic | $15/mo | 1,000/mo | + More monitors |
| Pro | $39/mo | 5,000/mo | + Priority support |
| Ultra | $99/mo | 25,000/mo | + Dedicated support |
