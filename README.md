
## 📝 Blogging Application (Django)  

### 📌 About the Project  

This is a **blogging application** built using the **Django framework**. It allows users to **write, categorize, and tag blog posts** while managing their profiles. The platform is designed for a **smooth and user-friendly experience**, making it easy for users to create and share their thoughts.

**Note:** The name of the project is yet to be finalized, so it will temporarily be referred to as "Blogging Application". 

### 📅 Project Timeline  

- **Previous Version Started:** *November 2024* (Paused due to custom user model issues)  
- **Current Version Started:** *February 2025*   
✔ User Authentication (Signup, Login, Logout) Completed   
🚀 Next Milestone: Implementing blog post creation, including a sub-form for categories.

### ⚠️ Why a New Repository?  

A previous version of this project was paused due to **issues faced while implementing a custom user model** in the middle of development. Instead of continuing with a broken setup, this new repository was created to ensure a **well-structured approach, with the custom user model implemented from the start**.  

---

## 🚧 Current Progress  

So far, the following have been implemented:  
✔ **Custom User Model** – Implemented from the beginning  
✔ **Database Models** – Post, Category, Tag, User     
✔ **User Authentication (Signup, Login, Logout)** implemented – Users must log in to access the home page (`@login_required` enforced).  
✔ **Base Templates** – `main.html`, `navbar.html`, and a structured `home.html` with *sidebar* and *blog feed*  
✔ **Blog Feed** – Displays blog posts on the home page   
✔ **Sidebar Components**:  
    - **User Profile Card** – Displays profile picture, username, display name, and number of blogs  
    - **Daily Writing Prompt** – Encourages blogging with a writing prompt  
    - **Word of the Day** – Placeholder, will fetch words from an API later  
    - **Quote of the Day** – Placeholder, will use an API for daily quotes  
    - **Followed Categories List** – Placeholder, to be implemented later  

🔜 **Next Steps:**

- **Enhance Blog Post Creation**:  
  - Implement post creation form  
  - Add sub-form for creating categories if no suitable category exists  
- **Refine Sidebar**:  
  - Fetch daily quote from an API  
  - Fetch word of the day from an API  
  - Implement followed categories list  
- **Develop Profile Management & User Dashboard**  

---

## 🛠️ Development Setup  

### 1️⃣ **Clone the Repository**  

```sh
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2️⃣ **Create & Activate a Virtual Environment**  

```sh
python -m venv .venv  # Create virtual environment
```

#### **For Windows:**  

```sh
.venv\Scripts\activate
```

#### **For macOS/Linux:**  

```sh
source .venv/bin/activate
```

### 3️⃣ **Install Dependencies**  

```sh
pip install -r requirements.txt
```

### 4️⃣ **Apply Migrations & Start Server**  

```sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### 5️⃣ **Create a Superuser (Optional, for Admin Access)**  

```sh
python manage.py createsuperuser
```

---

## 🚀 Future Enhancements  

- **Comments & Likes System**  
- **Markdown Support for Posts**  
- **Dark Mode for UI**  
- **Follow System for Users**  

---

## 💡 Contributing  

Contributions are welcome! Feel free to open issues and submit pull requests.  

---

## 📜 License  

This project is open-source and available under the **MIT License**.  
