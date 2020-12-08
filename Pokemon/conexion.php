<?php
	$conn= @mysqli_connect("localhost", "root", "","datos");

	//VALIDACION DE BASE DE DATOS

	if(!$conexion){ 
		echo ' Error en la base de Datos '; 
	}else{
		echo ' Conexion exitosa! ';
	}
?>