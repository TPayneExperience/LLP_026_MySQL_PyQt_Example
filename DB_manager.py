#!/usr/bin/python

import mysql.connector
from mysql.connector import errorcode
from datetime import datetime

##===============================================

class DatabaseUtility: 
	def __init__(self, database, tableName):
		self.db = database
		self.tableName = tableName

		f = open('C:\\Users\\The_Captain\\Desktop\\TPayne Experience\\_Episodes\\_LetsLearn\\026_LLP__SQL_Databases\\password.txt', 'r')
		p = f.read(); f.close();
		self.cnx = mysql.connector.connect(user = 'root',
									password = p,
									host = '127.0.0.1')
		self.cursor = self.cnx.cursor()

		self.ConnectToDatabase()
		self.CreateTable()
		
	def ConnectToDatabase(self):
		try:
			self.cnx.database = self.db
		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_BAD_DB_ERROR:
				self.CreateDatabase()
				self.cnx.database = self.db
			else:
				print(err.msg)

	def CreateDatabase(self):
		try:
			self.RunCommand("CREATE DATABASE %s DEFAULT CHARACTER SET 'utf8';" %self.db)
		except mysql.connector.Error as err:
			print("Failed creating database: {}".format(err))

	def CreateTable(self):
		cmd = (" CREATE TABLE IF NOT EXISTS " + self.tableName + " ("
			" `ID` int(5) NOT NULL AUTO_INCREMENT,"
			" `date` date NOT NULL,"
			" `time` time NOT NULL,"
			" `message` char(50) NOT NULL,"
			" PRIMARY KEY (`ID`)"
			") ENGINE=InnoDB;")
		self.RunCommand(cmd)

	def GetTable(self):
		self.CreateTable()
		return self.RunCommand("SELECT * FROM %s;" % self.tableName)

	def GetColumns(self):
		return self.RunCommand("SHOW COLUMNS FROM %s;" % self.tableName)

	def RunCommand(self, cmd):
		print ("RUNNING COMMAND: " + cmd)
		try:
			self.cursor.execute(cmd)
		except mysql.connector.Error as err:
			print ('ERROR MESSAGE: ' + str(err.msg))
			print ('WITH ' + cmd)
		try:
			msg = self.cursor.fetchall()
		except:
			msg = self.cursor.fetchone()
		return msg

	def AddEntryToTable(self, message):
		date1 = datetime.now().strftime("%y-%m-%d")
		time = datetime.now().strftime("%H:%M")
		
		cmd = " INSERT INTO " + self.tableName + " (date, time, message)"
		cmd += " VALUES ('%s', '%s', '%s' );" % (date1, time, message)
		self.RunCommand(cmd)

	def __del__(self):
		self.cnx.commit()
		self.cursor.close()
		self.cnx.close()

##===============================================
##===============================================


if __name__ == '__main__':
	db = 'myFirstDB'
	tableName = 'test8'

	dbu = DatabaseUtility(db, tableName)

	# dbu.AddEntryToTable ('testing')
	# dbu.AddEntryToTable ('testing2')
	# print (dbu.GetColumns())
	# print (dbu.GetTable())
	
