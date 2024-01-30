# VoxPop

VoxPop is an open comment platform that allows users to express their opinions on various topics. It provides a public feed where comments are displayed in chronological order. The platform features two-field comments, with users categorizing their comments as positive or negative.

## Features

1. **Open Platform for Comments:**
   - Users can leave comments without the need for registration.
   - Comments are stored in an array (no database usage for now).

2. **Two-Field Comments:**
   - Each comment consists of two fields:
     - Comment text
     - Comment category (positive or negative)

3. **Public Feed:**
   - Comments are displayed in a public feed.
   - The feed is paginated to avoid showing all comments at once.
   - Available for viewing by all users.

## Technologies Used

- FastAPI
- HTML Templates
- CSS

## Getting Started

### Prerequisites

- Python 3.x
- Install dependencies using `pip install -r requirements.txt`

### Running the Application

1. Clone the repository:
   ```bash
   git clone https://github.com/Bayashat/Vox-Pop
   cd VoxPop

2. Install dependencies:
    ```bash
    pip install -r requirements.txt

3. Run the FastAPI application:
   ```bash
   uvicorn app.main:app --reload

4. Open your browser and navigate to http://localhost:8000

## Directory Structure
```csharp
VoxPop/
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── repository.py
│   └── static
│       └── style.css
├── README.md
└── templates
    ├── comments
    │   └── index.html
    └── index.html
