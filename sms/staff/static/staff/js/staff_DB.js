const staffMenuBtn = document.getElementById('staffMenuBtn');
const staffSidebar = document.getElementById('staffSidebar');
const staffCloseSidebar = document.getElementById('staffCloseSidebar');

// Toggle sidebar
staffMenuBtn.addEventListener('click', () => {
    staffSidebar.classList.toggle('show');
});

// Close sidebar
staffCloseSidebar.addEventListener('click', (e) => {
    e.preventDefault();
    staffSidebar.classList.remove('show');
});

// Close on outside click
window.addEventListener('click', (e) => {
    if (!staffSidebar.contains(e.target) && !staffMenuBtn.contains(e.target)) {
        staffSidebar.classList.remove('show');
    }
});

// Simple auto-highlighting cards for fun
const staffCards = document.querySelectorAll('.staff-card');

setInterval(() => {
    staffCards.forEach(card => card.classList.remove('highlight'));
    const randomCard = staffCards[Math.floor(Math.random() * staffCards.length)];
    randomCard.classList.add('highlight');
}, 3000);

//student record
document.getElementById('searchInput').addEventListener('keyup', function () {
  const filter = this.value.toLowerCase();
  const rows = document.querySelectorAll('#studentTableBody tr');

  rows.forEach(row => {
    const text = row.innerText.toLowerCase();
    row.style.display = text.includes(filter) ? '' : 'none';
  });
});

// attendance entry

function showAttendanceForm(formId) {
  // Hide all forms first
  document.querySelectorAll('.attendance-form').forEach(form => {
    form.style.display = 'none';
  });

  // Show the selected form
  document.getElementById(formId).style.display = 'block';
}
