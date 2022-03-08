

function logined(){
    target2 = document.getElementById('signin');
    target2.style.display = 'none';
    target3 = document.getElementById('signup');
    target3.style.display = 'none';
    target = document.getElementById('signout');
    target.style.display = '';
    target4 = document.getElementById('mypage');
    target4.style.display= '';
}

function not_logined(){
    target1 = document.getElementById('signout');
    target1.style.display= 'none';
    target2 = document.getElementById('signin');
    target2.style.display = '';
    target3 = document.getElementById('signup');
    target3.style.display = '';
    target4 = document.getElementById('mypage');
    target4.style.display= 'none';

}




function set_loct_city(object){
    var Kangwon = ['강릉시', '고성군', '동해시', '삼척시',	'속초시',	'양구군',	'양양군',	'영월군',	'원주시',	'인제군',	'정선군',	'철원군',	'춘천시',	'태백시',	'평창군',	'홍천군',	'화천군',	'횡성군'];
    var kyeongki = ['가평군',	'고양시',	'과천시',	'광명시',	'광주시',	'구리시',	'군포시',	'김포시',	'남양주시',	'동두천시',	'부천시',	'성남시',	'수원시',	'시흥시',	'안산시',	'안성시',	'안양시',	'양주시',	'양평군',	'여주시',	'연천군',	'오산시',	'용인시',	'의왕시',	'의정부시',	'이천시',	'파주시',	'평택시',	'포천시',	'하남시',	'화성시'];
    var kyungnam = ['거제시',	'거창군',	'고성군',	'김해시',	'남해군',	'밀양시',	'사천시',	'산청군',	'양산시',	'의령군',	'진주시',	'창녕군',	'창원시',	'통영시',	'하동군',	'함안군',	'함양군',	'합천군'	];
    var kyungbuk  = ['경산시', '경주시',	'고령군',	'구미시',	'군위군',	'김천시',	'문경시',	'봉화군',	'상주시',	'성주군',	'안동시',	'영덕군',	'영양군',	'영주시',	'영천시',	'예천군',	'울릉군',	'울진군',	'의성군',	'청도군',	'청송군',	'칠곡군',	'포항시'	 ];
    var Chungnam = ['계룡시',	'공주시',	'금산군',	'논산시',	'당진시',	'보령시',	'부여군',	'서산시',	'서천군',	'아산시',	'예산군',	'천안시',	'청양군',	'태안군',	'홍성군'	];
    var Chungbuk = ['괴산군',	'단양군',	'보은군',	'영동군',	'옥천군',	'음성군',	'제천시',	'증평군',	'진천군',	'청주시',	'충주시'	];
    var Jeonnam = ['강진군',	'고흥군',	'곡성군',	'광양시',	'구례군',	'나주시',	'담양군',	'목포시',	'무안군',	'보성군',	'순천시',	'신안군',	'여수시',	'영광군',	'영암군',	'완도군',	'장성군',	'장흥군',	'진도군',	'함평군',	'해남군',	'화순군'	];
    var Jeonbuk = ['고창군',	'군산시',	'김제시',	'남원시',	'무주군',	'부안군',	'순창군',	'완주군',	'익산시',	'임실군',	'장수군',	'전주시',	'정읍시',	'진안군'];
    var Seoul = ['강남구',	'강동구',	'강북구',	'강서구',	'관악구',	'광진구',	'구로구',	'금천구',	'노원구',	'도봉구',	'동대문구',	'동작구',	'마포구',	'서대문구',	'서초구',	'성동구',	'성북구',	'송파구',	'양천구',	'영등포구',	'용산구',	'은평구',	'종로구',	'중구',	'중랑구'];
    var Incheon = ['강화군',	'계양구',	'남동구',	'동구',	'미추홀구',	'부평구',	'서구',	'연수구',	'옹진군',	'중구'];
    var Pusan = ['강서구',	'금정구',	'기장군',	'남구',	'동구',	'동래구',	'부산진구',	'북구',	'사상구',	'사하구',	'서구',	'수영구',	'연제구',	'영도구',	'중구',	'해운대구'];
    var Daejoen = ['대덕구',	'동구',	'서구',	'유성구',	'중구'];
    var Daegu = ['남구',	'달서구',	'달성군',	'동구',	'북구',	'서구',	'수성구',	'중구'];
    var Gwangju = ['광산구',	'남구',	'동구',	'북구',	'서구'];
    var Ulsan = ['남구',	'동구',	'북구',	'울주군',	'중구'];
    var Jeju = ['제주시', '서귀포시'];

    var target = document.getElementById('user_loct_city');
    
    if(object.value =='강원도') var d = Kangwon;
    else if(object.value =='경기도') var d = kyeongki;
    else if(object.value =='서울특별시') var d = Seoul;
    else if(object.value=='경상남도') var d = kyungnam;
    else if(object.value=='경상북도') var d = kyungbuk;
    else if(object.value=='전라남도') var d = Jeonnam;
    else if(object.value=='전라북도') var d = Jeonbuk;
    else if(object.value=='충청남도') var d = Chungnam;
    else if(object.value=='충청북도') var d = Chungbuk;
    else if(object.value=='부산광역시') var d = Pusan;
    else if(object.value=='울산광역시') var d = Ulsan;
    else if(object.value=='인천광역시') var d = Incheon;
    else if(object.value=='대구광역시') var d = Daegu;
    else if(object.value=='대전광역시') var d = Daejoen;
    else if(object.value=='광주광역시') var d = Gwangju;
    else if(object.value=='제주시') var d = Jeju;

    target.options.length = 0;
    for (x in d){
        var opt = document.createElement('option');
        opt.value = d[x];
        opt.innerHTML = d[x];
        target.appendChild(opt);
    }
    target.style.display = '';
}

