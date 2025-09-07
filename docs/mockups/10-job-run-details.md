# 10 — Job Run Details & Evidence

Goal: Inspect a workflow run, steps, retries, and artifacts.

Layout (wireframe):

```
+------------------------------------------------------------------+
|  Job Run: #8f23a                                                 |
|------------------------------------------------------------------|
|  Status: Succeeded  Duration: 06:42  Retries: 1                  |
|                                                                  |
|  Steps                                                           |
|  1) Parse Prompt → Spec               ✓                          |
|  2) brij Login                        ✓                          |
|  3) Create Experience                 ✓                          |
|  4) Registration Page                 ✓                          |
|  5) Modules                           ✓                          |
|  6) AI Assets                         ✓                          |
|  7) Publish Shopify                   ✓                          |
|  8) Email Customer                    ✓                          |
|                                                                  |
|  Artifacts                                                       |
|   - Screenshots (12) [View Gallery]                              |
|   - Playwright Trace [Open]                                      |
|   - Links: [Experience URL] [Shopify Products]                   |
+------------------------------------------------------------------+
```