# 03 — brij: Add Experience

Goal: Automate creation of a new experience in brij.

Layout (wireframe):

```
+--------------------------------------------------------------+
|  brij → Experiences                                          |
|--------------------------------------------------------------|
|  [ Add Experience ]                                          |
|   └─ Modal:                                                  |
|      Name:  ___________________                              |
|      Brand: [Fishing Co ▼]                                   |
|      Template: [Catalog + Reg + Warranty ▼]                  |
|      Visibility: [Private/Public]                            |
|      [ Create ]                                              |
|                                                              |
|  After create → tabs: [Overview] [Registration] [Modules]    |
+--------------------------------------------------------------+
```

Automation notes:
- Wait for modal, fill fields from spec, assert new experience appears.