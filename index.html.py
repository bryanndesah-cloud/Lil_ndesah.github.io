<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NDESANJO FAMILY RECIPES</title>

    <style>
        * {
            box-sizing: border-box;
            font-family: system-ui, 'Segoe UI', 'Roboto', sans-serif;
        }

        body {
            background: #fef7e8;
            margin: 0;
            padding: 20px;
            color: #2c2418;
        }

        .container {
            max-width: 1300px;
            margin: auto;
            background: #fffaf2;
            border-radius: 40px;
            overflow: hidden;
            border: 1px solid #f3e5cd;
        }

        .header {
            background: #f4a261;
            padding: 20px;
            text-align: center;
        }

        .main-content {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            padding: 20px;
        }

        .form-panel, .list-panel {
            flex: 1;
            min-width: 300px;
        }

        input, textarea {
            width: 100%;
            padding: 10px;
            margin: 8px 0;
            border-radius: 10px;
            border: 1px solid #ccc;
        }

        button {
            padding: 10px;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            background: #e76f51;
            color: white;
        }

        .recipe-card {
            background: #fff3e4;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
        }

        .modal {
            display: none;
            position: fixed;
            top:0; left:0;
            width:100%; height:100%;
            background: rgba(0,0,0,0.6);
            justify-content: center;
            align-items: center;
        }

        .modal-content {
            background: white;
            padding: 20px;
            border-radius: 20px;
            max-width: 500px;
            width: 90%;
        }
    </style>
</head>

<body>

<div class="container">
    <div class="header">
        <h1>🍲 NDESANJO FAMILY RECIPES</h1>
    </div>

    <div class="main-content">

        <!-- FORM -->
        <div class="form-panel">
            <h2 id="formTitle">Add Recipe</h2>

            <input type="text" id="recipeName" placeholder="Recipe name">
            <input type="text" id="recipeCategory" placeholder="Category">
            <textarea id="recipeIngredients" placeholder="Ingredients (one per line)"></textarea>
            <textarea id="recipeInstructions" placeholder="Instructions"></textarea>

            <button onclick="saveRecipe()">Save</button>
        </div>

        <!-- LIST -->
        <div class="list-panel">
            <h2>Recipes</h2>

            <input type="text" id="searchInput" placeholder="Search...">
            <button onclick="search()">Search</button>
            <button onclick="showAll()">Show All</button>

            <div id="recipeList"></div>
        </div>

    </div>
</div>

<!-- MODAL -->
<div id="modal" class="modal">
    <div class="modal-content">
        <h2 id="modalTitle"></h2>
        <p id="modalCategory"></p>
        <p id="modalIngredients"></p>
        <p id="modalInstructions"></p>
        <button onclick="closeModal()">Close</button>
    </div>
</div>

<script>
let recipes = JSON.parse(localStorage.getItem("recipes")) || [];
let editIndex = null;

function saveStorage() {
    localStorage.setItem("recipes", JSON.stringify(recipes));
}

function render(list = recipes) {
    const container = document.getElementById("recipeList");
    container.innerHTML = "";

    list.forEach((r, i) => {
        container.innerHTML += `
            <div class="recipe-card">
                <h3>${r.name}</h3>
                <button onclick="view(${i})">View</button>
                <button onclick="edit(${i})">Edit</button>
                <button onclick="removeRecipe(${i})">Delete</button>
            </div>
        `;
    });
}

function saveRecipe() {
    const name = document.getElementById("recipeName").value;
    const category = document.getElementById("recipeCategory").value;
    const ingredients = document.getElementById("recipeIngredients").value.split("\n");
    const instructions = document.getElementById("recipeInstructions").value;

    if (!name) return alert("Enter name");

    const recipe = { name, category, ingredients, instructions };

    if (editIndex !== null) {
        recipes[editIndex] = recipe;
        editIndex = null;
    } else {
        recipes.push(recipe);
    }

    saveStorage();
    render();
}

function removeRecipe(i) {
    recipes.splice(i,1);
    saveStorage();
    render();
}

function view(i) {
    const r = recipes[i];

    document.getElementById("modalTitle").innerText = r.name;
    document.getElementById("modalCategory").innerText = r.category;
    document.getElementById("modalIngredients").innerHTML = r.ingredients.join("<br>");
    document.getElementById("modalInstructions").innerText = r.instructions;

    document.getElementById("modal").style.display = "flex";
}

function closeModal() {
    document.getElementById("modal").style.display = "none";
}

function edit(i) {
    const r = recipes[i];

    document.getElementById("recipeName").value = r.name;
    document.getElementById("recipeCategory").value = r.category;
    document.getElementById("recipeIngredients").value = r.ingredients.join("\n");
    document.getElementById("recipeInstructions").value = r.instructions;

    editIndex = i;
}

function search() {
    const q = document.getElementById("searchInput").value.toLowerCase();

    const filtered = recipes.filter(r =>
        r.name.toLowerCase().includes(q) ||
        r.ingredients.join(" ").toLowerCase().includes(q)
    );

    render(filtered);
}

function showAll() {
    render();
}

render();
</script>

</body>
</html>
