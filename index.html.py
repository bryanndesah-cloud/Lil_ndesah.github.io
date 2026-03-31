<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
    <title>NDESANJO FAMILY RECIPIES</title>
    <style>
        * {
            box-sizing: border-box;
            font-family: system-ui, 'Segoe UI', 'Roboto', 'Helvetica Neue', sans-serif;
        }

        body {
            background: #fef7e8;
            margin: 0;
            padding: 20px;
            color: #2c2418;
        }

        .container {
            max-width: 1300px;
            margin: 0 auto;
            background: #fffaf2;
            border-radius: 40px;
            box-shadow: 0 20px 35px rgba(0, 0, 0, 0.05);
            overflow: hidden;
            border: 1px solid #f3e5cd;
        }

        /* Header */
        .header {
            background: #f4a261;
            padding: 1.5rem 2rem;
            text-align: center;
            border-bottom: 3px solid #e76f51;
        }

        .header h1 {
            margin: 0;
            font-size: 2.2rem;
            letter-spacing: 1px;
            color: #2c2418;
            font-weight: 700;
            text-shadow: 2px 2px 0 #f8e3c2;
        }

        .header p {
            margin: 0.5rem 0 0;
            font-size: 1rem;
            color: #2c2418;
            opacity: 0.9;
        }

        /* main layout */
        .main-content {
            display: flex;
            flex-wrap: wrap;
            gap: 2rem;
            padding: 2rem;
        }

        /* form panel */
        .form-panel {
            flex: 1.2;
            min-width: 280px;
            background: #ffffff;
            border-radius: 32px;
            padding: 1.5rem;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
            border: 1px solid #f3e2c9;
        }

        .form-panel h2 {
            margin-top: 0;
            border-left: 6px solid #f4a261;
            padding-left: 1rem;
            font-size: 1.6rem;
            color: #3b2c1f;
        }

        .form-group {
            margin-bottom: 1.2rem;
        }

        label {
            display: block;
            font-weight: 600;
            margin-bottom: 0.4rem;
            color: #5a3e2b;
        }

        input, textarea, select {
            width: 100%;
            padding: 0.75rem 1rem;
            border: 1px solid #e9dacb;
            border-radius: 28px;
            font-size: 0.95rem;
            background: #fefcf9;
            transition: all 0.2s;
        }

        input:focus, textarea:focus {
            outline: none;
            border-color: #f4a261;
            box-shadow: 0 0 0 3px rgba(244, 162, 97, 0.2);
        }

        textarea {
            border-radius: 24px;
            resize: vertical;
        }

        button {
            background: #f4a261;
            border: none;
            color: #2c2418;
            font-weight: bold;
            padding: 0.7rem 1.4rem;
            border-radius: 40px;
            cursor: pointer;
            font-size: 0.9rem;
            transition: 0.2s;
            margin-right: 0.5rem;
            margin-bottom: 0.5rem;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05);
        }

        button.primary {
            background: #e76f51;
            color: white;
        }

        button.secondary {
            background: #d4a373;
            color: white;
        }

        button.danger {
            background: #bc6c25;
            color: white;
        }

        button:hover {
            transform: translateY(-2px);
            filter: brightness(0.96);
        }

        /* search & list panel */
        .list-panel {
            flex: 2;
            min-width: 320px;
        }

        .search-section {
            background: #ffffff;
            border-radius: 32px;
            padding: 1.2rem 1.5rem;
            margin-bottom: 1.8rem;
            border: 1px solid #f3e2c9;
        }

        .search-row {
            display: flex;
            flex-wrap: wrap;
            gap: 0.8rem;
            align-items: flex-end;
        }

        .search-field {
            flex: 1;
            min-width: 140px;
        }

        .recipe-list {
            background: #ffffff;
            border-radius: 32px;
            padding: 1.2rem;
            border: 1px solid #f3e2c9;
            max-height: 550px;
            overflow-y: auto;
        }

        .recipe-card {
            background: #fef9ef;
            border-radius: 24px;
            padding: 1rem 1.2rem;
            margin-bottom: 0.8rem;
            transition: 0.1s;
            border: 1px solid #f4e2ce;
            cursor: pointer;
        }

        .recipe-card:hover {
            background: #fff3e4;
            border-color: #f4a261;
        }

        .recipe-title {
            font-weight: 800;
            font-size: 1.2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 8px;
        }

        .recipe-category {
            background: #e9dacb;
            padding: 0.2rem 0.7rem;
            border-radius: 50px;
            font-size: 0.7rem;
            font-weight: normal;
            color: #5a3e2b;
        }

        .recipe-actions {
            margin-top: 8px;
            display: flex;
            gap: 8px;
        }

        .recipe-actions button {
            padding: 0.3rem 1rem;
            font-size: 0.75rem;
            margin: 0;
        }

        .empty-message {
            text-align: center;
            color: #b68b5c;
            padding: 2rem;
            font-style: italic;
        }

        /* modal for details */
        .modal {
            display: none;
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background-color: rgba(0,0,0,0.6);
            align-items: center;
            justify-content: center;
            z-index: 1000;
        }

        .modal-content {
            background: #fffaf2;
            max-width: 600px;
            width: 90%;
            border-radius: 40px;
            padding: 1.8rem;
            max-height: 85vh;
            overflow-y: auto;
            border: 1px solid #f4a261;
            position: relative;
        }

        .modal-header {
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            border-bottom: 2px dashed #f4a261;
            padding-bottom: 0.5rem;
            margin-bottom: 1rem;
        }

        .close-modal {
            font-size: 1.8rem;
            cursor: pointer;
            font-weight: bold;
        }

        .ingredient-badge {
            background: #f2e5d4;
            display: inline-block;
            padding: 0.3rem 0.9rem;
            border-radius: 40px;
            margin: 0.2rem 0.4rem 0.2rem 0;
            font-size: 0.85rem;
        }

        hr {
            border: none;
            border-top: 1px solid #f0e0cc;
        }

        footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.8rem;
            color: #b68b5c;
            border-top: 1px solid #f3e5cd;
            background: #fefaf4;
        }

        @media (max-width: 780px) {
            .main-content {
                flex-direction: column;
            }
        }
    </style>
