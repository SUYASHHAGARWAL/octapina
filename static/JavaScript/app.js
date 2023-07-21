let scrollContainer = document.querySelector(".photos");
let backBtn = document.getElementById("backBtn");
let nextBtn = document.getElementById("nextBtn");

let new_scrollContainer = document.querySelector(".photos_1")
let new_backBtn = document.getElementById("backBtn_1");
let new_nextBtn = document.getElementById("nextBtn_1");

scrollContainer.addEventListener("wheel",(evt) =>{
    evt.preventDefault();
    scrollContainer.scrollLeft += evt.deltaY;
    scrollContainer.style.scrollBehavior = "auto";
});

nextBtn.addEventListener("click",()=>{
    scrollContainer.style.scrollBehavior = "smooth";
    scrollContainer.scrollLeft += 350;
});
  
backBtn.addEventListener("click",()=>{
    scrollContainer.style.scrollBehavior = "smooth";
    scrollContainer.scrollLeft -= 350;
});
  

// new_scrollContainer.addEventListener("wheel",(evt1) =>{
//     evt1.preventDefault();
//     new_scrollContainer.scrollLeft += evt1.deltaY;
//     new_scrollContainer.style.scrollBehavior = "auto";
// });

new_nextBtn.addEventListener("click",()=>{
    new_scrollContainer.style.scrollBehavior = "smooth";
    new_scrollContainer.scrollLeft += 500;
});
  
new_backBtn.addEventListener("click",()=>{
    new_scrollContainer.style.scrollBehavior = "smooth";
    new_scrollContainer.scrollLeft -= 500;
});
  
const batch=document.getElementById('batch-link');
console.log(batch,"hello");

batch.addEventListener('click',()=>{
    // window.location.href='/Templates/home.html';
        window.scrollTo({
            top: document.querySelector(".batch-container").offsetTop-80,
            left: 0,
            behavior: "smooth",
          });

    
})