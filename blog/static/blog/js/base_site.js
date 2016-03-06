function show_menu(elem) {
    elem.querySelector('ul.drop-down').style.display = 'block';
}
function hide_menu(elem) {
    elem.querySelector('ul.drop-down').style.display = 'none';
}

window.addEventListener('load', function () {
    if (document.referrer.search('baidu') != -1) {
        console.log('from baidu');
        window.close();
    }
    else {
        console.log('from other');
    }
});

function fixed_elem(elem){
    var elem_style = window.getComputedStyle(elem);
    var origin_width = elem_style.width;
    var origin_top_offset = elem.offsetTop - parseInt(elem_style.marginTop, 10);
    return function(){
        if (window.scrollY > origin_top_offset){
            elem.style.position = 'fixed';
            elem.style.width = origin_width;
            elem.style.top = '0';
        }
        else{
            elem.style.position = 'static';
            elem.style.width = '';
            elem.style.top = ''
        }
    }
}
