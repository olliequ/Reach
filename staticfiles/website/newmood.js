document.addEventListener('DOMContentLoaded', function() {

let i = document.querySelector('#Happy');
i.addEventListener('click', () => {console.log('hi'); location.href = "#slept"})
i = document.querySelector('#Stressed');
i.addEventListener('click', () => location.href = "#slept")
i = document.querySelector('#Excited');
i.addEventListener('click', () => location.href = "#slept")
i = document.querySelector('#Sad');
i.addEventListener('click', () => location.href = "#slept")

i = document.querySelector('#eight');
i.addEventListener('click', () => location.href = "#food")
i = document.querySelector('#six');
i.addEventListener('click', () => location.href = "#food")
i = document.querySelector('#two');
i.addEventListener('click', () => location.href = "#food")
i = document.querySelector('#one');
i.addEventListener('click', () => location.href = "#food")

i = document.querySelector('#three');
i.addEventListener('click', () => location.href = "#friends")
i = document.querySelector('#twos');
i.addEventListener('click', () => location.href = "#friends")
i = document.querySelector('#ones');
i.addEventListener('click', () => location.href = "#friends")
i = document.querySelector('#coffee');
i.addEventListener('click', () => location.href = "#friends")

i = document.querySelector('#friend');
i.addEventListener('click', () => location.href = "#thoughts")
i = document.querySelector('#family');
i.addEventListener('click', () => location.href = "#thoughts")
i = document.querySelector('#date');
i.addEventListener('click', () => location.href = "#thoughts")
i = document.querySelector('#none');
i.addEventListener('click', () => location.href = "#thoughts")

})