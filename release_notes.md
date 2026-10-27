# Release Notes – FastAPIProject

## Version 1.0.0 – 27 October 2026

### Project Overview
FastAPIProject is a learning project built with Python and FastAPI. It demonstrates how to create REST API endpoints, work with data, and test API responses.

### Features
- Created a FastAPI application with a home endpoint.
- Organised endpoints into separate routers for students, courses, items, and tickets.
- Added endpoints to create, read, update, and delete records where supported.
- Used SQLite and SQLAlchemy to store item data.
- Used Pydantic schemas to validate request data and format responses.
- Added HTTP status codes and error messages for invalid requests and missing records.

### Testing
- Used pytest and FastAPI TestClient for automated API tests.
- Tested item creation, invalid data, item lists, single-item lookup, updates, and deletion.
- Used a separate in-memory SQLite database for item tests.
- During development, corrected route mismatches and expected response messages found by tests.

### Technologies
- Python
- FastAPI
- SQLAlchemy and SQLite
- Pydantic
- pytest and TestClient
- Git and GitHub

### Known Limitations
- This is an educational project, not a production-ready service.
- Student data is stored in memory, so it does not persist after restarting the application.
- Automated tests and validation can be extended to cover more endpoints.

### Next Steps
- Add more automated tests for students, courses, and tickets.
- Improve input validation and error handling.
- Add authentication and user permissions.
- Prepare the application for deployment.

### Repository
https://github.com/ViktoriiaBut-tory/FastAPIProject
