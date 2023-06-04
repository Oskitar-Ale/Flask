//BOTON PARA GUARDAR LOS DATOS DEL FORMULARIO

document.querySelector("#btn-guardar").addEventListener('click',guardarEstudiante);


listarTablaEstudiante();

function guardarEstudiante(){
    var gnombre = document.querySelector("#lbnombre").value,
        gapellidos = document.querySelector("#lbapellidos").value,
        gdni = document.querySelector("#lbdni").value,
        gcelular = document.querySelector("#lbcel").value,
        gemail = document.querySelector("#lbmail").value

        addamigostoSystem(gnombre, gapellidos, gdni, gcelular,gemail );
        listarTablaEstudiante();

    }
    



//CREACION DE LAS COLUMNAS CON LOS DATOS OBTENIDOS DEL FORMULARIO

function listarTablaEstudiante(){
    var ListaEstudiante = ObtenerEstudiantes(),
        tbody=document.querySelector("#TablaEstudiantes tbody");

    tbody.innerHTML='';

    for(var i=0; i < ListaEstudiante.length; i++){
        var row = tbody.insertRow(0), //Iniciar por la primera fila de la tabla
            nombreCell =row.insertCell(0),
            apellidosCell=row.insertCell(1),
            dniCell=row.insertCell(2),
            celularCell=row.insertCell(3),
            emailCell=row.insertCell(4);



        nombreCell.innerHTML=ListaEstudiante[i].nombre;
        apellidosCell.innerHTML=ListaEstudiante[i].apellidos;
        dniCell.innerHTML=ListaEstudiante[i].dni;
        celularCell.innerHTML=ListaEstudiante[i].celular;
        emailCell.innerHTML=ListaEstudiante[i].email;


        tbody.appendChild(row);
    }

}
