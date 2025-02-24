
## 📝 Blogging Application (Django)  

### 📌 About the Project  

This is a **blogging application** built using the **Django framework**. It allows users to **write, categorize, and tag blog posts** while managing their profiles. The platform is designed for a **smooth and user-friendly experience**, making it easy for users to create and share their thoughts.

**Note:** The name of the project is yet to be finalized, so it will temporarily be referred to as "Blogging Application".

That would be a good idea! It helps track progress and makes it clear when this version of the project started. You can add something like this under the **"About the Project"** section:  

📅 **Start Date (This Version):** *February 2025*  

Or, if you want a more detailed approach, add a **Project Timeline** section at the end:  

### 📅 Project Timeline  

- **Previous Version Started:** *November 2024* (Paused due to custom user model issues)  
- **Current Version Started:** *February 2025*
🚀 Next Milestone: Implementing user authentication (signup, login, logout) and basic blog post creation.

### ⚠️ Why a New Repository?  

A previous version of this project was paused due to **issues faced while implementing a custom user model** in the middle of development. Instead of continuing with a broken setup, this new repository was created to ensure a **well-structured approach, with the custom user model implemented from the start**.  

---

## 🚧 Current Progress  

So far, the following have been implemented:  
✔ **Custom User Model** – Implemented from the beginning  
✔ **Database Models** – Post, Category, Tag, User  
✔ **Base Templates** – `main.html`, `navbar.html`, and a dummy `home.html`  

🔜 **Next Steps:**  

- Implement **User Authentication (Signup, Login, Logout)**  
- Add **Blog Post Features** (Create, Edit, Delete, View)  
- Integrate **Categories & Tags System**  
- Develop **Profile Management & User Dashboard**  

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
