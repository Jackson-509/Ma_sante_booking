document.addEventListener('DOMContentLoaded', () => {
  const buttons = document.querySelectorAll('.slot-btn');
  const formContainer = document.getElementById('form-container');
  const inputDate = document.getElementById('rdv-date');
  const inputHeure = document.getElementById('rdv-heure');

  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      const date = btn.dataset.date;
      const heure = btn.dataset.heure;

      inputDate.value = date;
      inputHeure.value = heure;

      formContainer.style.display = 'block';
      formContainer.scrollIntoView({ behavior: 'smooth' });
    });
  });
});