# 💰 Finance Tracker API

A backend system built using FastAPI to manage and analyze financial transactions.

## 🚀 Features

- Create, update, delete transactions
- Filter transactions by type, category, and date
- Financial summary (income, expense, balance)
- Clean REST API structure

## 🛠 Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite

## 📌 API Endpoints

### Transactions
- POST /transactions → Create
- GET /transactions → Get all (with filters)
- GET /transactions/{id} → Get one
- PUT /transactions/{id} → Update
- DELETE /transactions/{id} → Delete

### Analytics
- GET /analytics/summary → Get financial summary

### Home
- GET / → API status

## 📊 Sample Response

```json
{
  "total_income": 5000,
  "total_expense": 2000,
  "balance": 3000
}
