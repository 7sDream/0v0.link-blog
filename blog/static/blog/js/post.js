function image_add_title(content_div) {
    var images = content_div.querySelectorAll('img');
    Array.prototype.slice.call(images).forEach(function (image) {
        image.parentNode.classList.add('img-wrapper');
        var p = '<p class="img-desc"><span>' + image.alt + '</span></p>';
        image.parentNode.insertAdjacentHTML('beforeEnd', p);
    });
}

function build_toc(content_div){
    var toc = document.querySelector('#toc-card');
    var htmlStrings = [];
    var header_num = [0, 0, 0, 0, 0, 0 ,0];
    var current_level = 1;
    var headers = content_div.querySelectorAll('h2, h3, h4, h5, h6');
    if(headers.length === 0){
        toc.style.display = 'none';
        return false;
    }
    try{
        Array.prototype.slice.call(headers).forEach(function(elem){
            var elem_level =  Number(elem.tagName[1]);
            if(elem_level - current_level > 1){
                throw Error('toc level invalid!');
            }
            elem.id = elem.tagName.toLowerCase() + '-' + String(header_num[elem_level]++);
            switch (current_level - elem_level) {
                case 0: {
                    htmlStrings.push('</li><li><a href="#', elem.id, '">', elem.textContent, '</a>');
                    break;
                }
                case -1: { // h2 > h3
                    htmlStrings.push('<ul><li><a href="#', elem.id, '">', elem.textContent, '</a>');
                    break;
                }
                default : { // h3 > h2 or h4 > h2
                    for (; elem_level < current_level; current_level--){
                        htmlStrings.push('</li></ul>');
                    }
                    htmlStrings.push('<li><a href="#', elem.id, '">', elem.textContent, '</a>');
                }
            }
            current_level = elem_level;
        });
    }
    catch(e){
        console.error(e);
        toc.style.display = 'none';
        return false;
    }
    toc.insertAdjacentHTML('beforeend', htmlStrings.join(''));
    return true;
}

function md_to_html() {
    var content_div = document.querySelector('#content');
    var content = content_div.textContent;
    content_div.textContent = '';
    content_div.insertAdjacentHTML('afterbegin', markdown.toHTML(content));
    image_add_title(content_div);
    build_toc(content_div);
}

window.addEventListener('load', md_to_html);

window.addEventListener('scroll', fixed_elem(document.querySelector('#toc-card')));
