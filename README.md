# Financial Hub Integration Platform

## Overview

This platform serves as a comprehensive solution for integrating various financial services APIs, streamlining financial operations for developers and businesses. It facilitates managing user accounts, transactions, and seamless integration with external financial APIs like Plaid, Stripe, Revolut, and Wise.

## Technology Stack

- **Programming Language:** Python
- **Web Framework:** Django
- **Databases:** SQLite (development), PostgreSQL (production)
- **External Libraries/Tools:** Django REST Framework, dj-database-url, dotenv, requests

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip and virtualenv
- Node.js (for frontend)

### Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory and create a virtual environment:

   ```bash
   cd financial-hub-integration
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On Unix or MacOS: `source venv/bin/activate`
4. Install the required Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Set up environment variables by creating a `.env` file in the project root directory. Use `.env.example` as a template.

### Running the Application

1. Apply Django migrations to create the database schema:

   ```bash
   python manage.py migrate
   ```

2. Start the Django development server:

   ```bash
   python manage.py runserver
   ```

3. Access the application at `http://localhost:8000`.

## Testing

Run the automated tests with:

```bash
pytest
```

## Deployment

Refer to the CI/CD pipeline configuration in `.github/workflows/ci_cd.yml` for automated testing and deployment instructions.

## Contributing

Contributions are welcome! Please read our contributing guidelines and submit pull requests to our repository.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
