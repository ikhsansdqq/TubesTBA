#!/usr/bin/env python3
print("""Program Scanner<br>
Membaca huruf per huruf dan dipisahkan tiap token<br><br>
<form method='post'>
Daftar Token yang dipakai: <br>
<textarea name='token' id='token' cols=\"50\" rows=\"3\">
semua kata yg dibatasi spasi atau simbol token
simbol token: > < = >= <= = + -</textarea><br><br>
Teks Input: <br>
<textarea name='teks' id='teks' rows=\"6\">if a>b then
a = a+1
else
a = 5
endif</textarea><br>
<input type='submit' value='Parsing'><br>
Hasil : <br>
<textarea id='hasil' rows=\"20\"></textarea>
</form>
""")
def getToken(teks_=None, j_=None, *_args_):
    
    
    #// FA - Analisis Leksikal
    k_ = php_strlen(teks_)
    kata_ = ""
    #// abaikan spasi dan pindah baris
    while True:
        
        if not (php_substr(teks_, j_, 1) == " " or php_substr(teks_, j_, 1) == chr(13) or php_substr(teks_, j_, 1) == chr(10)):
            break
        # end if
        j_ += 1
    # end while
    #// ambil 1 kata/token
    while True:
        
        if not (j_ < k_ and php_substr(teks_, j_, 1) != " " and php_substr(teks_, j_, 1) != chr(13) and php_substr(teks_, j_, 1) != chr(10)):
            break
        # end if
        if php_substr(teks_, j_, 1) == ">":
            if kata_ != "":
                return kata_
            else:
                j_ += 1
                if php_substr(teks_, j_, 1) == "=":
                    j_ += 1
                    return ">="
                else:
                    return ">"
                # end if
            # end if
        else:
            if php_substr(teks_, j_, 1) == "<":
                if kata_ != "":
                    #// $kata="";
                    return kata_
                else:
                    j_ += 1
                    if php_substr(teks_, j_, 1) == "=":
                        j_ += 1
                        return "<="
                    else:
                        return "<"
                    # end if
                # end if
            else:
                if php_substr(teks_, j_, 1) == "=":
                    if kata_ != "":
                        return kata_
                    else:
                        j_ += 1
                        return "="
                    # end if
                else:
                    if php_substr(teks_, j_, 1) == "+":
                        if kata_ != "":
                            return kata_
                        else:
                            j_ += 1
                            return "+"
                        # end if
                    else:
                        if php_substr(teks_, j_, 1) == "-":
                            if kata_ != "":
                                return kata_
                            else:
                                j_ += 1
                                return "-"
                            # end if
                        # end if
                    # end if
                # end if
            # end if
        # end if
        kata_ += php_substr(teks_, j_, 1)
        j_ += 1
    # end while
    return kata_
    getToken.byref_j = j
# end def getToken
i_ = 0
if (php_isset(lambda : PHP_POST["teks"])):
    input_ = php_trim(PHP_POST["teks"])
    hsl_ = ""
    k_ = php_strlen(input_)
    while True:
        
        if not (i_ < k_):
            break
        # end if
        hsl_ += getToken(input_, i_)
        i_ = getToken.byref_j + "\\n"
    # end while
    print("\n   <script>\n       document.getElementById('teks').innerHTML='" + input_ + "';\n   </script>")
    print("\n   <script>\n      document.getElementById('hasil').innerHTML='" + hsl_ + "';\n    </script>")
# end if
