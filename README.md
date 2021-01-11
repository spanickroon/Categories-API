# Categories-API

### A simple Categories API that stores category tree to database and returns category parents, children and siblings by category id.

---

### Install

```bash
git clone https://github.com/spanickroon/Categories-API.git

cd MnemosCategoriesyne

touch .env.dev

sudo docker-compose up -d --build
sudo docker ps -a

```

Links for open api:

```
http://localhost:8000/categories/
```

Virtual environment variables for .env.dev file:

```
DATABASE_ENGINE=django.db.backends.postgresql

DATABASE_HOST=localhost (Your data)

DATABASE_NAME=testdb (Your data)

DATABASE_PASSWORD=test (Your data)

DATABASE_PORT=5432 

DATABASE_URL=postgres://test:test@localhost:5432/testdb (Your data)

DATABASE_USER=test (Your data)

SECRET_KEY= (Your data)

ALLOWED_HOSTS=localhost 127.0.0.1 0.0.0.0 [::1] (Your data)
```

### Docs

Use redoc from the link:

```
http://localhost:8000/redoc/
```

View logs:

```bash
sudo docker-compose logs -f
```

Use admin panel from the link:
```
http://localhost:8000/admin/
```

### Removed

For removed docer-compose containers use this:

```bash
sudo docker-compose down -v
```

And check:

```bash
sudo docker images
```


For removed images use this:

```bash
sudo docker systems pruno
```

### Technology stack

+ Django 3.1.5
+ Django-rest-framework 3.12.2
+ Python3 3.8.5
+ PostgreSQL

### Review





