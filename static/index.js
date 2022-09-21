const btn = document.getElementById('btn');

btn.addEventListener('click', function onClick(event) {
  // 👇️ change background color
  event.target.style.backgroundColor = 'yellow';

  // 👇️ optionally change text color
  event.target.style.color = 'blue';
});
