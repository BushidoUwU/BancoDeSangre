//Andres Rozo

let mysql = require("mysql"); //importar libreria para la conexion de la base de datos

const express = require("express"); //importar libreria de express

const app = express(); //estableze el cursor para usar express

let conection = mysql.createConnection({ //inicia la conexion con el servidor gestor de base de datos
    host: "localhost",
    user: "root",
    password: "",
    database: "bancodesangre",
});

//estableze el archivo a mostrar
app.use(express.static("views"))
//transforma los datos de la pagina en codigo legible por el programa
app.use(express.urlencoded({extended:false}));

//se le indica que muestre el archivo ejs
app.set("view engine", "ejs");

// Ruta para la vista de la pagina
app.get('/', function(req, res) {
    res.render('index'); // Renderiza la vista index.ejs
  });

//busca y ejecuta todo en la carpeta public
app.use(express.static("public"));
  
//captura los datos de la accion /validar para usarlos como codigo
app.post("/validardonador", function(req,res){
    const datos = req.body;

    let tipodocumento = datos.documenttype;
    let numerodocumento = datos.documentnumber;
    let primerapellido = datos.firstlastname;
    let primernombre = datos.firstname;
    let segundoapellido = datos.secondlastname;
    let segundonombre = datos.secondname;
    let tiposangre = datos.bloodtype;
    let nacimiento = datos.birthdate;
    let ultimadonacion = datos.lastdatedonation;
    let direccion = datos.address;
    let telefono = datos.phone;
    let celular = datos.cellphone;
    let correo = datos.mail;

    let buscar = "SELECT * FROM donante WHERE numerodocumento = "+numerodocumento+" AND tipodocumento = "+tipodocumento+"";

    conection.query(buscar, function(error, row){
        if(error){
            throw error;
        }else{

            if(row.length>0){
                console.log("No se puede registrar, el usuario ya existe");
            } else{
                let registrar = `
                    INSERT INTO donante (tipodocumento, numerodocumento, primerapellido, primernombre, segundoapellido, segundonombre, tiposangre, fechanacimiento, fechaultdonacion, direccion, telefono, celular, correo)
                    VALUES (`+tipodocumento+`,`+numerodocumento+`,"`+primerapellido+`","`+primernombre+`","`+segundoapellido+`","`+segundonombre+`",`+tiposangre+`,"`+nacimiento+`","`+ultimadonacion+`","`+direccion+`","`+telefono+`","`+celular+`","`+correo+`")
                `;

                conection.query(registrar, function(error){
                    if(error){
                        throw error;
                    }else{
                        console.log("Datos almacenados correctamente")
                    }
                });         
            }
        }
    });

    console.log(datos);
});

app.post("/validarsolicitud",function(req,res){
    const datos = req.body;

    let fechahoy = datos.today;
    let numerobolsas = datos.number_bags;
    let tiposangre = datos.bloodtype;

    let registrar = `
                    INSERT INTO formatodesolicitud (estado, numerodebolsas, fechasolicitud, nit, tiposangre)
                    VALUES (2,`+numerobolsas+`,"`+fechahoy+`",`+nit+`,`+tiposangre+`)
                `;

                conection.query(registrar, function(error){
                    if(error){
                        throw error;
                    }else{
                        console.log("Datos almacenados correctamente")
                    }
                }); 

});

let persona = 1;
app.post("/validarhospital", function(req,res){
    const datos = req.body;

    global.nit = datos.nit;
    let nombrehospital = datos.hospital_name;
    let correoh = datos.mailh;
    let telefono = datos.phone; 
    let direccion = datos.adress;

    let buscarh = "SELECT * FROM hospital WHERE nit = "+nit+"";

    conection.query(buscarh, function(error, row){
        if(error){
            throw error;
        }else{
            let contacto = persona++;
            if(row.length>0){
                console.log("No se puede registrar, el usuario ya existe");
            } else{               
                let registrar = `
                    INSERT INTO hospital (nit, nombrehospital, contacto, correo, direccion, telefono)
                    VALUES (`+nit+`,"`+nombrehospital+`",`+contacto+`,"`+correoh+`","`+direccion+`","`+telefono+`")
                `;

                conection.query(registrar, function(error){
                    if(error){
                        throw error;
                    }else{
                        console.log("Datos almacenados correctamente")
                    }
                });         
            }
        }
    });

});

//captura los datos de la accion /validar para usarlos como codigo
app.post("/validarcontacto", function(req,res){
    const datos = req.body;

    let tipodocumentoc = datos.documenttype;
    let numerodocumentoc = datos.documentnumber;
    let primerapellido = datos.firstlastname;
    let primernombre = datos.firstname;
    let segundoapellido = datos.secondlastname;
    let segundonombre = datos.secondname;
    let celular = datos.cellphone;
    let correo = datos.mailc;

    let buscarc = "SELECT * FROM personascontacto WHERE numerodocumento = "+numerodocumentoc+" AND tipodocumento = "+tipodocumentoc+"";

    conection.query(buscarc, function(error, row){
        if(error){
            throw error;
        }else{

            if(row.length>0){
                console.log("No se puede registrar, el usuario ya existe");
            } else{
                let registrar = `
                    INSERT INTO personascontacto (tipodocumento, numerodocumento, primerapellido, primernombre, segundoapellido, segundonombre, celular, correo)
                    VALUES (`+tipodocumentoc+`,`+numerodocumentoc+`,"`+primerapellido+`","`+primernombre+`","`+segundoapellido+`","`+segundonombre+`","`+celular+`","`+correo+`")
                `;

                conection.query(registrar, function(error){
                    if(error){
                        throw error;
                    }else{
                        console.log("Datos almacenados correctamente")
                    }
                });         
            }
        }
    });  

    console.log(datos);
})

//verifica la conexion de la base de datos
conection.connect(function(err){ 
    if(err){
        throw err;
    }else{
        console.log("conexion exitosa");
    }
});

//crea el servidor en el cual se ejecutara la pagina
app.listen(3000, function(){
    console.log("Servidor creado http://localhost:3000");
})

//conection.end(); //termina la conexion de la base de datos

//ctrl + c para finalizar la conexion