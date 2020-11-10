create database Khounpaserd
on primary
(name = Khounpaserd01,
filename = 'D:\Mydatabase\Khounpaserd01.mdf',
Size = 5, maxsize = 20, filegrowth = 1)
log on
(name = Khounpaserd,
filename = 'D:\Mydatabase\Khounpaserd01.log',
Size = 3, maxsize = 5, filegrowth = 1)
