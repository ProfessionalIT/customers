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
    // F-Festa; E-Evento;
    if (par_month==0){
        var arrEventos = new Array('5/01/2015;E;Volta as aulas.');
        return arrEventos;
    } else if (par_month==1){
        var arrEventos = new Array('02/02/2015;F;Nossa Senhora dos Navegantes','03/02/2015;F;Aniversário da Escola', '16/02/2015;P;Ponte Carnaval', '17/02/2015;N;Carnaval');
        return arrEventos;
    } else if (par_month==2){
        var arrEventos = new Array('06/3/2015;E;Reunião com os Pais');
        return arrEventos;
    } else if (par_month==3){
        var arrEventos = new Array('03/04/2015;N;Sexta-Feira da Paixão', '05/04/2015;N;Páscoa', '21/04/2015;N;Tiradentes');
        return arrEventos;
    } else if (par_month==4){
        var arrEventos = new Array('01/05/2015;N;Dia do Trabalhor', '10/05/2015;E;Dia das Mães');
        return arrEventos;
    } else if (par_month==5){
        var arrEventos = new Array('04/06/2015;N;Corpus Christi', '26/06/2015;F;Festa Junina');
        return arrEventos;
    } else if (par_month==6){
        var arrEventos = new Array();
        return arrEventos;
    } else if (par_month==7){
        var arrEventos = new Array('10/8/2012;E;Homenagem aos Pais');
        return arrEventos;
    } else if (par_month==8){
        var arrEventos = new Array('07/9/2012;N;Independência do Brasil', '20/9/2012;N;Revolução Farroupilha', '21/9/2012;P;(Ponte)');
        return arrEventos;
    } else if (par_month==9){
        var arrEventos = new Array('12/10/2012;N;Nossa Sra Aparecida');
        return arrEventos;
    } else if (par_month==10){
        var arrEventos = new Array('03/11/2013;E;Format. Dança Gaúcha', '29/11/2013;E;Formatura Jardim B');
        return arrEventos;
    } else if (par_month==11){
        var arrEventos = new Array('03/12/2014;E;Apresentação de Ballet - 19:00 hs.',
                                   '11/12/2014;E;Apresentação de Capoeira - 19:00 hs.',
                                   '12/12/2014;E;Encerramento do Ano e Chegada do Papai Noel - 15:00 hs.',
                                   '15/12/2014;R;Recesso Fim de Ano.',
                                   '16/12/2014;R;Recesso Fim de Ano.',
                                   '17/12/2014;R;Recesso Fim de Ano.',
                                   '18/12/2014;R;Recesso Fim de Ano.',
                                   '19/12/2014;R;Recesso Fim de Ano.',
                                   '22/12/2014;R;Recesso Fim de Ano.',
                                   '23/12/2014;R;Recesso Fim de Ano.',
                                   '24/12/2014;R;Recesso Fim de Ano.',
                                   '26/12/2014;R;Recesso Fim de Ano.',
                                   '29/12/2014;R;Recesso Fim de Ano.',
                                   '30/12/2014;R;Recesso Fim de Ano.',
                                   '31/12/2014;R;Recesso Fim de Ano.',
                                   '25/12/2014;N;Feriado de Natal.');
        return arrEventos;
    } else {
        var arrEventos = new Array();
        return arrEventos;
    }
}
function writeCalendar(){
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
    html_content += "<table border='1' bgcolor='#ffffff' style='float:left;margin-bottom: 10px;'>";
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
    html_content += "<table border='0'>";
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
            //eval("sp"+ii).style.backgroundColor = "#FFFFFF";
            document.getElementById("sp"+ii).style.backgroundColor = "#FFFFFF";
        } catch(err) {
            document.getElementById("sp"+ii).style.backgroundColor = "#FFFFFF";
        }
    }
    var dCount = 0;
    obj_events = document.getElementById('eventsDescriptions');
    obj_events.innerHTML='';
    for (ii=0;ii<=41;ii++){
        //eval("sp"+ii).style.background='None';
        document.getElementById("sp"+ii).style.background = "None";
        if (((ii<7)&&(arrN[ii]>20))||((ii>27)&&(arrN[ii]<20))){
            //eval("sp"+ii).innerHTML = arrN[ii];
            document.getElementById("sp"+ii).innerHTML = arrN[ii];
            //eval("sp"+ii).className = "c3";
            document.getElementById("sp"+ii).className = "c3";
        } else {
            //eval("sp"+ii).innerHTML = arrN[ii];
            document.getElementById("sp"+ii).innerHTML = arrN[ii];
            if ((dCount==0)||(dCount==6)){
                //eval("sp"+ii).className = "c2";
                document.getElementById("sp"+ii).className = "c2";
            } else {
                //eval("sp"+ii).className = "c1";
                document.getElementById("sp"+ii).className = "c1";
            }
            if ((arrN[ii]==dd)&&(mm==currM)&&(yyyy==currY)){
                //eval("sp"+ii).style.backgroundColor="#eeeeee";
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
                            xxSpan = "<img src='http://media.bambinocampones.com.br/images/festa_bkp.png' class='activity_bkg' />";
                            //eval("sp"+ii).style.background="url('http://media.bambinocampones.com.br/images/festa_bkp.png')";
                            document.getElementById("sp"+ii).style.background="url('http://media.bambinocampones.com.br/images/festa_bkp.png')";
                        } else if (xxTipo=='E'){
                            xxSpan = "<img src='http://media.bambinocampones.com.br/images/evento_bkp.png' class='activity_bkg' />";
                            //eval("sp"+ii).style.background="url('http://media.bambinocampones.com.br/images/evento_bkp.png')";
                            document.getElementById("sp"+ii).style.background="url('http://media.bambinocampones.com.br/images/evento_bkp.png')";
                        } else if (xxTipo=='N'){
                            xxSpan = "<img src='http://media.bambinocampones.com.br/images/feriado_bkp.png' class='activity_bkg' />";
                            //eval("sp"+ii).style.background="url('http://media.bambinocampones.com.br/images/feriado_bkp.png')";
                            document.getElementById("sp"+ii).style.background="url('http://media.bambinocampones.com.br/images/feriado_bkp.png')";
                        } else if (xxTipo=='P'){
                            xxSpan = "<img src='http://media.bambinocampones.com.br/images/ponte_bkp.png' class='activity_bkg' />";
                            //eval("sp"+ii).style.background="url('http://media.bambinocampones.com.br/images/ponte_bkp.png')";
                            document.getElementById("sp"+ii).style.background="url('http://media.bambinocampones.com.br/images/ponte_bkp.png')";
                        } else if (xxTipo=='R'){
                            xxSpan = "<img src='http://media.bambinocampones.com.br/images/recesso_bkp.png' class='activity_bkg' />";
                            //eval("sp"+ii).style.background="url('http://media.bambinocampones.com.br/images/recesso_bkp.png')";
                            document.getElementById("sp"+ii).style.background="url('http://media.bambinocampones.com.br/images/recesso_bkp.png')";
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
