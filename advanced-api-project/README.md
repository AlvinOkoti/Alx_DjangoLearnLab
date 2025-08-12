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

### Book List API Query Options

**Filtering**
- `/api/books/?title=1984`
- `/api/books/?author=1`
- `/api/books/?publication_year=1949`

**Searching**
- `/api/books/?search=Orwell`  → Finds books by George Orwell
- `/api/books/?search=Farm`    → Finds "Animal Farm"

**Ordering**
- `/api/books/?ordering=publication_year`  → Oldest first
- `/api/books/?ordering=-publication_year` → Newest first

