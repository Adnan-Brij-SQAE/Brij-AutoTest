# 01 — Credentials & Connections

Goal: Capture and validate access to Shopify and brij securely.

Layout (wireframe):

```
+-------------------------------------------------------------+
|  Connect Accounts                                            |
|-------------------------------------------------------------|
| [ Shopify ]  Install app → [Connect via OAuth] (status: ✓)   |
|                                                             |
| [ brij ]     Email __________  Password ________ [Connect]  |
|              or [Use Secret From Vault] (status: pending)   |
|                                                             |
| Advanced:                                                    |
|  - Region: [US/EU]  - Headless: [Yes/No]                    |
|  - Store URL: ____________________                           |
|                                                             |
|                 [ Test Connections ]   [ Continue → ]       |
+-------------------------------------------------------------+
```

States:
- Shopify connected (token stored), brij pending, test button disabled until both ok.
- Errors inline with remediation (e.g., 2FA, invalid creds).