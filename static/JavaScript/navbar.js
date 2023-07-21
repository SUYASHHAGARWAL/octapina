
const navbar=document.getElementById('header1');
console.log(navbar)
window.addEventListener('scroll',function(){
    if(window.scrollY>=56){
        navbar.style.background="rgba(255, 254, 254, 0.837)";
        
    }else if(window.scrollY<56){
        navbar.style.background="transparent";
        
    }
});