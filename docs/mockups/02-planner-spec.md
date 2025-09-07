# 02 — Prompt → Plan & Spec Review

Goal: Parse prompt, generate structured spec, show assumptions, allow edits.

Layout (wireframe):

```
+----------------------------------------------------------------+
|  Describe your experience                                      |
|----------------------------------------------------------------|
|  "Create a web app experience for a fishing brand ..."         |
|                                                                |
|  [ Generate Plan ]                                             |
|----------------------------------------------------------------|
|  Plan Summary                                                  |
|  - Type: D2C Catalog + Registration + Warranty                 |
|  - Products: 12 (from Shopify)                                 |
|  - Modules: Registration, Warranty, Custom Gallery             |
|  - AI Assets: 3 images, 1 video                                |
|                                                                |
|  Assumptions [edit]:                                           |
|  - Brand tone: Outdoorsy, rugged                               |
|  - Missing warranty copy → template A                          |
|----------------------------------------------------------------|
|  Spec (JSON) [view/edit]     [ Accept & Start Automation → ]   |
+----------------------------------------------------------------+
```