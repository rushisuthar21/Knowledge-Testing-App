# Django Quiz App 📝

A multi-user **web application** built with **Django** and **Python** to test users' knowledge on a specific topic, track performance, and provide meaningful feedback.

---

## **Project Objective**
The goal of this project is to create an interactive and robust quiz platform where users can:  

- Test their knowledge through dynamic quizzes.  
- Track their progress over time.  
- Retake quizzes to improve their scores.  

---

## **Key Features**

### 1. User Account & Authentication 🔐
- Users must **register** or **log in** to take quizzes.  
- User accounts allow **personalized score tracking**.

### 2. Dynamic Quiz Generation 🎯
- Database contains **20+ pre-defined questions** on a chosen topic.  
- Each quiz randomly selects **5 questions** for each session.

### 3. Question Format ❓
- Each question has **4 possible answers**, with **1 correct answer**.  
- Ensures clarity and consistency across quizzes.

### 4. Instant Scoring & Feedback 🏆
- Users receive:  
  - **Score out of 5**  
  - **Percentage score** (0%–100%)  
  - **Performance message** based on the score:  
    - 0–2 correct: *“Please try again!”*  
    - 3–4 correct: *“Good effort!”*  
    - 5 correct: *“You are a genius!”*

### 5. Retake Option 🔄
- Users scoring **less than 50%** can **retake the quiz**.

### 6. Performance Tracking & Analytics 📊
- Users can **view all past quiz scores**.  
- Displays **average, highest, and lowest scores** across all quizzes.

### 7. Relevant & Meaningful Questions ✅
- Questions are **carefully curated** to maintain **topic coherence**.  
- Promotes an effective learning experience.

---

## **Technology Stack**

- **Backend:** Python, Django  
- **Database:** SQLite (or any relational database)  
- **Frontend:** HTML, CSS, JavaScript  
- **Authentication:** Django’s built-in authentication system  

---

## **Usage**
1. Clone the repository  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
