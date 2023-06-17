<?php
$stack=[
   'n' => 0,
   'isi' => []
];

function push(&$stack,$x) {
   $stack['n']++;
   $stack['isi'][$stack['n']]=$x;
}

function pop(&$stack) {
   $x=$stack['isi'][$stack['n']];
   $stack['n']--;
   return $x;
}

function isEmpty($stack) {
   if ($stack['n']==0) return true;
   return false;
}

function readTop($stack) {
   return $stack['isi'][$stack['n']];
}

/* Aturan Produksi CFG

S -> AB | CD
A -> xA | y
B -> yB | x  
C -> aD | b  
D -> bC | a

*/

$tabelParsing = [
   'S' => [
   	       'x'=>'AB',
           'y'=>'AB',
   	       'a'=>'CD',
           'b'=>'CD',
           '#'=>'-',
           ],
   'A' => [
   	       'x'=>'xA',
           'y'=>'y',
   	       'a'=>'-',
           'b'=>'-',
           '#'=>'-',
           ],
   'B' => [
   	       'x'=>'x',
           'y'=>'yB',
   	       'a'=>'-',
           'b'=>'-',
           '#'=>'-',
           ],
   'C' => [
   	       'x'=>'-',
           'y'=>'-',
   	       'a'=>'aD',
           'b'=>'b',
           '#'=>'-',
           ],
   'D' => [
   	       'x'=>'-',
           'y'=>'-',
   	       'a'=>'a',
           'b'=>'bC',
           '#'=>'-',
           ],
 ];
 $simbolAwal='S'; //Non Terminal yang menjadi simbol awal
?>

<style>
td {
      width: 50px;
      text-align: center;
   }

</style>

<form method='post'>
Aturan Produksi : <br>
<textarea name='cfg' rows="7" cols="34" readonly>
LL(1) DENGAN NOTASI SEDERHANA
S -> AB | CD
A -> xA | y
B -> yB | x  
C -> aD | b  
D -> bC | a
</textarea><br><br>
Parse Table<br>
<?php
   printTable($tabelParsing);
?>
<br>
Contoh input diterima:<br>
yx, xyx, xyyx, xxyyx<br><br>
Input : <br>
<textarea name='teks' id='tes' rows="3">xyyx</textarea><br><br>
<input type='submit' value='Parsing'><br>
Hasil : <br>
<textarea id='hasil' rows="3"></textarea>
</form>

<?php

function printTable($tbl) {
   echo "<table border='1'>";
   foreach ($tbl as $jdl_baris => $dt) {
      echo "<tr><th></th>";
      foreach ($dt as $jdl => $isi) {
         if ($jdl=='#')
            echo "<th>EOS</th>";
         else
            echo "<th>".$jdl."</th>";
      }
      echo "</tr>";
      break;
   }
   foreach ($tbl as $jdl_baris => $dt) {
      echo "<tr><td>".$jdl_baris."</td>";
      foreach ($dt as $jdl => $isi) {
         echo "<td>".$isi."</td>";
      }
      echo "</tr>";
   }
   echo "</table>";
}

function getToken($teks,&$j) { // FA - Analisis Leksikal
   $k=strlen($teks);
   $simbol=substr($teks,$j,1);
   $j++;
   return $simbol;
}

$i=0;
$hsl="";
if (isset($_POST['teks'])) {
	$input=$_POST['teks'].'#'; // # sebagai pengganti EOS
	echo "
    <script>
       document.getElementById('hasil').innerHTML='';
    </script>";
    push($stack,$simbolAwal);
    $simbol=getToken($input,$i);  
    while (!isEmpty($stack)) {
    	$top=readTop($stack);
        if ($top>='a') { // top = terminal
           if ($top==$simbol) {
           	  pop($stack);
              $simbol=getToken($input,$i);
           } else {
           	 $hsl="Error/Ditolak";
           	 break;
           }	 
        }
        else if ($top<='Z') { // top = non terminal
           $sel=$tabelParsing[$top][$simbol];
           if ($sel!='-') {
           	  pop($stack);
              for ($k=strlen($sel)-1;$k>=0;$k--) {
              	push($stack,substr($sel,$k,1));
              }  
           } else {
           	 $hsl="Error/Ditolak";
           	 break;
           }	 
        }
	}
	echo "
    <script>
       document.getElementById('tes').innerHTML='".
       substr($input,0,strlen($input)-1)."';
    </script>";
	if ($simbol=='#' and $hsl=='') 
  	   echo "
	   <script>
	       document.getElementById('hasil').innerHTML='DITERIMA';
	   </script>";
	else
  	   echo "
	   <script>
	       document.getElementById('hasil').innerHTML='".$hsl."';
	   </script>";
}


?>