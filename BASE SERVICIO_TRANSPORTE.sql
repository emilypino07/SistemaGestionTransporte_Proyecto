create database Serviciotransporte
use Serviciotransporte
create table Servicios
(
Idservicio int identity (1,1) Primary key,
codigo varchar (10),
cedula varchar (10),
nombre varchar (40),
apellido varchar (40),
email varchar (50),
tipo varchar (17),
fecha date,
distancia decimal (10,2),
costo_km decimal (10,2),
estaciones int,
tarifa decimal (10,2)
)
--Mostrar los datos que se guardan desde la interfaz
select * from Servicios





