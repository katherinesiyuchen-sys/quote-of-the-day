# Quote of the Day

A simple full-stack web application that displays a random quote. Built with a React frontend and a Flask backend, this project aims to practice basic client-server communication and API integration.

## Demo

Displays a random quote on page load with the ability to fetch a new quote using a button.

## Tech Stack

* **Frontend:** React (Create React App)
* **Backend:** Flask (Python)
* **API Communication:** Fetch API
* **Other:** Flask-CORS

## Project Structure

```
quote-of-the-day/
├── frontend/        # React frontend
├── backend/         # Flask backend
├── requirements.txt # Python dependencies
```

## Getting Started

### Backend Setup

```bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
cd backend
python3 app.py
```

Runs on: http://127.0.0.1:5000

---

### Frontend Setup

```bash
cd frontend
npm install
npm start
```

Runs on: http://localhost:3000

---

## API

### `GET /quote`

Returns a random quote.

**Response:**

```json
{
  "quote": "The only way to do great work is to love what you do."
}
```
