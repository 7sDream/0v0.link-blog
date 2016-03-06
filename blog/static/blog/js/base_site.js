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

(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');

ga('create', 'UA-74761842-1', 'auto');
ga('send', 'pageview');
