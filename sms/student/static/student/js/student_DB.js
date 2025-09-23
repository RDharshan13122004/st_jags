// Show current date and time
function updateDateTime() {
    const now = new Date();
    const dateTimeElement = document.getElementById('dateTime');
    dateTimeElement.innerHTML = now.toLocaleString();
}
setInterval(updateDateTime, 1000);
updateDateTime();

const hamburger = document.getElementById('hamburger');
const sidebar = document.getElementById('sidebar');
const closeSidebar = document.getElementById('closeSidebar');

// Open sidebar
hamburger.addEventListener('click', () => {
    sidebar.classList.toggle('show');
});

// Close sidebar
closeSidebar.addEventListener('click', (e) => {
    e.preventDefault();
    sidebar.classList.remove('show');
});

// Optional: Close sidebar on outside click
window.addEventListener('click', (e) => {
    if (!sidebar.contains(e.target) && !hamburger.contains(e.target)) {
        sidebar.classList.remove('show');
    }
});

// attendance info toggle

document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector(".attendance-form");
  const views = {
    table: document.getElementById("table-view"),
    time: document.getElementById("time-view"),
    pie: document.getElementById("pie-view"),
    plot: document.getElementById("plot-view"),
  };

  // Hide all views initially
  Object.values(views).forEach(v => v.style.display = "none");

  form.addEventListener("submit", function (e) {
    e.preventDefault(); // Prevent form from reloading the page

    // Hide all views first
    Object.values(views).forEach(v => {
      v.style.display = "none";
      v.classList.remove("fade-in");
    });

    // Get all selected checkboxes
    const checked = document.querySelectorAll('input[name="view"]:checked');
    checked.forEach((box) => {
      const viewId = box.value + "-view";
      const viewElement = document.getElementById(viewId);
      if (viewElement) {
        viewElement.style.display = "block";
        setTimeout(() => viewElement.classList.add("fade-in"), 10);
      }
    });
  });
});

// results 

document.addEventListener("DOMContentLoaded", function () {
    const radios = document.querySelectorAll(".semester-selection input[type='radio']");
    radios.forEach(radio => {
        radio.addEventListener("change", function () {
            this.closest("form").submit(); // auto submit form
        });
    });
});
