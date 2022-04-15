<?php
$tal1=1;
$tal2=1;
$tmp=0;
$ans=0;
$b=2;
while(strlen($ans)<1000) {           
    $ans=bcadd($tal1,$tal2); 
    $tmp=$tal1;
    $tal1=$tal2;
    $tal2=bcadd($tal2,$tmp);    
    $b++;
}
echo $b;
?>
