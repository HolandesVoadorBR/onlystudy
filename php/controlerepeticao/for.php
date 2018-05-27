<!DOCTYPE html>
<html>
<head>
	<title>For</title>
</head>
<body>
<?php
	echo 'Estrutura de repetição .FOR. <br><br>';

	//O primeiro comando de repetição a ser aborado
	//for = para (para cada um dos valores)
	//sintaxe
	//for(valores_iniciais; condições; incremento){
		//'código a ser executado'
	// }

	for($i = 0; $i < 10; $i++){ // para (declara valor; condição; incrementação)
		echo($i .' '); //Imprimir resultado 0 1 2 3 4 5 6 7 8 9 
	}
?>
</body>
</html>