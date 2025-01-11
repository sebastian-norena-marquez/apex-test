
# 

1. **Construir y Ejecutar la Aplicación con Docker

### Construir la Imagen

```bash
docker-compose build
```

### Ejecutar los Contenedores

```bash
docker-compose up
```

```bash
docker-compose up --build
```

### Verificar la Aplicación

- La API estará disponible en: [http://localhost:8000](http://localhost:8000)
- MongoDB estará expuesto en el puerto `27017`.

2. **Prueba la API:**
   Abre la documentación interactiva en: [http://localhost:8000/docs](http://localhost:8000/docs)

---

---

## 3. Probar la Integración con Ejemplos

### Crear un Producto

```bash
curl -X POST http://localhost:8000/products -H "Content-Type: application/json" -d '{
  "product_id": "123",
  "name": "Producto Ejemplo",
  "description": "Descripción del producto",
  "price": 19.99,
  "stock": 100
}'
```

### Obtener Todos los Productos

```bash
curl -X GET http://localhost:8000/products
```

### Obtener un Producto por ID

```bash
curl -X GET http://localhost:8000/products/123
```

### Actualizar un Producto

```bash
curl -X PUT http://localhost:8000/products/123 -H "Content-Type: application/json" -d '{
  "name": "Nuevo Nombre",
  "price": 25.99
}'
```

### Eliminar un Producto

```bash
curl -X DELETE http://localhost:8000/products/123
```

---

## 4. Pruebas Unitarias

### Ejecutar Todas las Pruebas

```bash
TESTING=true poetry run pytest
```
### Colelccion de postman

```bash
TEST.postman_collection.json
```
