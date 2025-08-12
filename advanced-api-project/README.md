# Book API Endpoints

## Public Endpoints
- **GET /books/** → Retrieve all books
- **GET /books/<id>/** → Retrieve a single book

## Authenticated Endpoints
- **POST /books/create/** → Add a new book
- **PUT /books/<id>/update/** → Update an existing book
- **DELETE /books/<id>/delete/** → Delete a book

## Permissions
- Public read access.
- Write, update, and delete access restricted to authenticated users.
- Role-based permissions can be enabled via `IsAdminOrReadOnly`.
