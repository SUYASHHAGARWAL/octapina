const btns=document.getElementsByClassName('btn');
for (i = 0; i < btns.length; i++) {
    btns[i].addEventListener('click', function (e) {
        const user_table=this.nextElementSibling;
    if(user_table.classList.contains('none1')){
        user_table.classList.remove('none1');
        e.target.classList.add('button-active');
    }else{
        user_table.classList.add('none1');
        e.target.classList.remove('button-active');
    }
    })
}

// setTimeout(() => {
//     document.querySelector('.msg-box').style.display="none";
// }, 4000);