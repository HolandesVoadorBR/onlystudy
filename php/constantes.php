<!DOCTYPE html>
<html>
<head>
	<title>Constantes</title>
</head>
<body>

<?php
	echo "Constantes: \n";
	echo "Constantes são valores que não se alteram na execução <br><br>";

	// As constantes são definidas com a função 'define' sintaxe:
	// (bool) define(nome_constante, valor[, não sensitive])
	// indiferente do uso de maius ou minus, case sensitive

	define("minhaconstante", "Brasil");
	echo minhaconstante .'<br>'; // Resultado Brasil
	echo MinhaConstante .'<br><br>'; // Resultado MinhaConstante

	define("minhaConstanteB", "Brasil", TRUE);
	echo minhaConstanteB .'<br>'; // Resultado Brasil
	echo MINHACONSTANTEB .'<br>'; // Resultado Brasil

	// O case sensitive está ativado ignorando as maiscu e minus constanteB

?>

</body>
</html>