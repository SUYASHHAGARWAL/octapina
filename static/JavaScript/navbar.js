const batch=document.querySelector('#batch-link');
console.log(batch);

batch.addEventListener('click',()=>{
    // window.location.href='/Templates/home.html';
    setTimeout(function(){
        window.scrollTo({
            top: document.querySelector(".batch-container").offsetTop-80,
            left: 0,
            behavior: "smooth",
          });
    },500);
    
})
const navbar=document.getElementById('header1');
console.log(navbar)
window.addEventListener('scroll',function(){
    if(window.scrollY>=56){
        navbar.style.background="rgba(255, 254, 254, 0.837)";
        
    }else if(window.scrollY<56){
        navbar.style.background="transparent";
        
    }
});