# Diet Dash 🍽️

**Diet Dash** is a personalized diet planning web application designed to help users achieve their health and fitness goals—whether it's weight loss, muscle gain, or maintaining a balanced lifestyle. The platform provides tailored meal plans based on user preferences (Veg/Non-Veg) and fitness objectives, along with useful tools like a BMI calculator and daily calorie estimator.

---

## 🌟 Features

- 🎯 Goal-Based Diet Plans (Weight Loss, Muscle Gain, Maintenance)
- ⚖️ BMI and Daily Calorie Calculator
- 🥗 Personalized Meals Based on Dietary Preferences (Veg/Non-Veg)
- 📊 Nutritional Breakdown (Calories, Protein, Carbs, Fats)
- 🛠️ Admin Panel to Add, Update, and Manage Meals
- 💻 Clean and Responsive Frontend Interface

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Django (Two separate projects)
  - `Login-Backend/`: Handles user-related features *(optional in this README)*
  - `MainInterface-Backend/`: Manages diet plans and meal logic
- **Database**: MySQL (`dietdash`)

---

## 📁 Project Structure
Diet Dash/

│── Login-Backend/ # (Optional – can be ignored in use)

│── MainInterface-Backend/ # Diet Plan Backend

│ ├── diet/ # Django App for diet logic

│ ├── maininterfacebackend/ # Django Project Config

│── Frontend/ # Frontend Files

│ ├── login/ # Login UI (optional)

│ ├── main_interface/ # Diet Plans UI

│── README.md

---

## 📌 Usage

**1. Clone the repository**  

``` bash
git clone https://github.com/your-username/diet-dash.git
```

**2. Setup Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```


