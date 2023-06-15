Program Scanner<br>
Membaca huruf per huruf dan dipisahkan tiap token<br><br>
<form method='post'>
Daftar Token yang dipakai: <br>
<textarea name='token' id='token' cols="50" rows="3">
semua kata yg dibatasi spasi atau simbol token
simbol token: > < = >= <= = + -</textarea><br><br>

Teks Input: <br>
<textarea name='teks' id='teks' rows="6">if a>b then
   a = a+1
else
   a = 5
endif</textarea><br>

<input type='submit' value='Parsing'><br>
Hasil : <br>
<textarea id='hasil' rows="20"></textarea>
</form>

<?php

function getToken($teks,&$j) { // FA - Analisis Leksikal
   $k=strlen($teks);
   $kata="";

   //abaikan spasi dan pindah baris
   while (substr($teks,$j,1)==' ' or 
	      substr($teks,$j,1)==chr(13) or 
         substr($teks,$j,1)==chr(10)) {
  	      $j++;
   }

   //ambil 1 kata/token
   while ($j<$k and
         substr($teks,$j,1)!=' ' and 
	      substr($teks,$j,1)!=chr(13) and 
         substr($teks,$j,1)!=chr(10)) {
   	   if (substr($teks,$j,1)=='>') {
   	   	  if ($kata!='') {
   	   	  	 return $kata;
   	   	  }
   	   	  else {
   	   	    $j++;
   	   	  	 if (substr($teks,$j,1)=='=') {
   	   	       $j++;
   	   	       return ">=";
   	   	    }
   	   	    else return ">";
   	   	  }    	   	  
         }   	   	
   	   else if (substr($teks,$j,1)=='<') {
   	   	  if ($kata!='') {
   	   	  	 //$kata="";
   	   	  	 return $kata;
   	   	  }
   	   	  else {
   	   	    $j++;
   	   	  	 if (substr($teks,$j,1)=='=') {
   	   	       $j++;
   	   	       return "<=";
   	   	    }
   	   	    else return "<";
   	   	  } 
         }
   	   else if (substr($teks,$j,1)=='=') {
   	   	  if ($kata!='') {
   	   	  	 return $kata;
   	   	  }
   	   	  else {
   	   	    $j++;
   	   	    return "=";
   	   	  }
         }   	   	
         else if (substr($teks,$j,1)=='+') {
              if ($kata!='') {
                return $kata;
              }
              else {
                $j++;
                return "+";
              }
         }
         else if (substr($teks,$j,1)=='-') {
              if ($kata!='') {
                return $kata;
              }
              else {
                $j++;
                return "-";
              }
         }
         $kata.=substr($teks,$j,1);
   	   $j++;
   }
   return $kata;
}

$i=0;
if (isset($_POST['teks'])) {
	$input=trim($_POST['teks']);
	$hsl="";
   $k=strlen($input);
   while ($i<$k) {
       $hsl.=getToken($input,$i).'\n';
	}
   echo "
   <script>
       document.getElementById('teks').innerHTML='".$input."';
   </script>";
	echo "
	<script>
	    document.getElementById('hasil').innerHTML='".$hsl."';
	</script>";

}
?>