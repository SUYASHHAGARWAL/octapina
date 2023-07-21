const modal = document.getElementById('profile-modal');
const profileLink = document.getElementById('profile-link');
const closeButton = document.getElementsByClassName('close')[0];
const id = document.getElementById('profilebtn')
id.addEventListener('click', function(event) {
  event.preventDefault(); 
  modal.style.display = 'block';
});
profileLink.addEventListener('click', function(event) {
  event.preventDefault(); 
  modal.style.display = 'block';
});

closeButton.addEventListener('click', function() {
  modal.style.display = 'none';
});

window.addEventListener('click', function(event) {
  if (event.target === modal) {
    modal.style.display = 'none';
  }
});
