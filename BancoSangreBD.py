import pymysql

myconection = pymysql.connect(host= "localhost", user= "root", password= "")

con = myconection.cursor()

con.execute("CREATE DATABASE IF NOT EXISTS bancodesangre;")

tiposangre = """ CREATE TABLE IF NOT EXISTS tiposangre(
    codigo tinyint unsigned AUTO_INCREMENT NOT NULL,
    tiposangre VARCHAR(9) NOT NULL,
    rh VARCHAR(2) NOT NULL,

    PRIMARY KEY (codigo)
);"""

tipodocumento = """CREATE TABLE IF NOT EXISTS tipodocumento(
    codigo tinyint unsigned AUTO_INCREMENT not null,
    tipodocumento VARCHAR(22) NOT NULL,

    PRIMARY KEY (codigo)
);"""

donante = """CREATE TABLE IF NOT EXISTS donante (
    id int unsigned AUTO_INCREMENT NOT NULL,
    tipodocumento tinyint unsigned NOT NULL,
    numerodocumento BIGINT NOT NULL,
    primerapellido VARCHAR(255) NOT NULL,
    primernombre VARCHAR(255) NOT NULL,
    segundoapellido VARCHAR(255) NOT NULL,
    segundonombre VARCHAR(255) NOT NULL,
    tiposangre tinyint unsigned NOT NULL,
    fechanacimiento DATE NOT NULL,
    fechaultdonacion DATE,
    direccion VARCHAR(255),
    telefono VARCHAR(16),
    celular VARCHAR(16),
    correo VARCHAR(255) NOT NULL,

    PRIMARY KEY (id),
    FOREIGN KEY (tipodocumento) REFERENCES tipodocumento (codigo),
    FOREIGN KEY (tiposangre) REFERENCES tiposangre (codigo)
);"""

bolsadesangre = """CREATE TABLE IF NOT EXISTS bolsadesangre(
    numerobolsa int unsigned AUTO_INCREMENT not null,
    tiposangre tinyint unsigned not null,
    fechadonacion date not null,
    fechacaducidad date not null,
    
    PRIMARY KEY (numerobolsa),
    FOREIGN KEY (tiposangre) REFERENCES tiposangre(codigo)
);"""

estado = """CREATE TABLE IF NOT EXISTS estado(
    codigo tinyint unsigned AUTO_INCREMENT not null,
    estado varchar(12) not null,
    
    PRIMARY KEY (codigo)    
);"""

personascontacto = """CREATE TABLE IF NOT EXISTS personascontacto (
    id tinyint unsigned AUTO_INCREMENT NOT NULL,
    tipodocumento tinyint unsigned NOT NULL,
    numerodocumento BIGINT NOT NULL,
    primerapellido VARCHAR(255) NOT NULL,
    primernombre VARCHAR(255) NOT NULL,
    segundoapellido VARCHAR(255) NOT NULL,
    segundonombre VARCHAR(255) NOT NULL,
    celular VARCHAR(16),
    correo VARCHAR(255) NOT NULL,

    PRIMARY KEY (id),
    FOREIGN KEY (tipodocumento) REFERENCES tipodocumento (codigo)
);"""

hospital = """CREATE TABLE IF NOT EXISTS hospital (
    nit int unsigned NOT NULL,
    nombrehospital VARCHAR(255) NOT NULL,
    contacto tinyint unsigned NOT NULL,
    correo VARCHAR(255) NOT NULL,
    direccion VARCHAR(255) NOT NULL,
    telefono VARCHAR(16),

    PRIMARY KEY (nit),
    FOREIGN KEY (contacto) REFERENCES personascontacto (id)
);"""

formatodesolicitud = """CREATE TABLE IF NOT EXISTS formatodesolicitud (
    numerosolicitud int unsigned AUTO_INCREMENT NOT NULL,
    estado tinyint unsigned NOT NULL,
    numerodebolsas smallint unsigned NOT NULL,
    fechasolicitud date NOT NULL,
    nit int unsigned NOT NULL,
    tiposangre tinyint unsigned NOT NULL,

    PRIMARY KEY (numerosolicitud),
    FOREIGN KEY (estado) REFERENCES estado (codigo),
    FOREIGN KEY (nit) REFERENCES hospital (nit),
    FOREIGN KEY (tiposangre) REFERENCES tiposangre (codigo)
);"""

formatoentrega = """CREATE TABLE IF NOT EXISTS formatoentrega (
    numeroentrega int unsigned AUTO_INCREMENT NOT NULL,
    numerosolicitud int unsigned NOT NULL,
    numerobolsa int unsigned NOT NULL,
    fechaentrega date NOT NULL,

    PRIMARY KEY (numeroentrega),
    FOREIGN KEY (numerobolsa) REFERENCES bolsadesangre (numerobolsa)
);"""

con.execute("USE bancodesangre;")

con.execute(tiposangre)
con.execute(tipodocumento)
con.execute(donante)
con.execute(bolsadesangre)
con.execute(estado)
con.execute(personascontacto)
con.execute(hospital)
con.execute(formatodesolicitud)
con.execute(formatoentrega)

sql = "INSERT INTO tiposangre (tiposangre, rh) VALUES (%s,%s);"
val = [
    ('A', '+'),
    ('A', '-'),
    ('B', '+'),
    ('B', '-'),
    ('AB', '+'),
    ('AB', '-'),
    ('O', '+'),
    ('O', '-'),
]

con.executemany(sql,val)
myconection.commit() #sube los datos a la DB

print(f"Se han insertado {con.rowcount} registros")

sql = "INSERT INTO estado (estado) VALUES (%s);"
val = [
    ('Parcial'),
    ('Pendiente'),
    ('Entregado'),
    ('Anulado'),
]

con.executemany(sql,val)
myconection.commit() #sube los datos a la DB

print(f"Se han insertado {con.rowcount} registros")

sql = "INSERT INTO tipodocumento (tipodocumento) VALUES (%s);"
val = [
    ('Cedula de Ciudadania'),
    ('Cedula de Extranjeria'),
    ("Pasaporte")
]

con.executemany(sql,val)
myconection.commit() #sube los datos a la DB

print(f"Se han insertado {con.rowcount} registros")

con.close()