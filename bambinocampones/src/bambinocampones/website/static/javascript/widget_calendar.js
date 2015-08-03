var dados_globais;

function maxDays(mm, yyyy){
    var mDay;
    if((mm == 3) || (mm == 5) || (mm == 8) || (mm == 10)){
        mDay = 30;
    } else {
        mDay = 31;
        if(mm == 1){
            if (yyyy/4 - parseInt(yyyy/4) != 0){
                mDay = 28;
            } else {
                mDay = 29;
            }
        }
    }
    return mDay;
}
function getEventByMonthYear(par_month, par_year){

    var evtJan = new Array();
    var evtFev = new Array();
    var evtMar = new Array();
    var evtAbr = new Array();
    var evtMai = new Array();
    var evtJun = new Array();
    var evtJul = new Array();
    var evtAgo = new Array();
    var evtSet = new Array();
    var evtOut = new Array();
    var evtNov = new Array();
    var evtDez = new Array();

    var obj = eval(dados_globais);

    var evento = "";

    for (var i = 0; i < obj.length; i++) {

        dt_evento = new Date(obj[i].fields.data_agendamento);
        mes_evento = dt_evento.getMonth() + 1;
        data_evento = dt_evento.getDate() + "/" + mes_evento + "/" + dt_evento.getFullYear();
        tipo_evento = obj[i].fields.tipo;
        titulo_evento = obj[i].fields.titulo;

        evento = data_evento + ";" + tipo_evento + ";" + titulo_evento;

        if (mes_evento==1) {
            evtJan.push(evento);
        } else if (mes_evento==2) {
            evtFev.push(evento);
        } else if (mes_evento==3) {
            evtMar.push(evento);
        } else if (mes_evento==4) {
            evtAbr.push(evento);
        } else if (mes_evento==5) {
            evtMai.push(evento);
        } else if (mes_evento==6) {
            evtJun.push(evento);
        } else if (mes_evento==7) {
            evtJul.push(evento);
        } else if (mes_evento==8) {
            evtAgo.push(evento);
        } else if (mes_evento==9) {
            evtSet.push(evento);
        } else if (mes_evento==10) {
            evtOut.push(evento);
        } else if (mes_evento==11) {
            evtNov.push(evento);
        } else if (mes_evento==12) {
            evtDez.push(evento);
        }
    }

    if (par_month==0){
        return evtJan;
    } else if (par_month==1){
        return evtFev;
    } else if (par_month==2){
        return evtMar;
    } else if (par_month==3){
        return evtAbr;
    } else if (par_month==4){
        return evtMai;
    } else if (par_month==5){
        return evtJun;
    } else if (par_month==6){
        return evtJul;
    } else if (par_month==7){
        return evtAgo;
    } else if (par_month==8){
        return evtSet;
    } else if (par_month==9){
        return evtOut;
    } else if (par_month==10){
        return evtNov;
    } else if (par_month==11){
        return evtDez;
    } else {
        var arrEventos = new Array();
        return arrEventos;
    }
}

