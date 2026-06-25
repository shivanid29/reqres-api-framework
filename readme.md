# ReqRes API Automation Framework

## Project Overview

This project implements a scalable, fully data-driven API test automation framework targeting the ReqRes REST API using **Python**, **Pytest**, and **Requests**. 

The architecture separates core HTTP client logic, validation components, and static test data inputs. This separation ensures that adding or updating test cases requires modifying configuration maps rather than writing new functional code.

**Application Under Test:** [ReqRes Mock API Portal](https://reqres.in)

---

## 🛠️ Key Architectural Design

* **Data-Driven Framework Engine:** Test scenarios, input parameters, endpoints, and validation criteria are separated from execution logic and stored entirely within JSON schemas.
* **Dynamic Secret Token Injection:** Runtime token replacement replaces custom placeholders (`${EMAIL}`, `${PASSWORD}`) with secure local environment variables or platform tokens.
* **Centralized Network Wrapper:** Standardizes communication rules globally by wrapping python `requests` calls to inject uniform configuration parameters, handle execution logs, and structure custom headers.
* **Dot-Notation Response Parser:** A specialized utility component splits path lookups (`data.id`) dynamically to validate values nested within JSON payloads without manual index mapping.
* **Automated HTML Dashboards:** Integrated with `pytest-html` to output self-contained test diagnostics and tracking.

---

## 📂 Project Structure

```text
reqres-api-framework/
├── .github/
│   └── workflows/
│       └── api-tests.yml         # CI/CD orchestration pipeline
├── tests/
│   ├── test_data.json            # Data-driven test case repository matrix
│   └── test_reqres_api.py        # Parameterized core test runner suite
├── utils/
│   ├── __init__.py
│   ├── api_client.py             # Core HTTP client wrapping requests
│   ├── assertions.py             # Target validation engine & JSON parser
│   ├── json_reader.py            # Static file data ingestion and token handler
│   └── logger.py                 # Core diagnostic tracking output streams
├── .env                          # Restricted local target secrets configuration
├── .gitignore                    # Unversioned file mapping exclusions
├── pytest.ini                    # Test execution definitions and output flags
└── requirements.txt              # Unified library dependency list