</head>
<body>
<div class="container">
    <div class="header">
        <h1>🍲 NDESANJO FAMILY RECIPIES</h1>
        <p>Preserving generations of taste • Cook with love</p>
    </div>

    <div class="main-content">
        <!-- LEFT: Add/Edit Recipe Form -->
        <div class="form-panel">
            <h2 id="formTitle">📖 Add New Recipe</h2>
            <form id="recipeForm">
                <div class="form-group">
                    <label>🍛 Recipe name *</label>
                    <input type="text" id="recipeName" placeholder="e.g., Granny's Jollof Rice" required>
                </div>
                <div class="form-group">
                    <label>📂 Category (optional)</label>
                    <input type="text" id="recipeCategory" placeholder="e.g., Dinner, Dessert, Soup">
                </div>
                <div class="form-group">
                    <label>🥕 Ingredients (one per line)</label>
                    <textarea id="recipeIngredients" rows="4" placeholder="2 cups rice&#10;1 onion&#10;2 tbsp oil"></textarea>
                </div>
                <div class="form-group">
                    <label>📝 Instructions</label>
                    <textarea id="recipeInstructions" rows="5" placeholder="Step by step..."></textarea>
                </div>
                <div style="display: flex; flex-wrap: wrap; gap: 10px; margin-top: 10px;">
                    <button type="submit" class="primary" id="submitBtn">➕ Add Recipe</button>
                    <button type="button" id="cancelEditBtn" style="background: #cdb28b;">✖ Cancel Edit</button>
                </div>
                <input type="hidden" id="editId" value="">
            </form>
        </div>

        <!-- RIGHT: Search and List -->
        <div class="list-panel">
            <div class="search-section">
                <div class="search-row">
                    <div class="search-field">
                        <label>🔍 Search by name</label>
                        <input type="text" id="searchNameInput" placeholder="pasta, cake...">
                    </div>
                    <div class="search-field">
                        <label>🥄 Search by ingredient</label>
                        <input type="text" id="searchIngredientInput" placeholder="cheese, tomato...">
                    </div>
                    <div>
                        <button id="searchNameBtn" class="secondary">Search Name</button>
                        <button id="searchIngredientBtn" class="secondary">Search Ingredient</button>
                        <button id="clearSearchBtn">Show All</button>
                    </div>
                </div>
            </div>

            <div class="recipe-list" id="recipeListContainer">
                <!-- dynamic recipe cards appear here -->
                <div class="empty-message">✨ Loading family recipes...</div>
            </div>
        </div>
    </div>
    <footer>NDESANJO family secret kitchen • Recipes stored in your browser</footer>
