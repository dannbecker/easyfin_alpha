document.querySelector('button').addEventListener('click', function () {
    var cep = document.querySelector('#cep');
    cep = cep.value.replace('-', '');
    fetch("https://viacep.com.br/ws/"+ cep +"/json/")
        .then((response) => {
//            console.log(JSON.parse(response.responseText));
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

