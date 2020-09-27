const collectIDs = (tag) => {
    let id = [];
    document.querySelectorAll("*").forEach(elem => {
       if (elem.id && elem.id.includes(tag)) {
        id.push(elem.id);
       }
    });

    return id;
};

const createInput = (name, text) => {
    const input = document.createElement('input');
    input.setAttribute('type', 'hidden');
    input.setAttribute('name', name);
    input.setAttribute('value', text);

    return input;
};

window.addEventListener('load', () => {
//    const sentenceIDs = collectIDs('sentence');
//    sentenceIDs.forEach(elem => {
//        console.log(elem);
//        const div = document.querySelector('#' + elem);
//        const input = createInput(elem, div.querySelector('p').innerText);
//        div.appendChild(input);
//    });

    const adjIDs = collectIDs('adj');
    adjIDs.forEach(elem => {
        console.log(elem);
        const div = document.querySelector('#' + elem);
        const input = createInput(elem, div.querySelector('p').innerText);
        div.appendChild(input);

        const container = div.parentElement;
        const synContainer = container.querySelector('.sentence-container')
        const btn = div.querySelector('.open-button');
        const btnImg = btn.querySelector('img');
        let open = true;

        btn.addEventListener('click', () => {
            open = !open;
            if (open) {
                btnImg.setAttribute('src', '/static/img/open.svg')
                container.classList.remove('suggest-closed')
                synContainer.classList.remove('sentence-hidden')

            }
            else {
                btnImg.setAttribute('src', '/static/img/close.svg')
                container.classList.add('suggest-closed')
                synContainer.classList.add('sentence-hidden')
            }
        });
    });

    const synonymIDs = collectIDs('synonym');
    synonymIDs.forEach(elem => {
        console.log(elem);
        const div = document.querySelector('#' + elem);
        const adjDiv = document.querySelector('#' + elem.replace('synonym', 'adj'));
        const paragraphs = div.querySelectorAll('.suggest-word-container');
        const adjParagraph = adjDiv.querySelector('.suggest-word-container');

        let selected = null;

        const select = p => {
            p.classList.add('selected');
            const input = createInput(elem, p.innerText)
            p.appendChild(input);
            selected = input;
        }

        const handle = d => {
            const p = d.querySelector('p');
            d.addEventListener('click', () => {
                if (selected) {
                    selected.remove();
                    selected = null;
                }
                paragraphs.forEach(_d => {
                    const _p = _d.querySelector('p');
                    _p.classList.remove('selected');
                })
                adjParagraph.querySelector('p').classList.remove('selected');

                select(p);
            });
        };
        paragraphs.forEach(handle);
        handle(adjParagraph);
        select(adjParagraph.querySelector('p'));
    });

    const rows = document.querySelector('.suggest-body').querySelectorAll('.suggest-row-container');
    rows.forEach(row => {
        const pTags = row.querySelector('.suggest-original-line').querySelectorAll('p');
        const suggestContainers = document.querySelectorAll('.suggest-adj-sentence-container');
        suggestContainers.forEach(suggestion => {
            suggestion.addEventListener('mouseover', (event) => {
                const adjective = suggestion.querySelector('.adj-content').innerText;
                pTags.forEach(elem => {
                    elem.classList.remove('highlight-adjective');
                    if (elem.id === adjective) {
                        elem.classList.add('highlight-adjective')
                    }
                });
            });
        });
    });
});