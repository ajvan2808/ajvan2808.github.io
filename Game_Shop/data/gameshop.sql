-- phpMyAdmin SQL Dump
-- version 4.9.7
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: May 21, 2021 at 06:40 AM
-- Server version: 5.7.32
-- PHP Version: 7.4.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gameshop`
--

-- --------------------------------------------------------

--
-- Table structure for table `Category`
--

CREATE TABLE `Category` (
  `ID` int(11) NOT NULL,
  `Type` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `Category`
--

INSERT INTO `Category` (`ID`, `Type`) VALUES
(1, 'Fun'),
(2, 'Action'),
(3, 'Battle Royale'),
(4, 'Horor, Interactive');

-- --------------------------------------------------------

--
-- Table structure for table `Customer`
--

CREATE TABLE `Customer` (
  `Customer_ID` int(11) NOT NULL,
  `Fullname` varchar(300) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Username` varchar(300) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Password` varchar(300) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Email` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `Customer`
--

INSERT INTO `Customer` (`Customer_ID`, `Fullname`, `Username`, `Password`, `Email`) VALUES
(1, 'Van Hong Hanh', 'HanhVan', '12345', 'hanh@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `Order`
--

CREATE TABLE `Order` (
  `Order_ID` int(11) NOT NULL,
  `CustomerID` int(11) DEFAULT NULL,
  `Order_date` datetime DEFAULT NULL,
  `Total` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `Order`
--

INSERT INTO `Order` (`Order_ID`, `CustomerID`, `Order_date`, `Total`) VALUES
(1, 1, '2021-05-20 00:34:00', 150),
(2, 1, '2021-05-20 00:41:09', 50),
(3, 1, '2021-05-20 00:42:38', 50),
(4, 1, '2021-05-20 00:52:31', 150),
(5, 1, '2021-05-20 00:59:38', 80),
(6, 1, '2021-05-20 01:02:35', 45),
(7, 1, '2021-05-20 01:05:50', 0),
(8, 1, '2021-05-20 01:09:23', 45),
(9, 1, '2021-05-20 14:46:59', 40),
(10, 1, '2021-05-20 17:45:17', 90),
(11, 1, '2021-05-20 17:48:59', 40),
(12, 1, '2021-05-20 17:50:07', 40),
(13, 1, '2021-05-20 17:52:07', 80),
(14, 1, '2021-05-20 17:54:03', 55),
(15, 1, '2021-05-20 18:02:10', 40),
(16, 1, '2021-05-20 23:25:22', 150),
(17, 1, '2021-05-20 23:27:50', 45),
(18, 1, '2021-05-20 23:28:22', 40),
(19, 1, '2021-05-20 23:29:19', 50);

-- --------------------------------------------------------

--
-- Table structure for table `Order_detail`
--

CREATE TABLE `Order_detail` (
  `Detail_ID` int(11) NOT NULL,
  `OrderID` int(11) DEFAULT NULL,
  `GameID` int(11) DEFAULT NULL,
  `Quantity` int(11) NOT NULL,
  `Game_price` int(11) NOT NULL,
  `Order_total` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `Order_detail`
--

INSERT INTO `Order_detail` (`Detail_ID`, `OrderID`, `GameID`, `Quantity`, `Game_price`, `Order_total`) VALUES
(1, 1, 2, 1, 50, 50),
(2, 1, 10, 1, 55, 55),
(3, 1, 15, 1, 45, 45),
(4, 2, 2, 1, 50, 50),
(5, 3, 2, 1, 50, 50),
(6, 4, 2, 2, 50, 100),
(7, 4, 7, 1, 50, 50),
(8, 5, 3, 1, 40, 40),
(9, 5, 5, 1, 40, 40),
(10, 6, 4, 1, 45, 45),
(11, 8, 6, 1, 45, 45),
(12, 9, 3, 1, 40, 40),
(13, 10, 2, 1, 50, 50),
(14, 10, 3, 1, 40, 40),
(15, 11, 3, 1, 40, 40),
(16, 12, 3, 1, 40, 40),
(17, 13, 3, 1, 40, 40),
(18, 13, 5, 1, 40, 40),
(19, 14, 10, 1, 55, 55),
(20, 15, 5, 1, 40, 40),
(21, 16, 3, 1, 40, 40),
(22, 16, 10, 2, 55, 110),
(23, 17, 12, 1, 45, 45),
(24, 18, 3, 1, 40, 40),
(25, 19, 2, 1, 50, 50);

-- --------------------------------------------------------

--
-- Table structure for table `Products`
--

CREATE TABLE `Products` (
  `Game_ID` int(11) NOT NULL,
  `Name` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Price` float NOT NULL,
  `Description` text COLLATE utf8mb4_unicode_ci,
  `Images` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Type_ID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `Products`
--

INSERT INTO `Products` (`Game_ID`, `Name`, `Price`, `Description`, `Images`, `Type_ID`) VALUES
(1, 'Mario', 40, 'Super Mario Bros. is a platform game. In the game, Mario must race through the Mushroom Kingdom and save Princess Toadstool (later Princess Peach) from Bowser. Mario jumps, runs, and walks across each level. The worlds are full of enemies and platforms, and open holes.', 'Mario.jpg', 1),
(2, 'Fall Guys', 50, 'Ultimate Knockout flings hordes of contestants together online in a mad dash through round after round of escalating chaos until one victor remains! Battle bizarre obstacles, shove through unruly competitors, and overcome the unbending laws of physics as you stumble towards greatness.', 'FallGuys.jpg', 1),
(3, 'Gang Beasts', 40, 'Gang Beasts is a silly multiplayer party game with surly gelatinous characters, brutal slapstick fight sequences, and absurd hazardous environments, set in the mean streets of Beef City.', 'GangBeasts.jpg', 1),
(4, 'Over Cooked', 45, 'Overcooked is a chaotic couch co-op cooking game for one to four players. ... In Overcooked players must journey through a variety of cruel and unusual kitchens on their quest to become master chefs capable of conquering an ancient edible evil which plagues the land.', 'OverCooked.jpg', 1),
(5, 'Moving Out', 40, 'Moving Out is a ridiculous physics-based moving simulator that brings new meaning to \'couch co-op\'! ... Up to four players can cozy up on the couch to argue over the best way to move a couch. Test your skills AND your friendship! Physics!', 'MovingOut.jpg', 1),
(6, 'Sea Of Thieves', 45, 'Sea of Thieves is a 2018 first-person multiplayer action-adventure game in which players cooperate with each other to explore an open world via a pirate ship. ... The player assumes the role of a pirate who completes voyages from different trading companies in order to become the ultimate pirate legend.', 'SeaOfThieves.jpg', 2),
(7, 'Outriders', 50, 'OUTRIDERS is a story driven RPG-Shooter that will put the player in the shoes of an Outrider, the last hope of the human race trapped on Enoch, a dangerous and untamed planet. The campaign can be played entirely in single player, or in co-op with up to three players.', 'Outriders.jpg', 2),
(8, 'MadMax', 55, 'Mad Max is an action-adventure video game based on the Mad Max franchise. ... Mad Max emphasizes vehicular combat, in which players can use weapon and armor upgrades on their car to fight enemies. It is set in an open post-apocalyptic wasteland consisting of deserts, canyons, and caves.', 'MadMax.jpg', 2),
(9, 'Jedi', 50, 'Star Wars Jedi: Fallen Order is an action-adventure video game played from a third-person perspective. It also adopted the \'Metroidvania\' style of exploration and progression. Players control Cal Kestis and have access to a lightsaber and the Force, which are used in both combat and puzzle scenarios.', 'Jedi.jpg', 2),
(10, 'Playerunknown\'s Battleground', 55, 'Battlegrounds is a player versus player shooter game in which up to one hundred players fight in a battle royale, a type of large-scale last man standing deathmatch where players fight to remain the last alive. Players can choose to enter the match solo, duo, or with a small team of up to four people.', 'PlayerunknownBattleground.jpg', 3),
(11, 'Resident Evil 2', 45, 'Resident Evil 2 on Steam. A deadly virus engulfs the residents of Raccoon City in September of 1998, plunging the city into chaos as flesh eating zombies roam the streets for survivors. An unparalleled adrenaline rush, gripping storyline, and unimaginable horrors await you.', 'ResidentEvil2.jpg', 2),
(12, 'Assasin\'s Creed', 45, 'Assassin\'s Creed is an action-adventure game set in an open world environment and played from a third-person perspective in which the player primarily assumes the role of Altaïr, as experienced by protagonist Desmond Miles.', 'AssasinCreed.jpg', 2),
(13, 'The Witcher', 50, 'The Witcher 3: Wild Hunt is an action role-playing game with a third-person perspective. Players control Geralt of Rivia, a monster slayer known as a Witcher. Geralt walks, runs, rolls and dodges, and (for the first time in the series) jumps, climbs and swims.', 'TheWitcher.jpg', 2),
(14, 'Fornite', 55, 'Fortnite is a survival game where 100 players fight against each other in player versus player combat to be the last one standing. It is a fast-paced, action-packed game, not unlike The Hunger Games, where strategic thinking is a must in order to survive. There are an estimated 125 million players on Fortnite.', 'Fornite.jpg', 3),
(15, 'Grand Theft Auto', 45, 'Grand Theft Auto V is an action-adventure game played from either a third-person or first-person perspective. Players complete missions—linear scenarios with set objectives—to progress through the story. Outside of the missions, players may freely roam the open world.', 'GrandTheftAuto.jpg', 2),
(16, 'God Of War', 40, 'God of War is an action-adventure game franchise created by David Jaffe at Sony\'s Santa Monica Studio. ... Based in ancient mythology, the story follows Kratos, a Spartan warrior who was tricked into killing his family by his former master, the Greek God of War Ares.', 'GodOfWar.jpg', 2),
(17, 'Until Dawn', 50, 'Until Dawn is an interactive drama in which players primarily assume control of eight young adults who have to survive on Blackwood Mountain until they are rescued at dawn. ... Players control the characters in a linear environment and find clues and items.', 'UntilDawn.jpg', 4),
(18, 'Escape Game', 40, 'Beat all the trials to escape the Fort with the treasure! You will need all your endurance and dexterity to escape an old fort lost in the sea by passing all its obstacles and beating the trial. Team up with your friends or family, gather all the clues and keys to solve the final enigma.', 'EscapeGame.jpg', 2),
(19, 'It Takes Two', 45, 'It Takes Two is an action-adventure video game with elements from platform games. It is specifically designed for split-screen cooperative multiplayer, which means that it must be played with another player through either local or online play. ... The game also features a large number of minigames.', 'ItTakesTwo.jpg', 2),
(20, 'Jumanji', 40, 'A Game For Those Who Seek To Find A Way To Leave Their World Behind. Grab your pawn, roll the eight-sided number die and move through the jungle. Draw a danger card, then use your decoder to discover the secret message and see if disaster strikes. Your fellow players must race against time to rescue you.', 'Jumanji.jpg', 2);

-- --------------------------------------------------------

--
-- Table structure for table `ShopAdmin`
--

CREATE TABLE `ShopAdmin` (
  `id` int(11) NOT NULL,
  `Fullname_Ad` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Username_Ad` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Password_Ad` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `ShopAdmin`
--

INSERT INTO `ShopAdmin` (`id`, `Fullname_Ad`, `Username_Ad`, `Password_Ad`) VALUES
(1, 'Van Hong Hanh', 'HanhVan', '12345'),
(2, 'Sales', 'SaleAdmin', 'SaleAdmin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Category`
--
ALTER TABLE `Category`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `Customer`
--
ALTER TABLE `Customer`
  ADD PRIMARY KEY (`Customer_ID`);

--
-- Indexes for table `Order`
--
ALTER TABLE `Order`
  ADD PRIMARY KEY (`Order_ID`),
  ADD KEY `CustomerID` (`CustomerID`);

--
-- Indexes for table `Order_detail`
--
ALTER TABLE `Order_detail`
  ADD PRIMARY KEY (`Detail_ID`),
  ADD KEY `OrderID` (`OrderID`),
  ADD KEY `GameID` (`GameID`);

--
-- Indexes for table `Products`
--
ALTER TABLE `Products`
  ADD PRIMARY KEY (`Game_ID`),
  ADD KEY `Type_ID` (`Type_ID`);

--
-- Indexes for table `ShopAdmin`
--
ALTER TABLE `ShopAdmin`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Category`
--
ALTER TABLE `Category`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `Customer`
--
ALTER TABLE `Customer`
  MODIFY `Customer_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `Order`
--
ALTER TABLE `Order`
  MODIFY `Order_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `Order_detail`
--
ALTER TABLE `Order_detail`
  MODIFY `Detail_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `Products`
--
ALTER TABLE `Products`
  MODIFY `Game_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `ShopAdmin`
--
ALTER TABLE `ShopAdmin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Order`
--
ALTER TABLE `Order`
  ADD CONSTRAINT `order_ibfk_1` FOREIGN KEY (`CustomerID`) REFERENCES `Customer` (`Customer_ID`);

--
-- Constraints for table `Order_detail`
--
ALTER TABLE `Order_detail`
  ADD CONSTRAINT `order_detail_ibfk_1` FOREIGN KEY (`OrderID`) REFERENCES `Order` (`Order_ID`),
  ADD CONSTRAINT `order_detail_ibfk_2` FOREIGN KEY (`GameID`) REFERENCES `Products` (`Game_ID`);

--
-- Constraints for table `Products`
--
ALTER TABLE `Products`
  ADD CONSTRAINT `products_ibfk_1` FOREIGN KEY (`Type_ID`) REFERENCES `Category` (`ID`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
