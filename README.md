# 📚 RESTPrograms

A simple RESTful API to manage university programs.
Made by: Iskolutions (Causon, Efondo, Franco, Lopez)

**Base URL:** `https://restprograms.onrender.com`  

---

## 📦 Endpoints

### Create a Program  
**POST** `/programs`

**Body (JSON):**
```json
{
  "name": "Computer Science",
  "year_duration": 4,
  "level": "Undergraduate",
  "degree_type": "BS"
}
```

**Response:**
- `201 Created`
```json
{
  "Message": "Program created successfully",
  "Program": {
    "Program ID": 1,
    "Program Name": "Computer Science",
    "Year Duration": 4,
    "Level": "Undergraduate",
    "Degree Type": "BS"
  }
}
```

---

### Get All or Filtered Programs  
**GET** `/programs`  
Optional query parameters:
- `name`: case-insensitive match
- `year_length`: integer (e.g. 4)
- `degree_type`: case-insensitive match
- `id`: integer
- `level`: case-insensitive match

**Example:**  
`GET /programs?year_length=4&degree_type=bs`

**Response:**
- `200 OK`
```json
[
  {
    "id": 1,
    "name": "Computer Science",
    "year_duration": 4,
    "level": "Undergraduate",
    "degree_type": "BS"
  }
]
```

---

### Replace a Program (Full Update)  
**PUT** `/programs/<id>`

**Body (JSON):** *All fields are required*
```json
{
  "name": "Information Technology",
  "year_duration": 4,
  "level": "Undergraduate",
  "degree_type": "BS"
}
```

**Response:**
- `200 OK`
```json
{
  "Message": "Program updated successfully",
  "Program": {
    "Program ID": 1,
    "Program Name": "Information Technology",
    "Year Duration": 4,
    "Level": "Undergraduate",
    "Degree Type": "BS"
  }
}
```

---

### Modify a Program (Partial Update)  
**PATCH** `/programs/<id>`

**Body (JSON):** *Any of the following fields*
- `name`
- `year_duration`
- `level`
- `degree_type`

**Example:**
```json
{
  "name": "IT"
}
```

**Response:**
- `200 OK`
```json
{
  "message": "Program updated successfully",
  "updated_fields": {
    "name": "IT"
  }
}
```

---

### Delete a Program  
**DELETE** `/programs/<id>`

**Response (Success):**
- `200 OK`
```json
{
  "Message": "Program deleted successfully"
}
```

**Response (Not Found):**
- `404 Not Found`
```json
{
  "Error": "Program not found"
}
```

---

## ⚠️ Error Responses

Common errors include:
- `400 Bad Request`: Missing or invalid fields
- `404 Not Found`: Resource not found
- `500 Internal Server Error`: Unexpected server/database error

---

## 🛠️ Setup (For Local Dev)

```bash
pip install flask
python your_file_name.py
```

Make sure `programs.db` is in the same directory or created by `create_tables()`.

---

## 🔗 Deployment

This API is deployed on [Render](https://render.com)  
**Live URL:** [https://restprograms.onrender.com](https://restprograms.onrender.com)

---
