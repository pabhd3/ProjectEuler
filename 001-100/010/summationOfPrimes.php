<?php
  // Check if a number is prime
  function isPrime($n){
    for ($i = 2; $i < $n; $i++) {
      if($n % $i == 0){ return False; }
    }
    return True;
  }
  // Get the summation of primes
  function summationOfPrimes($n){
    $sum = 0;
    for($i = 0; $i < $n; $i++){
      if(isPrime($i)){ $sum += $i; }
    }
    return $sum;
  }
  // Get user input
  $prompt = "Enter an integer n: ";
  $n = readline($prompt);
  $sum = summationOfPrimes($n);
  echo "\nSummation of primes below $n";
  echo "\n$sum\n"
?>
