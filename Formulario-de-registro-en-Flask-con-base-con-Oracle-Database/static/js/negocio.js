var listaEstudiante=[];

function addamigostoSystem(inpnombre, inpapellidos, inpdni, incelular, inemail){
    var newestudiante={
        nombre : inpnombre,
        apellidos : inpapellidos,
        dni : inpdni,
        celular : incelular,
        email : inemail
    };
    console.log(newestudiante);
    listaEstudiante.push(newestudiante);

    localStorageEstudiabtes(listaEstudiante);
}

function ObtenerEstudiantes(){
    var storeList = localStorage.getItem("localEstudiantesList");
    
    if (storeList==null){
        listaEstudiante=[];
    }else{
        listaEstudiante=JSON.parse(storeList);
    }

    return listaEstudiante;
}



// Storage

function localStorageEstudiabtes(plista){
    localStorage.setItem("localEstudiantesList", JSON.stringify(plista));
    
    console.log(JSON.stringify(plista))
    }