function writeCalendar(data){
    dados_globais = data;
    var now = new Date;
    var dd = now.getDate();
    var mm = now.getMonth();
    var dow = now.getDay();
    var yyyy = now.getFullYear();
    var arrM = new Array("Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro");
    var arrY = new Array();
    for (ii=0;ii<=4;ii++){
        arrY[ii] = yyyy - 2 + ii;
    }
    var arrD = new Array("Dom","Seg","Ter","Qua","Qui","Sex","Sab");
    var html_content = "";
    html_content = "<form name='calForm' id='calForm'>";
    html_content += "<table border='1' bgcolor='#ffffff' style='margin-bottom: 10px;width: 100%;' class='table'>";
    html_content += "<tr><td>";
    html_content += "<table width='100%'><tr>";
    html_content += "<td align='left'>";
    html_content += "<select name='selMonth' onChange='changeCal();'>";
    for (ii=0;ii<=11;ii++){
        if (ii==mm){
            html_content += "<option value= " + ii + " Selected>" + arrM[ii] + "</option>";
        } else {
            html_content += "<option value= " + ii + ">" + arrM[ii] + "</option>";
        }
    }
    html_content += "</select>";
    html_content += "</td>";
    html_content += "<td align='right'>";
    html_content += "<select name='selYear' onChange='changeCal();'>";
    for (ii=0;ii<=4;ii++) {
        if (ii==2){
            html_content += "<option value= " + arrY[ii] + " Selected>" + arrY[ii] + "</option>";
        } else {
            html_content += "<option value= " + arrY[ii] + ">" + arrY[ii] + "</option>";
        }
    }
    html_content += "</select>";
    html_content += "</td>";
    html_content += "</tr></table>";
    html_content += "</td></tr>";
    html_content += "<tr><td>";
    html_content += "<table border='0' style='width: 100%;'>";
    html_content += "<tr>";
    for (ii=0;ii<=6;ii++){
        html_content += "<td align='center'><span class='label'>" + arrD[ii] + "</span></td>";
    }
    html_content += "</tr>";
    aa = 0;
    for (kk=0;kk<=5;kk++){
        html_content += "<tr>";
        for (ii=0;ii<=6;ii++){
            html_content += "<td align='center'><span id=sp" + aa + ">1</span></td>";
            aa += 1;
        }
        html_content += "</tr>";
    }
    html_content += "</table>";
    html_content += "</td></tr>";
    html_content += "</table>";
    html_content += "</form>";
    document.getElementById('calendarPanel').innerHTML=html_content;
    changeCal();
}
function changeCal(){
    var now = new Date;
    var dd = now.getDate();
    var mm = now.getMonth();
    var dow = now.getDay();
    var yyyy = now.getFullYear();
    var currM = parseInt(document.calForm.selMonth.value);
    var prevM;
    if (currM!=0){
        prevM = currM - 1;
    } else {
        prevM = 11;
    }
    var currY = parseInt(document.calForm.selYear.value);
    arrEventos = getEventByMonthYear(currM, currY);
    var mmyyyy = new Date();
    mmyyyy.setFullYear(currY);
    mmyyyy.setMonth(currM);
    mmyyyy.setDate(1);
    var day1 = mmyyyy.getDay();
    if (day1 == 0){
        day1 = 7;
    }
    var arrN = new Array(41);
    var aa;
    for (ii=0;ii<day1;ii++){
        arrN[ii] = maxDays((prevM),currY) - day1 + ii + 1;
    }
    aa = 1;
    for (ii=day1;ii<=day1+maxDays(currM,currY)-1;ii++){
        arrN[ii] = aa;
        aa += 1;
    }
    aa = 1;
    for (ii=day1+maxDays(currM,currY);ii<=41;ii++){
        arrN[ii] = aa;
        aa += 1;
    }
    for (ii=0;ii<=41;ii++){
        try {
            document.getElementById("sp"+ii).style.backgroundColor = "#FFFFFF";
        } catch(err) {
            document.getElementById("sp"+ii).style.backgroundColor = "#FFFFFF";
        }
    }
    var dCount = 0;
    obj_events = document.getElementById('eventsDescriptions');
    obj_events.innerHTML='';
    for (ii=0;ii<=41;ii++){
        document.getElementById("sp"+ii).style.background = "None";
        if (((ii<7)&&(arrN[ii]>20))||((ii>27)&&(arrN[ii]<20))){
            document.getElementById("sp"+ii).innerHTML = arrN[ii];
            document.getElementById("sp"+ii).className = "c3";
        } else {
            document.getElementById("sp"+ii).innerHTML = arrN[ii];
            if ((dCount==0)||(dCount==6)){
                document.getElementById("sp"+ii).className = "c2";
            } else {
                document.getElementById("sp"+ii).className = "c1";
            }
            if ((arrN[ii]==dd)&&(mm==currM)&&(yyyy==currY)){
                document.getElementById("sp"+ii).style.backgroundColor="#eeeeee";
            }
            if (arrEventos.length==0) {
                obj_events.innerHTML="Sem atividades neste mês."
            } else {
                for (xx=0;xx<arrEventos.length;xx++){
                    xxDados  = arrEventos[xx];
                    xxDadosArr = xxDados.split(";");
                    xxData   = xxDadosArr[0];
                    xxDataArr = xxData.split("/");
                    xxDia = parseInt(xxDataArr[0]);
                    xxMes = parseInt(xxDataArr[1]);
                    xxAno = parseInt(xxDataArr[2]);
                    xxTipo  = xxDadosArr[1];
                    xxDescr = xxDadosArr[2];
                    xxSpan='';
                    if ((arrN[ii]==xxDia)&&(xxMes==currM+1)&&(xxAno==currY)) {
                        if (xxTipo=='F'){
                            xxSpan = "<img src='/static/images/festa_bkp.png' class='activity_bkg' />";
                            document.getElementById("sp"+ii).style.background="url('/static/images/festa_bkp.png')";
                        } else if (xxTipo=='E'){
                            xxSpan = "<img src='/static/images/evento_bkp.png' class='activity_bkg' />";
                            document.getElementById("sp"+ii).style.background="url('/static/images/evento_bkp.png')";
                        } else if (xxTipo=='N'){
                            xxSpan = "<img src='/static/images/feriado_bkp.png' class='activity_bkg' />";
                            document.getElementById("sp"+ii).style.background="url('/static/images/feriado_bkp.png')";
                        } else if (xxTipo=='P'){
                            xxSpan = "<img src='/static/images/ponte_bkp.png' class='activity_bkg' />";
                            document.getElementById("sp"+ii).style.background="url('/static/images/ponte_bkp.png')";
                        } else if (xxTipo=='R'){
                            xxSpan = "<img src='/static/images/recesso_bkp.png' class='activity_bkg' />";
                            document.getElementById("sp"+ii).style.background="url('/static/images/recesso_bkp.png')";
                        }
                        obj_events.innerHTML+=xxSpan + ' ' + xxDia + '/' + xxMes + ' - ' + xxDescr + '</br>';
                    }
                }
            }
        }
        dCount += 1;
        if (dCount>6){
            dCount=0;
        }
    }
}
