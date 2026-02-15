# logtool-v2 — Cloud Log Cleaner & JSON Summary (Period 2)

logtool-v2 is the second version of **logtool**, built for cloud engineering practice.  
It reads raw logs, filters out invalid entries, outputs a cleaned log file, and generates a structured JSON summary that could be used in a real monitoring dashboard.

---

## 📌 Features

### ✔️ Log Validation
A log line is considered valid if:
- It contains **exactly 4 fields** separated by `|`
- The log level is one of: **INFO**, **WARN**, **ERROR**

All other lines are counted as invalid.

---

### ✔️ Clean Output Logs  
Valid logs are written to:


clean_logs.txt


In the format:


timestamp | LEVEL | service | message


(LEVEL is automatically converted to uppercase.)

---

### ✔️ JSON Summary Generation

A second output file is produced:


summary.json


with the exact required structure:

```json
{
  "total_lines": 0,
  "valid_lines": 0,
  "invalid_lines": 0,
  "levels": { "INFO": 0, "WARN": 0, "ERROR": 0 },
  "top_services": [{ "service": "auth", "count": 0 }],
  "top_errors": [{ "message": "DB timeout", "count": 0 }]
}
```

The script automatically calculates:

total lines

valid lines

invalid lines

counts per level

top 3 services used in valid logs

top 3 error messages (ERROR level only)

🚀 How to Run

Ensure these files are in the same folder:

starter_period2.py

logs.txt

Run the script:

python starter_period2.py

Two output files will be generated:

clean_logs.txt
summary.json
📁 Files Included

starter_period2.py

logs.txt (input)

clean_logs.txt (generated)

summary.json (generated)
