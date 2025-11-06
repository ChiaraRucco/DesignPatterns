// JavaScript logic for the interactive demo
class MetadataRow {
  constructor(source, table, ingestionType, transformation) {
    this.source = source || "";
    this.table = table || "";
    this.ingestionType = ingestionType || "full";
    this.transformation = transformation || "";
  }
}

const metadataTable = [
  new MetadataRow("Source A", "Table A", "full", "Transform A"),
  new MetadataRow("Source B", "Table B", "incremental", "Transform B"),
];

function renderTable() {
  const table = document.createElement("table");
  table.style.width = "100%";
  table.style.borderCollapse = "collapse";
  table.innerHTML = `
    <thead>
      <tr>
        <th style='border: 1px solid #ddd; padding: 8px;'>Source</th>
        <th style='border: 1px solid #ddd; padding: 8px;'>Table</th>
        <th style='border: 1px solid #ddd; padding: 8px;'>Ingestion Type</th>
        <th style='border: 1px solid #ddd; padding: 8px;'>Transformation</th>
        <th style='border: 1px solid #ddd; padding: 8px;'>Actions</th>
      </tr>
    </thead>
    <tbody>
      ${metadataTable
        .map(
          (row, index) => `
            <tr>
              <td style='border: 1px solid #ddd; padding: 8px;'>${row.source}</td>
              <td style='border: 1px solid #ddd; padding: 8px;'>${row.table}</td>
              <td style='border: 1px solid #ddd; padding: 8px;'>${row.ingestionType}</td>
              <td style='border: 1px solid #ddd; padding: 8px;'>${row.transformation}</td>
              <td style='border: 1px solid #ddd; padding: 8px;'>
                <button onclick="simulateRow(${index})" style='padding: 5px 10px; background-color: #4caf50; color: white; border: none; border-radius: 5px; cursor: pointer;'>Simulate</button>
                <button onclick="deleteRow(${index})" style='padding: 5px 10px; background-color: #f44336; color: white; border: none; border-radius: 5px; cursor: pointer;'>Delete</button>
              </td>
            </tr>
          `
        )
        .join("")}
    </tbody>
  `;
  return table;
}

function simulateRow(index) {
  const row = metadataTable[index];
  const modal = document.getElementById("simulation-modal");
  const overlay = document.getElementById("modal-overlay");
  const details = document.getElementById("simulation-details");
  const progressBar = document.getElementById("loading-progress");

  details.textContent = `Simulating ingestion for Source: ${row.source}, Table: ${row.table}, Type: ${row.ingestionType}, Transformation: ${row.transformation}`;
  modal.style.display = "block";
  overlay.style.display = "block";

  let progress = 0;
  progressBar.style.width = "0%";
  const interval = setInterval(() => {
    progress += 10;
    progressBar.style.width = `${progress}%`;
    if (progress >= 100) {
      clearInterval(interval);
    }
  }, 300);
}

function closeSimulationModal() {
  const modal = document.getElementById("simulation-modal");
  const overlay = document.getElementById("modal-overlay");
  modal.style.display = "none";
  overlay.style.display = "none";
}

function deleteRow(index) {
  metadataTable.splice(index, 1);
  updateDemo();
}

function addRow() {
  metadataTable.push(new MetadataRow());
  updateDemo();
}

function updateDemo() {
  const container = document.getElementById("mind-orchestrator");
  container.innerHTML = "";
  container.appendChild(renderTable());
  const addButton = document.createElement("button");
  addButton.textContent = "Add Row";
  addButton.style.padding = "10px 20px";
  addButton.style.backgroundColor = "#2196f3";
  addButton.style.color = "white";
  addButton.style.border = "none";
  addButton.style.borderRadius = "5px";
  addButton.style.cursor = "pointer";
  addButton.onclick = addRow;
  container.appendChild(addButton);
}

document.addEventListener("DOMContentLoaded", () => {
  const orchestrator = document.getElementById("mind-orchestrator");
  if (orchestrator) {
    updateDemo();
  }

  const addRowButton = document.getElementById("add-row");
  if (addRowButton) {
    addRowButton.addEventListener("click", addRow);
  }
});