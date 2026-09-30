### Perturbation Log

---

### System 1 — Validated, Routed Pipeline

* **Change I made (file + what I changed):** Omitted a mandatory field within a test fixture by assigning an empty string to `coverage_limit` prior to execution.

* **Command I ran:** `.\.venv\Scripts\python.exe -c "from policy_extractor.retry import extract_with_retry; ..."`

* **What I predicted:** The pipeline validation routine would flag the omitted value, trigger a single retry attempt, and ultimately escalate the file rather than guessing data.

* **What actually happened (paste the key output line):** `{"kind":"escalation","policy_id":"POL-EMPTY","field":"coverage_limit","reason":"missing required field","retries_used":1,"status":"retry_futile_escalation"}`

* **How this differs from the unperturbed run:** Baseline runs extract records successfully without intervention, whereas this alteration triggers a safety escalation path because the required attribute is absent.

---

### System 2 — Schema-Enforced Two-Pass Extraction

* **Change I made (file + what I changed):** Altered the income document fixture so that the recorded `stated_monthly_total` conflicted with the itemized row sum.

* **Command I ran:** `mortgage-extract fixtures/documents/income_sum_mismatch.txt`

* **What I predicted:** The arithmetic validation check would flag the discrepancy between the declared sum and the computed component total.

* **What actually happened (paste the key output line):** `"field": "total_monthly_income", "calculated": 9642.17, "stated": 10892.17, "delta": -1250.0` and `"consistent": false`.

* **How this differs from the unperturbed run:** Standard inputs return `consistent: true` with zero discrepancies. Introducing a mathematical mismatch causes the verification layer to flag the data integrity error.

---

### System 3 — Multi-Source Synthesis

* **Change I made (file + what I changed):** Executed the investigation utility with an argument forcing the supply chain data stream to simulate a failure state (`--simulate-timeout`).

* **Command I ran:** `supply-chain-investigate meridian --offline --simulate-timeout`

* **What I predicted:** The report generation engine would gracefully handle the missing connector, noting the feed timeout without crashing the entire briefing process.

* **What actually happened (paste the key output line):** `Sources unavailable: logistics unavailable (timeout)` and `late_shipment_count _[missing source: timeout reading logistics]`.

* **How this differs from the unperturbed run:** Normal multi-source combinations synthesize all records into a merged output, whereas simulated service outages cleanly bypass the failed channel and substitute an explanatory placeholder.
