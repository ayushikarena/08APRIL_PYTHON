function deleteMovie(id){



fetch(

"/delete/"+id+"/",

{


method:"DELETE",



headers:{


"X-CSRFToken":
getCookie("csrftoken")


}



}


)



.then(
response=>response.json()
)



.then(data=>{



console.log(data);



// Remove movie card


document
.getElementById(
"movie"+id
)
.remove();



// Success message


document
.getElementById(
"message"
)
.innerHTML=
data.message;



})



}





function getCookie(name){


let cookieValue=null;


if(document.cookie){


let cookies=document.cookie.split(';');


for(let i=0;i<cookies.length;i++){


let cookie=cookies[i].trim();



if(cookie.startsWith(name+'=')){


cookieValue=
cookie.substring(
name.length+1
);


break;

}


}


}


return cookieValue;


}