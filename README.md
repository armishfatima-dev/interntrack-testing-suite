# InternTrack Testing Suite & Security Review

This repository contains the automated test suite and OWASP-informed security review for the InternTrack backend API (Week 5 Task 2).

## Tech Stack

- FastAPI & SQLAlchemy
- Pytest & HTTPX (Isolated testing with in-memory SQLite)
- Slowapi (Rate limiting)
- Passlib (Bcrypt password hashing)

## Key Security Implementations (OWASP-Informed)

- **CORS Policy:** Restricted to explicit trusted frontend domains instead of wide-open wildcards (`*`).
- **Rate Limiting:** Enforced on the `/auth/login` endpoint (`5/minute`) to prevent brute-force attacks.
- **Error Handling:** Global exception handler implemented to prevent raw stack trace and path leakage.
- **Data Security:** Environment-driven secret configuration and parameterized ORM queries to prevent injection.

## Project Structure

- `app/`: Core backend application, routers, models, and authentication logic.
- `tests/`: Isolated automated test suite (`conftest.py`, `test_auth.py`, `test_routes.py`, `test_progression.py`).
- `SECURITY_REVIEW.md`: Detailed breakdown of 6 OWASP findings, applied fixes, and verification methods.

## Running Tests Locally

To execute the automated test suite, run:

```powershell
pytest -v

```
