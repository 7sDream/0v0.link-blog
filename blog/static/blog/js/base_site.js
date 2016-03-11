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
        if (window.scrollY > origin_top_offset && elem.style.position !== 'fixed'){
            elem.style.position = 'fixed';
            elem.style.width = origin_width;
            elem.style.top = '0';
        }
        else if (window.scrollY <= origin_top_offset){
            elem.style.position = '';
            elem.style.width = '';
            elem.style.top = ''
        }
    }
}

function scroll_to_top(speed){
    if (scroll_to_top.s_timeout_id === undefined){
        (function by_five(){
            if(window.scrollY > 1){
                window.scrollTo(0, window.scrollY * speed);
                scroll_to_top.s_timeout_id = setTimeout(by_five, 10);
            }
            else {
                window.scrollTo(0, 0);
                clearTimeout(scroll_to_top.s_timeout_id);
                scroll_to_top.s_timeout_id = undefined;
            }
        })();
    }
    return false;
}

function search_validator(form) {
    var value = form.keyword.value;
    if (value === null || value === '') {
        alert('搜索参数不能为空哒！');
        return false;
    }
    return true;
}

(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');

ga('create', 'UA-74761842-1', 'auto');
ga('send', 'pageview');
