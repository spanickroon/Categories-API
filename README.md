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

Successful post request:

![изображение](https://user-images.githubusercontent.com/37241257/104203088-ca13d380-543c-11eb-8955-bcb3f1d1123c.png)

Getting a category with id 2:

![изображение](https://user-images.githubusercontent.com/37241257/104203246-f7f91800-543c-11eb-832c-37b1096c4c45.png)

Getting a category with id 8:

![изображение](https://user-images.githubusercontent.com/37241257/104203344-1101c900-543d-11eb-8b33-0719ee44d13a.png)

Database records:

![изображение](https://user-images.githubusercontent.com/37241257/104203508-46a6b200-543d-11eb-9f33-4b2ec945a0fd.png)

Tests:

![изображение](https://user-images.githubusercontent.com/37241257/104203639-6ccc5200-543d-11eb-8653-0ce71c730201.png)





