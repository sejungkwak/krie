// DOM elements
const btnPosts = document.getElementById('btnPosts')
const btnComments = document.getElementById('btnComments')
const btnAbout = document.getElementById('btnAbout')
const profilePosts = document.getElementById('profilePosts')
const profileComments = document.getElementById('profileComments')
const profileAbout = document.getElementById('profileAbout')

// Profile page button event listeners
btnPosts.addEventListener('click', () => {
    profilePosts.classList.add('active');
    profileComments.classList.remove('active');
    profileAbout.classList.remove('active');
})
btnComments.addEventListener('click', () => {
    profileComments.classList.add('active');
    profilePosts.classList.remove('active');
    profileAbout.classList.remove('active');
})
btnAbout.addEventListener('click', () => {
    profileAbout.classList.add('active');
    profilePosts.classList.remove('active');
    profileComments.classList.remove('active');
})