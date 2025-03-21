
## 📝 Blogging Application (Django)  

### 📌 About the Project  

This is a **blogging application** built using the **Django framework**. It allows users to **write, categorize, and tag blog posts** while managing their profiles. The platform is designed for a **smooth and user-friendly experience**, making it easy for users to create and share their thoughts.

**Note:** The name of the project is yet to be finalized, so it will temporarily be referred to as "Blogging Application". 

### 📅 Project Timeline  

- **Previous Version Started:** *November 2024* (Paused due to custom user model issues)  
- **Current Version Started:** *February 2025*  
✔ User Authentication (Signup, Login, Logout) Completed  
✔ Blog post creation form (with sub-form for category creation) Completed  
🚀 Next Milestone: Blog detail view and blog interaction features.  

### ⚠️ Why a New Repository?  

A previous version of this project was paused due to **issues faced while implementing a custom user model** in the middle of development. Instead of continuing with a broken setup, this new repository was created to ensure a **well-structured approach, with the custom user model implemented from the start**.  

---

## 🚧 Current Progress  

The following features have been implemented:  

✔ **Custom User Model** – Implemented from the beginning  
✔ **Database Models** – Post, Category, Tag, User  
✔ **User Authentication (Signup, Login, Logout)** – Users must log in to access the home page (`@login_required` enforced).  
✔ **Base Templates** – `main.html`, `navbar.html`, and a structured `home.html` with *sidebar* and *blog feed*  
✔ **Blog Feed** – Displays blog posts on the home page  

✔ **Sidebar Components**:  
- **User Profile Card** – Displays profile picture, username, display name, and number of blogs  
- **Daily Writing Prompt** – Encourages blogging with a writing prompt  
- **Word of the Day** – Placeholder, will fetch words from an API later  
- **Quote of the Day** – Placeholder, will use an API for daily quotes  
- **Followed Categories List** – Placeholder, to be implemented later  

✔ **Blog Post Creation**:  
- Fully functional post-creation form  
- Ability to select existing categories or create a new category via sub-form  
- Multiple tags supported for each blog  

✔ **Profile Management**:  
- **View Profile Page** – Accessible for any user, displaying user details and their blog list  
- **Header Section** – Displays profile picture, username, and account creation date  
- **Role Icon** – Indicates if a user is a staff, admin, or a regular user  
- **Follow/Unfollow Button** – (Placeholder for future implementation)  
- **Edit Profile Feature** – Logged-in users can edit their profile picture, username, display name, email, and bio via a dedicated form  

---

### 🔜 Next Steps  

- **Blog Detail Page** – Allow users to view the full content of a blog post when clicking on “Read More” or the blog title  
- **Enhance Sidebar** –  
  - Fetch daily quotes and word of the day from APIs  
  - Display followed categories (when the following feature is implemented)  
- **Following Feature** – Ability to follow other users and categories  
- **Blog Interaction Features** – Add likes, comments, and sharing options  

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
