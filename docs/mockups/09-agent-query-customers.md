# 09 — Agent: Customer Count Query

Goal: Answer natural-language questions by using API or UI automation.

Layout (wireframe):

```
+----------------------------------------------------------------+
|  Ask a question                                                |
|----------------------------------------------------------------|
|  "Tell me total customers whose registrations are approved"    |
|                                                                |
|  [ Submit ]                                                    |
|----------------------------------------------------------------|
|  Result: 1,248                                                 |
|  Evidence: [Screenshot] [Trace] [Network JSON]                 |
|  Method: API (fallback: UI with filter → count KPI)            |
|  Filters: Registration status = Approved                       |
|                                                                |
|  [ Re-run with different timeframe ]                            |
+----------------------------------------------------------------+
```