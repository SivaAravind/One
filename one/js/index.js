function realTime() {
  let date = new Date();
  let h = date.getHours();
  let m = date.getMinutes();
  let s = date.getSeconds();

  /* let session = 'AM';

  if(h == 0 ){
    h = 12;
  }
  if( h > 12){
    //h = h-12;
    session = 'PM';
  } */
  let session = (h>12) ? 'PM' : 'AM';

  h = (h<10) ? '0'+ h : h;
  m = (m<10) ? '0'+ m : m;
  s = (s<10) ? '0'+ s : s;

  var time = h+" : "+m+" : "+s+" "+ session;
  document.getElementById('Time').innerText = time;
  //document.getElementById('Time').textConetnt = time;

  setTimeout(realTime, 1000);
}

realTime();







































// calculator 
// let n = document.getElementById('firstNo').innerText;
// let m = document.getElementById('secondNo').innerText;


// function calculatorAdd(n,m) {
//   var add =  n + m;
//   document.getElementById('add').innerText = add;
// }
// calculatorAdd(n,m);

// function calculator() {
//   //var add = calculatorAdd();
//   //document.getElementById('add').innerText=add;
//   console.log(document.getElementById('firstNo').innerText);
// }
// calculator();