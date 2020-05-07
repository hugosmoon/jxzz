function create_visit_log(page){
    $.ajax({
        type: 'POST',
        url: "/jxzz_2/create_visit_log/" ,
        data: {
        'page':page,
        'ip':returnCitySN["cip"],
        'city':returnCitySN["cname"]
        } ,   
    });
}