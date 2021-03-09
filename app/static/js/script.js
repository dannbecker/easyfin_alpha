document.addEventListener('DOMContentLoaded', function() {
    
    document.querySelector('#nome').value = '';
    document.querySelector('#rua').value = '';
	document.querySelector('#numero').value = '';
	document.querySelector('#complemento').value = '';
	document.querySelector('#bairro').value = '';
	document.querySelector('#cidade').value = '';
	document.querySelector('#estado').value = '';
    
    document.querySelector('#cep').value = '';
    cep.focus();    

 }, false);


document.querySelector('#search-cep').addEventListener('click', function () {
    var cep = document.querySelector('#cep');
    cep = cep.value.replace('-', '');
    fetch("https://viacep.com.br/ws/"+ cep +"/json/")
        .then((response) => {
            return response.json();
        })
        .then((myContent) => {
            atribuirCampos(myContent);
//           document.querySelector('.par').innerHTML = myContent;
//            document.querySelector('.par').classList.add('box');
        });

}, false);

function atribuirCampos(data)
{
const rua = document.querySelector("#rua");
const complemento = document.querySelector("#complemento");
const bairro = document.querySelector("#bairro");
const cidade = document.querySelector("#cidade");
const estado = document.querySelector("#estado");

rua.value = data.logradouro;
complemento.value = data.complemento;
bairro.value = data.bairro;
cidade.value = data.localidade;
estado.value = data.uf;
}