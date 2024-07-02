const rawMaterialTable = document.getElementById("rawMaterialTable");
const addBtn = document.getElementById("addBtn");

let rawMaterials = [];

addBtn.addEventListener("click", () => {
  const name = prompt("Enter the name of the raw material:");
  const quantity = prompt("Enter the quantity of the raw material:");
  const unit = prompt("Enter the unit of the raw material:");

  // if (name || quantity || unit) {
  //   alert("All fields are required. Please fill in all the details.");
  //   return;
  // }

  // const rawMaterial = {
  //   id: rawMaterials.length + 1,
  //   name: name || "",
  //   quantity: quantity || "",
  //   unit: unit || "",
  // };

  // Check if all fields are empty
  if (!name && !quantity && !unit) {
    alert("At least one field is required. Please fill in at least one detail.");
    return;
  }

  // Create the raw material object with provided details
  const rawMaterial = {
    id: rawMaterials.length + 1,
    name: name || "N/A", // Default to "N/A" if no name is provided
    quantity: quantity || "N/A", // Default to "N/A" if no quantity is provided
    unit: unit || "N/A", // Default to "N/A" if no unit is provided
  };

  
  rawMaterials.push(rawMaterial);

  addRowToTable(rawMaterial);
});

function addRowToTable(rawMaterial) {
  const tbody = rawMaterialTable.getElementsByTagName("tbody")[0];
  const row = tbody.insertRow();

  const nameCell = row.insertCell();
  nameCell.textContent = rawMaterial.name;

  const quantityCell = row.insertCell();
  quantityCell.textContent = rawMaterial.quantity;

  const unitCell = row.insertCell();
  unitCell.textContent = rawMaterial.unit;

  const actionsCell = row.insertCell();

  const deleteBtn = document.createElement("button");
  deleteBtn.textContent = "Delete";
  deleteBtn.className = "bg-red-500 hover:bg-red-600 text-white font-bold py-1 px-2 rounded"; // Tailwind CSS classes for styling
  deleteBtn.addEventListener("click", () => {
    deleteRowFromTable(row);
    rawMaterials = rawMaterials.filter((rm) => rm.id !== rawMaterial.id);
  });

  actionsCell.appendChild(deleteBtn);
}

function deleteRowFromTable(row) {
  row.parentNode.removeChild(row);
}

