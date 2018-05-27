<!DOCTYPE html>
<html>
<head>
	<title>Switch:</title>
</head>
<body>
<?php
	echo "O comando switch: <br><br>";
	// Funciona de forma semelhante ao IF
	// quando a intenção depende apenas do valor de uma variável
	// Sintaxe
	// switch(variavel){
	// case valor1:
		//código a ser executado
		//break;
	// case valorn:
		//código a ser executado
		//break;
	// default:
		//código a ser executado
		//break;
	//}

	$i = 1;

	switch($i) //Se $i for
	{	
		case 0: //valor 0 então
			echo('O valor de i é 0'); //imprimir (False)
			break; //parar os códigos
		case 1: //valor 1 então
			echo ('O valor de i é 1'); //Imprimir (True)
			break; //parar os códigos
		case 2:
			echo('O valor de i é 2');
			break;
	}
?>

</body>
</html>