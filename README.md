
## 📝 Blogging Application (Django)  

### 📌 About the Project  

This is a **blogging application** built using the **Django framework**. It allows users to **write, categorize, and tag blog posts** while managing their profiles. The platform is designed for a **smooth and user-friendly experience**, making it easy for users to create and share their thoughts.

**Note:** The name of the project is yet to be finalized, so it will temporarily be referred to as "Blogging Application". 

### 📅 Project Timeline  

- **Previous Version Started:** *November 2024* (Paused due to custom user model issues)  
- **Current Version Started:** *February 2025*   

### ⚠️ Why a New Repository?  

A previous version of this project was paused due to **issues faced while implementing a custom user model** in the middle of development. Instead of continuing with a broken setup, this new repository was created to ensure a **well-structured approach, with the custom user model implemented from the start**.  

---

## ✨ Features  

- **User Authentication**: Signup, login, logout, and profile management.  
- **Create, Edit & Delete Blog Posts**: Users can write, update, and remove their own posts.  
- **Markdown Support**: Blog content supports **bold**, *italic*, __underline__, `code`, and ~~strikethrough~~.  
- **Category & Tag System**: Posts can be categorized and tagged, with dedicated pages for each.  
- **Post Viewing**: Clicking a post title opens a detailed view with the author's profile.  
- **Profile Editing**: Users can update their profile details.  
- **Search Feature** *(Planned)*: Users will be able to search for blog posts.  
- **Styling & UI Enhancements** *(In Progress)*: Implementing a clean and modern design.  
- **Error Handling**: Custom pages for **404 Not Found** and **Unauthorized Access**.  

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