</div>

<!-- Modal for viewing details -->
<div id="recipeModal" class="modal">
    <div class="modal-content">
        <div class="modal-header">
            <h2 id="modalTitle">Recipe Details</h2>
            <span class="close-modal">&times;</span>
        </div>
        <div id="modalBody">
            <p><strong>Category:</strong> <span id="modalCategory"></span></p>
            <p><strong>🥣 Ingredients:</strong></p>
            <div id="modalIngredients"></div>
            <p><strong>👩‍🍳 Instructions:</strong></p>
            <p id="modalInstructions" style="white-space: pre-line;"></p>
        </div>
        <hr>
        <button id="editFromModalBtn" class="secondary">✏️ Edit this recipe</button>
    </div>
</div>

<script>
    // ---------- STORAGE KEY ----------
    const STORAGE_KEY = "ndesanjoFamilyRecipes";

    // ---------- Sample initial recipes ----------
    const defaultRecipes = [
        {
            id: Date.now() + 1,
            name: "Mama’s Chicken Curry",
            category: "Main Course",
            ingredients: ["500g chicken thighs", "2 onions", "3 garlic cloves", "1 tbsp curry powder", "400ml coconut milk", "Salt & pepper"],
            instructions: "1. Brown chicken in oil.\n2. Sauté onions, garlic and curry powder.\n3. Add coconut milk and chicken, simmer 25 min.\n4. Serve with rice."
        },
        {
            id: Date.now() + 2,
            name: "Auntie’s Banana Bread",
            category: "Dessert",
            ingredients: ["3 ripe bananas", "1/2 cup butter", "1 cup sugar", "2 eggs", "1 tsp baking soda", "1.5 cups flour"],
            instructions: "Mash bananas, cream butter & sugar, add eggs, then dry ingredients. Bake at 175°C for 55 min."
        },
        {
            id: Date.now() + 3,
            name: "Ndongo Vegetable Stew",
            category: "Vegan",
            ingredients: ["Spinach", "Eggplant", "Tomatoes", "Onion", "Peanut butter", "Vegetable broth"],
            instructions: "Sauté onions and tomatoes, add vegetables and broth, stir in peanut butter. Simmer 20 min."
        }
    ];

    // Global state
    let recipes = [];
    let currentSearchMode = "all"; // "all", "name", "ingredient"
    let searchKeyword = "";

    // DOM elements
    const recipeForm = document.getElementById("recipeForm");
    const recipeNameInput = document.getElementById("recipeName");
    const recipeCategoryInput = document.getElementById("recipeCategory");
    const recipeIngredientsInput = document.getElementById("recipeIngredients");
    const recipeInstructionsInput = document.getElementById("recipeInstructions");
    const editIdInput = document.getElementById("editId");
    const submitBtn = document.getElementById("submitBtn");
    const cancelEditBtn = document.getElementById("cancelEditBtn");
    const formTitle = document.getElementById("formTitle");
    const recipeListContainer = document.getElementById("recipeListContainer");
    const searchNameInput = document.getElementById("searchNameInput");
    const searchIngredientInput = document.getElementById("searchIngredientInput");
    const searchNameBtn = document.getElementById("searchNameBtn");
    const searchIngredientBtn = document.getElementById("searchIngredientBtn");
    const clearSearchBtn = document.getElementById("clearSearchBtn");

    // Modal elements
    const modal = document.getElementById("recipeModal");
    const modalTitleSpan = document.getElementById("modalTitle");
    const modalCategorySpan = document.getElementById("modalCategory");
    const modalIngredientsDiv = document.getElementById("modalIngredients");
    const modalInstructionsP = document.getElementById("modalInstructions");
    const closeModalSpan = document.querySelector(".close-modal");
    const editFromModalBtn = document.getElementById("editFromModalBtn");

    let currentModalRecipeId = null;

    // Helper: Load from localStorage
    function loadRecipes() {
        const stored = localStorage.getItem(STORAGE_KEY);
        if (stored) {
            recipes = JSON.parse(stored);
        } else {
            recipes = defaultRecipes;
            saveRecipes();
        }
    }

    function saveRecipes() {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(recipes));
    }

    // Generate new ID
    function generateId() {
        return Date.now() + Math.floor(Math.random() * 10000);
    }

    // Reset form to "Add mode"
    function resetForm() {
        recipeForm.reset();
        editIdInput.value = "";
        submitBtn.textContent = "➕ Add Recipe";
        formTitle.innerHTML = "📖 Add New Recipe";
        recipeNameInput.value = "";
        recipeCategoryInput.value = "";
        recipeIngredientsInput.value = "";
        recipeInstructionsInput.value = "";
        currentModalRecipeId = null;
    }

    // Fill form with recipe data for editing
    function editRecipeById(id) {
        const recipe = recipes.find(r => r.id == id);
        if (!recipe) return;
        recipeNameInput.value = recipe.name;
        recipeCategoryInput.value = recipe.category || "";
        recipeIngredientsInput.value = recipe.ingredients.join("\n");
        recipeInstructionsInput.value = recipe.instructions;
        editIdInput.value = recipe.id;
        submitBtn.textContent = "✏️ Update Recipe";
        formTitle.innerHTML = "✏️ Edit Recipe";
        // scroll to form
        document.querySelector(".form-panel").scrollIntoView({ behavior: "smooth" });
    }

    // Add or update recipe
    function handleSubmit(e) {
        e.preventDefault();
        const name = recipeNameInput.value.trim();
        if (!name) {
            alert("Recipe name is required!");
            return;
        }
        const category = recipeCategoryInput.value.trim();
        const ingredientsRaw = recipeIngredientsInput.value;
        let ingredients = ingredientsRaw.split(/\r?\n/).filter(line => line.trim().length > 0);
        if (ingredients.length === 0) ingredients = ["No ingredients listed"];
        const instructions = recipeInstructionsInput.value.trim() || "No instructions provided.";

        const editId = editIdInput.value;
        if (editId) {
            // update existing
            const index = recipes.findIndex(r => r.id == editId);
            if (index !== -1) {
                recipes[index] = {
                    ...recipes[index],
                    name: name,
                    category: category,
                    ingredients: ingredients,
                    instructions: instructions
                };
                saveRecipes();
                resetForm();
                renderRecipeList();
                alert("Recipe updated!");
            }
        } else {
            // add new
            const newRecipe = {
                id: generateId(),
                name: name,
                category: category,
                ingredients: ingredients,
                instructions: instructions
            };
            recipes.push(newRecipe);
            saveRecipes();
            resetForm();
            renderRecipeList();
            alert("New recipe added!");
        }
    }

    // Delete recipe
    function deleteRecipe(id) {
        if (confirm("Delete this family recipe forever?")) {
            recipes = recipes.filter(r => r.id != id);
            saveRecipes();
            if (currentModalRecipeId == id) closeModal();
            renderRecipeList();
        }
    }

    // Show details modal
    function showRecipeDetails(id) {
        const recipe = recipes.find(r => r.id == id);
        if (!recipe) return;
        currentModalRecipeId = recipe.id;
        modalTitleSpan.textContent = recipe.name;
        modalCategorySpan.textContent = recipe.category || "Uncategorized";
        // ingredients
        modalIngredientsDiv.innerHTML = "";
        recipe.ingredients.forEach(ing => {
            const span = document.createElement("span");
            span.className = "ingredient-badge";
            span.textContent = ing;
            modalIngredientsDiv.appendChild(span);
        });
        modalInstructionsP.textContent = recipe.instructions;
        modal.style.display = "flex";
    }

    function closeModal() {
        modal.style.display = "none";
        currentModalRecipeId = null;
    }

    // Render list based on search filters
    function renderRecipeList() {
        let filteredRecipes = [...recipes];
        if (currentSearchMode === "name" && searchKeyword.trim() !== "") {
            const kw = searchKeyword.toLowerCase();
            filteredRecipes = filteredRecipes.filter(r => r.name.toLowerCase().includes(kw));
        } else if (currentSearchMode === "ingredient" && searchKeyword.trim() !== "") {
            const kw = searchKeyword.toLowerCase();
            filteredRecipes = filteredRecipes.filter(r => 
                r.ingredients.some(ing => ing.toLowerCase().includes(kw))
            );
        }

        if (filteredRecipes.length === 0) {
            recipeListContainer.innerHTML = `<div class="empty-message">🍽️ No recipes match your search.<br>Try adding a new family favorite!</div>`;
            return;
        }

        recipeListContainer.innerHTML = "";
        filteredRecipes.forEach(recipe => {
            const card = document.createElement("div");
            card.className = "recipe-card";
            card.innerHTML = `
                <div class="recipe-title">
                    <span>🍲 ${escapeHtml(recipe.name)}</span>
                    <span class="recipe-category">${escapeHtml(recipe.category || "any")}</span>
                </div>
                <div class="recipe-actions">
                    <button class="view-btn" data-id="${recipe.id}">👀 View</button>
                    <button class="edit-btn" data-id="${recipe.id}">✏️ Edit</button>
                    <button class="delete-btn danger" data-id="${recipe.id}">🗑 Delete</button>
                </div>
            `;
            recipeListContainer.appendChild(card);
        });

        // attach event listeners for dynamic buttons
        document.querySelectorAll(".view-btn").forEach(btn => {
            btn.addEventListener("click", (e) => {
                e.stopPropagation();
                const id = parseInt(btn.dataset.id);
                showRecipeDetails(id);
            });
        });
        document.querySelectorAll(".edit-btn").forEach(btn => {
            btn.addEventListener("click", (e) => {
                e.stopPropagation();
                const id = parseInt(btn.dataset.id);
                editRecipeById(id);
            });
        });
        document.querySelectorAll(".delete-btn").forEach(btn => {
            btn.addEventListener("click", (e) => {
                e.stopPropagation();
                const id = parseInt(btn.dataset.id);
                deleteRecipe(id);
            });
        });
    }

    // simple escape for safety
    function escapeHtml(str) {
        if (!str) return "";
        return str.replace(/[&<>]/g, function(m) {
            if (m === '&') return '&amp;';
            if (m === '<') return '&lt;';
            if (m === '>') return '&gt;';
            return m;
        }).replace(/[\uD800-\uDBFF][\uDC00-\uDFFF]/g, function(c) {
            return c;
        });
    }

    // Search handlers
    function searchByName() {
        const keyword = searchNameInput.value.trim();
        if (keyword === "") {
            alert("Enter a name keyword to search.");
            return;
        }
        currentSearchMode = "name";
        searchKeyword = keyword;
        renderRecipeList();
    }

    function searchByIngredient() {
        const keyword = searchIngredientInput.value.trim();
        if (keyword === "") {
            alert("Enter an ingredient to search.");
            return;
        }
        currentSearchMode = "ingredient";
        searchKeyword = keyword;
        renderRecipeList();
    }

    function clearSearch() {
        searchNameInput.value = "";
        searchIngredientInput.value = "";
        currentSearchMode = "all";
        searchKeyword = "";
        renderRecipeList();
    }

    // Cancel edit
    function cancelEdit() {
        resetForm();
    }

    // Modal edit button - close modal then open edit form for that recipe
    function editFromModal() {
        if (currentModalRecipeId) {
            closeModal();
            editRecipeById(currentModalRecipeId);
        }
    }

    // Event listeners
    recipeForm.addEventListener("submit", handleSubmit);
    cancelEditBtn.addEventListener("click", cancelEdit);
    searchNameBtn.addEventListener("click", searchByName);
    searchIngredientBtn.addEventListener("click", searchByIngredient);
    clearSearchBtn.addEventListener("click", clearSearch);
    closeModalSpan.addEventListener("click", closeModal);
    editFromModalBtn.addEventListener("click", editFromModal);
    window.addEventListener("click", (e) => {
        if (e.target === modal) closeModal();
    });

    // initial load
    loadRecipes();
    renderRecipeList();
    resetForm();
</script>
</body>
</html>