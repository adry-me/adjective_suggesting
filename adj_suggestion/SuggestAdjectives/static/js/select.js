window.addEventListener('load', () => {
    const selectedWords = {};

    // REGION HANDLE WORD CLICK
    (() => {
        const lines = [];
        const hiddenLines = document.querySelector('#hidden-input').querySelectorAll('p')
        hiddenLines.forEach(line => {
            lines.push(line.innerText);
        });

        lines.forEach((line, index) => {
            selectedWords[line] = [];
            const container = document.querySelector(`#original-${index + 1}`);
            const selectedContainer = document.querySelector(`#selected-${index + 1}`);
            const p = document.createElement('p');
            const words = line.split(' ');

            container.appendChild(p);

            words.forEach(word => {
                const newspan = document.createElement('span');
                newspan.innerText = word;

                p.appendChild(newspan);
                p.innerHTML += ' ';
            });

           const spans = p.querySelectorAll('span');
           spans.forEach((span, spanIdx) => {
                let span_tag = `${spanIdx}_open`
                span_tag = !open
                const selP = document.createElement('p');
                selP.id = `${span.innerText.trim()}-${index}-${spanIdx}`;
                selP.classList.add('selected-word-dummy');
                span.addEventListener('click', () => {
                    if (!span_tag) {
                        console.log(span)
                        selP.innerText = span.innerText;
                        selectedContainer.appendChild(selP);
                        span_tag = open;
                        selectedWords[line].push(span.innerText.trim());
                    }

                    else {
                        console.log(span);
                        selP.innerText = span.innerText;
                        selectedContainer.removeChild(selP);
                        span_tag = !open;
                        const index = selectedWords[line].indexOf(span.innerText.trim());
                        if (index > -1) {
                            selectedWords[line].splice(index, 1);
                        };
                    }
                });
            });
        });
    })();

    // REGION ON CHECKBOX CHANGE
    (() => {
        const cbAll = document.querySelector('#all');
        const body = document.querySelector('#AuthorColBody');
        const cbAuthors = {};
        body.querySelectorAll('input[type=checkbox]').forEach(cb => {
            cbAuthors[`cb${cb.id}`] = cb
        });

        let checkedCount = 0;

        cbAll.addEventListener('change', (e) => {
            if (e.target.checked) {
                Object.values(cbAuthors).forEach(cb => cb.checked = true);
                checkedCount = Object.keys(cbAuthors).length;
            }
            if (!e.target.checked) {
                Object.values(cbAuthors).forEach(cb => cb.checked = false);
                checkedCount = 0;
            }
        });

        Object.values(cbAuthors).forEach(author => {
            author.addEventListener('change', (e) => {
                if (!e.target.checked) {
                    cbAll.checked = false;
                    checkedCount--;
                }
                else {
                    checkedCount++;
                    cbAll.checked = checkedCount === Object.keys(cbAuthors).length;
                }
            });
        });
    })();

    // REGION ON CHECK
    (() => {
        let proceedEvtListener;

        let isProcessing = false;
        const btn = document.querySelector('#check-btn');
        const proceedBtn = document.querySelector('#proceed-btn')
        btn.addEventListener('click', () => {
            if (isProcessing) { return; };

            const wordDummies = document.querySelectorAll('.selected-word-dummy');
            wordDummies.forEach(wordDummy => {
                wordDummy.removeAttribute('style');
            });
            const wordList = [];
            Object.values(selectedWords).forEach(l => {
                l.forEach(w => {
                    wordList.push(w);
                });
            });
            isProcessing = true;
            btn.setAttribute('style', 'cursor: default;');
            $.ajax({
                type: 'GET',
                url: '/SuggestAdjectives/api/check/adjective-exists',
                data: {'words': wordList},
                dataType: 'JSON',
                success: (response) => {
                    console.log(response);
                    response.no.forEach(word => {
                        const wordDummies = document.querySelectorAll('.selected-word-dummy');
                        wordDummies.forEach(wordDummy => {
                            if (wordDummy.id.split('-')[0] === word) {
                                wordDummy.setAttribute('style', 'color: red !important');
                            }
                        });
                    });

                    isProcessing = false;
                    btn.removeAttribute('style');
                    proceedBtn.classList.remove('inactive');

                    if (proceedEvtListener) {
                        proceedBtn.removeEventListener('click', proceedEvtListener)
                    };

                    proceedEvtListener = () => {
                        const form = document.querySelector('#proceed-form')

                        const addInput = (n, v) => {
                            const input = document.createElement('input');
                            input.setAttribute('type', 'hidden');
                            input.setAttribute('name', n);
                            input.setAttribute('value', v);

                            form.appendChild(input);
                        }

                        addInput('selected-words', JSON.stringify(selectedWords));


                        if (response.no.length > 0) {
                            const block = document.querySelector('#waiting-screen');
                            block.classList.remove('hidden-object');

                            $.ajax({
                                type: 'GET',
                                url: '/SuggestAdjectives/api/save/adjectives',
                                data: {
                                    'words': response.no,
                                },
                                success: (r) => {
                                    form.submit();
                                },
                                error: (r) => {
                                    return alert('ERROR OCCURRED!')
                                }
                            });
                        }
                        else {
                            form.submit();
                        }
                    };

                    proceedBtn.addEventListener('click', proceedEvtListener)
                },
            });
        });
    })();
});