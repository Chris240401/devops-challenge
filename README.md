# 🚀 DevOps Challenge – Microservicio FastAPI + Docker + CI/CD

Este microservicio implementa una API REST con FastAPI, protegida con API Key y JWT Header, lista para ser desplegada vía Docker y GitHub Actions.

---

## 🔧 Tecnologías

- [FastAPI](https://fastapi.tiangolo.com/)
- [Docker](https://www.docker.com/)
- [GitHub Actions](https://docs.github.com/actions)
- [Pytest](https://docs.pytest.org/)
- Python 3.12

---

## 🚀 Ejecutar desde DockerHub

> Requiere tener [Docker instalado](https://www.docker.com/products/docker-desktop/)

```bash
docker run -p 8000:8000 \
  -e X-Parse-REST-API-Key=2f5ae96c-b558-4c7b-a590-a501ae1c3f6c \
  -e X-JWT-KWY=abc123 \
  chris240401/devops-challenge

Luego accede a:

http://localhost:8000/docs ← documentación interactiva (Swagger)

http://localhost:8000 ← mensaje base

curl -X POST "http://localhost:8000/DevOps" \
  -H "Content-Type: application/json" \
  -H "X-Parse-REST-API-Key: 2f5ae96c-b558-4c7b-a590-a501ae1c3f6c" \
  -H "X-JWT-KWY: abc123" \
  -d "{\"message\": \"Hello\", \"to\": \"Juan\", \"from\": \"System\", \"timeToLifeSec\": 45}"

El pipeline se ejecuta automáticamente en cada push a main

Corre tests con pytest

Construye imagen Docker

Publica en Docker Hub


