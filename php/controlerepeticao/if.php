<!DOCTYPE html>
<html>
<head>
	<title>if</title>
</head>
<body>
<?php
	echo "IF, Else if, else <br><br>";

	//IF comando de decisão
	//sintaxe
	//if(condição) {
	//codigo a ser executado
	//}
	//else if(condicao){
	//codigo a ser executado
	//}
	//else(condicao){
	//codigo a ser executado
	//}

	if(3 > 5) // Se 3 for maior que 5 então
		echo('Não entra no primeiro if <br>. '); // Imprimir
	
	if(1 < 10) // Se 1 for menor que 10 então (True)
		echo('Entra no segundo if. <br>'); // Imprimir
	else // Senão
		echo('Não entra no segundo if <br>. '); // Imprimir (Falso)

	$i = 5; // Variável declarada
	if($i == 3){ // se $i é igual a 3 então (False)
		echo('O valor de i é 3.<br> '); // imprimir
	} else if($i == 4){ // se $i é igual a 4 então (False)
		echo('O valor de i é 4.<br> '); // imprimir
	} else // senão
		echo('<br> O valor de i não é nem 3 e nem 4. ' ); //imprimir (True)
?>
</body>
</html>