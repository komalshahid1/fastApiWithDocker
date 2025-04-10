# FastAPI Aurora Application

A modern, containerized FastAPI application with PostgreSQL database integration, designed for scalability and maintainability.

## 🚀 Features

- FastAPI web framework for high-performance API development
- PostgreSQL database with SQLAlchemy ORM
- Docker containerization for easy deployment
- Environment-based configuration
- Database migrations with Alembic
- Type-safe API with Pydantic models
- RESTful API endpoints

## 📋 Prerequisites

- Docker and Docker Compose
- Python 3.9+
- PostgreSQL (if running locally)

## 🛠️ Project Structure

```
.
├── app/                    # Application source code
│   ├── main.py            # FastAPI application entry point
│   ├── database.py        # Database configuration
│   ├── models.py          # SQLAlchemy models
│   └── schemas.py         # Pydantic schemas
├── alembic/               # Database migration files
├── .env                   # Environment variables
├── .env.example          # Example environment variables
├── Dockerfile            # Docker build configuration
├── docker-compose.yml    # Docker service definitions
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd fastapi_aurora_app
   ```

2. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. **Build and start the services**
   ```bash
   docker-compose up --build
   ```

4. **Access the API**
   - API will be available at `http://localhost:8000`
   - API documentation at `http://localhost:8000/docs`

## 📚 API Endpoints


### User Management
- `POST /users/`
  - Create a new user
  - Request body: `{"email": "string", "name": "string"}`
  - Response: Created user object

- `GET /users/`
  - Get all users
  - Response: List of user objects

## 🔧 Development

### Running Tests
```bash
# Add test commands here when tests are implemented
```

### Database Migrations
```bash
# Generate new migration
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head
```

### Local Development
```bash
# Start development server
docker-compose up --build

# View logs
docker-compose logs -f
```

## 🛡️ Security

- Environment variables for sensitive data
- Input validation with Pydantic
- SQL injection prevention with SQLAlchemy

## 📦 Dependencies

- FastAPI
- SQLAlchemy
- Pydantic
- Alembic
- PostgreSQL
- Docker

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- FastAPI team for the amazing framework
- SQLAlchemy for the powerful ORM
- Docker for containerization
