<?php
  // Determine if a triplet is a pythagorean triplet
  function isPythagoreanTriplet($triplet){
    $a = $triplet[0]; $b = $triplet[1];
    $c = sqrt(pow($a, 2) + pow($b, 2));
    $test1 = False; $test2 = False;
    if($a < $b && $b < $c){ $test1 = True; }
    if(filter_var($c, FILTER_VALIDATE_INT)){ $test2 = True; }
    return $test1 && $test2;
  }
  // Print the triplet in a specific format
  function printTriplet($triplet){
    $a = $triplet[0]; $b = $triplet[1];
    $c = sqrt(pow($a, 2) + pow($b, 2));
    $product = $a * $b * $c;
    echo "a = $a   b = $b   c = $c   abc = $product\n";
  }
  // Find all the pythagorean triplets below n
  function pythagoreanTriplets($n){
    $i = 0; $j = 0; $iWorks = True;
    while($iWorks){
      $jWorks = True; $j = 0;
      while($jWorks){
        if(pow($i, 2) > $n){ $iWorks = False; }
        if(pow($i, 2) + pow($j, 2) < $n){
          if(isPythagoreanTriplet([$i, $j])){ printTriplet([$i, $j]);  }
        }
        else{ $jWorks = False;}
        $j++;
      }
      $i++;
    }
  }
  // Get user input
  $prompt = "Enter an integer n: ";
  $n = readline($prompt);
  pythagoreanTriplets($n);
?>
