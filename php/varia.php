<!DOCTYPE html>
<html>
<head>
	<title>Variavel</title>
</head>
<body>

<?php
echo "Declarando variavel:  <br><br>";

$variavel = "Valor declarado "; //Declarando variavel
echo($variavel); // Resultado informado

?>
</br>
</br>
--------------------------------------------------
</br>

<?php
echo "verificando se variavel esta definida: ";
// Para saber se a variavel está definida ou não;
// Sintaxe (bool) isset(nome_variavel)
//(Bool) usado para True or false

if(isset($variavel)) // se(variavel_esta_definida) entao
	echo " A variavel esta definida (primeiro if) <br><br>"; // imprimir ""

$variavel = ""; // declarando variavel

if(isset($variavel))
	echo " A variavel esta definida (segundo if) ";
?>
</br>
</br>
--------------------------------------------------
</br>



</body>
</html>