function set_positions(obj){
    var city =  obj.value;
    var state = document.getElementById('user_loct_state');
    var loct = state.value +' ' +city;
    console.log(loct);
    
    
}
    





function open_ch_loct(){
    target1 = document.getElementById('bt1');
    target1.style.display = 'none';
    target2 = document.getElementById('bt2');
    target2.style.display = 'none';
    target3 = document.getElementById('bt3');
    target3.style.display = 'none';
    target4 = document.getElementById('loct_div');
    target4.style.display = '';

}

function close_ch_loct(){
    target1 = document.getElementById('bt1');
    target1.style.display = '';
    target2 = document.getElementById('bt2');
    target2.style.display = '';
    target3 = document.getElementById('bt3');
    target3.style.display = '';
    target4 = document.getElementById('loct_div');
    target4.style.display = 'none';

}

function open_ch(){
    target1 = document.getElementById('bt1');
    target1.style.display = 'none';
    target2 = document.getElementById('bt2');
    target2.style.display = 'none';
    target3 = document.getElementById('bt3');
    target3.style.display = 'none';
    target4 = document.getElementById('change_div');
    target4.style.display = '';

}

function close_ch(){
    target1 = document.getElementById('bt1');
    target1.style.display = '';
    target2 = document.getElementById('bt2');
    target2.style.display = '';
    target3 = document.getElementById('bt3');
    target3.style.display = '';
    target4 = document.getElementById('change_div');
    target4.style.display = 'none';


}

function open_del(){
    target1 = document.getElementById('bt1');
    target1.style.display = 'none';
    target2 = document.getElementById('bt2');
    target2.style.display = 'none';
    target3 = document.getElementById('bt3');
    target3.style.display = 'none';
    target4 = document.getElementById('del_div');
    target4.style.display = '';

}


function close_del(){
    target1 = document.getElementById('bt1');
    target1.style.display = '';
    target2 = document.getElementById('bt2');
    target2.style.display = '';
    target3 = document.getElementById('bt3');
    target3.style.display = '';
    target4 = document.getElementById('del_div');
    target4.style.display = 'none';

}


