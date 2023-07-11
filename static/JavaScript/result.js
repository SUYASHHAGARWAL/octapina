var start = 0;
    var end = 1260; 
    var start2 = 0;
    var end2 = 57; 
    var start3 = 0;
    var end3 = 9; 
    var start4 = 0;
    var end4 = 15960; 
    var start5 = 0;
    var end5 = 107; 
    var start6 = 0;
    var end6 = 65; 
    function counter1() {
      document.querySelectorAll('#result-count')[0].innerHTML=start+'+';
      start+=10;

      if (start <= end) {
        setTimeout(counter1, 20); 
      }
    }
    function counter2() {
        document.querySelectorAll('#result-count')[1].innerHTML=start2+'+';
        start2++;
  
        if (start2 <= end2) {
          setTimeout(counter2, 20); 
        }
      }
      function counter3() {
        document.querySelectorAll('#result-count')[2].innerHTML=start3+'+';
        start3++;
  
        if (start3 <= end3) {
          setTimeout(counter3, 100); 
        }
      }
      function counter4() {
        document.querySelectorAll('#result-count')[3].innerHTML=start4+'+';
        start4+=200;
  
        if (start4 <= end4) {
          setTimeout(counter4, 40); 
        }
      }
      function counter5() {
        document.querySelectorAll('#result-count')[4].innerHTML=start5+'+';
        start5++;
  
        if (start5 <= end5) {
          setTimeout(counter5, 20); 
        }
      }

      function counter6() {
        document.querySelectorAll('#result-count')[5].innerHTML=start6+'+';
        start6++;
  
        if (start6 <= end6) {
          setTimeout(counter6, 20); 
        }
      }
    counter1();
    counter2();
    counter3();
    counter4();
    counter5();
    counter6();

