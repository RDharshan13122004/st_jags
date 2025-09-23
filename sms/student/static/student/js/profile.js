function toggleSection(id) {
  const section = document.getElementById(id);
  section.classList.toggle('show');
}

// Automatically show on load (optional)
window.addEventListener("DOMContentLoaded", () => {
  document.getElementById("personal").classList.add("show");
  document.getElementById("academic").classList.add("show");
});
