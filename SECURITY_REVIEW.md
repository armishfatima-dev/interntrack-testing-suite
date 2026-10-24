# OWASP-Informed Security Review: InternTrack

## Executive Summary

This document outlines the structured security audit performed on the InternTrack backend. Six key vulnerabilities were identified and remediated following OWASP Top 10 guidelines.

---

## Findings & Remediations

### 1. Overly Permissive CORS Policy

- **OWASP Category:** A05:2021 – Security Misconfiguration
- **Finding:** Initial configuration used `allow_origins=["*"]`, exposing API endpoints to unauthorized cross-origin requests.
- **Fix Applied:** Restricted `allow_origins` to explicitly trusted frontend domains (`http://localhost:3000`, `http://127.0.0.1:3000`).
- **Verification:** Verified via FastAPI middleware configurations and integration test checks.

### 2. Lack of Rate Limiting on Authentication Endpoints

- **OWASP Category:** A07:2021 – Identification and Authentication Failures
- **Finding:** The `/auth/login` route lacked brute-force protection, allowing unlimited rapid credential guessing attempts.
- **Fix Applied:** Integrated `slowapi` rate limiter enforcing a strict limit (`5/minute`) on login attempts.
- **Verification:** Verified by triggering rapid authentication requests and confirming `429 Too Many Requests` responses.

### 3. Stack Trace Leakage in Global Exceptions

- **OWASP Category:** A09:2021 – Security Logging and Monitoring Failures / Information Disclosure
- **Finding:** Unhandled exceptions exposed raw Python stack traces and internal database path details to clients.
- **Fix Applied:** Implemented a global exception handler returning sanitized, generic JSON error messages (`500 Internal Server Error`).
- **Verification:** Tested error handling responses under simulated exception states to ensure zero trace leakage.

### 4. Hardcoded Secret Keys Risk

- **OWASP Category:** A02:2021 – Cryptographic Failures
- **Finding:** JWT secret tokens were initialized with weak default fallback strings directly in source code.
- **Fix Applied:** Configured token handling to draw from secure environment variables (`SECRET_KEY`).
- **Verification:** Inspected code implementation and verified environment injection behavior.

### 5. Insecure Password Hashing Algorithms

- **OWASP Category:** A02:2021 – Cryptographic Failures
- **Finding:** Ensuring password storage relies strictly on strong cryptographic hashing rather than weak digests.
- **Fix Applied:** Implemented `passlib` with `bcrypt` crypt context for secure password hashing and verification.
- **Verification:** Inspected database records created during test fixture execution to confirm valid `bcrypt` hashing prefixes.

### 6. Potential SQL Injection Vectors in Search/Filter Parameters

- **OWASP Category:** A03:2021 – Injection
- **Finding:** Direct raw SQL query construction risks in dynamic search/filter endpoints.
- **Fix Applied:** Mandated the exclusive use of SQLAlchemy ORM parameterized queries (`select()`, `filter()`).
- **Verification:** Ran test suites with malformed query parameters and verified clean ORM parameter binding.
