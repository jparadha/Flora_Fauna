-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 27-05-2026 a las 03:58:52
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `gestion_fauna_flora`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `faunaflora`
--

CREATE TABLE `faunaflora` (
  `ID` int(11) NOT NULL,
  `CodigoIdentificacion` varchar(20) DEFAULT NULL,
  `NombreCientifico` varchar(100) DEFAULT NULL,
  `Habitat` varchar(50) DEFAULT NULL,
  `EstadoConservacion` varchar(50) DEFAULT NULL,
  `RegionGeografica` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `faunaflora`
--

INSERT INTO `faunaflora` (`ID`, `CodigoIdentificacion`, `NombreCientifico`, `Habitat`, `EstadoConservacion`, `RegionGeografica`) VALUES
(1, 'FAUNA-001', 'Panthera leo', 'Sabana', 'Vulnerable', 'África'),
(3, 'FLORA-003', 'Phalaenopsis amabilis', 'Selva Tropical', 'En Peligro', 'Sudeste Asiático'),
(4, 'FAUNA-002', 'Puma concolor', 'Cordillera y Zonas precordilleranas', 'Casi Amenazado', 'Chile');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `faunaflora`
--
ALTER TABLE `faunaflora`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `CodigoIdentificacion` (`CodigoIdentificacion`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `faunaflora`
--
ALTER TABLE `faunaflora`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
