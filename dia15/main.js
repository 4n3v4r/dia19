const textarea = document.querySelector("textarea");
const counter = document.querySelector(".counter");

function contarCaracteres()
{
    const caracteresDigitados = textarea.value.length;
    counter.textContent = caracteresDigitados;
}