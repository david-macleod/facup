from pprint import pprint
import itertools
import json

pyramid = {} 

#PREMIER LEAGUE

for y in range(1993, 2016):
    pyramid[y]= {1: {11: {'name': 'PREMIER LEAGUE',
										'nteams': 20,
										'pro': [], 
										'rel' : [21]
										}
							   }
						 }

for y in range(1993, 1996):
	pyramid[y][1][11]['nteams'] = 22
	

#DIVISION ONE

nteams = {}

for y in itertools.chain(range(1920, 1940),
									range(1947, 1988),
									range(1991, 1993)):
	nteams[y] = 22

nteams[1988] = 21

for y in itertools.chain(range(1905, 1916),
									range(1989, 1991)):
	nteams[y] = 20
	
for y in range(1898, 1905):
	nteams[y] = 18
	
for y in range(1892, 1898):
	nteams[y] = 16

nteams[1891] = 14

for y in range(1888, 1892):
	nteams[y] = 12
									
	
for y in itertools.chain(range(1888, 1916),
									range(1920, 1940),
									range(1947, 1993)):
    pyramid[y] = {1: {11: {'name': 'FIRST DIVISION',
									   'nteams': nteams[y],
									   'pro': [], 
									   'rel': [21]
                                       }
                                 }
					      }
				  
# CHAMPIONSHIP

for y in range(2005, 2016):
    pyramid[y][2] =  {21: {'name': 'CHAMPIONSHIP',
									     'nteams': 24,
									     'pro': [11], 
									     'rel': [31]
										 }
							    }
								
# DIVISION ONE (2)
								
for y in range(1993, 2006):
    pyramid[y][2] =  {21: {'name': 'FIRST DIVISION',
									     'nteams': 24,
									     'pro': [11], 
									     'rel': [31]
										 }
							    }
							

# DIVISION TWO

nteams = {}

for y in range(1989, 1993):
	nteams[y] = 24
	
nteams[1988] = 23

for y in itertools.chain(range(1920, 1940),
									range(1947, 1988)):
	nteams[y] = 22
	
for y in range(1906, 1916):
	nteams[y] = 20
	
for y in range(1899, 1906):
	nteams[y] = 18
	
for y in range(1895, 1899):
	nteams[y] = 16
	
nteams[1894] = 15
nteams[1893] = 12
	
rel = {}

for y in itertools.chain(range(1959, 1993),
								   range(1921, 1922)):
	rel[y] = [31]
	
for y in itertools.chain(range(1922, 1940),
									range(1947, 1959)):
	rel[y] = [31, 32]
	
for y in itertools.chain(range(1893, 1916),
									range(1920, 1921)):
	rel[y] = []
	
	
for y in itertools.chain(range(1893, 1916),
									range(1920, 1940),
									range(1947, 1993)):
    pyramid[y][2] =  {21: {'name': 'SECOND DIVISION',
									     'nteams': nteams[y],
									     'pro': [11], 
									     'rel': rel[y]
										 }
							    }	

								
# LEAGUE ONE
								
for y in range(2005, 2016):
    pyramid[y][3] =  {31: {'name': 'LEAGUE ONE',
									     'nteams': 24,
									     'pro': [21], 
									     'rel': [41]
										 }
							    }
								
# DIVISION TWO (2)
								
for y in range(1993, 2005):
    pyramid[y][3] =  {31: {'name': 'SECOND DIVISION',
									     'nteams': 24,
									     'pro': [21], 
									     'rel': [41]
										 }
							    }
								
# DIVISION THREE
								
for y in range(1959, 1993):
    pyramid[y][3] =  {31: {'name': 'THIRD DIVISION',
									     'nteams': 24,
									     'pro': [21], 
									     'rel': [41]
										 }
							    }

for y in range(1952, 1959):
    pyramid[y][3] =  {31: {'name': 'THIRD DIVISION NORTH',
									     'nteams': 24,
									     'pro': [21], 
									     'rel': ['NA']
										 },
								32: {'name': 'THIRD DIVISION SOUTH',
											 'nteams': 24,
											 'pro': [21], 
											 'rel': ['NA']
											 }
									}	
									
for y in range(1947, 1952):
    pyramid[y][3] =  {31: {'name': 'THIRD DIVISION NORTH',
									     'nteams': 22,
									     'pro': [21], 
									     'rel': ['NA']
										 },
								32: {'name': 'THIRD DIVISION SOUTH',
											 'nteams': 22,
											 'pro': [21], 
											 'rel': ['NA']
											 }
									}	

for y in itertools.chain(range(1933, 1940),
									range(1924, 1932)):
    pyramid[y][3] =  {31: {'name': 'THIRD DIVISION NORTH',
									     'nteams': 22,
									     'pro': [21], 
									     'rel': ['NA']
										 },
								32: {'name': 'THIRD DIVISION SOUTH',
											 'nteams': 22,
											 'pro': [21], 
											 'rel': ['NA']
											 }
									}
									
for y in range(1932, 1933):
    pyramid[y][3] =  {31: {'name': 'THIRD DIVISION NORTH',
									     'nteams': 22,
									     'pro': [21], 
									     'rel': ['NA']
										 },
								32: {'name': 'THIRD DIVISION SOUTH',
											 'nteams': 21,
											 'pro': [21], 
											 'rel': ['NA']
											 }
									}		

for y in range(1922, 1924):
    pyramid[y][3] =  {31: {'name': 'THIRD DIVISION NORTH',
									     'nteams': 22,
									     'pro': [21], 
									     'rel': ['NA']
										 },
								32: {'name': 'THIRD DIVISION SOUTH',
											 'nteams': 20,
											 'pro': [21], 
											 'rel': ['NA']
											 }
									}									
									
			
for y in range(1921, 1922):
    pyramid[y][3] =  {31: {'name': 'THIRD DIVISION',
									     'nteams': 22,
									     'pro': [21], 
									     'rel': ['NA']
										 }
							    }									

								
# LEAGUE TWO
								
for y in range(2005, 2016):
    pyramid[y][4] =  {41: {'name': 'LEAGUE TWO',
									     'nteams': 24,
									     'pro': [31], 
									     'rel': [501]
										 }
							    }
								
								
# THIRD DIVISION (2)

for y in range(1996, 2005):
    pyramid[y][4] =  {41: {'name': 'THIRD DIVISION',
									     'nteams': 24,
									     'pro': [31], 
									     'rel': ['NA']
										 }
							    }	
								
for y in range(1993, 1996):
    pyramid[y][4] =  {41: {'name': 'THIRD DIVISION',
									     'nteams': 22,
									     'pro': [31], 
									     'rel': ['NA']
										 }
							    }

for y in range(1992, 1993):
    pyramid[y][4] =  {41: {'name': 'FOURTH DIVISION',
									     'nteams': 23,
									     'pro': [31], 
									     'rel': ['NA']
										 }
							    }		

for y in range(1959, 1992):
    pyramid[y][4] =  {41: {'name': 'FOURTH DIVISION',
									     'nteams': 22,
									     'pro': [31], 
									     'rel': ['NA']
										 }
							    }								


								
# NATIONAL LEAGUE								
								
								
json.dumps(pyramid)
								
#pprint(pyramid) 