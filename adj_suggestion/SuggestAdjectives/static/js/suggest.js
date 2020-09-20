window.addEventListener('load', () => {
    const sentenceDivs = document.getElementsByClassName('sentence-col');
    for (let i = 0; i < sentenceDivs.length; i++) {
        const sentences = sentenceDivs[i].getElementsByTagName('p');
        for (let j = 0; j < sentences.length; j++) {
            //sentences[j].onclick = console.log(sentences[j].innerText);
            sentences[j].addEventListener("click", console.log(sentences[j]));
        }
    }
});