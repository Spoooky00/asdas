-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 21, 2024 at 03:56 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `datavault_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `account_management`
--

CREATE TABLE `account_management` (
  `AM_User_name` varchar(100) NOT NULL,
  `AM_Email` varchar(100) NOT NULL,
  `AM_Role` int(11) NOT NULL COMMENT '1-doctor, 0-nurse',
  `AM_Password` varchar(100) NOT NULL,
  `AM_Status` int(11) NOT NULL DEFAULT 1 COMMENT '1 = enabled, 0 = disabled'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `account_management`
--

INSERT INTO `account_management` (`AM_User_name`, `AM_Email`, `AM_Role`, `AM_Password`, `AM_Status`) VALUES
('testadminz', 'test@admin.com', 1, 'testpw', 1),
('testclient', 'test@client.com', 0, 'testpw', 1);

-- --------------------------------------------------------

--
-- Table structure for table `daily_logs`
--

CREATE TABLE `daily_logs` (
  `DL_ID` int(11) NOT NULL,
  `User_NFC_ID` varchar(100) NOT NULL,
  `DL_Concerm` varchar(5000) NOT NULL,
  `DL_Timein` timestamp NULL DEFAULT NULL,
  `DL_Timeout` timestamp NULL DEFAULT NULL,
  `DL_PersonInCharge` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inventory`
--

CREATE TABLE `inventory` (
  `Item_ID` int(11) NOT NULL,
  `Item_name` varchar(100) NOT NULL,
  `Quantity` varchar(100) NOT NULL,
  `Manufacturer` varchar(100) NOT NULL,
  `Description` varchar(100) NOT NULL,
  `Item_code` varchar(100) NOT NULL,
  `Item_expiry` date DEFAULT NULL,
  `Item_type` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `inventory`
--

INSERT INTO `inventory` (`Item_ID`, `Item_name`, `Quantity`, `Manufacturer`, `Description`, `Item_code`, `Item_expiry`, `Item_type`) VALUES
(1, 'Test00', 'Test1', 'Test2', 'Test3', 'Test4', '2024-05-22', 'Test5');

-- --------------------------------------------------------

--
-- Table structure for table `pmr2`
--

CREATE TABLE `pmr2` (
  `User_NFC_ID` varchar(100) NOT NULL,
  `PMR_Fname` varchar(100) NOT NULL,
  `PMR_Lname` varchar(100) NOT NULL,
  `PMR_Section` varchar(100) NOT NULL,
  `PMR_Yr_lvl` varchar(100) NOT NULL,
  `PMR_DB` varchar(100) NOT NULL,
  `PMR_Address` varchar(100) NOT NULL,
  `PMR_Gender` varchar(100) NOT NULL,
  `PMR_BT` varchar(100) NOT NULL,
  `PMR_LUD` varchar(100) NOT NULL,
  `PMR_ECN` varchar(100) NOT NULL,
  `PMR_RTTP` varchar(100) NOT NULL,
  `PMR_ECNO` varchar(100) NOT NULL,
  `PMR_HI` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pmr2`
--

INSERT INTO `pmr2` (`User_NFC_ID`, `PMR_Fname`, `PMR_Lname`, `PMR_Section`, `PMR_Yr_lvl`, `PMR_DB`, `PMR_Address`, `PMR_Gender`, `PMR_BT`, `PMR_LUD`, `PMR_ECN`, `PMR_RTTP`, `PMR_ECNO`, `PMR_HI`) VALUES
('12345678', 'TEST', 'PATIENTa', 'IT', '3', '09/11/1990', 'Mandaluyong', 'Male', 'A+', '05/11/2024', 'TEST CONTACT', 'TEST RELATIVES', '09123123', 'TEST DATA'),
('11223344', 'DATA FROM UI', 'TEST', 'IT', '4', '2024-05-21', 'TES LOC', 'Male', 'O+', '05/21/2024', 'TEST TAO', 'Parent', '112233', 'aa');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account_management`
--
ALTER TABLE `account_management`
  ADD PRIMARY KEY (`AM_User_name`);

--
-- Indexes for table `inventory`
--
ALTER TABLE `inventory`
  ADD PRIMARY KEY (`Item_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `inventory`
--
ALTER TABLE `inventory`
  MODIFY `Item_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
