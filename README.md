# Order Management API

A simple Order Management system built using **Django** and **Django REST Framework**, implementing
JWT-based authentication and role-based access control.  
The project is fully API-driven and does not use the Django Admin panel.

---

##  Tech Stack
- Python 3.x
- Django
- Django REST Framework
- JWT Authentication (SimpleJWT)
- SQLite (default, can be replaced with PostgreSQL)

---

##  User Roles
- **Admin**
  - Create and manage products
  - View all orders
- **Customer**
  - Register and login via API
  - Place orders
  - View only their own orders

---

##  Features
- JWT-based authentication
- Role-based authorization
- Nested order creation
- Order total calculation
- Clean APIView-based implementation
- No Django Admin usage (as per requirement)

---

##  Setup Instructions

### 1 Clone Repository
```bash
git clone <repository-url>
cd order_management
