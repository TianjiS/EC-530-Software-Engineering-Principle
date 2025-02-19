# Smart Home API

## Overview
This API is designed for a **smart home system**, which manages Users, Houses, Rooms, and Devices. It follows **CRUD Principles** 

## Features
- **CRUD Operations** for Users, Houses, Rooms, and Devices
- **Error Handling** with Input Validation
- **Unit Testing**
- **JSON-based API responses**

---

##  API Structure
The API follows a **hierarchical structure**:
- **Users** own **Houses**
- **Houses** contain multiple **Rooms**
- **Rooms** have **Devices**

---

##  User API

| Action | HTTP Method | Endpoint | Description |
|--------|------------|----------|-------------|
| Create | `POST` | `/users` | Create a new user |
| Read | `GET` | `/users/{id}` | Get user details |
| Update | `PUT` | `/users/{id}` | Update user info |
| Delete | `DELETE` | `/users/{id}` | Delete the user |

**Data Structures** can be viewed in attached code

**To use this API** pip install Flask, and run the API with python app.py

**Error Handling**
| Error Type              | HTTP Status Code | Description                                      |
|-------------------------|-----------------|--------------------------------------------------|
| Bad Request            | 400             | Invalid input or missing required fields        |
| Unauthorized           | 401             | Authentication failure (e.g., invalid token)    |
| Forbidden             | 403             | Access denied to the requested resource        |
| Not Found             | 404             | Resource does not exist (e.g., user not found) |
| Conflict              | 409             | Duplicate data (e.g., email already exists)    |
| Internal Server Error | 500             | Unexpected system failure                      |



