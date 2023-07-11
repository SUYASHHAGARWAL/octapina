const password_btn=document.querySelector('#pwd');
const otp_btn=document.querySelector('#otp');
const pwd_login=document.querySelector('#area1');
const otp_login=document.querySelector('#area2');
password_btn.addEventListener('click',()=>{
    password_btn.classList.remove('noneactive');
    password_btn.classList.add('activebtn');
    otp_btn.classList.add('noneactive');
    otp_btn.classList.remove('activebtn');
    pwd_login.style.display="block";
    otp_login.style.display="none";
})
otp_btn.addEventListener('click',()=>{
    password_btn.classList.add('noneactive');
    password_btn.classList.remove('activebtn');
    otp_btn.classList.remove('noneactive');
    otp_btn.classList.add('activebtn');
    pwd_login.style.display="none";
    otp_login.style.display="block";
})

const flip_button=document.querySelector('.existinguser');
const signinpage=document.querySelector('#sign-in-box');
const loginpage=document.querySelector('#login-box1');
const fullbox=document.querySelector('.login-signup-page');

flip_button.addEventListener('click',()=>{
    fullbox.style.transform="rotateY(180deg)";
    signinpage.style.display="flex";
    loginpage.classList.add('none');
})
document.querySelector('#login').addEventListener('click',()=>{
    fullbox.style.transform="rotateY(0deg)";
    signinpage.style.display="none";
    loginpage.classList.remove('none');
})
const forgetpage=document.querySelector('.forget-password-container');
const forget_btn=document.querySelector('.forget');
const close_btn=document.querySelector('.close-btn');
forget_btn.addEventListener('click',()=>{
    forgetpage.classList.remove('none');
})
close_btn.addEventListener('click',()=>{
    forgetpage.classList.add('none');
})
