async function loadUsers(){

const response=await fetch("http://BACKEND_PUBLIC_IP:5000/users");

const data=await response.json();

let list=document.getElementById("users");

list.innerHTML="";

data.forEach(user=>{

list.innerHTML+=`<li>${user.name}</li>`;

});

}
