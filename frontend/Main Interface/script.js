document.addEventListener("DOMContentLoaded", function () {
  // Initialize AOS
  AOS.init({
    duration: 800,
    easing: 'ease-out-quad',
    once: true
  });

  // Hide Loader
  window.addEventListener("load", function () {
    setTimeout(function() {
      document.body.classList.add('loaded');
    }, 1500);
  });

  // Custom Cursor
  const cursorDot = document.querySelector(".cursor-dot");
  
  document.addEventListener("mousemove", (e) => {
    cursorDot.style.left = `${e.clientX}px`;
    cursorDot.style.top = `${e.clientY}px`;
  });

  const interactiveElements = document.querySelectorAll(
    "a, button, input, select, .btn, .nav-link"
  );

  interactiveElements.forEach((el) => {
    el.addEventListener("mouseenter", () => {
      cursorDot.style.transform = "translate(-50%, -50%) scale(2.5)";
      cursorDot.style.opacity = "0.7";
      cursorDot.style.backgroundColor = "#CDDC39";
    });
    
    el.addEventListener("mouseleave", () => {
      cursorDot.style.transform = "translate(-50%, -50%) scale(1)";
      cursorDot.style.opacity = "1";
      cursorDot.style.backgroundColor = "#4CAF50";
    });
  });

  // Search functionality (UPDATED)
  const goalSelect = document.getElementById("goal-select");
  const searchButton = document.querySelector(".btn-search");

  if (searchButton && goalSelect) {
    searchButton.addEventListener("click", function () {
      const selectedGoal = goalSelect.value;
      if (!selectedGoal) {
        goalSelect.style.animation = "shake 0.5s";
        setTimeout(() => {
          goalSelect.style.animation = "";
        }, 500);
        return;
      }
      fetchDietPlan(selectedGoal);
    });
  } else {
    console.error("Search Button ya Goal Dropdown nahi mila!");
  }

  // Animate leaves on scroll
  const leaves = document.querySelectorAll(".leaf");

  window.addEventListener("scroll", () => {
    const scrollPosition = window.scrollY;
    leaves.forEach((leaf, index) => {
      const speed = index === 0 ? 0.1 : index === 1 ? 0.15 : 0.2;
      leaf.style.transform = `rotate(${15 + index * 15}deg) translateY(${scrollPosition * speed}px)`;
    });
  });
});

async function fetchDietPlan(goal) {
  const searchButton = document.querySelector(".btn-search");
  const originalText = searchButton.innerHTML;
  searchButton.innerHTML = `<i class="fas fa-spinner fa-spin"></i> Finding Meals...`;
  searchButton.disabled = true;

  try {
    // UPDATED: Local Django server URL
    const response = await fetch(`http://127.0.0.1:8000/api/meals/?goal=${encodeURIComponent(goal)}`);

    if (!response.ok) {
      throw new Error('Network response was not ok');
    }

    const data = await response.json();
    displayDietPlan(data);
  } catch (error) {
    console.error('Error fetching meals:', error);
    alert('Failed to fetch meals. Please try again later.');
  } finally {
    searchButton.innerHTML = originalText;
    searchButton.disabled = false;
  }
}

function displayDietPlan(data) {
  const modal = document.createElement("div");
  modal.className = "diet-modal";
  modal.innerHTML = `
    <div class="modal-content">
      <span class="close-modal">&times;</span>
      <h2>Your <span class="highlight">${document.getElementById("goal-select").selectedOptions[0].text}</span> Meal Plan</h2>
      <div class="meals-grid"></div>
    </div>
  `;

  document.body.appendChild(modal);

  const mealsGrid = modal.querySelector(".meals-grid");

  if (!data || data.length === 0) {
    mealsGrid.innerHTML = "<p>No meals found for the selected goal. Please try another option.</p>";
  } else {
    data.forEach(meal => {
      const mealCard = document.createElement("div");
      mealCard.className = "meal-card";
      mealCard.innerHTML = `
        <div class="meal-image" style="background-image: url('${meal.image_url || 'assets/meal-placeholder.jpg'}')"></div>
        <div class="meal-info">
          <h3>${meal.name}</h3>
          <div class="meal-macros">
            <div><i class="fas fa-fire"></i> ${meal.calories} cal</div>
            <div><i class="fas fa-bread-slice"></i> ${meal.carbs}g carbs</div>
            <div><i class="fas fa-dumbbell"></i> ${meal.protein}g protein</div>
            <div><i class="fas fa-oil-can"></i> ${meal.fat}g fat</div>
          </div>
          <div class="meal-type">${meal.type}</div>
        </div>
      `;
      mealsGrid.appendChild(mealCard);
    });
  }

  modal.querySelector(".close-modal").addEventListener("click", () => {
    modal.style.opacity = "0";
    setTimeout(() => {
      document.body.removeChild(modal);
    }, 300);
  });

  setTimeout(() => {
    modal.style.opacity = "1";
  }, 10);
}

function calculateBMI() {
    const height = parseFloat(document.getElementById("height").value) / 100;
    const weight = parseFloat(document.getElementById("weight").value);
    const resultElement = document.getElementById("bmi-result");

    if (!height || !weight || height <= 0 || weight <= 0) {
        resultElement.textContent = "Please enter valid values.";
        return;
    }

    const bmi = weight / (height * height);
    let category = "";

    if (bmi < 18.5) category = "Underweight";
    else if (bmi < 24.9) category = "Normal weight";
    else if (bmi < 29.9) category = "Overweight";
    else category = "Obese";

    resultElement.textContent = `Your BMI is ${bmi.toFixed(2)} (${category})`;
}


function filterMeals(type) {
    const meals = document.querySelectorAll(".meal-card");

    meals.forEach(meal => {
        if (type === "All") {
            meal.style.display = "block";
        } else {
            if (meal.getAttribute("data-type") === type) {
                meal.style.display = "block";
            } else {
                meal.style.display = "none";
            }
        }
    });
}


