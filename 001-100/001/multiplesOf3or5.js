function multiplesOf3or5(){
  let n = document.getElementById("inputN").value;
  let sum = 0;
  for(let i = 0; i < n; i++){
    if(i % 3 == 0 || i % 5 == 0) { sum++; }
  }
  let answer = `Sum of multiples of 3 or 5 below ${n}<br>${sum}`;
  document.getElementById("answer").innerHTML = answer;
}
