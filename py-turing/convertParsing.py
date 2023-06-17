#!/usr/bin/env python3
stack_ = Array({"n": 0, "isi": Array()})
def push(stack_=None, x_=None, *_args_):
    
    
    stack_["n"] += 1
    stack_["isi"][stack_["n"]] = x_
    push.byref_stack = stack
# end def push
def pop(stack_=None, *_args_):
    
    
    x_ = stack_["isi"][stack_["n"]]
    stack_["n"] -= 1
    return x_
    pop.byref_stack = stack
# end def pop
def isEmpty(stack_=None, *_args_):
    
    
    if stack_["n"] == 0:
        return True
    # end if
    return False
    
# end def isEmpty
def readTop(stack_=None, *_args_):
    
    
    return stack_["isi"][stack_["n"]]
    
# end def readTop
#// Aturan Produksi CFG
#// S -> AB | CD
#// A -> xA | y
#// B -> yB | x
#// C -> aD | b
#// D -> bC | a
#//
tabelParsing_ = Array({"S": Array({"x": "AB", "y": "AB", "a": "CD", "b": "CD", "#": "-"})}, {"A": Array({"x": "xA", "y": "y", "a": "-", "b": "-", "#": "-"})}, {"B": Array({"x": "x", "y": "yB", "a": "-", "b": "-", "#": "-"})}, {"C": Array({"x": "-", "y": "-", "a": "aD", "b": "b", "#": "-"})}, {"D": Array({"x": "-", "y": "-", "a": "a", "b": "bC", "#": "-"})})
simbolAwal_ = "S"
pass
print("""
<style>
td {
width: 50px;
text-align: center;
}
</style>
<form method='post'>
Aturan Produksi : <br>
<textarea name='cfg' rows=\"7\" cols=\"34\" readonly>
LL(1) DENGAN NOTASI SEDERHANA
S -> AB | CD
A -> xA | y
B -> yB | x  
C -> aD | b  
D -> bC | a
</textarea><br><br>
Parse Table<br>
""")
printTable(tabelParsing_)
print("""<br>
Contoh input diterima:<br>
yx, xyx, xyyx, xxyyx<br><br>
Input : <br>
<textarea name='teks' id='tes' rows=\"3\">xyyx</textarea><br><br>
<input type='submit' value='Parsing'><br>
Hasil : <br>
<textarea id='hasil' rows=\"3\"></textarea>
</form>
""")
def printTable(tbl_=None, *_args_):
    
    
    print("<table border='1'>")
    for jdl_baris_,dt_ in tbl_.items():
        print("<tr><th></th>")
        for jdl_,isi_ in dt_.items():
            if jdl_ == "#":
                print("<th>EOS</th>")
            else:
                print("<th>" + jdl_ + "</th>")
            # end if
        # end for
        print("</tr>")
        break
    # end for
    for jdl_baris_,dt_ in tbl_.items():
        print("<tr><td>" + jdl_baris_ + "</td>")
        for jdl_,isi_ in dt_.items():
            print("<td>" + isi_ + "</td>")
        # end for
        print("</tr>")
    # end for
    print("</table>")
    
# end def printTable
def getToken(teks_=None, j_=None, *_args_):
    
    
    #// FA - Analisis Leksikal
    k_ = php_strlen(teks_)
    simbol_ = php_substr(teks_, j_, 1)
    j_ += 1
    return simbol_
    getToken.byref_j = j
# end def getToken
i_ = 0
hsl_ = ""
if (php_isset(lambda : PHP_POST["teks"])):
    input_ = PHP_POST["teks"] + "#"
    #// # sebagai pengganti EOS
    print("""
    <script>
    document.getElementById('hasil').innerHTML='';
    </script>""")
    push(stack_, simbolAwal_)
    stack_ = push.byref_stack
    simbol_ = getToken(input_, i_)
    i_ = getToken.byref_j
    while True:
        
        if not ((not isEmpty(stack_))):
            break
        # end if
        top_ = readTop(stack_)
        if top_ >= "a":
            #// top = terminal
            if top_ == simbol_:
                pop(stack_)
                stack_ = pop.byref_stack
                simbol_ = getToken(input_, i_)
                i_ = getToken.byref_j
            else:
                hsl_ = "Error/Ditolak"
                break
            # end if
        else:
            if top_ <= "Z":
                #// top = non terminal
                sel_ = tabelParsing_[top_][simbol_]
                if sel_ != "-":
                    pop(stack_)
                    stack_ = pop.byref_stack
                    k_ = php_strlen(sel_) - 1
                    while k_ >= 0:
                        
                        push(stack_, php_substr(sel_, k_, 1))
                        stack_ = push.byref_stack
                        k_ -= 1
                    # end while
                else:
                    hsl_ = "Error/Ditolak"
                    break
                # end if
            # end if
        # end if
    # end while
    print("\n    <script>\n       document.getElementById('tes').innerHTML='" + php_substr(input_, 0, php_strlen(input_) - 1) + "';\n    </script>")
    if simbol_ == "#" and hsl_ == "":
        print("""
        <script>
        document.getElementById('hasil').innerHTML='DITERIMA';
        </script>""")
    else:
        print("\n      <script>\n          document.getElementById('hasil').innerHTML='" + hsl_ + "';\n    </script>")
    # end if
# end if
